#!/usr/bin/env python3
"""Survival analysis of dependency-arc lengths across UD treebanks (commul/universal_dependencies).

Reframes each dependency arc as a (possibly right-censored) time-to-event object: an arc's
"lifetime" is its length in tokens, and it is censored at the maximum length geometrically
achievable from the dependent's position in the sentence (max(dist-to-left-edge,
dist-to-right-edge)). This removes the mechanical confound between sentence length and raw
dependency-length statistics that plagues pooled mean-dependency-distance (MDD) comparisons.

Method (survival-hazard framing) vs Baseline (pooled MDD, the standard DLM statistic):
  - Baseline: mean/median raw arc length per (language, register).
  - Method:   Kaplan-Meier survival curves, Nelson-Aalen cumulative/instantaneous hazard,
              a stratified Cox proportional-hazards model (register + empirical word-order +
              morphological richness, stratified by language family as a frailty substitute),
              per-family residual-hazard ranking against a word-order-matched cluster baseline,
              and a sentence-length-resampling robustness check comparing Cox-coefficient
              stability against MDD-ratio instability.
"""

from __future__ import annotations

import gc
import json
import multiprocessing as mp
import random
import re
import resource
import sys
import time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from huggingface_hub import HfApi, hf_hub_download
from lifelines import CoxPHFitter, KaplanMeierFitter, NelsonAalenFitter
from loguru import logger

# --------------------------------------------------------------------------------------
# Setup: logging, resource limits, hardware
# --------------------------------------------------------------------------------------
WORKDIR = Path(__file__).resolve().parent
LOG_DIR = WORKDIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(LOG_DIR / "run.log", rotation="30 MB", level="DEBUG")

# RAM budget: container limit is 29GB (cgroup v2). Use ~55% (16GB) as a hard ceiling for this
# process's virtual address space, well below the container OOM point, since HF downloads
# (cached to disk, not RAM) and pandas/lifelines intermediates are the main consumers.
RAM_BUDGET_BYTES = 16 * 1024**3
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET_BYTES * 2, RAM_BUDGET_BYTES * 2))
NUM_CPUS = len(__import__("os").sched_getaffinity(0)) if hasattr(__import__("os"), "sched_getaffinity") else 8
logger.info(f"NUM_CPUS={NUM_CPUS}, RAM budget={RAM_BUDGET_BYTES / 1e9:.1f}GB (virtual, 2x headroom)")

HF_DATASET_ID = "commul/universal_dependencies"
RNG_SEED = 20260813
random.seed(RNG_SEED)
np.random.seed(RNG_SEED)

# Scale knobs (overridable via CLI for the gradual-scaling protocol).
MAX_SENT_PER_SPLIT = 4000  # cap sentences drawn from any single (config, split) — bounds runtime
MAX_CONFIGS: int | None = None  # None = all 350 treebank configs
MAX_ARCS_FOR_COX = 300_000  # subsample cap for Cox fitting / robustness check (fitting cost)
MAX_ARCS_FOR_KM = 40_000  # subsample cap per (language, register) curve for KM/NA plotting

OUT_JSON = WORKDIR / "method_out.json"

# --------------------------------------------------------------------------------------
# Static linguistic reference tables (self-contained — no external API calls at runtime)
# --------------------------------------------------------------------------------------

