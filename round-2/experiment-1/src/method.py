#!/usr/bin/env python3
"""Survival analysis of UD dependency-arc lengths.

Research question: does spoken register minimize dependency-arc length more
than written register, and how does this interact with word-order typology
and morphological richness, once position-bounded censoring is modeled
properly (an arc that reaches the maximum length structurally possible from
its token's position is "censored", not necessarily "as long as it wanted to
be")?

OUR METHOD: Cox proportional-hazards survival regression (duration=arc_length,
event=1 iff arc_length < censoring_bound), which is the correct model for
position-bounded, right-censored dependency lengths.

BASELINE: logistic regression on a dichotomized (long vs short, median-split)
arc length that ignores the censoring structure entirely -- the naive
approach an analyst would reach for without recognizing arcs are censored.
Both are fit on identical covariates/data so the only difference is whether
censoring is modeled (Fallback A2 in the artifact plan).

Where the actual sampled data diverges from the artifact plan's assumptions
(documented inline and in the output's `deviations_from_plan` field):
  - The gold-labeled spoken/written treebanks (en_childes/en_ewt,
    fr_rhapsodie/fr_gsd, sl_sst/sl_ssj) are ALL Indo-European in this
    114,480-row stratified sample -> family has zero variance in the gold
    subset, so shared-frailty-by-family (Phase 3) is impossible there.
    Fallback used: cluster-robust standard errors by language_code instead
    (Fallback B1's spirit: a fixed/robust alternative to frailty).
  - word_order_type is also CONSTANT (verb-medial/SVO) across all six gold
    treebanks -> Phase 8's word-order-variant comparison is run on the FULL
    corpus (13 families, 3 word-order categories) instead of the gold
    subset, where it is estimable.
  - fr_gsd's register in this stratified sample is tagged 'web' (not
    'written') for a slice of its sentences; we treat register as binary
    spoken vs. non-spoken (register_spoken) throughout, so this does not
    change the spoken/written contrast, only the non-spoken label's name.
  - Family-level bootstrap residuals (Phase 4) are run on the FULL corpus
    (13 families) rather than the (family-invariant) gold subset, since
    that is the level at which "family" varies at all.
  - No continuous empirical word-order measure (e.g.
    fraction_dependents_before_head) exists in the dataset actually
    delivered -- only the categorical Grambank word_order_type. Variant B
    uses an ordinal encoding of that categorical field (canonical
    initial<medial<final) as a linear proxy, and Variant C is register x
    word-order INTERACTION (rather than "both in parallel", which would be
    collinear with Variant A/B combined) to test whether typology moderates
    the register effect -- a more informative comparison.
"""

from __future__ import annotations

import glob
import gc
import json
import multiprocessing as mp
import resource
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
import psutil
import statsmodels.api as sm
from lifelines import CoxPHFitter, NelsonAalenFitter
from loguru import logger
from scipy.stats import false_discovery_control

# ----------------------------------------------------------------------------
# Setup: logging, hardware, memory limits
# ----------------------------------------------------------------------------
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

WORKSPACE = Path(__file__).resolve().parent
DATA_DIR = Path(
    "/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/"
    "gen_art/gen_art_dataset_1"
)
FULL_DATA_GLOB = str(DATA_DIR / "full_data_out" / "full_data_out_*.json")

GOLD_TREEBANKS = {"en_childes", "en_ewt", "fr_rhapsodie", "fr_gsd", "sl_sst", "sl_ssj"}
GOLD_SPOKEN_TREEBANKS = {"en_childes", "fr_rhapsodie", "sl_sst"}
GOLD_WRITTEN_TREEBANKS = {"en_ewt", "fr_gsd", "sl_ssj"}
WORD_ORDER_ORDINAL = {"verb-initial": 0, "verb-medial": 1, "verb-final": 2}

RNG_SEED = 20260813


def _detect_cpus() -> int:
    try:
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return max(1, int(int(parts[0]) / int(parts[1])))
    except (FileNotFoundError, ValueError):
        pass
    try:
        return len(os.sched_getaffinity(0))  # type: ignore[name-defined]
    except Exception:
        pass
    return mp.cpu_count()


import os  # noqa: E402

NUM_CPUS = _detect_cpus()
NUM_WORKERS = max(1, NUM_CPUS - 1)
logger.info(f"Detected {NUM_CPUS} CPUs, using {NUM_WORKERS} worker processes")

# 114,480 rows of small scalar records -> a few hundred MB at most in pandas.
# Budget generously but well under the 29GB container limit.
_avail = psutil.virtual_memory().available
RAM_BUDGET_BYTES = int(min(6 * 1024**3, _avail * 0.5))
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET_BYTES * 3, RAM_BUDGET_BYTES * 3))
logger.info(f"RAM budget set to {RAM_BUDGET_BYTES / 1e9:.2f} GB (available {_avail / 1e9:.2f} GB)")


