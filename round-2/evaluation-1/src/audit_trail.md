# Methodological Transparency Audit

## Gold-label source documentation

- **en**: en_childes (spoken) vs en_ewt (written). MacWhinney CHILDES corpus (child-directed/child speech transcripts, gold spoken-modality annotation) vs EWT (English Web Treebank, UD gold written). n_spoken(sample)=47012, n_written(sample)=93027. register classified via classify_register(): CoNLL-U comment modality/channel tags where present, else curated name-based fallback matching the treebank's known genuine gold spoken-corpus status (not majority-written default).
- **fr**: fr_rhapsodie (spoken) vs fr_gsd (written). Rhapsodie (Lacheret et al., gold prosody/spoken corpus) vs GSD (UD gold written). n_spoken(sample)=41025, n_written(sample)=115251. register classified via classify_register(): CoNLL-U comment modality/channel tags where present, else curated name-based fallback matching the treebank's known genuine gold spoken-corpus status (not majority-written default).
- **sl**: sl_sst (spoken) vs sl_ssj (written). SST (Slovenian Spoken/Spontaneous Treebank, gold transcribed speech) vs SSJ (UD gold written). n_spoken(sample)=63348, n_written(sample)=105847. register classified via classify_register(): CoNLL-U comment modality/channel tags where present, else curated name-based fallback matching the treebank's known genuine gold spoken-corpus status (not majority-written default).

## Word-order operationalization comparison

{
  "operationalizations_implemented": 1,
  "description": "Only ONE word-order operationalization is implemented in the iter-1 pipeline: empirical fraction of dependents preceding their head, computed directly per treebank from parsed head-position data (word_order_score). No second (e.g. WALS-fetched dominant-order class) operationalization was implemented, so no comparability/CI-overlap check across operationalizations is possible -- this is reported here as an honest audit finding, not fabricated.",
  "coefficient_in_full_cox_model": {
    "coef": -0.028272384721701235,
    "ci_lower": -0.03363361634514231,
    "ci_upper": -0.022911153098260157,
    "p": 4.851205828584694e-25
  },
  "recommendation": "A future iteration should add a second, independently-sourced word-order measure (e.g. WALS 81A dominant order) fitted on the identical 300k-arc subsample to test operationalization robustness."
}

## Label-noise sensitivity (heuristic-labeled rows only: ['it_kiparlaforest', 'it_parlamint', 'uk_parlamint', 'it_isdt', 'uk_iu'])

| noise level | coef | ci_lower | ci_upper | p | n |
|---|---|---|---|---|---|
| 0pct_flip | 0.01119024265540771 | 0.003571330863880752 | 0.018809154446934668 | 0.003993327480158677 | 258309 |
| 5pct_flip | 0.007459178642586277 | -0.00011807831349604312 | 0.015036435598668598 | 0.05367857291534252 | 258309 |
| 10pct_flip | 0.012717724919618067 | 0.005172379548616152 | 0.02026307029061998 | 0.0009547539157145836 | 258309 |
| 20pct_flip | 0.00540286693317198 | -0.002087502301842876 | 0.012893236168186835 | 0.15743864828621593 | 258309 |

## Bootstrap procedure specification (family outlier ranking)

{
  "iter1_family_ranking_had_bootstrap_ci": false,
  "iter1_note": "family_residual_hazard_ranking in the iter-1 output has no CI fields -- no bootstrap was run for the family outlier ranking in iter1. This evaluation adds one (below).",
  "n_replicates": 500,
  "sampling": "with replacement, resampling treebanks within each family (block bootstrap over treebanks, not individual arcs, to respect within-treebank arc correlation)",
  "random_seed": 20260813
}

### Bootstrap CI results (this evaluation)

n_replicates=500, seed=20260813

| family | n_treebanks_sampled | point_h10 | ci_lower | ci_upper | iter1_residual_hazard |
|---|---|---|---|---|---|
| Dravidian | 0 | None | None | None | None |
| NW-Caucasian | 2 | 3.619922459926899 | 3.1491123478760676 | 4.090732571977731 | 0.8328966688723298 |
| Anatolian | 0 | None | None | None | None |
| Sign | 0 | None | None | None | None |
| Turkic | 1 | None | None | None | None |
| Afro-Asiatic(Cushitic) | 1 | None | None | None | None |
| Iranian | 0 | None | None | None | None |
| Romance | 1 | None | None | None | None |
| Tai-Kadai | 0 | None | None | None | None |
| Baltic | 0 | None | None | None | None |
| Unclassified | 9 | 4.339421563150986 | 3.759251557693375 | 5.11325369662343 | 0.424684260611079 |
| Creole | 0 | None | None | None | None |
| Indo-Aryan | 3 | 4.017754728084793 | 2.654636325059429 | 5.736416818433054 | -0.4159598346016202 |
| Kartvelian | 0 | None | None | None | None |
| Hellenic | 5 | 3.0254796718938066 | 2.7846362402383518 | 3.316529746118509 | -0.3632750782359708 |
| Celtic | 1 | None | None | None | None |
| Semitic | 7 | 3.1164291857291184 | 2.537776017076086 | 3.945315478705177 | -0.3452085300247201 |
| Sino-Tibetan | 9 | 3.031233423758057 | 2.6609902018465252 | 3.5604462280920144 | -0.3335202206303012 |
| Mande | 1 | None | None | None | None |
| Armenian | 3 | 2.6859738985900052 | 2.6574879548589205 | 2.7158681165130094 | -0.29933526917316744 |
| Germanic | 4 | 2.7652851562098677 | 2.5648350103165938 | 3.025189572335765 | -0.25702035267432155 |
| Koreanic | 0 | None | None | None | None |
| Austronesian | 1 | None | None | None | None |
| Slavic | 7 | 2.764475441507367 | 2.6511659232564213 | 2.8757119822102966 | -0.19989035770411867 |
| Albanian | 2 | 3.00495792772909 | 2.8891570918151066 | 3.1207587636430736 | -0.1930148361132109 |
| Niger-Congo | 0 | None | None | None | None |
| Basque(isolate) | 1 | None | None | None | None |
| Afro-Asiatic(Chadic) | 0 | None | None | None | None |
| Austroasiatic | 0 | None | None | None | None |
| Japonic | 0 | None | None | None | None |
| Afro-Asiatic(Egyptian) | 2 | 2.8187781877891815 | 2.7900052723734046 | 2.8475511032049585 | -0.047175742494597994 |
| Uralic | 0 | None | None | None | None |