# ISO-639-derived treebank language code -> language family (coarse, standard genealogical
# classification). Codes not covered default to "Unclassified" (logged, excluded from
# family-level claims but retained in the raw arc table). Built from established typological
# classification (Glottolog/WALS genealogy), not fetched at runtime.
LANG_FAMILY: dict[str, str] = {
    # Germanic
    "af": "Germanic", "gsw": "Germanic", "bar": "Germanic", "da": "Germanic", "nl": "Germanic",
    "en": "Germanic", "fo": "Germanic", "de": "Germanic", "got": "Germanic", "lb": "Germanic",
    "nds": "Germanic", "no": "Germanic", "sv": "Germanic", "yi": "Germanic", "ang": "Germanic",
    "is": "Germanic",
    # Romance
    "ca": "Romance", "fr": "Romance", "frm": "Romance", "fro": "Romance", "gl": "Romance",
    "it": "Romance", "la": "Romance", "lij": "Romance", "oc": "Romance", "pro": "Romance",
    "pt": "Romance", "ro": "Romance", "es": "Romance", "scn": "Romance", "nap": "Romance",
    "qpm": "Romance",
    # Slavic
    "be": "Slavic", "bg": "Slavic", "cs": "Slavic", "hr": "Slavic", "mk": "Slavic", "pl": "Slavic",
    "ru": "Slavic", "sk": "Slavic", "sl": "Slavic", "sr": "Slavic", "uk": "Slavic", "hsb": "Slavic",
    "orv": "Slavic", "cu": "Slavic", "ruc": "Slavic",
    # Baltic
    "lt": "Baltic", "lv": "Baltic", "ltg": "Baltic",
    # Celtic
    "br": "Celtic", "cy": "Celtic", "ga": "Celtic", "gd": "Celtic", "gv": "Celtic", "sga": "Celtic",
    # Indo-Aryan (Indic)
    "as": "Indo-Aryan", "bn": "Indo-Aryan", "bho": "Indo-Aryan", "gu": "Indo-Aryan",
    "hi": "Indo-Aryan", "mr": "Indo-Aryan", "ne": "Indo-Aryan", "or": "Indo-Aryan",
    "pa": "Indo-Aryan", "sa": "Indo-Aryan", "sd": "Indo-Aryan", "si": "Indo-Aryan",
    "ur": "Indo-Aryan",
    # Iranian
    "fa": "Iranian", "kmr": "Iranian", "ps": "Iranian", "sdh": "Iranian", "zza": "Iranian",
    "azz": "Iranian",
    # Hellenic
    "el": "Hellenic", "grc": "Hellenic", "cpg": "Hellenic",
    # Armenian
    "hy": "Armenian", "axm": "Armenian", "xcl": "Armenian", "hyw": "Armenian",
    # Albanian
    "sq": "Albanian", "aln": "Albanian",
    # Anatolian (extinct IE)
    "hit": "Anatolian",
    # Uralic
    "et": "Uralic", "fi": "Uralic", "hu": "Uralic", "krl": "Uralic", "koi": "Uralic",
    "kpv": "Uralic", "mdf": "Uralic", "myv": "Uralic", "olo": "Uralic", "sme": "Uralic",
    "sms": "Uralic", "vep": "Uralic", "yrk": "Uralic",
    # Semitic
    "ar": "Semitic", "he": "Semitic", "mt": "Semitic", "am": "Semitic", "hbo": "Semitic",
    "akk": "Semitic", "ajp": "Semitic", "aii": "Semitic", "qaf": "Semitic",
    # Afro-Asiatic non-Semitic
    "egy": "Afro-Asiatic(Egyptian)", "cop": "Afro-Asiatic(Egyptian)", "bej": "Afro-Asiatic(Cushitic)",
    "ha": "Afro-Asiatic(Chadic)",
    # Sino-Tibetan
    "zh": "Sino-Tibetan", "yue": "Sino-Tibetan", "lzh": "Sino-Tibetan", "wuu": "Sino-Tibetan",
    # Japonic / Koreanic
    "ja": "Japonic", "ko": "Koreanic",
    # Austronesian
    "id": "Austronesian", "jv": "Austronesian", "tl": "Austronesian", "ceb": "Austronesian",
    # Tai-Kadai
    "th": "Tai-Kadai",
    # Turkic
    "az": "Turkic", "kk": "Turkic", "ky": "Turkic", "tr": "Turkic", "tt": "Turkic", "ug": "Turkic",
    "uz": "Turkic", "sah": "Turkic", "ota": "Turkic", "otk": "Turkic",
    # Dravidian
    "ta": "Dravidian", "te": "Dravidian", "ml": "Dravidian",
    # Austroasiatic
    "vi": "Austroasiatic",
    # Basque isolate
    "eu": "Basque(isolate)",
    # Kartvelian
    "ka": "Kartvelian",
    # Northwest Caucasian
    "ab": "NW-Caucasian", "abq": "NW-Caucasian",
    # Niger-Congo / Mande
    "wo": "Niger-Congo", "bm": "Mande", "yo": "Niger-Congo",
    # Creoles
    "ht": "Creole", "pcm": "Creole",
    # Sign languages (excluded from register axis, kept in raw table)
    "ssp": "Sign", "swl": "Sign",
}

# Treebank name -> register, for corpora carrying no in-comment modality metadata.
# Curated from known UD corpus documentation. Everything not listed here and not resolved
# by in-comment metadata defaults to "written" (the overwhelming UD majority: news, wiki,
# legal, literary, learner-essay text) — this default is logged explicitly as a limitation.
KNOWN_SPOKEN_TREEBANKS = {
    "fr_rhapsodie", "en_eslspok", "en_childes", "it_kiparlaforest", "it_parlamint",
    "uk_parlamint", "en_gum",  # en_gum has per-sentence genre override (handled by comment parser)
}
KNOWN_SIGN_TREEBANKS = {"ko_ksl", "ssp_lse", "swl_sslc"}
SPOKEN_GENRE_VALUES = {"conversation", "interview", "speech", "vlog", "discourse"}

NEEDED_COLS = ["sent_id", "comments", "tokens", "head", "deprel", "feats"]


def classify_register(config_name: str, comments: Any) -> tuple[str, str | None]:
    """Return (register, genre_raw). register in {'spoken','written','sign'}."""
    if config_name in KNOWN_SIGN_TREEBANKS:
        return "sign", "sign-language"
    text = " ".join(str(c) for c in comments) if comments is not None and len(comments) else ""
    if re.search(r"modalit(y|ies)\s*=\s*speech", text, re.I) or re.search(
        r"channel\s*=\s*(face to face|phone|audio)", text, re.I
    ):
        return "spoken", "speech(modality-tag)"
    if re.search(r"modalit(y|ies)\s*=\s*(writing|written)", text, re.I):
        return "written", "writing(modality-tag)"
    m = re.search(r"meta::genre\s*=\s*([a-zA-Z_\-]+)", text)
    if m:
        genre = m.group(1).lower()
        return ("spoken" if genre in SPOKEN_GENRE_VALUES else "written"), genre
    if config_name in KNOWN_SPOKEN_TREEBANKS:
        return "spoken", "name-pattern-fallback"
    return "written", None


