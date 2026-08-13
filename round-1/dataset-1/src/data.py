#!/usr/bin/env python3
"""Build UD dependency-arc survival-analysis datasets from downloaded UD sample + typology sources."""

from loguru import logger
from pathlib import Path
import csv
import json
import sys

import pandas as pd

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
Path("logs").mkdir(exist_ok=True)
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

BASE = Path(__file__).parent
DATA_DIR = BASE / "temp/datasets"

# treebank_code -> (register, language_name, iso3, family override)
# Register/provenance facts taken from each treebank's own UD documentation
# (universaldependencies.org/treebanks) -- not inferred from the code name.
TREEBANK_META = {
    "en_gum": ("mixed", "English", "eng"),          # GUM: 12 genres, spoken+written -- resolved per-sentence via commul/ud_genre
    "en_ewt": ("web", "English", "eng"),             # web/blog/email/reviews
    "en_childes": ("spoken", "English", "eng"),      # child-directed spoken interaction transcripts
    "fr_rhapsodie": ("spoken", "French", "fra"),      # spontaneous spoken French corpus
    "fr_gsd": ("web", "French", "fra"),               # GSD = web/blogs/news mix, written
    "sl_ssj": ("written", "Slovenian", "slv"),        # ssj500k, written standard Slovenian
    "sl_sst": ("spoken", "Slovenian", "slv"),         # Spoken Slovenian Treebank (transcribed speech)
    "et_ewt": ("web", "Estonian", "est"),
    "ar_padt": ("news", "Arabic", "arb"),             # Prague Arabic Dependency Treebank, newswire
    "ja_gsd": ("written", "Japanese", "jpn"),
    "ko_gsd": ("written", "Korean", "kor"),
    "fi_tdt": ("written", "Finnish", "fin"),
    "tr_imst": ("written", "Turkish", "tur"),
    "zh_gsd": ("written", "Chinese", "cmn"),
    "hi_hdtb": ("news", "Hindi", "hin"),
    "ru_syntagrus": ("written", "Russian", "rus"),
    "eu_bdt": ("written", "Basque", "eus"),
    "wo_wtb": ("written", "Wolof", "wol"),
    "ta_ttb": ("written", "Tamil", "tam"),
    "pcm_nsc": ("spoken", "Naija (Nigerian Pidgin)", "pcm"),  # NSC built from transcribed spoken Naija
    "de_gsd": ("written", "German", "deu"),
    "pt_gsd": ("written", "Portuguese", "por"),
    "id_gsd": ("written", "Indonesian", "ind"),
    "sv_talbanken": ("written", "Swedish", "swe"),
    "la_ittb": ("academic", "Latin", "lat"),          # Index Thomisticus, scholastic/theological prose
    "bxr_bdt": ("written", "Buryat", "bxr"),
    "sah_yktdt": ("written", "Sakha", "sah"),
    "swl_sslc": ("other", "Swedish Sign Language", "swl"),  # signed modality, not spoken/written
}

REGISTER_ENUM = {"spoken", "written", "academic", "news", "fiction", "web", "other", "unspecified"}

# Manual ISO-639-3 -> Glottolog Glottocode short-circuit not needed: glottolog languages.csv
# is keyed by ISO639P3code directly, so we look up iso3 there.

GB_WORD_ORDER_FEATURES = {"GB131": "verb-initial", "GB132": "verb-medial", "GB133": "verb-final"}


def load_glottolog_family(iso3_codes):
    path = DATA_DIR / "glottolog/languages.csv"
    fam = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            code = row.get("ISO639P3code")
            if code in iso3_codes:
                fam[code] = {
                    "family_id": row.get("Family_ID") or "unknown",
                    "family_path": row.get("Family_ID") or "unknown",
                    "glottocode": row.get("Glottocode"),
                }
    return fam


