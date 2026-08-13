# Does spoken language shorten dependency links?

`demo/` — Self-contained demo (Colab-ready notebook or markdown). Run without setup.  
`src/` — Full source code, data, and outputs from the experiment execution.

**Type:** experiment  
**ID:** `art_AC8BwlWvA3iR`

## Layman Summary

We statistically test whether spoken sentences across English, French and Slovenian keep words and their grammatical partners closer together than written sentences do, using survival analysis to handle position-limited distances fairly.

## Full Summary

This experiment implements a censored survival-analysis pipeline over 114,480 Universal Dependencies dependency-arc records (28 treebanks, 20+ languages, 13 Glottolog families) to test whether spoken register minimizes dependency-arc length more than written register, and how word-order typology and morphological richness interact with that pattern. The core method (method.py) fits Cox proportional-hazards models where duration=arc_length and event=1 iff arc_length is strictly below its position-bounded censoring_bound (an arc that hits the maximum length structurally possible from its token's position is treated as censored, not as a fully observed outcome) -- the correct treatment for position-bounded dependency distances, which a naive analysis would silently miss. A baseline logistic regression on a median-dichotomized (long/short) arc length, ignoring censoring entirely, is fit on identical covariates for direct comparison. The pipeline covers: (1) a primary Cox fit on the gold-labeled spoken/written subset (en_childes/en_ewt, fr_rhapsodie/fr_gsd, sl_sst/sl_ssj; n=25,710 in this stratified sample) with robust cluster-by-language standard errors (adapted from the planned shared-frailty-by-family since the gold subset is 100% Indo-European in this sample, so family has zero variance there); (2) 500-replicate stratified bootstrap of family-level Nelson-Aalen cumulative-hazard-at-d=10 residuals (relative to the pooled corpus) across all 13 families present in the full corpus, with Benjamini-Hochberg FDR correction to flag confirmed family-level outliers; (3) a secondary Cox fit on the full 114,480-arc corpus with family as a fixed effect and mixed gold+heuristic register labels; (4) label-noise sensitivity analysis flipping 5/10/20% of heuristically-labeled register values and re-fitting; (5) three word-order operationalization variants (categorical Grambank word_order_type, an ordinal linear proxy, and a register-by-word-order interaction) run on the full corpus, since the gold subset also has zero word-order variance (all six gold treebanks are verb-medial/SVO) -- both of these deviations from the artifact plan are documented in the output's deviations_from_plan field; and (6) a random-head-permutation null baseline (heads reassigned uniformly within sentence-length bounds) compared via Nelson-Aalen curves and AUC difference against the observed data. All Cox fits use a small ridge penalizer for numerical stability under near-collinear typology covariates. Key results from the executed run: the censoring-aware primary Cox fit finds NO significant register effect on the gold subset (register_spoken beta=-0.032, HR=0.968, p=0.366), while the censoring-naive baseline logistic regression on the identical data DOES find a significant effect (beta=0.076, OR=1.079, p=0.006) -- a direct empirical demonstration that ignoring position-bounded censoring can manufacture spurious register effects; the full-corpus secondary Cox (mixed gold+heuristic labels, family fixed effects) is directionally consistent but only marginal (p=0.063); label-noise sensitivity shows the register coefficient staying small and stable in sign as 0/5/10/20% of heuristic labels are flipped; word-order variants A/B/C agree the register effect is small and non-significant regardless of operationalization; the family-level bootstrap flags 8 of 13 families as BH-significant outliers in position-relative hazard, i.e. substantial residual heterogeneity by language family after accounting for register; and the random-head-permutation null shows a large, clear separation from the observed data (mean arc length 3.38 observed vs. 8.77 under random head reassignment, Nelson-Aalen AUC difference 78.8), confirming strong general dependency-length minimization even though the specific spoken-vs-written contrast is weak in this sample. Output follows the exp_gen_sol_out schema: one dataset of 54 examples, each tagged metadata_analysis_type (primary_cox_fit, primary_baseline_logit, family_bootstrap_ranking, full_corpus_cox, label_noise_sensitivity, word_order_variant, random_permutation_null, model_coefficient) with full nested statistics in metadata_full_result. Downstream paper-writing steps should read metadata_full_result off each example for exact coefficients, CIs, p-values, and BH-adjusted significance flags rather than parsing the human-readable output/input strings.

## Dependencies

- `art_V4iFzwfu7i49` — gold-labeled dataset

## Output Files

- `method.py`
- `full_method_out.json`
- `mini_method_out.json`
- `preview_method_out.json`

## Demo Files

- **method.py** — Research methodology implementation

---
*Generated by AI Inventor Pipeline*