def lang_of(config_name: str) -> str:
    return config_name.split("_")[0]


def family_of(lang: str) -> str:
    return LANG_FAMILY.get(lang, "Unclassified")


# --------------------------------------------------------------------------------------
# Phase 1: discover treebank configs + splits
# --------------------------------------------------------------------------------------
def discover_configs() -> list[dict]:
    api = HfApi()
    info = api.dataset_info(HF_DATASET_ID)
    configs = info.card_data.get("configs", []) if info.card_data else []
    if not configs:
        raise RuntimeError("No configs found in dataset card_data — cannot proceed.")
    logger.info(f"Discovered {len(configs)} treebank configs in {HF_DATASET_ID}")
    return configs


def download_one_file(repo_path: str) -> str | None:
    try:
        return hf_hub_download(HF_DATASET_ID, repo_path, repo_type="dataset")
    except Exception as e:
        logger.warning(f"Download failed for {repo_path}: {e}")
        return None


# --------------------------------------------------------------------------------------
# Phase 2: per-config arc extraction (runs in worker processes)
# --------------------------------------------------------------------------------------
def process_config(config_name: str, split_paths: dict[str, str], max_sent_per_split: int) -> dict | None:
    """Parse one treebank's downloaded parquet split files into compact arc arrays +
    treebank-level covariates (morphological richness, empirical word-order score)."""
    lang = lang_of(config_name)
    fam = family_of(lang)

    arc_lengths: list[int] = []
    censor_bounds: list[int] = []
    events: list[int] = []
    sent_lens: list[int] = []
    unique_feats: set[str] = set()
    total_tokens = 0
    dep_before_head = 0
    total_dir_arcs = 0
    n_sentences = 0
    register_votes: dict[str, int] = defaultdict(int)
    genre_seen: set[str] = set()

    for split, local_path in split_paths.items():
        try:
            df = pd.read_parquet(local_path, columns=NEEDED_COLS)
        except Exception as e:
            logger.warning(f"[{config_name}/{split}] failed to read parquet: {e}")
            continue
        n = len(df)
        if n == 0:
            continue
        if n > max_sent_per_split:
            idx = np.random.RandomState(hash((config_name, split)) % (2**31)).choice(
                n, size=max_sent_per_split, replace=False
            )
            df = df.iloc[idx]
            logger.debug(f"[{config_name}/{split}] capped {n} -> {max_sent_per_split} sentences")

        for row in df.itertuples(index=False):
            tokens = row.tokens
            if tokens is None or len(tokens) == 0:
                continue
            slen = len(tokens)
            heads = row.head
            deprels = row.deprel
            feats = row.feats
            if heads is None or len(heads) != slen:
                continue

            reg, genre = classify_register(config_name, row.comments)
            register_votes[reg] += 1
            if genre:
                genre_seen.add(genre)

            n_sentences += 1
            total_tokens += slen
            sent_lens.append(slen)
            if feats is not None:
                for f in feats:
                    if f is not None:
                        unique_feats.add(f)

            for i in range(slen):
                hv = heads[i]
                try:
                    head_id = int(hv)
                except (TypeError, ValueError):
                    continue
                if head_id == 0:
                    continue  # root: no arc
                dep_pos0 = i
                head_pos0 = head_id - 1
                if head_pos0 < 0 or head_pos0 >= slen:
                    continue  # malformed / out-of-range head reference
                deprel = deprels[i] if deprels is not None and i < len(deprels) else None
                if deprel != "punct":
                    total_dir_arcs += 1
                    if dep_pos0 < head_pos0:
                        dep_before_head += 1
                arclen = abs(head_pos0 - dep_pos0)
                dist_left = dep_pos0
                dist_right = (slen - 1) - dep_pos0
                cbound = max(dist_left, dist_right)
                event = 1 if arclen < cbound else 0
                arc_lengths.append(arclen)
                censor_bounds.append(cbound)
                events.append(event)

    if n_sentences == 0 or not arc_lengths:
        return None

    register = max(register_votes, key=register_votes.get)  # majority register for this treebank
    morph_richness = len(unique_feats) / total_tokens if total_tokens else 0.0
    word_order_score = dep_before_head / total_dir_arcs if total_dir_arcs else 0.5

    return {
        "config": config_name,
        "language": lang,
        "family": fam,
        "register": register,
        "genre_tags": sorted(genre_seen)[:5],
        "n_sentences": n_sentences,
        "morph_richness": morph_richness,
        "word_order_score": word_order_score,  # 0=strictly head-initial(VO-like) .. 1=head-final(OV-like)
        "arc_length": np.array(arc_lengths, dtype=np.int16),
        "censor_bound": np.array(censor_bounds, dtype=np.int16),
        "event": np.array(events, dtype=np.int8),
    }