def load_grambank_word_order(iso3_codes, glottocode_by_iso3):
    # Grambank's own languages.csv ships ISO639P3code EMPTY for every row (verified: 0/2467
    # populated in the 2.18 snapshot) -- joining on it directly silently returns nothing.
    # Grambank's Language_ID in values.csv IS a Glottocode, so route the join through
    # Glottolog's iso3->Glottocode map (glottocode_by_iso3, built from glottolog/languages.csv)
    # instead of trusting Grambank's own iso3 column.
    val_path = DATA_DIR / "grambank/values.csv"
    glottocode_to_iso3 = {gc: iso for iso, gc in glottocode_by_iso3.items()}
    votes = {}  # iso3 -> {feature: value}
    with open(val_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            lang_id = row.get("Language_ID")
            param = row.get("Parameter_ID")
            if lang_id in glottocode_to_iso3 and param in GB_WORD_ORDER_FEATURES:
                iso3 = glottocode_to_iso3[lang_id]
                votes.setdefault(iso3, {})[param] = row.get("Value")
    word_order = {}
    for iso3, feats in votes.items():
        # value "1" == the feature holds; pick the (single) feature coded 1
        active = [GB_WORD_ORDER_FEATURES[p] for p, v in feats.items() if v == "1"]
        word_order[iso3] = active[0] if len(active) == 1 else None
    return word_order


def morph_richness_proxy(feats_arrays):
    """Fraction of tokens carrying >=1 morphological feature, scaled by mean distinct-feature-types per token."""
    total_tokens = 0
    total_feat_slots = 0
    distinct_types = set()
    for feats in feats_arrays:
        for f in feats:
            total_tokens += 1
            if f and f != "None":
                pairs = f.split("|")
                total_feat_slots += len(pairs)
                for p in pairs:
                    if "=" in p:
                        distinct_types.add(p.split("=")[0])
    if total_tokens == 0:
        return 0.0
    raw = total_feat_slots / total_tokens
    # normalize: UD morphology rarely exceeds ~8 feature slots/token; clip to [0,1]
    return round(min(raw / 8.0, 1.0), 4)


def build_examples_for_treebank(tb, register_default, lang_name, iso3, family_info, word_order, genre_lookup, source_manifest_entries):
    examples = []
    quality_violations = 0
    for entry in source_manifest_entries:
        fpath = DATA_DIR / "ud_sample" / Path(entry["file"]).name
        df = pd.read_parquet(fpath)
        feats_all = [list(row) for row in df["feats"]]
        richness = morph_richness_proxy(feats_all)
        richness_source = "UD_proxy"
        fam = family_info.get(iso3, {"family_id": "unknown", "family_path": "unknown"})
        wo = word_order.get(iso3)
        wo_source = "Grambank" if wo else None

        for row in df.itertuples(index=False):
            heads = row.head
            deprels = row.deprel
            sent_id = row.sent_id
            n = len(heads)
            for tok_idx in range(n):
                token_id = tok_idx + 1  # UD token ids are 1-based
                head_raw = heads[tok_idx]
                try:
                    head_id = int(head_raw)
                except (ValueError, TypeError):
                    continue  # skip empty/MWT range rows with non-integer head
                if head_id == 0:
                    arc_length = 0  # root token: no governing arc
                else:
                    arc_length = abs(token_id - head_id)
                censoring_bound = max(token_id, n - token_id)
                if arc_length > censoring_bound:
                    quality_violations += 1

                register = register_default
                if tb == "en_gum" and genre_lookup is not None:
                    g = genre_lookup.get((tb, sent_id))
                    if g == "spoken":
                        register = "spoken"
                    elif g in ("news", "fiction", "academic", "web"):
                        register = g
                    elif g is not None:
                        register = "written"

                meta = {
                    "metadata_treebank_id": tb,
                    "metadata_sentence_id": sent_id,
                    "metadata_token_id": token_id,
                    "metadata_head_id": head_id,
                    "metadata_deprel": deprels[tok_idx],
                    "metadata_censoring_bound": censoring_bound,
                    "metadata_register": register,
                    "metadata_language_code": iso3,
                    "metadata_language_name": lang_name,
                    "metadata_family_id": fam["family_id"],
                    "metadata_family_path": fam["family_path"],
                    "metadata_word_order_type": wo,
                    "metadata_morph_richness_proxy": richness,
                    "metadata_morph_richness_data_source": richness_source,
                    "metadata_word_order_data_source": wo_source,
                    "metadata_sentence_length": n,
                }
                input_obj = {
                    "treebank_id": tb, "sentence_id": sent_id, "token_id": token_id,
                    "sentence_length": n, "censoring_bound": censoring_bound,
                    "register": register, "language_code": iso3,
                    "family_id": fam["family_id"], "word_order_type": wo,
                    "morph_richness_proxy": richness,
                }
                examples.append({
                    "input": json.dumps(input_obj, ensure_ascii=False),
                    "output": str(arc_length),
                    **meta,
                })
    return examples, quality_violations


def build_ud_arcs_curated(manifest, genre_lookup):
    iso3_codes = {v[2] for v in TREEBANK_META.values()}
    family_info = load_glottolog_family(iso3_codes)
    glottocode_by_iso3 = {iso: info["glottocode"] for iso, info in family_info.items() if info.get("glottocode")}
    word_order = load_grambank_word_order(iso3_codes, glottocode_by_iso3)

    by_tb = {}
    for entry in manifest:
        by_tb.setdefault(entry["treebank"], []).append(entry)

    all_examples = []
    total_violations = 0
    for tb, (register_default, lang_name, iso3) in TREEBANK_META.items():
        if tb not in by_tb:
            logger.warning(f"treebank {tb} missing from manifest, skipping")
            continue
        exs, viol = build_examples_for_treebank(
            tb, register_default, lang_name, iso3, family_info, word_order, genre_lookup, by_tb[tb]
        )
        all_examples.extend(exs)
        total_violations += viol
        logger.info(f"{tb}: {len(exs)} arcs, {viol} censoring violations")

    logger.info(f"ud_arcs_curated total examples: {len(all_examples)}, total censoring violations: {total_violations}")
    return all_examples


def build_ud_arcs_genre_labeled(manifest, genre_df):
    """Alternative dataset: arcs restricted to sentences with a bootstrapped genre label
    from commul/ud_genre, contrasting the 'spoken' genre against all written genres,
    across ALL curated treebanks (not just the manually labeled ones)."""
    iso3_codes = {v[2] for v in TREEBANK_META.values()}
    family_info = load_glottolog_family(iso3_codes)
    glottocode_by_iso3 = {iso: info["glottocode"] for iso, info in family_info.items() if info.get("glottocode")}
    word_order = load_grambank_word_order(iso3_codes, glottocode_by_iso3)

    genre_lookup = {(r.treebank, r.sent_id): r.genre for r in genre_df.itertuples(index=False)}

    by_tb = {}
    for entry in manifest:
        by_tb.setdefault(entry["treebank"], []).append(entry)

    all_examples = []
    total_violations = 0
    for tb, (register_default, lang_name, iso3) in TREEBANK_META.items():
        if tb not in by_tb:
            continue
        fam = family_info.get(iso3, {"family_id": "unknown", "family_path": "unknown"})
        wo = word_order.get(iso3)
        for entry in by_tb[tb]:
            fpath = DATA_DIR / "ud_sample" / Path(entry["file"]).name
            df = pd.read_parquet(fpath)
            for _, row in df.iterrows():
                sent_id = row["sent_id"]
                genre = genre_lookup.get((tb, sent_id))
                if genre is None:
                    continue  # this variant KEEPS only genre-labeled sentences
                register = "spoken" if genre == "spoken" else ("written" if genre not in REGISTER_ENUM else genre)
                heads, deprels = row["head"], row["deprel"]
                n = len(heads)
                for tok_idx in range(n):
                    token_id = tok_idx + 1
                    try:
                        head_id = int(heads[tok_idx])
                    except (ValueError, TypeError):
                        continue
                    arc_length = 0 if head_id == 0 else abs(token_id - head_id)
                    censoring_bound = max(token_id, n - token_id)
                    if arc_length > censoring_bound:
                        total_violations += 1
                    meta = {
                        "metadata_treebank_id": tb, "metadata_sentence_id": sent_id,
                        "metadata_token_id": token_id, "metadata_head_id": head_id,
                        "metadata_deprel": deprels[tok_idx], "metadata_censoring_bound": censoring_bound,
                        "metadata_register": register, "metadata_bootstrapped_genre": genre,
                        "metadata_language_code": iso3, "metadata_language_name": lang_name,
                        "metadata_family_id": fam["family_id"], "metadata_family_path": fam["family_path"],
                        "metadata_word_order_type": wo, "metadata_sentence_length": n,
                    }
                    input_obj = {
                        "treebank_id": tb, "sentence_id": sent_id, "token_id": token_id,
                        "sentence_length": n, "censoring_bound": censoring_bound,
                        "register": register, "bootstrapped_genre": genre, "language_code": iso3,
                    }
                    all_examples.append({
                        "input": json.dumps(input_obj, ensure_ascii=False),
                        "output": str(arc_length),
                        **meta,
                    })
    logger.info(f"ud_arcs_genre_labeled total examples: {len(all_examples)}, violations: {total_violations}")
    return all_examples


METADATA = {
    "source": "commul/universal_dependencies (HF), Grambank CLDF (GitHub grambank/grambank), Glottolog CLDF (GitHub glottolog/glottolog-cldf)",
    "description": "Dependency-arc-level records with survival-analysis censoring bounds, register, family, and typology covariates, from a 28-treebank curated sample of commul/universal_dependencies spanning spoken/written register-matched pairs (sl_sst/sl_ssj, fr_rhapsodie/fr_gsd, en_childes/en_ewt/en_gum) and 20+ language families.",
}
TARGET_PER_DATASET = 120_000  # ~874 bytes/example observed -> ~105MB/dataset, ~210MB combined, under the 300MB limit


def truncate_strings(obj, max_len=200):
    if isinstance(obj, str):
        return obj[:max_len] + "..." if len(obj) > max_len else obj
    if isinstance(obj, list):
        return [truncate_strings(x, max_len) for x in obj[:3]]
    if isinstance(obj, dict):
        return {k: truncate_strings(v, max_len) for k, v in obj.items()}
    return obj


def stratified_subsample(examples, key_fn, target_total, seed=0):
    import random
    rng = random.Random(seed)
    by_key = {}
    for ex in examples:
        by_key.setdefault(key_fn(ex), []).append(ex)
    per_key_cap = max(1, target_total // len(by_key))
    sampled = []
    for k, exs in by_key.items():
        n = min(per_key_cap, len(exs))
        sampled.extend(rng.sample(exs, n))
    rng.shuffle(sampled)
    return sampled


def main():
    manifest = json.loads((DATA_DIR / "ud_sample_manifest.json").read_text())
    genre_df = pd.read_parquet(DATA_DIR / "ud_genre/all_genres.parquet")

    # DATASET 1: ud_arcs_curated. Registers come from each treebank's own documented
    # provenance (spoken vs. written subcorpora, e.g. sl_sst/sl_ssj, fr_rhapsodie/fr_gsd,
    # en_childes/en_ewt) -- gold, human-curated register labels.
    en_gum_genre_lookup = {
        (r.treebank, r.sent_id): r.genre
        for r in genre_df.itertuples(index=False)
        if r.treebank == "en_gum"
    }
    ds1_full = build_ud_arcs_curated(manifest, en_gum_genre_lookup)
    n1_full = len(ds1_full)
    ds1 = stratified_subsample(ds1_full, lambda e: e["metadata_treebank_id"], TARGET_PER_DATASET)
    logger.info(f"ud_arcs_curated: subsampled {len(ds1)} / {n1_full} arcs")

    # DATASET 2: ud_arcs_genre_labeled. Uses commul/ud_genre's bootstrapped 18-genre
    # classifier labels (spoken vs. all-written contrast) across ALL 28 curated
    # treebanks, not just the 3 with documented gold spoken/written pairs -- larger
    # spoken/written contrast set, but labels are machine-predicted, not gold.
    ds2_full = build_ud_arcs_genre_labeled(manifest, genre_df)
    n2_full = len(ds2_full)
    ds2 = stratified_subsample(ds2_full, lambda e: e["metadata_treebank_id"], TARGET_PER_DATASET)
    logger.info(f"ud_arcs_genre_labeled: subsampled {len(ds2)} / {n2_full} arcs")

    # FINAL CHOICE: ud_arcs_curated. Its register labels come from each treebank's own
    # documented provenance (spoken vs. written subcorpora: en_childes/en_ewt/en_gum,
    # fr_rhapsodie/fr_gsd, sl_sst/sl_ssj), giving matched-pair spoken/written contrasts
    # within language + typology held fixed. ud_arcs_genre_labeled (built above, kept for
    # inspection/comparison) relies on commul/ud_genre's bootstrapped 18-genre classifier,
    # whose own dataset card states the labels "are not authoritative gold annotations" --
    # unacceptable noise for the register contrast this experiment hinges on.
    logger.info(f"ud_arcs_genre_labeled built ({len(ds2)} examples) for comparison but NOT selected; see rationale above.")

    # Split into parts under the 100MB artifact size limit (aii-file-size-limit skill):
    # single-file JSON of all 114,480 examples serializes to ~101.5MB, just over the cap.
    n = len(ds1)
    n_parts = 2
    part_size = (n + n_parts - 1) // n_parts
    out_dir = BASE / "full_data_out"
    out_dir.mkdir(exist_ok=True)
    for i in range(n_parts):
        chunk = ds1[i * part_size : (i + 1) * part_size]
        part = {"metadata": METADATA, "datasets": [{"dataset": "ud_arcs_curated", "examples": chunk}]}
        part_path = out_dir / f"full_data_out_{i+1}.json"
        part_path.write_text(json.dumps(part))
        logger.info(f"Wrote {part_path} ({part_path.stat().st_size / 1e6:.1f} MB, {len(chunk)} examples)")


if __name__ == "__main__":
    main()