# ----------------------------------------------------------------------------
# Data loading
# ----------------------------------------------------------------------------
KEEP_COLS = [
    "treebank_id",
    "sentence_id",
    "token_id",
    "head_id",
    "censoring_bound",
    "register",
    "language_code",
    "language_name",
    "family_id",
    "word_order_type",
    "morph_richness_proxy",
    "sentence_length",
]


def load_full_data(shard_glob: str = FULL_DATA_GLOB, max_rows: int | None = None) -> pd.DataFrame:
    """Load all shards, keep only needed metadata columns to save memory."""
    shards = sorted(glob.glob(shard_glob))
    if not shards:
        raise FileNotFoundError(f"No shards found matching {shard_glob}")
    logger.info(f"Loading {len(shards)} shard(s): {shards}")
    records: list[dict] = []
    for shard_path in shards:
        with open(shard_path, "r") as f:
            payload = json.load(f)
        for ds in payload["datasets"]:
            for ex in ds["examples"]:
                rec = {c: ex.get(f"metadata_{c}") for c in KEEP_COLS}
                records.append(rec)
        del payload
        gc.collect()
        if max_rows is not None and len(records) >= max_rows:
            records = records[:max_rows]
            break
    df = pd.DataFrame.from_records(records)
    del records
    gc.collect()
    logger.info(f"Loaded {len(df)} rows, {df.memory_usage(deep=True).sum() / 1e6:.1f} MB")
    return df