def _worker(args):
    config_name, split_paths, max_sent = args
    try:
        return process_config(config_name, split_paths, max_sent)
    except Exception:
        logger.exception(f"process_config failed for {config_name}")
        return None


# --------------------------------------------------------------------------------------
# Phase 3: analysis helpers
# --------------------------------------------------------------------------------------
def km_summary(durations: np.ndarray, events: np.ndarray, n_points: int = 20) -> dict:
    kmf = KaplanMeierFitter()
    kmf.fit(durations, event_observed=events)
    sf = kmf.survival_function_
    ci = kmf.confidence_interval_
    idx = np.unique(np.linspace(0, len(sf) - 1, min(n_points, len(sf))).astype(int))
    times = sf.index.values[idx].tolist()
    surv = sf.iloc[idx, 0].values.tolist()
    lo = ci.iloc[idx, 0].values.tolist()
    hi = ci.iloc[idx, 1].values.tolist()
    return {
        "durations": [float(t) for t in times],
        "survival": [float(s) for s in surv],
        "conf_int_lower": [float(x) for x in lo],
        "conf_int_upper": [float(x) for x in hi],
        "median_arc_length": float(kmf.median_survival_time_) if np.isfinite(kmf.median_survival_time_) else None,
    }


def na_summary(durations: np.ndarray, events: np.ndarray, n_points: int = 20, horizon_d: int = 10) -> dict:
    naf = NelsonAalenFitter()
    naf.fit(durations, event_observed=events)
    ch = naf.cumulative_hazard_
    idx = np.unique(np.linspace(0, len(ch) - 1, min(n_points, len(ch))).astype(int))
    times = ch.index.values[idx].tolist()
    cum_haz = ch.iloc[idx, 0].values.tolist()
    inst_haz = np.gradient(ch.iloc[:, 0].values, ch.index.values) if len(ch) > 1 else np.array([0.0])
    inst_sampled = inst_haz[idx].tolist() if len(inst_haz) == len(ch) else [None] * len(idx)
    h_at_horizon = float(np.interp(horizon_d, ch.index.values, ch.iloc[:, 0].values)) if len(ch) else None
    return {
        "durations": [float(t) for t in times],
        "cumulative_hazard": [float(x) for x in cum_haz],
        "instantaneous_hazard": [None if x is None else float(x) for x in inst_sampled],
        "cumulative_hazard_at_d10": h_at_horizon,
    }


def subsample(df: pd.DataFrame, n_max: int, seed: int = RNG_SEED) -> pd.DataFrame:
    if len(df) <= n_max:
        return df
    return df.sample(n=n_max, random_state=seed)


def fit_cox(df: pd.DataFrame, covariates: list[str], strata: str | None = None, penalizer: float = 0.1) -> dict:
    cols = covariates + ["duration", "event"] + ([strata] if strata else [])
    data = df[cols].copy()
    data = data.replace([np.inf, -np.inf], np.nan).dropna()
    # drop covariates that are (near-)constant after any filtering — these produce a
    # singular/NaN Hessian in Newton-Raphson rather than a real convergence failure.
    usable_covs = [c for c in covariates if data[c].std() > 1e-8]
    dropped = set(covariates) - set(usable_covs)
    if dropped:
        logger.warning(f"Cox: dropping near-constant covariates {dropped}")
    if strata:
        data[strata] = data[strata].astype("category")
        vc = data[strata].value_counts()
        keep = vc[vc >= 20].index
        data = data[data[strata].isin(keep)]
        data[strata] = data[strata].cat.remove_unused_categories()
        if data[strata].nunique() < 2:
            strata = None

    last_err = None
    for pen in (penalizer, max(penalizer * 5, 1.0), 5.0):
        try:
            cph = CoxPHFitter(penalizer=pen)
            fit_cols = usable_covs + ["duration", "event"] + ([strata] if strata else [])
            cph.fit(data[fit_cols], duration_col="duration", event_col="event", strata=[strata] if strata else None)
            summ = cph.summary
            coefs = {}
            for cov in covariates:
                if cov in summ.index:
                    row = summ.loc[cov]
                    coefs[cov] = {
                        "coef": float(row["coef"]),
                        "ci_lower": float(row["coef lower 95%"]),
                        "ci_upper": float(row["coef upper 95%"]),
                        "p": float(row["p"]),
                    }
                else:
                    coefs[cov] = None  # dropped: near-constant in this sample
            return {
                "coefficients": coefs,
                "n_obs": int(len(data)),
                "concordance": float(cph.concordance_index_),
                "penalizer_used": pen,
            }
        except Exception as e:  # ConvergenceError or similar
            last_err = e
            logger.warning(f"Cox fit failed at penalizer={pen} (strata={strata}): {e}")
    raise RuntimeError(f"Cox fit failed at all penalizer levels: {last_err}")


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------
@logger.catch(reraise=True)
def main():
    t0 = time.time()
    configs = discover_configs()
    if MAX_CONFIGS:
        configs = configs[:MAX_CONFIGS]

    # ---- Phase 1: parallel download of all needed parquet files ----
    all_repo_paths: set[str] = set()
    config_split_map: dict[str, dict[str, str]] = {}
    for c in configs:
        cname = c["config_name"]
        config_split_map[cname] = {}
        for df_entry in c.get("data_files", []):
            all_repo_paths.add(df_entry["path"])

    logger.info(f"Downloading {len(all_repo_paths)} parquet files across {len(configs)} treebanks...")
    path_to_local: dict[str, str] = {}
    with ThreadPoolExecutor(max_workers=min(32, NUM_CPUS * 4)) as pool:
        futs = {pool.submit(download_one_file, p): p for p in all_repo_paths}
        done = 0
        for fut in as_completed(futs):
            p = futs[fut]
            local = fut.result()
            if local:
                path_to_local[p] = local
            done += 1
            if done % 50 == 0:
                logger.info(f"  downloaded {done}/{len(all_repo_paths)}")
    logger.info(f"Download complete: {len(path_to_local)}/{len(all_repo_paths)} succeeded")

    for c in configs:
        cname = c["config_name"]
        for df_entry in c.get("data_files", []):
            local = path_to_local.get(df_entry["path"])
            if local:
                config_split_map[cname][df_entry["split"]] = local

    # ---- Phase 2: parallel per-treebank arc extraction ----
    work_items = [
        (cname, splits, MAX_SENT_PER_SPLIT)
        for cname, splits in config_split_map.items()
        if splits
    ]
    logger.info(f"Processing {len(work_items)} treebanks with {NUM_CPUS} worker processes...")
    treebank_results: list[dict] = []
    with ProcessPoolExecutor(max_workers=NUM_CPUS, mp_context=mp.get_context("spawn")) as pool:
        futs = [pool.submit(_worker, item) for item in work_items]
        for i, fut in enumerate(as_completed(futs)):
            try:
                res = fut.result()
            except Exception:
                logger.exception("worker crashed")
                res = None
            if res:
                treebank_results.append(res)
            if (i + 1) % 25 == 0:
                logger.info(f"  processed {i + 1}/{len(work_items)} treebanks")
    logger.info(f"Extracted arcs from {len(treebank_results)}/{len(work_items)} treebanks in {time.time() - t0:.1f}s")

    if not treebank_results:
        raise RuntimeError("No treebanks yielded usable arcs — aborting.")

    n_arcs_total = sum(len(r["arc_length"]) for r in treebank_results)
    n_censored = sum(int(r["event"].size - r["event"].sum()) for r in treebank_results)
    logger.info(f"Total arcs={n_arcs_total}, censored={n_censored} ({100 * n_censored / n_arcs_total:.2f}%)")

    # ---- Build a flat arc-level DataFrame for global stats (register/family/etc are treebank-level covariates) ----
    frames = []
    for r in treebank_results:
        m = len(r["arc_length"])
        frames.append(
            pd.DataFrame(
                {
                    "duration": r["arc_length"],
                    "event": r["event"],
                    "censor_bound": r["censor_bound"],
                    "config": r["config"],
                    "language": r["language"],
                    "family": r["family"],
                    "register": r["register"],
                    "morph_richness": r["morph_richness"],
                    "word_order_score": r["word_order_score"],
                }
            )
        )
    arcs = pd.concat(frames, ignore_index=True)
    del frames
    gc.collect()
    logger.info(f"Assembled arc table: {len(arcs):,} rows, {arcs.memory_usage(deep=False).sum() / 1e6:.1f} MB")

    for col in ["config", "language", "family", "register"]:
        arcs[col] = arcs[col].astype("category")

    # ---- Kaplan-Meier per (language, register) ----
    km_curves: dict[str, dict] = {}
    lang_reg_groups = arcs.groupby(["language", "register"], observed=True)
    for (lang, reg), grp in lang_reg_groups:
        if len(grp) < 30:
            continue
        s = subsample(grp, MAX_ARCS_FOR_KM)
        key = f"{lang}|{reg}"
        try:
            km_curves[key] = km_summary(s["duration"].values, s["event"].values)
            km_curves[key]["n_arcs"] = int(len(grp))
            km_curves[key]["pct_censored"] = float(100 * (1 - grp["event"].mean()))
            km_curves[key]["mean_arc_length"] = float(grp["duration"].mean())
        except Exception:
            logger.warning(f"KM fit failed for {key}")
    logger.info(f"Fit {len(km_curves)} Kaplan-Meier (language, register) curves")

    # ---- Nelson-Aalen per treebank ----
    na_curves: dict[str, dict] = {}
    for r in treebank_results:
        cname = r["config"]
        d = r["arc_length"]
        e = r["event"]
        if len(d) < 30:
            continue
        if len(d) > MAX_ARCS_FOR_KM:
            idx = np.random.RandomState(RNG_SEED).choice(len(d), MAX_ARCS_FOR_KM, replace=False)
            d, e = d[idx], e[idx]
        try:
            na_curves[cname] = na_summary(d, e)
        except Exception:
            logger.warning(f"NA fit failed for {cname}")
    logger.info(f"Fit {len(na_curves)} Nelson-Aalen treebank hazard curves")

    # ---- Cox proportional-hazards model (register + word_order + morph, stratified by family) ----
    cox_df = arcs[arcs["register"].isin(["spoken", "written"])].copy()
    word_order_scale = (cox_df["word_order_score"] - cox_df["word_order_score"].mean()) / cox_df[
        "word_order_score"
    ].std()
    morph_scale = (cox_df["morph_richness"] - cox_df["morph_richness"].mean()) / cox_df["morph_richness"].std()
    cox_fit_df = pd.DataFrame(
        {
            "duration": cox_df["duration"].values,
            "event": cox_df["event"].values,
            "register": (cox_df["register"] == "spoken").astype(int).values,
            "word_order_scale": word_order_scale.values,
            "morph_scale": morph_scale.values,
            "family": cox_df["family"].values,
        }
    )
    cox_fit_sample = subsample(cox_fit_df, MAX_ARCS_FOR_COX)
    try:
        cox_result = fit_cox(
            cox_fit_sample, ["register", "word_order_scale", "morph_scale"], strata="family"
        )
        logger.info(f"Cox model fit on {cox_result['n_obs']:,} arcs: {cox_result['coefficients']}")
    except Exception:
        logger.exception("Stratified Cox fit failed; retrying without strata")
        cox_result = fit_cox(cox_fit_sample, ["register", "word_order_scale", "morph_scale"], strata=None)

    # ---- Per-family residual-hazard ranking vs word-order-cluster baseline (empirical-Bayes-lite frailty) ----
    fam_rows = []
    for r in treebank_results:
        fam_rows.append(
            {
                "family": r["family"],
                "config": r["config"],
                "word_order_score": r["word_order_score"],
                "h_at_10": na_curves.get(r["config"], {}).get("cumulative_hazard_at_d10"),
                "n_arcs": len(r["arc_length"]),
            }
        )
    fam_df = pd.DataFrame(fam_rows).dropna(subset=["h_at_10"])
    fam_agg = (
        fam_df.groupby("family")
        .apply(lambda g: pd.Series({
            "mean_h10": np.average(g["h_at_10"], weights=g["n_arcs"]),
            "mean_word_order": np.average(g["word_order_score"], weights=g["n_arcs"]),
            "n_treebanks": len(g),
            "n_arcs": g["n_arcs"].sum(),
        }), include_groups=False)
        .reset_index()
    )
    fam_agg = fam_agg[fam_agg["n_arcs"] >= 200]
    wo_median = fam_agg["mean_word_order"].median()
    fam_agg["typological_cluster"] = np.where(fam_agg["mean_word_order"] >= wo_median, "head-final-leaning", "head-initial-leaning")
    fam_agg["cluster_baseline"] = fam_agg.groupby("typological_cluster")["mean_h10"].transform("mean")
    fam_agg["residual_hazard"] = fam_agg["mean_h10"] - fam_agg["cluster_baseline"]
    fam_agg = fam_agg.sort_values("residual_hazard", key=lambda s: s.abs(), ascending=False)
    top_outlier_families = fam_agg.head(10).to_dict(orient="records")
    logger.info(f"Family residual-hazard ranking computed for {len(fam_agg)} families")

    # ---- Robustness: sentence-length-resampling validation ----
    robustness: dict[str, dict] = {}
    for lang, grp in arcs.groupby("language", observed=True):
        regs = grp["register"].unique().tolist()
        if "spoken" not in regs or "written" not in regs:
            continue
        spoken = grp[grp["register"] == "spoken"]
        written = grp[grp["register"] == "written"]
        if len(spoken) < 200 or len(written) < 200:
            continue
        try:
            mdd_orig_s, mdd_orig_w = spoken["duration"].mean(), written["duration"].mean()
            mdd_ratio_original = float(mdd_orig_s / mdd_orig_w)

            combo = pd.concat([spoken.assign(reg_bin=1), written.assign(reg_bin=0)], ignore_index=True)
            combo_sample = subsample(combo, 60_000)
            orig_fit = fit_cox(
                combo_sample.drop(columns=["register"]).rename(columns={"reg_bin": "register"}),
                ["register"],
                strata=None,
            )
            if orig_fit["coefficients"].get("register") is None:
                continue
            beta_orig = orig_fit["coefficients"]["register"]["coef"]

            # balance by censoring-bound decile (proxy for sentence-position/length composition,
            # since raw sentence length isn't retained per-arc at this stage)
            combo["bound_decile"] = pd.qcut(combo["censor_bound"], 10, duplicates="drop")
            resampled_parts = []
            for _, bin_grp in combo.groupby("bound_decile", observed=True):
                s_bin = bin_grp[bin_grp["reg_bin"] == 1]
                w_bin = bin_grp[bin_grp["reg_bin"] == 0]
                k = min(len(s_bin), len(w_bin))
                if k < 5:
                    continue
                resampled_parts.append(s_bin.sample(k, random_state=RNG_SEED))
                resampled_parts.append(w_bin.sample(k, random_state=RNG_SEED))
            if not resampled_parts:
                continue
            resampled = pd.concat(resampled_parts, ignore_index=True)
            mdd_res_s = resampled.loc[resampled["reg_bin"] == 1, "duration"].mean()
            mdd_res_w = resampled.loc[resampled["reg_bin"] == 0, "duration"].mean()
            mdd_ratio_resampled = float(mdd_res_s / mdd_res_w)

            resampled_sample = subsample(resampled, 60_000)
            res_fit = fit_cox(
                resampled_sample.drop(columns=["register"]).rename(columns={"reg_bin": "register"}),
                ["register"],
                strata=None,
            )
            if res_fit["coefficients"].get("register") is None:
                continue
            beta_res = res_fit["coefficients"]["register"]["coef"]

            coef_delta = beta_res - beta_orig
            mdd_shift = abs(mdd_ratio_original - mdd_ratio_resampled)
            robustness[lang] = {
                "beta_register_original": beta_orig,
                "beta_register_resampled": beta_res,
                "coef_delta": coef_delta,
                "mdd_ratio_original": mdd_ratio_original,
                "mdd_ratio_resampled": mdd_ratio_resampled,
                "mdd_ratio_shift": mdd_shift,
                "n_spoken": int(len(spoken)),
                "n_written": int(len(written)),
                "n_resampled": int(len(resampled)),
                "verdict": "COX_STABLE" if abs(coef_delta) < 0.15 else "COX_UNSTABLE",
                "mdd_verdict": "MDD_SHIFTS" if mdd_shift > 0.02 else "MDD_STABLE",
            }
        except Exception:
            logger.exception(f"Robustness check failed for language={lang}")
    logger.info(f"Robustness check completed for {len(robustness)} spoken/written language pairs")

    # ---- Cross-check against prior-literature-predicted directions ----
    beta_register = cox_result["coefficients"].get("register") or {}
    beta_order = cox_result["coefficients"].get("word_order_scale") or {}
    beta_morph = cox_result["coefficients"].get("morph_scale") or {}
    spoken_written_langs = [
        lang
        for lang, grp in arcs.groupby("language", observed=True)
        if "spoken" in grp["register"].unique() and "written" in grp["register"].unique()
    ]
    # Per-language sign of (mean_spoken - mean_written) arc length, positive coef here means
    # spoken has HIGHER hazard density at small arc lengths (front-loaded) is inferred from Cox
    # sign of the pooled register coefficient in the KM/Cox framing (coef>0 => higher hazard => shorter survival => front-loaded).
    n_langs_spoken_frontloaded = 0
    for lang in spoken_written_langs:
        s_key, w_key = f"{lang}|spoken", f"{lang}|written"
        if s_key in km_curves and w_key in km_curves:
            if (km_curves[s_key].get("median_arc_length") or 1e9) <= (km_curves[w_key].get("median_arc_length") or 1e9):
                n_langs_spoken_frontloaded += 1
    cross_check = {
        "hypothesis_direction": "spoken_front_loaded + free_order_flatter + high_morph_flatter",
        "beta_register_direction": "positive(front-loaded/higher-hazard)" if beta_register.get("coef", 0) > 0 else "negative(flatter)",
        "beta_order_direction": "positive" if beta_order.get("coef", 0) > 0 else "negative",
        "beta_morph_direction": "positive" if beta_morph.get("coef", 0) > 0 else "negative",
        "n_langs_with_spoken_written_pair": len(spoken_written_langs),
        "n_langs_spoken_median_leq_written": n_langs_spoken_frontloaded,
        "n_family_outliers_reported": len(top_outlier_families),
    }

    n_langs = len(spoken_written_langs) or 1
    cox_stable_count = sum(1 for v in robustness.values() if v["verdict"] == "COX_STABLE")
    mdd_unstable_count = sum(1 for v in robustness.values() if v["mdd_verdict"] == "MDD_SHIFTS")
    hypothesis_verdict = {
        "spoken_front_loaded": "CONFIRMED" if n_langs_spoken_frontloaded > 0.6 * n_langs else "NOT_CONFIRMED",
        "word_order_effect": (
            "CONFIRMED"
            if beta_order and not (beta_order["ci_lower"] <= 0 <= beta_order["ci_upper"])
            else "UNCERTAIN"
        ),
        "family_deviance_exists": "CONFIRMED" if len(top_outlier_families) > 0 else "NOT_CONFIRMED",
        "robustness_to_sent_length": (
            "CONFIRMED"
            if (robustness and cox_stable_count > 0.5 * len(robustness) and mdd_unstable_count > 0.3 * len(robustness))
            else "UNCERTAIN"
        ),
    }
    logger.info(f"Hypothesis verdict: {hypothesis_verdict}")

    # ---- Assemble output per schema (exp_gen_sol_out.json): one example per treebank ----
    examples = []
    baseline_mdds = arcs.groupby("config", observed=True)["duration"].mean()
    for r in treebank_results:
        cname = r["config"]
        d = r["arc_length"]
        km_med = None
        for reg_key in (f"{r['language']}|{r['register']}",):
            if reg_key in km_curves:
                km_med = km_curves[reg_key]["median_arc_length"]
        na_h10 = na_curves.get(cname, {}).get("cumulative_hazard_at_d10")
        pct_censored = float(100 * (1 - r["event"].mean())) if len(r["event"]) else None
        out_obj = {
            "n_arcs": int(len(d)),
            "n_sentences": r["n_sentences"],
            "mean_arc_length": float(d.mean()) if len(d) else None,
            "median_arc_length_km": km_med,
            "pct_censored": pct_censored,
            "cumulative_hazard_at_d10": na_h10,
            "morph_richness": r["morph_richness"],
            "word_order_score": r["word_order_score"],
        }
        examples.append(
            {
                "input": (
                    f"Treebank={cname} language={r['language']} family={r['family']} "
                    f"register={r['register']} genre_tags={r['genre_tags']} n_sentences={r['n_sentences']} "
                    f"n_arcs={len(d)}: characterize the dependency-arc-length distribution as a "
                    f"right-censored survival process (Kaplan-Meier + Nelson-Aalen)."
                ),
                "output": json.dumps(out_obj),
                "metadata_language": r["language"],
                "metadata_family": r["family"],
                "metadata_register": r["register"],
                "metadata_word_order_score": str(r["word_order_score"]),
                "metadata_morph_richness": str(r["morph_richness"]),
                "predict_baseline_pooled_mdd": str(float(baseline_mdds.get(cname, float("nan")))),
                "predict_survival_hazard_median": str(km_med) if km_med is not None else "NA",
            }
        )

    results = {
        "metadata": {
            "method_name": "dependency_arc_survival_analysis",
            "description": (
                "Kaplan-Meier / Nelson-Aalen / stratified-Cox survival-hazard characterization of "
                "UD dependency-arc lengths as right-censored time-to-event objects, vs a pooled "
                "mean-dependency-distance (MDD) baseline, with a sentence-length-resampling "
                "robustness check and family-level residual-hazard ranking against word-order-"
                "matched typological clusters."
            ),
            "hf_dataset": HF_DATASET_ID,
            "n_treebanks_discovered": len(configs),
            "n_treebanks_processed": len(treebank_results),
            "n_languages": int(arcs["language"].nunique()),
            "n_families": int(arcs["family"].nunique()),
            "n_arcs_total": int(n_arcs_total),
            "n_arcs_censored": int(n_censored),
            "pct_censored": float(100 * n_censored / n_arcs_total),
            "n_spoken_written_language_pairs": len(spoken_written_langs),
            "spoken_written_languages": spoken_written_langs,
            "scale_knobs": {
                "max_sent_per_split": MAX_SENT_PER_SPLIT,
                "max_arcs_for_cox": MAX_ARCS_FOR_COX,
                "max_arcs_for_km_curve": MAX_ARCS_FOR_KM,
            },
            "register_classification_note": (
                "Register inferred per sentence from CoNLL-U comment metadata "
                "(modality/channel tags, meta::genre values) where present; falls back to a "
                "curated name-based table for known spoken corpora (Rhapsodie, CHILDES, ESL-spoken, "
                "KIParla, ParlaMint); defaults to 'written' otherwise (documented limitation: "
                "true genre coverage in UD comments is partial, majority-written default reflects "
                "UD's actual written-text-dominated composition)."
            ),
            "kaplan_meier_by_language_register": km_curves,
            "nelson_aalen_by_treebank_sample": {k: na_curves[k] for k in list(na_curves)[:60]},
            "cox_model": {
                "spec": "duration ~ register + word_order_scale + morph_scale, stratified by family",
                **cox_result,
            },
            "family_residual_hazard_ranking": {
                "all_families": fam_agg.to_dict(orient="records"),
                "top_outliers": top_outlier_families,
            },
            "robustness_sentence_length_resampling": robustness,
            "robustness_summary": {
                "n_language_pairs_tested": len(robustness),
                "cox_stable_count": cox_stable_count,
                "mdd_unstable_count": mdd_unstable_count,
            },
            "cross_check_prior_literature": cross_check,
            "hypothesis_verdict": hypothesis_verdict,
            "runtime_seconds": time.time() - t0,
        },
        "datasets": [{"dataset": HF_DATASET_ID, "examples": examples}],
    }

    OUT_JSON.write_text(json.dumps(results, indent=2, default=str))
    logger.info(f"Wrote {OUT_JSON} ({OUT_JSON.stat().st_size / 1e6:.2f} MB) in {time.time() - t0:.1f}s total")


if __name__ == "__main__":
    main()