# ----------------------------------------------------------------------------
# Phase 1: validation + survival-analysis feature construction
# ----------------------------------------------------------------------------
def validate_and_featurize(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["arc_length"] = (df["head_id"] - df["token_id"]).abs()
    n_violations = int((df["arc_length"] > df["censoring_bound"]).sum())
    logger.info(f"Censoring-bound violations: {n_violations} / {len(df)}")
    assert n_violations == 0, f"Found {n_violations} censoring-bound violations"

    df["event"] = (df["arc_length"] < df["censoring_bound"]).astype(int)
    n_censored = int((df["event"] == 0).sum())
    logger.info(f"Censored rows: {n_censored} ({100 * n_censored / len(df):.2f}%)")

    # lifelines requires strictly positive duration for Cox partial likelihood
    # ties; root tokens (arc_length==0) get a small positive epsilon so they
    # remain valid "instant events" at the very start of the risk set rather
    # than being dropped.
    df["arc_length_surv"] = df["arc_length"].clip(lower=1e-3)

    df["register_spoken"] = (df["register"] == "spoken").astype(int)
    df["is_gold_treebank"] = df["treebank_id"].isin(GOLD_TREEBANKS)
    df["heuristic_label_source"] = np.where(
        df["is_gold_treebank"], "gold", "heuristic"
    )
    df["word_order_ordinal"] = df["word_order_type"].map(WORD_ORDER_ORDINAL)
    df["family_id"] = df["family_id"].fillna("unknown")
    return df


def standardize(series: pd.Series) -> tuple[pd.Series, float, float]:
    mean, std = float(series.mean()), float(series.std(ddof=0))
    if std == 0 or np.isnan(std):
        std = 1.0
    return (series - mean) / std, mean, std


# ----------------------------------------------------------------------------
# Cox fitting helpers
# ----------------------------------------------------------------------------
def add_dummies(df: pd.DataFrame, col: str, prefix: str) -> tuple[pd.DataFrame, list[str]]:
    """Manual dummy-encoding (drop_first) -- much faster than formulaic's C()
    for the Cox fits below, which is what caused multi-minute stalls on
    114k-row fits with a 13-level categorical. Category values are sanitized
    into valid formula identifiers (formulaic parses '-' as subtraction, so
    e.g. 'verb-initial' would otherwise break the formula string)."""
    import re

    safe_col = df[col].astype(str).map(lambda v: re.sub(r"[^0-9a-zA-Z_]", "_", v))
    dummies = pd.get_dummies(safe_col, prefix=prefix, drop_first=True, dtype=float)
    return pd.concat([df, dummies], axis=1), list(dummies.columns)


def fit_cox(
    df: pd.DataFrame,
    formula: str,
    cluster_col: str | None = None,
    label: str = "cox_model",
) -> dict:
    t0 = time.time()
    cph = CoxPHFitter(penalizer=0.01)  # small ridge penalty: stabilizes near-collinear covariates
    fit_kwargs = dict(
        df=df[["arc_length_surv", "event"] + _formula_cols(df, formula)],
        duration_col="arc_length_surv",
        event_col="event",
        formula=formula,
        show_progress=False,
    )
    if cluster_col is not None:
        fit_kwargs["cluster_col"] = cluster_col
        fit_kwargs["df"] = df[
            ["arc_length_surv", "event", cluster_col] + _formula_cols(df, formula)
        ]
    logger.info(f"Fitting Cox model '{label}': n={len(df)}, formula='{formula}'")
    try:
        cph.fit(**fit_kwargs)
        logger.info(f"Cox model '{label}' converged in {time.time() - t0:.1f}s")
        summary = cph.summary
        coefs = {
            idx: {
                "beta": float(row["coef"]),
                "se": float(row["se(coef)"]),
                "hazard_ratio": float(row["exp(coef)"]),
                "ci_lower": float(row["coef lower 95%"]),
                "ci_upper": float(row["coef upper 95%"]),
                "p_value": float(row["p"]),
            }
            for idx, row in summary.iterrows()
        }
        result = {
            "label": label,
            "convergence": "success",
            "n_obs": int(cph._n_examples),
            "n_events": int(df["event"].sum()),
            "concordance": float(cph.concordance_index_),
            "log_likelihood": float(cph.log_likelihood_),
            "coefficients": coefs,
        }
    except Exception as e:
        logger.error(f"Cox fit failed for {label} after {time.time() - t0:.1f}s: {e}")
        result = {
            "label": label,
            "convergence": "failed",
            "error": str(e),
            "coefficients": {},
        }
    return result


def _formula_cols(df: pd.DataFrame, formula: str) -> list[str]:
    """Best-effort extraction of raw columns referenced by a patsy/formulaic
    formula string (handles bare names and C(name) categorical wraps)."""
    import re

    tokens = re.findall(r"C\(([a-zA-Z_][a-zA-Z0-9_]*)\)|([a-zA-Z_][a-zA-Z0-9_]*)", formula)
    cols = set()
    for a, b in tokens:
        name = a or b
        if name in df.columns:
            cols.add(name)
    return sorted(cols)


# ----------------------------------------------------------------------------
# Baseline: censoring-naive logistic regression on dichotomized arc length
# ----------------------------------------------------------------------------
def fit_baseline_logit(df: pd.DataFrame, covariate_cols: list[str], label: str = "baseline_logit") -> dict:
    d = df.dropna(subset=covariate_cols + ["arc_length"]).copy()
    median_len = d["arc_length"].median()
    d["arc_long"] = (d["arc_length"] > median_len).astype(int)
    X = sm.add_constant(d[covariate_cols].astype(float))
    y = d["arc_long"].astype(float)
    try:
        model = sm.Logit(y, X).fit(disp=0, maxiter=100)
        coefs = {
            name: {
                "beta": float(model.params[name]),
                "se": float(model.bse[name]),
                "odds_ratio": float(np.exp(model.params[name])),
                "ci_lower": float(model.conf_int().loc[name, 0]),
                "ci_upper": float(model.conf_int().loc[name, 1]),
                "p_value": float(model.pvalues[name]),
            }
            for name in X.columns
        }
        result = {
            "label": label,
            "convergence": "success" if model.mle_retvals.get("converged", True) else "did_not_converge",
            "n_obs": int(len(d)),
            "median_split_arc_length": float(median_len),
            "pseudo_r2": float(model.prsquared),
            "coefficients": coefs,
        }
    except Exception as e:
        logger.error(f"Baseline logit fit failed for {label}: {e}")
        result = {"label": label, "convergence": "failed", "error": str(e), "coefficients": {}}
    return result


# ----------------------------------------------------------------------------
# Phase 4: bootstrap family-level Nelson-Aalen residuals
# ----------------------------------------------------------------------------
def _na_at_d10(durations: np.ndarray, events: np.ndarray, d: float = 10.0) -> float:
    naf = NelsonAalenFitter()
    naf.fit(durations, event_observed=events)
    ch = naf.cumulative_hazard_
    idx = ch.index.values
    valid = idx[idx <= d]
    if len(valid) == 0:
        return float(ch.iloc[0, 0])
    return float(ch.loc[valid[-1]].iloc[0])


def _bootstrap_replicate(args) -> dict[str, float] | None:
    seed, families, family_groups_durations, family_groups_events = args
    rng = np.random.default_rng(seed)
    per_family_na = {}
    all_d, all_e = [], []
    for fam in families:
        durs = family_groups_durations[fam]
        evs = family_groups_events[fam]
        n = len(durs)
        if n < 20:
            continue
        idx = rng.integers(0, n, size=n)
        d_s, e_s = durs[idx], evs[idx]
        per_family_na[fam] = _na_at_d10(d_s, e_s)
        all_d.append(d_s)
        all_e.append(e_s)
    if not per_family_na:
        return None
    pooled_d = np.concatenate(all_d)
    pooled_e = np.concatenate(all_e)
    global_na = _na_at_d10(pooled_d, pooled_e)
    return {fam: v - global_na for fam, v in per_family_na.items()}


def run_family_bootstrap(df: pd.DataFrame, n_reps: int, n_workers: int) -> dict:
    families = sorted(df["family_id"].unique())
    family_groups_durations = {
        fam: df.loc[df["family_id"] == fam, "arc_length_surv"].to_numpy()
        for fam in families
    }
    family_groups_events = {
        fam: df.loc[df["family_id"] == fam, "event"].to_numpy()
        for fam in families
    }
    n_families_per_group = {fam: len(v) for fam, v in family_groups_durations.items()}
    logger.info(f"Bootstrapping family residuals over {len(families)} families, n_reps={n_reps}")

    point_estimates = {}
    for fam in families:
        d = family_groups_durations[fam]
        e = family_groups_events[fam]
        if len(d) < 20:
            continue
        pooled_d = df["arc_length_surv"].to_numpy()
        pooled_e = df["event"].to_numpy()
        point_estimates[fam] = _na_at_d10(d, e) - _na_at_d10(pooled_d, pooled_e)

    seeds = [RNG_SEED + i for i in range(n_reps)]
    args = [
        (s, families, family_groups_durations, family_groups_events) for s in seeds
    ]
    replicate_residuals: dict[str, list[float]] = {fam: [] for fam in families}
    start = time.time()
    with ProcessPoolExecutor(max_workers=n_workers, mp_context=mp.get_context("spawn")) as pool:
        futures = [pool.submit(_bootstrap_replicate, a) for a in args]
        for i, fut in enumerate(as_completed(futures)):
            res = fut.result()
            if res is None:
                continue
            for fam, val in res.items():
                replicate_residuals[fam].append(val)
            if (i + 1) % max(1, n_reps // 10) == 0:
                logger.info(f"  bootstrap {i + 1}/{n_reps} done ({time.time() - start:.1f}s elapsed)")
    elapsed = time.time() - start
    logger.info(f"Bootstrap complete in {elapsed:.1f}s ({elapsed / n_reps:.3f}s/replicate)")

    min_valid_replicates = min(20, max(2, n_reps // 2))
    family_rows = []
    for fam in families:
        vals = np.array(replicate_residuals[fam])
        if fam not in point_estimates or len(vals) < min_valid_replicates:
            continue
        pe = point_estimates[fam]
        se = float(vals.std(ddof=1))
        ci_lower, ci_upper = np.percentile(vals, [2.5, 97.5]).tolist()
        z = pe / se if se > 0 else np.nan
        p_value = float(2 * (1 - _std_normal_cdf(abs(z)))) if not np.isnan(z) else 1.0
        family_rows.append(
            {
                "family_id": fam,
                "n_arcs": n_families_per_group[fam],
                "point_estimate_na_d10_residual": pe,
                "bootstrap_se": se,
                "bootstrap_ci_lower": ci_lower,
                "bootstrap_ci_upper": ci_upper,
                "bootstrap_n_valid_replicates": len(vals),
                "bootstrap_z": float(z) if not np.isnan(z) else None,
                "bootstrap_p_value": p_value,
            }
        )
    return {
        "method": f"{n_reps}_bootstrap_nelson_aalen_d10_residual_vs_pooled",
        "n_reps_requested": n_reps,
        "elapsed_seconds": elapsed,
        "families": family_rows,
    }


def _std_normal_cdf(x: float) -> float:
    from math import erf, sqrt

    return 0.5 * (1 + erf(x / sqrt(2)))


def apply_bh_correction(family_rows: list[dict]) -> list[dict]:
    if not family_rows:
        return family_rows
    pvals = np.array([r["bootstrap_p_value"] for r in family_rows])
    order = np.argsort(pvals)
    adj = false_discovery_control(pvals, method="bh")
    for r, a in zip(family_rows, adj):
        r["bh_adjusted_p"] = float(a)
        r["bh_significant"] = bool(a < 0.05)
    ranked = sorted(family_rows, key=lambda r: r["bootstrap_p_value"])
    return ranked


# ----------------------------------------------------------------------------
# Phase 7: label-noise sensitivity
# ----------------------------------------------------------------------------
def label_noise_sensitivity(df: pd.DataFrame, noise_levels: list[int], formula: str) -> dict:
    results = []
    heuristic_idx = df.index[df["heuristic_label_source"] == "heuristic"].to_numpy()
    rng = np.random.default_rng(RNG_SEED + 999)
    baseline_fit = fit_cox(df, formula, cluster_col="family_id", label="noise_0pct")
    beta0 = baseline_fit["coefficients"].get("register_spoken", {})
    results.append(
        {
            "noise_level_pct": 0,
            "register_beta": beta0.get("beta"),
            "register_ci_lower": beta0.get("ci_lower"),
            "register_ci_upper": beta0.get("ci_upper"),
            "convergence": baseline_fit["convergence"],
        }
    )
    for noise_pct in noise_levels:
        d = df.copy()
        n_flip = int(len(heuristic_idx) * noise_pct / 100)
        flip_idx = rng.choice(heuristic_idx, size=n_flip, replace=False)
        d.loc[flip_idx, "register_spoken"] = 1 - d.loc[flip_idx, "register_spoken"]
        fit = fit_cox(d, formula, cluster_col="family_id", label=f"noise_{noise_pct}pct")
        beta = fit["coefficients"].get("register_spoken", {})
        results.append(
            {
                "noise_level_pct": noise_pct,
                "n_flipped": n_flip,
                "register_beta": beta.get("beta"),
                "register_ci_lower": beta.get("ci_lower"),
                "register_ci_upper": beta.get("ci_upper"),
                "convergence": fit["convergence"],
            }
        )
        del d
        gc.collect()
    return {"noise_levels": [0] + noise_levels, "trajectory": results}


# ----------------------------------------------------------------------------
# Phase 8: word-order operationalization variants (run on full corpus, see
# module docstring for why gold subset is not usable here)
# ----------------------------------------------------------------------------
def word_order_variants(df: pd.DataFrame) -> dict:
    d = df.dropna(subset=["word_order_type", "word_order_ordinal"]).copy()
    d["word_order_ordinal_std"], wo_mean, wo_std = standardize(d["word_order_ordinal"])
    d["morph_richness_std"], m_mean, m_std = standardize(d["morph_richness_proxy"])
    d, wo_dummy_cols = add_dummies(d, "word_order_type", "wo")

    variant_a = fit_cox(
        d,
        "register_spoken + morph_richness_std + " + " + ".join(wo_dummy_cols),
        cluster_col="family_id",
        label="variant_A_grambank_categorical",
    )
    variant_b = fit_cox(
        d,
        "register_spoken + morph_richness_std + word_order_ordinal_std",
        cluster_col="family_id",
        label="variant_B_ordinal_proxy_continuous",
    )
    d["register_x_word_order"] = d["register_spoken"] * d["word_order_ordinal_std"]
    variant_c = fit_cox(
        d,
        "register_spoken + morph_richness_std + word_order_ordinal_std + register_x_word_order",
        cluster_col="family_id",
        label="variant_C_register_by_word_order_interaction",
    )
    return {
        "n_obs": int(len(d)),
        "word_order_ordinal_mean": wo_mean,
        "word_order_ordinal_std": wo_std,
        "variant_A_grambank_categorical": variant_a,
        "variant_B_ordinal_proxy_continuous": variant_b,
        "variant_C_register_by_word_order_interaction": variant_c,
    }


# ----------------------------------------------------------------------------
# Phase 9: random-head-permutation null baseline
# ----------------------------------------------------------------------------
def random_permutation_null(df: pd.DataFrame, n_sample: int, seed: int = RNG_SEED + 42) -> dict:
    rng = np.random.default_rng(seed)
    n_sample = min(n_sample, len(df))
    sample = df.sample(n=n_sample, random_state=seed).copy()

    token_id = sample["token_id"].to_numpy()
    sent_len = sample["sentence_length"].to_numpy()
    new_head = rng.integers(1, sent_len + 1)
    # avoid self-loop where feasible (redraw once for ties)
    tie_mask = new_head == token_id
    if tie_mask.any():
        redraw = rng.integers(1, sent_len[tie_mask] + 1)
        new_head[tie_mask] = redraw

    null_arc_length = np.abs(token_id - new_head).astype(float)
    null_censoring_bound = np.maximum(token_id, sent_len - token_id)
    null_arc_length_surv = np.clip(null_arc_length, 1e-3, None)
    null_event = (null_arc_length < null_censoring_bound).astype(int)

    obs_d = sample["arc_length_surv"].to_numpy()
    obs_e = sample["event"].to_numpy()

    naf_obs = NelsonAalenFitter().fit(obs_d, event_observed=obs_e)
    naf_null = NelsonAalenFitter().fit(null_arc_length_surv, event_observed=null_event)

    max_d = float(min(obs_d.max(), null_arc_length_surv.max(), 50))
    grid = np.linspace(0.1, max_d, 200)
    obs_curve = naf_obs.predict(grid).to_numpy()
    null_curve = naf_null.predict(grid).to_numpy()
    auc_diff = float(np.trapezoid(np.abs(obs_curve - null_curve), grid))

    return {
        "n_sample": int(n_sample),
        "grid_max_duration": max_d,
        "observed_na_curve": {"d": grid.tolist(), "cumhaz": obs_curve.tolist()},
        "null_na_curve": {"d": grid.tolist(), "cumhaz": null_curve.tolist()},
        "auc_difference": auc_diff,
        "observed_mean_arc_length": float(sample["arc_length"].mean()),
        "null_mean_arc_length": float(null_arc_length.mean()),
    }


# ----------------------------------------------------------------------------
# Output compilation (exp_gen_sol_out schema)
# ----------------------------------------------------------------------------
def make_example(input_desc: str, output_val: str, predict_method: str = "result", **metadata) -> dict:
    ex = {"input": input_desc, "output": str(output_val)}
    ex[f"predict_{predict_method}"] = str(output_val)
    for k, v in metadata.items():
        ex[f"metadata_{k}"] = v
    return ex


def coefficient_examples(
    model_result: dict, model_label: str, context_desc: str, predict_method: str = "cox_survival"
) -> list[dict]:
    """One example per individual coefficient of a fitted model -- gives
    downstream consumers (paper-writing) direct per-covariate access without
    parsing the nested full_result JSON of the model-level summary example."""
    exs = []
    for coef_name, coef_stats in model_result.get("coefficients", {}).items():
        exs.append(
            make_example(
                f"Coefficient '{coef_name}' from {model_label} ({context_desc}).",
                output_val=f"beta={coef_stats.get('beta')}, se={coef_stats.get('se')}, "
                f"p={coef_stats.get('p_value')}, "
                f"ci=[{coef_stats.get('ci_lower')},{coef_stats.get('ci_upper')}]",
                predict_method=predict_method,
                analysis_type="model_coefficient",
                model_label=model_label,
                coefficient_name=coef_name,
                full_result=coef_stats,
            )
        )
    return exs


def compile_examples(results: dict) -> list[dict]:
    examples = []

    pcf = results["primary_cox_fit"]
    reg = pcf["coefficients"].get("register_spoken", {})
    examples.append(
        make_example(
            "Primary Cox PH fit on gold-labeled spoken/written subset "
            "(en_childes/en_ewt, fr_rhapsodie/fr_gsd, sl_sst/sl_ssj): "
            "does spoken register reduce dependency-arc hazard (i.e. shorten "
            "arcs) relative to written, controlling for morphological richness, "
            "with language-clustered robust SEs?",
            output_val=f"register_spoken beta={reg.get('beta')}, HR={reg.get('hazard_ratio')}, p={reg.get('p_value')}",
            predict_method="cox_survival",
            analysis_type="primary_cox_fit",
            full_result=pcf,
        )
    )
    examples.extend(
        coefficient_examples(
            pcf, "primary_cox_gold_subset", "gold-labeled spoken/written subset, language-clustered SEs",
            predict_method="cox_survival",
        )
    )

    bl = results["primary_baseline_logit"]
    blreg = bl["coefficients"].get("register_spoken", {})
    examples.append(
        make_example(
            "Baseline (censoring-naive) logistic regression on median-split "
            "arc length, gold subset, same covariates as primary Cox -- the "
            "comparison method that ignores position-bounded censoring.",
            output_val=f"register_spoken beta={blreg.get('beta')}, OR={blreg.get('odds_ratio')}, p={blreg.get('p_value')}",
            predict_method="baseline_logit",
            analysis_type="primary_baseline_logit",
            full_result=bl,
        )
    )
    examples.extend(
        coefficient_examples(
            bl, "primary_baseline_logit_gold_subset", "gold-labeled subset, censoring-naive median-split logistic",
            predict_method="baseline_logit",
        )
    )

    fam_res = results["family_bootstrap_rankings"]
    for fam_row in fam_res["families"]:
        examples.append(
            make_example(
                f"Family-level bootstrap Nelson-Aalen residual (cumulative hazard "
                f"at d=10 minus pooled-corpus value) for family {fam_row['family_id']}, "
                f"{fam_res['method']}, BH-corrected across all families.",
                output_val=f"residual={fam_row['point_estimate_na_d10_residual']:.4f}, "
                f"bh_adjusted_p={fam_row.get('bh_adjusted_p')}, "
                f"bh_significant={fam_row.get('bh_significant')}",
                predict_method="bootstrap_nelson_aalen_bh",
                analysis_type="family_bootstrap_ranking",
                full_result=fam_row,
            )
        )

    fcc = results["full_corpus_cox"]
    freg = fcc["coefficients"].get("register_spoken", {})
    examples.append(
        make_example(
            "Secondary Cox PH fit on full 114,480-arc corpus (mixed gold + "
            "heuristic-treebank-level register labels), family as fixed effect, "
            "register + word-order + morphological-richness covariates.",
            output_val=f"register_spoken beta={freg.get('beta')}, HR={freg.get('hazard_ratio')}, p={freg.get('p_value')}",
            predict_method="cox_survival",
            analysis_type="full_corpus_cox",
            full_result=fcc,
        )
    )
    examples.extend(
        coefficient_examples(
            fcc, "full_corpus_cox_family_fixed_effect", "full 114,480-arc corpus, mixed gold+heuristic labels",
            predict_method="cox_survival",
        )
    )

    lns = results["label_noise_sensitivity"]
    for row in lns["trajectory"]:
        examples.append(
            make_example(
                f"Label-noise sensitivity: full-corpus Cox register coefficient "
                f"after randomly flipping {row['noise_level_pct']}% of heuristically-"
                f"labeled (non-gold-treebank) register labels.",
                output_val=f"register_beta={row['register_beta']}, ci=[{row['register_ci_lower']},{row['register_ci_upper']}]",
                predict_method="cox_survival",
                analysis_type="label_noise_sensitivity",
                full_result=row,
            )
        )

    wov = results["word_order_variants"]
    for variant_key in [
        "variant_A_grambank_categorical",
        "variant_B_ordinal_proxy_continuous",
        "variant_C_register_by_word_order_interaction",
    ]:
        v = wov[variant_key]
        vreg = v["coefficients"].get("register_spoken", {})
        examples.append(
            make_example(
                f"Word-order operationalization {variant_key}, full corpus "
                f"(gold subset has zero word-order variance -- see module "
                f"docstring for why).",
                output_val=f"register_spoken beta={vreg.get('beta')}, HR={vreg.get('hazard_ratio')}, p={vreg.get('p_value')}",
                predict_method="cox_survival",
                analysis_type="word_order_variant",
                full_result=v,
            )
        )
        examples.extend(
            coefficient_examples(
                v, variant_key, "word-order operationalization robustness check, full corpus",
                predict_method="cox_survival",
            )
        )

    rb = results["random_baseline"]
    examples.append(
        make_example(
            "Random-head-permutation null baseline: Nelson-Aalen cumulative "
            "hazard of observed dependency arcs vs. arcs with heads permuted "
            "uniformly within sentence-length bounds (same n, same censoring logic).",
            output_val=f"auc_difference={rb['auc_difference']:.4f}, "
            f"observed_mean_arc_length={rb['observed_mean_arc_length']:.3f}, "
            f"null_mean_arc_length={rb['null_mean_arc_length']:.3f}",
            predict_method="nelson_aalen_permutation_null",
            analysis_type="random_permutation_null",
            full_result=rb,
        )
    )

    return examples


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
@logger.catch(reraise=True)
def main(
    max_rows: int | None = None,
    n_bootstrap_reps: int = 500,
    output_path: str = "method_out.json",
):
    t_start = time.time()
    logger.info(f"=== Starting run: max_rows={max_rows}, n_bootstrap_reps={n_bootstrap_reps} ===")

    df = load_full_data(max_rows=max_rows)
    df = validate_and_featurize(df)

    gold_df = df[df["is_gold_treebank"]].copy()
    logger.info(
        f"Gold subset: n={len(gold_df)}, spoken={int((gold_df['register_spoken'] == 1).sum())}, "
        f"non-spoken={int((gold_df['register_spoken'] == 0).sum())}, "
        f"families={gold_df['family_id'].nunique()}, word_order_variance={gold_df['word_order_type'].nunique()}"
    )

    # ---- Phase 3: primary Cox on gold subset (family-invariant -> cluster by language) ----
    gold_df["morph_richness_std"], g_mean, g_std = standardize(gold_df["morph_richness_proxy"])
    primary_cox_fit = fit_cox(
        gold_df,
        "register_spoken + morph_richness_std",
        cluster_col="language_code",
        label="primary_cox_gold_subset_language_clustered",
    )
    primary_cox_fit["subset"] = "gold_labeled"
    primary_cox_fit["n_spoken"] = int((gold_df["register_spoken"] == 1).sum())
    primary_cox_fit["n_written"] = int((gold_df["register_spoken"] == 0).sum())
    primary_cox_fit["morph_richness_standardization"] = {"mean": g_mean, "std": g_std}
    primary_cox_fit["frailty_note"] = (
        "gold subset is 100% Indo-European (single family) in this sampled "
        "dataset; robust cluster-by-language_code SEs used in place of "
        "shared frailty by family (Fallback B1)"
    )

    baseline_logit_gold = fit_baseline_logit(
        gold_df, ["register_spoken", "morph_richness_std"], label="baseline_logit_gold_subset"
    )

    # ---- Phase 4-5: family-level bootstrap on FULL corpus + BH correction ----
    family_bootstrap = run_family_bootstrap(df, n_reps=n_bootstrap_reps, n_workers=NUM_WORKERS)
    family_bootstrap["families"] = apply_bh_correction(family_bootstrap["families"])
    n_sig = sum(1 for r in family_bootstrap["families"] if r["bh_significant"])
    logger.info(f"BH-significant family outliers: {n_sig} / {len(family_bootstrap['families'])}")

    # ---- Phase 6: secondary Cox on full corpus ----
    df["word_order_ordinal_std"] = np.nan
    valid_wo = df["word_order_ordinal"].notna()
    df.loc[valid_wo, "word_order_ordinal_std"], fw_mean, fw_std = standardize(
        df.loc[valid_wo, "word_order_ordinal"]
    )
    df["morph_richness_std"], fm_mean, fm_std = standardize(df["morph_richness_proxy"])
    full_corpus_df = df.dropna(subset=["word_order_ordinal_std"]).copy()
    full_corpus_df, family_dummy_cols = add_dummies(full_corpus_df, "family_id", "fam")
    full_corpus_cox = fit_cox(
        full_corpus_df,
        "register_spoken + word_order_ordinal_std + morph_richness_std + "
        + " + ".join(family_dummy_cols),
        cluster_col=None,
        label="full_corpus_cox_family_fixed_effect",
    )
    full_corpus_cox["n_total_input"] = int(len(df))
    full_corpus_cox["n_used_after_word_order_dropna"] = int(len(full_corpus_df))
    full_corpus_cox["n_heuristic_labeled"] = int((df["heuristic_label_source"] == "heuristic").sum())
    full_corpus_cox["n_gold_labeled"] = int((df["heuristic_label_source"] == "gold").sum())

    # ---- Phase 7: label-noise sensitivity ----
    label_noise = label_noise_sensitivity(
        full_corpus_df,
        noise_levels=[5, 10, 20],
        formula="register_spoken + word_order_ordinal_std + morph_richness_std",
    )

    # ---- Phase 8: word-order variants (full corpus) ----
    wo_variants = word_order_variants(df)

    # ---- Phase 9: random-head-permutation null baseline ----
    random_baseline = random_permutation_null(gold_df, n_sample=min(50000, len(gold_df)))

    elapsed = time.time() - t_start
    logger.info(f"=== All analyses complete in {elapsed:.1f}s ===")

    results = {
        "primary_cox_fit": primary_cox_fit,
        "primary_baseline_logit": baseline_logit_gold,
        "family_bootstrap_rankings": family_bootstrap,
        "full_corpus_cox": full_corpus_cox,
        "label_noise_sensitivity": label_noise,
        "word_order_variants": wo_variants,
        "random_baseline": random_baseline,
        "provenance": {
            "gold_subset": {
                "n_spoken": int((gold_df["register_spoken"] == 1).sum()),
                "n_written_or_web": int((gold_df["register_spoken"] == 0).sum()),
                "n_total": int(len(gold_df)),
                "treebanks": sorted(GOLD_TREEBANKS),
                "families_present": sorted(gold_df["family_id"].unique().tolist()),
                "word_order_types_present": sorted(
                    [w for w in gold_df["word_order_type"].unique().tolist() if isinstance(w, str)]
                ),
                "annotation_source": "gold_labeled_per_hypothesis",
            },
            "full_corpus": {
                "n_total": int(len(df)),
                "n_gold_labeled": int((df["heuristic_label_source"] == "gold").sum()),
                "n_heuristic_labeled": int((df["heuristic_label_source"] == "heuristic").sum()),
                "n_treebanks": int(df["treebank_id"].nunique()),
                "n_families": int(df["family_id"].nunique()),
                "annotation_source": "mixed_gold_and_heuristic",
            },
            "elapsed_seconds": elapsed,
            "num_cpus_used": NUM_WORKERS,
            "n_bootstrap_reps": n_bootstrap_reps,
        },
        "deviations_from_plan": [
            "Gold subset is 100% Indo-European family (single level) in this "
            "114,480-row stratified sample -> primary Cox uses robust "
            "cluster-by-language SEs instead of shared frailty-by-family.",
            "Gold subset has zero word-order-type variance (all six treebanks "
            "verb-medial/SVO) -> word-order variants (Phase 8) run on full "
            "corpus instead, where 3 word-order categories and 13 families vary.",
            "Family-level bootstrap residuals (Phase 4) run on full corpus "
            "(13 families) rather than gold subset, for the same reason.",
            "No continuous empirical word-order measure exists in the delivered "
            "dataset (only categorical Grambank word_order_type); Variant B uses "
            "an ordinal proxy (verb-initial<medial<final) and Variant C tests "
            "register x word-order interaction instead of a collinear 'both "
            "parallel' specification.",
            "Row counts (gold n=25,710; full n=114,480) reflect the stratified "
            "sample delivered by the dataset artifact, not the full 6.13M-arc "
            "extraction cited in the artifact plan's summary.",
        ],
    }

    examples = compile_examples(results)
    output = {
        "metadata": {
            "method_name": "cox_survival_vs_censoring_naive_logistic_UD_dependency_arcs",
            "description": "Survival analysis (Cox PH, censoring-aware) vs. baseline "
            "(logistic regression, censoring-naive) of UD dependency-arc lengths, "
            "testing spoken-register minimization, family-level outliers via "
            "bootstrap+BH-FDR, label-noise sensitivity, word-order operationalization "
            "robustness, and a random-head-permutation null baseline.",
            "n_bootstrap_reps": n_bootstrap_reps,
            "elapsed_seconds": elapsed,
        },
        "datasets": [{"dataset": "ud_dependency_survival_analysis", "examples": examples}],
    }

    out_path = WORKSPACE / output_path
    out_path.write_text(json.dumps(output, indent=2, default=str))
    logger.info(f"Wrote output to {out_path} ({out_path.stat().st_size / 1e6:.2f} MB)")
    return output


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--max-rows", type=int, default=None)
    parser.add_argument("--n-bootstrap-reps", type=int, default=500)
    parser.add_argument("--output", type=str, default="method_out.json")
    args = parser.parse_args()
    main(max_rows=args.max_rows, n_bootstrap_reps=args.n_bootstrap_reps, output_path=args.output)
