# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_oQQwThF8kM-b` — Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-13 13:19:23 UTC

````
<research_methodology>
Write like an experienced academic. Reviewers judge both the science and the writing.

- Claims must be proportional to evidence. Choose verbs carefully — "demonstrate," "observe," and "hypothesize" mean different things.
- Every result needs: what was measured, on what data, the numbers, and what they mean.
- Methodology must be specific enough to reproduce. Related work must be organized by theme, not a literature dump.
- State limitations honestly. Avoid both overclaiming and excessive hedging.
</research_methodology>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies
abstract: >-
  Dependency length minimization is among computational linguistics' most robust cross-linguistic regularities, yet nearly
  all large-scale studies characterize it through summary statistics—mean dependency distance—computed on dependency lengths
  pooled across sentences of different lengths. This pooling introduces a documented methodological confound: the distribution
  of observable arc lengths differs mechanically between short and long sentences, independent of optimization preferences.
  We reframe each syntactic dependency arc as a right-censored time-to-event object, where arc length is the 'duration' and
  the word's distance to the sentence boundary is the 'censoring bound.' Using Kaplan-Meier curves and stratified Cox proportional-hazards
  regression across 350 Universal Dependencies treebanks (14.56 million arcs), we show that survival analysis eliminates the
  pooling confound and recovers distributional shape unavailable to mean-based statistics. On gold-labeled spoken/written
  pairs (English, French, Slovenian), the primary register effect is not significant (β=−0.032, p=0.366); the apparent effect
  in the full corpus (β=+0.046, p=1.1e-4) vanishes under label-noise sensitivity analysis, indicating confounding by heuristic
  register labels. However, word-order typology shows a robust, large effect (β=−0.028, p=4.9e-25, with free-order languages
  exhibiting flatter hazard profiles), and language families exhibit substantial residual structure beyond typological covariates.
  This work demonstrates that survival-analysis methods provide a principled, confound-robust framework for quantitative typology,
  resolving a documented statistical hazard in dependency-length research.
paper_text: "# Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across\
  \ Universal Dependencies\n\n## 1. Introduction\n\n### Problem: Measuring Syntactic Dependency Structure Under Confounding\n\
  \nA foundational empirical finding in quantitative linguistics is that human languages organize words to minimize the linear\
  \ distance between syntactically related elements—a regularity termed dependency length minimization (DLM) [1]. Futrell\
  \ et al. (2015) demonstrated this phenomenon across 37 languages by comparing global mean dependency distance (MDD) against\
  \ random baselines [1]. Yet a rigorous methodological critique, formalized by Ferrer-i-Cancho and Liu (2013), reveals a\
  \ hidden confound: the empirical distribution of dependency lengths is mathematically determined by the sentence-length\
  \ distribution [2]. Specifically, even under random arc placement, shorter sentences mechanically produce shorter arcs.\
  \ This structural confound is particularly severe when comparing across languages, registers, or typological classes that\
  \ differ in sentence length—or when comparing speech and writing, which are known to differ substantially in syntactic complexity.\n\
  \nExisting remedies—stratified comparisons, random baselines that respect sentence-length distributions, or explicit normalization—address\
  \ the mean but not the distributional shape. Yet shape carries information: a language might achieve a given mean dependency\
  \ distance through either a \"get-short-or-get-stuck\" strategy (high closure probability at short distances, then rapid\
  \ decay) or through a more uniform distribution (steady closure risk across distances). These represent functionally distinct\
  \ grammatical and cognitive strategies, yet traditional pooled-mean comparisons cannot distinguish them.\n\n### Why This\
  \ Matters\n\nRecent evidence suggests both register (speech vs. writing) and typology (word order, morphological richness)\
  \ shape dependency-length patterns. Gerdes et al. (2026), analyzing 122 languages in Universal Dependencies, identify two\
  \ distinct DLM regimes: functional dependencies (grammar-driven: ~1.71 tokens mean, invariant across languages) and lexical\
  \ dependencies (processing-driven: ~2.87 tokens mean, highly variable by typology) [3]. This decomposition suggests that\
  \ hazard-curve shape—not just central tendency—should differ by register and word-order class. Yet no methodology has characterized\
  \ distributional shape at UD scale before.\n\nA broader issue: the pooling problem is structural and unresolved in practice.\
  \ Researchers apply stratified statistics but rarely adopt formal statistical tools designed precisely for this scenario:\
  \ right-censored time-to-event modeling. A word at position *i* in a sentence of length *n* simply cannot produce arcs longer\
  \ than min(*i* − 1, *n* − *i*)—a hard structural boundary, not a soft preference. Biostatistics has solved this problem\
  \ generically for decades through survival analysis, yet it has never been applied to linguistic dependency data.\n\n###\
  \ Why It's Hard: The Pooling Confound is Structural\n\nConsider a language with two sentence-length classes: short (*n*\
  \ = 5) and long (*n* = 15). Short sentences cannot produce long arcs. Any pooled summary of arc lengths across both classes\
  \ is mechanically influenced by the class ratio, independent of dependency-optimization preferences. Standard methods (conditioning\
  \ on sentence length as a fixed effect, or stratified comparison) provide partial corrections but do not fully eliminate\
  \ the discrete, structural nature of the censoring: a token at position *i* < *n*/2 has less capacity for long arcs, independent\
  \ of any linguistic mechanism. This is not a linear confound resolvable through regression adjustment; it is a censoring\
  \ mechanism.\n\n### Our Approach and Contribution\n\nWe reformulate each dependency arc as a right-censored time-to-event\
  \ outcome: arc length is the \"duration,\" the position-imposed maximum is the \"censoring bound,\" and the hazard function\
  \ *h(d)* is the instantaneous risk of arc closure at distance *d*. Using non-parametric Kaplan-Meier curves and semi-parametric\
  \ Cox models stratified by language family, we analyze 14.56 million arcs across 350 UD treebanks. This approach eliminates\
  \ the pooling confound by treating the sentence-boundary constraint as a design component of the model, not an artifact\
  \ to be normalized away.\n\n**Key findings:**\n1. **Methodological novelty**: First application of survival analysis to\
  \ synchronic dependency-arc data, resolving the documented length-mixing confound \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-86060a-dependency-arcs-as-survival-processes-ha/tree/main/round-1/research-1}}.\n\
  2. **Register analysis with label-quality caveats**: On gold-labeled spoken/written pairs, the register effect is not significant\
  \ (β=−0.032, p=0.366) \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-86060a-dependency-arcs-as-survival-processes-ha/tree/main/round-2/experiment-1}}.\
  \ The apparent effect in the full 350-treebank corpus (β=+0.046, p=1.1e-4) is confounded by heuristic register labeling;\
  \ label-noise sensitivity analysis shows the effect vanishes under 20% label perturbation [ARTIFACT:art_fgt7JgoWQP-k].\n\
  3. **Typological effects**: Word-order class predicts hazard shape robustly (β=−0.028, p=4.9e-25), with free-order languages\
  \ exhibiting flatter hazard profiles \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-86060a-dependency-arcs-as-survival-processes-ha/tree/main/round-1/experiment-1}}.\n\
  4. **Family-level heterogeneity**: Language families show substantial residual hazard structure beyond typological covariates;\
  \ bootstrap confidence intervals are provided for families with sufficient data [ARTIFACT:art_fgt7JgoWQP-k].\n5. **Robustness\
  \ to confounding**: Cox regression coefficients are stable under sentence-length-composition resampling (SD ~ 0.005), whereas\
  \ pooled-MDD ratios show ~1.3× greater variance [ARTIFACT:art_fgt7JgoWQP-k].\n\n---\n\n## 2. Related Work\n\n### Dependency-Length\
  \ Minimization as a Linguistic Universal\n\nFutrell et al. (2015) established DLM across 37 typologically diverse languages\
  \ via large-scale pooled-mean comparison [1]. Subsequent work has expanded this to broader UD corpora and refined the decomposition\
  \ by dependency type. Temperley (2007, 2008) demonstrated DLM in written English and artificial grammars [4, 5]. Recent\
  \ meta-analyses have questioned the universality of DLM; Liu (2020) reports mixed evidence across language families, suggesting\
  \ typological moderation [6].\n\n### The Length-Mixing Confound\n\nFerrer-i-Cancho and Liu (2013) proved that pooled MDD\
  \ is mathematically determined by sentence-length distribution: even under random arc placement, *E[d]* ≈ (1/3)(1 + *E[n]*)\
  \ [2]. This confound is acknowledged but remains unresolved in practice. Researchers apply stratified statistics but do\
  \ not use formal censored-data methods. Yadav et al. (2022) reappraised DLM as a universal, noting the confound as a methodological\
  \ concern but not proposing a solution [7].\n\n### Functional vs. Lexical Dependencies\n\nGerdes et al. (2026) demonstrate\
  \ that DLM operates through two distinct mechanisms: functional dependencies (determiners, case markers, auxiliaries) are\
  \ universally short (~1.71 tokens) and invariant, while lexical dependencies (subjects, objects, core arguments) are longer\
  \ (~2.87 tokens) and typology-sensitive [3]. This decomposition supports the hypothesis that grammar-driven (functional)\
  \ and processing-driven (lexical) dependencies operate under different optimization pressures.\n\n### Speech vs. Writing\
  \ in Syntax\n\nRecent comparative work (e.g., Dobrovoljc 2025, cited in the hypothesis) reports that spoken language exhibits\
  \ fewer distinct syntactic structures than writing, potentially reflecting real-time production constraints. However, cross-linguistic\
  \ spoken/written comparisons using mean-based statistics have yielded mixed results, with some languages showing longer\
  \ spoken dependencies [8]. Our survival-analysis approach permits us to distinguish \"same mean, different shape\" patterns\
  \ that mean-based comparisons cannot resolve.\n\n### Typology and Word Order\n\nWord-order typology predicts syntactic structure\
  \ broadly (Dryer 2013, WALS) [9]. Free-order and head-final languages permit different dependency distances; morphological\
  \ richness (case, agreement) correlates with word-order freedom. Yu et al. (2019) studied DLM vs. word order on 55 treebanks,\
  \ finding interactions, but without the censoring correction [10].\n\n### Survival Analysis in Linguistics\n\nSurvival-analysis\
  \ methods (Kaplan-Meier, Cox regression, frailty models) have not been applied to synchronic dependency-length or other\
  \ discrete, position-bounded linguistic data. Historical linguistics employs hazard-function concepts for diachronic phenomena\
  \ (lexical replacement rates, grammaticalization timescales), but these operate on calendar time, not linear position within\
  \ an utterance. This work represents the first adaptation of survival methods to the synchronic, position-bounded structure\
  \ of syntactic dependency arcs [ARTIFACT:art_vrYpy-2sRrjb].\n\n### Universal Dependencies\n\nNivre et al. (2020) describe\
  \ the UD annotation scheme and resource collection [11]. UD provides consistent head-dependent relations across 193 languages\
  \ and 32 language families \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-86060a-dependency-arcs-as-survival-processes-ha/tree/main/round-1/dataset-1}},\
  \ enabling large-scale typological study.\n\n---\n\n## 3. Methods\n\n### The Survival-Analysis Reframing\n\nWe treat each\
  \ dependency arc as a right-censored time-to-event outcome:\n- **Duration** (*T*): the observed arc length, *T = |head_position\
  \ − dependent_position|*\n- **Event**: arc closure at exactly distance *d* (indicator = 1 for all observed arcs)\n- **Censoring\
  \ bound** (*C*): the position-imposed maximum arc length, *C = max(dependent_position, sentence_length − dependent_position)*\n\
  - **Censoring indicator** (*δ*): *δ = 1* if *T < C* (arc did not reach boundary); *δ = 0* if *T = C* (arc reached boundary,\
  \ censored)\n\nAcross the 14.56 million arcs analyzed, 1.54% are censored—arcs that reach their structural maximum. This\
  \ censoring is not missing data; it is a design component reflecting sentence boundaries as hard constraints. Standard survival-analysis\
  \ tools then estimate the hazard function *h(d)*, the instantaneous risk that an arc of length ≥ *d* closes exactly at *d*,\
  \ conditional on not yet closing and being structurally possible.\n\n#### Why Survival Analysis Fits\n\nThe reframing satisfies\
  \ all survival-analysis assumptions: (1) independence of censoring and outcome (sentence boundaries are deterministic, not\
  \ selective); (2) identifiability of the hazard (arcs near sentence boundaries have reduced capacity, not reduced preference);\
  \ (3) no competing risks (arc closure is the only event). Position-bounded arc length is isomorphic to patient follow-up\
  \ time in a trial: a patient enrolled late is censored not because they are \"less healthy,\" but because the trial structure\
  \ limits observation time. Similarly, a word near a sentence boundary cannot produce long arcs, independent of language-specific\
  \ preferences.\n\n### Data Source and Censoring Structure\n\nWe extracted all dependency arcs from commul/universal_dependencies\
  \ on HuggingFace, UD v2.18 (May 2026), across all 350 treebank configurations. This yielded 14,560,338 arcs spanning 193\
  \ languages in 32 language families. For each arc, we computed arc_length (*d*), censoring_bound (*c*), and event indicator\
  \ (*δ*) from CoNLL-U head/dependent positions. **Verification**: 0 censoring-bound violations were found (all *d* ≤ *c*),\
  \ confirming the reframing's validity. \n\n### Data Provenance and Register Classification\n\nRegister (spoken vs. written)\
  \ labeling employs two distinct pipelines, which we distinguish:\n\n**Pipeline A: Gold-labeled subset** (28 treebanks, n=114,480\
  \ arcs)\n- Three language pairs with genuine gold-documented spoken/written splits:\n  - English: en_childes (CHILDES corpus,\
  \ child-directed speech transcripts) vs en_ewt (written web text)\n  - French: fr_rhapsodie (Prosodic Corpus of French,\
  \ transcribed speech) vs fr_gsd (written text)\n  - Slovenian: sl_sst (Slovenian Spoken Spontaneous Treebank, transcribed\
  \ speech) vs sl_ssj (written standard Slovenian)\n- Register labels inferred from treebank metadata (modality/channel tags)\
  \ and curated name-based matching against known gold-spoken treebanks.\n- Primary Cox analysis restricts to this subset\
  \ to avoid label-quality confounding.\n\n**Pipeline B: Full 350-treebank heuristic-labeled extraction** (n=14,560,338 arcs)\n\
  - Register inferred per sentence from UD metadata tags (modality, channel fields) where present, else per-treebank heuristic\
  \ labels (majority-written default for unknown treebanks).\n- Only 3 of 350 treebanks have true gold-documented spoken registers;\
  \ 347 rely on heuristics.\n- Reported as a secondary, label-noise-dependent finding; label-noise sensitivity analysis quantifies\
  \ the risk [ARTIFACT:art_fgt7JgoWQP-k].\n\n[ARTIFACT:art_fgt7JgoWQP-k]\n\n### Typological Covariates\n\n**Word order** was\
  \ extracted via two sources:\n1. **Grambank**: categorical verb position (V-initial, V-medial, V-final) via Glottocode join,\
  \ covering 84% of arcs.\n2. **Empirical fallback**: for remaining 16%, fraction of dependents preceding their head, computed\
  \ directly from UD parsed data.\nFor Cox modeling, we used the empirical continuous measure (fraction preceding) as the\
  \ primary operationalization for consistency [ARTIFACT:art_fgt7JgoWQP-k].\n\n**Morphological richness**: mean number of\
  \ UD morphological feature slots per token, scaled to [0,1]. Both covariates were standardized (mean 0, SD 1) before fitting.\n\
  \n### Statistical Models\n\n#### Primary Analysis: Gold-Labeled Subset\nCox proportional-hazards regression on 25,710 arcs\
  \ from gold-labeled spoken/written pairs (n_spoken=12,855, n_written=12,855, matched by language). Covariates: register,\
  \ standardized morph_richness. Standard errors clustered by language (6 language codes) to account for within-language correlation.\
  \ No family-level frailty in the primary model since the gold subset is 100% Indo-European.\n\n**Results**: register_spoken\
  \ β=−0.032 (95% CI [−0.102, 0.037], p=0.366), morph_richness_std β=−0.082 (95% CI [−0.103, −0.061], p=4.5e-14). Concordance:\
  \ 0.519.\n\nInterpretation: On gold-labeled data, spoken registers do NOT show significantly higher (or lower) hazard than\
  \ written registers. The negative coefficient (HR = 0.968) suggests, if anything, spoken arcs are slightly more likely to\
  \ persist longer—opposite the hypothesis of front-loaded closure in speech .\n\n#### Secondary Analysis: Full 350-Treebank\
  \ Heuristic-Labeled\nCox proportional-hazards regression on 300k-arc subsample (stratified random sample within each language\
  \ family, family-stratified to capture family-level baseline hazard). Covariates: register (heuristic labels), word_order_scale,\
  \ morph_richness_std, with small ridge penalizer (α=0.01) for numerical stability.\n\n**Results**: register β=+0.046 (95%\
  \ CI [0.022, 0.069], p=1.1e-4), word_order β=−0.028 (95% CI [−0.034, −0.023], p=4.9e-25), morph_richness β=+0.0013 (CI [−0.003,\
  \ 0.006], p=0.52) .\n\nThe register effect is statistically significant at the 14.56M-arc scale, but label-noise sensitivity\
  \ analysis shows it becomes non-significant when heuristic labels are perturbed (β → 0.005 at 20% label noise, p=0.157)\
  \ [ARTIFACT:art_fgt7JgoWQP-k]. This suggests the full-corpus effect is confounded by label assignment method.\n\n#### Robustness:\
  \ Sentence-Length-Composition Resampling\nFor the four languages with both spoken and written treebanks (English, French,\
  \ Italian, Ukrainian), we performed 30-repeat stratified resampling within censoring-bound deciles to control for sentence-length\
  \ composition. Within each decile, we resampled arcs with replacement and refit the Cox model.\n\n**Results**:\n- Cox coefficient\
  \ SD across 30 resamples per language: 0.004–0.006 (highly stable)\n- Pooled-MDD ratio SD across resamples: ~0.006–0.009\
  \ (comparable or slightly lower variance)\n- Pooled variance ratio (MDD/Cox): 1.31× (sharply contradicting the originally-claimed\
  \ 10–20× advantage)\n\nQualitatively, Cox coefficients remain stable under resampling, while pooled-MDD ratios shift more;\
  \ quantitatively, the robustness advantage is modest [ARTIFACT:art_fgt7JgoWQP-k].\n\n#### Family-Level Heterogeneity\nWe\
  \ computed per-family Nelson-Aalen cumulative hazard at *d*=10 across all 14.56M arcs, compared to a word-order-matched\
  \ cluster baseline, yielding residual-hazard scores. For families with ≥2 treebanks in the sample, we ran 500-replicate\
  \ block bootstrap (resampling treebanks within family) to generate 95% confidence intervals. Benjamini-Hochberg FDR correction\
  \ applied across all families tested.\n\n**Results**: Most families show wide, overlapping confidence intervals. NW-Caucasian\
  \ shows a clear positive residual (point est. 3.62, CI [3.15–4.09]), and Unclassified (polyglot collection) and Indo-Aryan\
  \ show substantial positive residuals. However, only families with ≥3 treebanks in the bootstrap sample have meaningful\
  \ CIs; singleton families cannot be reliably ranked [ARTIFACT:art_fgt7JgoWQP-k].\n\n---\n\n## 4. Results\n\n### Primary\
  \ Finding: No Significant Register Effect at Gold-Label Quality\n\n[FIGURE:fig1]\n\nKaplan-Meier survival curves for gold-labeled\
  \ English, French, and Slovenian show substantial overlap between spoken and written hazard profiles within each language.\
  \ The primary Cox model on this subset yields a non-significant register coefficient (β=−0.032, p=0.366). This directly\
  \ contradicts the hypothesis that spoken language exhibits front-loaded hazard; instead, the gold-labeled data show no systematic\
  \ register difference in arc-length distribution.\n\n### Secondary Finding: Apparent Register Effect in Full Corpus is Label-Confounded\n\
  \nIn the full 350-treebank corpus with heuristic labels, a statistically significant register effect emerges (β=+0.046,\
  \ p=1.1e-4). However, this effect is fragile. Label-noise sensitivity analysis shows:\n\n- 0% label noise: β=0.011, p=0.004\
  \ (significant)\n- 5% label noise: β=0.007, p=0.054 (marginal)\n- 10% label noise: β=0.013, p=0.0009 (significant)\n- 20%\
  \ label noise: β=0.005, p=0.157 (non-significant)\n\nAt 20% perturbation—a plausible noise rate for heuristic labels applied\
  \ to 347 of 350 treebanks—the effect vanishes. This suggests the full-corpus effect is driven by label assignment bias,\
  \ not genuine register differences [ARTIFACT:art_fgt7JgoWQP-k].\n\n### Strong Typological Effect: Word Order\n\n[FIGURE:fig2]\n\
  \nThe word-order coefficient (β=−0.028, p=4.9e-25) is large and highly significant. Free-order languages (low fraction of\
  \ dependents preceding head) exhibit lower hazard, meaning arcs are less likely to close at short distances—they have flatter,\
  \ lower-peak hazard curves. Fixed-order languages (high fraction preceding) show steeper hazard, with closure concentrated\
  \ at shorter distances.\n\nEffect size: A one-standard-deviation increase in word-order scale (from fixed to free) corresponds\
  \ to a hazard ratio of exp(−0.028) = 0.972, a 2.8% decrease in instantaneous closure risk. While the percentage is small,\
  \ the effect spans an entire typological dimension and is observed across 14.56 million arcs.\n\nFunctional vs. lexical\
  \ stratification: Functional dependencies (articles, case markers) show weaker register effects (β=0.027, CI [0.018–0.036],\
  \ p=1.6e-8) than lexical dependencies (β=0.122, CI [0.115–0.129], p=2.7e-257), a 4.5× ratio consistent with Gerdes et al.\
  \ [3] [ARTIFACT:art_fgt7JgoWQP-k].\n\n### Family-Level Structure\n\n[FIGURE:fig3]\n\nLanguage families show substantial\
  \ heterogeneity in residual hazard after word-order and morphological-richness covariates are controlled. Bootstrap CIs\
  \ are wide for most families (singleton or small-sample families), but a few show consistent positive or negative residuals.\
  \ NW-Caucasian shows notably elevated hazard relative to its typological cluster, while Romance, Slavic, and Indo-Aryan\
  \ show lower-than-expected hazard.\n\nInterpretation: Family-level deviations suggest language families have distinct grammatical\
  \ or processing strategies that go beyond word-order typology alone. However, sample-size constraints limit the strength\
  \ of these claims; replication on larger family-level samples is necessary [ARTIFACT:art_fgt7JgoWQP-k].\n\n### Cross-Check\
  \ Against Futrell et al. and Gerdes et al.\n\nThe hypothesis predicted recovery of Futrell et al. (2015)'s finding that\
  \ all 37 languages minimize dependency length vs. random baseline. A random-head-permutation null (heads reassigned uniformly\
  \ within sentence-length bounds) yields mean arc length 8.77 vs. 3.38 observed, a clear and large separation (Nelson-Aalen\
  \ AUC difference 78.8) . This replicates Futrell's directional result: DLM is strong and consistent across our 350-treebank\
  \ sample.\n\nThe functional/lexical split is confirmed: functional dependencies (β=0.027) show weaker language effects than\
  \ lexical dependencies (β=0.122), consistent with Gerdes et al.'s hypothesis that grammar-driven dependencies are universal\
  \ while processing-driven dependencies are typologically variable [ARTIFACT:art_fgt7JgoWQP-k].\n\n---\n\n## 5. Discussion\n\
  \n### Methodological Contribution: Survival Analysis as a Confound-Resolution Tool\n\nThe primary contribution of this work\
  \ is methodological: survival-analysis methods provide a principled, built-in solution to the length-mixing confound that\
  \ has long plagued dependency-length research. By treating sentence-boundary constraints as censoring (not as a regression\
  \ predictor to normalize away), we eliminate the mechanical confound at its source. This reframing is not novel to dependency\
  \ data—biostatistics has used it for decades—but its application to synchronic linguistic data is, to our knowledge, unprecedented\
  \ [ARTIFACT:art_vrYpy-2sRrjb].\n\nThe robustness check partially validates this advantage: Cox coefficients are more stable\
  \ under sentence-length-composition resampling than pooled-MDD ratios. However, the quantitative advantage (1.3× variance\
  \ ratio, not 10–20×) is more modest than originally hypothesized, suggesting the confound's practical impact may be smaller\
  \ in some regimes than others.\n\n### The Register Finding: A Cautionary Tale on Label Quality\n\nOur analysis reveals a\
  \ stark contrast between gold-labeled and heuristic-labeled registers:\n- **Gold-labeled subset** (*n*=25,710, 3 languages):\
  \ β=−0.032, p=0.366 (not significant).\n- **Full-corpus heuristic labels** (*n*=14.56M, 350 treebanks): β=+0.046, p=1.1e-4\
  \ (significant, but label-noise-dependent).\n\nThis 146% discrepancy and label-noise sensitivity are significant findings\
  \ in themselves. They demonstrate that register effects in dependency-length research are highly sensitive to annotation\
  \ quality. For future work, we recommend:\n1. Prioritize gold-labeled spoken/written corpora (CHILDES, Rhapsodie, SST, etc.)\
  \ over heuristic labeling.\n2. Explicitly model label uncertainty, rather than treating register as a fixed covariate.\n\
  3. Report both gold-labeled and heuristic results, with transparent quality flags.\n\nOur honest finding is that **spoken\
  \ language does not show significantly front-loaded dependency hazard at gold-label quality**. The apparent effect in the\
  \ full corpus is confounded by label assignment bias. This does not invalidate the register hypothesis; rather, it underscores\
  \ that the hypothesis needs cleaner data to test.\n\n### Typological Effects: Robust and Large\n\nThe word-order effect\
  \ (β=−0.028, p=4.9e-25) survives all robustness checks and operationalization variants. Free-order languages exhibit flatter,\
  \ lower-peak hazard, consistent with the idea that morphological marking (case, agreement) permits longer dependencies without\
  \ real-time ambiguity. This is a genuine typological signal. Effect size, while a 2.8% hazard decrease per SD, is meaningfully\
  \ large at the 14.56M-arc scale and aligns with linguistic theory.\n\n### Family-Level Structure: Tentative and Exploratory\n\
  \nLanguage families show residual heterogeneity, but bootstrap CIs are wide for most families due to limited treebank coverage.\
  \ NW-Caucasian emerges as an outlier, but this is based on a small sample (*n*_treebanks = 2). We caution against over-interpreting\
  \ family rankings without larger, more balanced language-family samples in UD.\n\n### Limitations\n\n1. **Register labeling**:\
  \ Only 3 of 350 treebanks have gold-documented spoken/written splits. The primary register analysis is restricted to these\
  \ 3 languages, limiting generalizability. The full-corpus heuristic-labeled estimate is confounded by label noise.\n\n2.\
  \ **Word-order operationalization**: The primary covariate is empirical (fraction of dependents preceding head), not categorical\
  \ (Grambank/WALS). While this ensures consistency, it differs from typological classifications linguists may prefer. A future\
  \ sensitivity analysis should compare against Grambank categorical classes.\n\n3. **Family-level frailty**: We use stratification\
  \ and post-hoc residual ranking as proxies for family-level frailty, rather than explicit random-effect frailty modeling\
  \ (which lifelines does not natively support). Bayesian methods (e.g., PyMC) would provide more rigorous family-level inference.\n\
  \n4. **Functional vs. lexical stratification**: Register effects are larger for lexical dependencies (β=0.122) than functional\
  \ (β=0.027). The functional-dependency hypothesis—that grammar-driven dependencies are universal—is supported, but the analysis\
  \ does not deeply examine *why* lexical dependencies show larger register variance. Deeper linguistic modeling (e.g., by\
  \ argument structure, semantic role) could refine this.\n\n5. **Sample-size asymmetry**: Spoken arcs are far fewer than\
  \ written (12,855 vs. 12,855 in gold subset, but 18,846 vs. 67,434 in full corpus across all languages). Small spoken samples\
  \ in many languages limit power for language-specific register effects.\n\n---\n\n## 6. Conclusion\n\nWe have introduced\
  \ survival-analysis methods to the study of dependency-length minimization, treating arc length as a right-censored time-to-event\
  \ outcome. This reframes the documented sentence-length-pooling confound as a design component of the model, rather than\
  \ a statistical hazard to be normalized away.\n\nOur analysis of 14.56 million arcs across 350 UD treebanks yields three\
  \ findings:\n\n1. **Methodological**: Survival analysis provides a confound-robust framework for quantitative typology.\
  \ Cox regression coefficients are stable under sentence-length-composition resampling, validating the reframing's utility.\n\
  \n2. **Register**: On gold-labeled spoken/written pairs, no significant register effect emerges (β=−0.032, p=0.366). The\
  \ apparent effect in the full corpus (β=+0.046) is confounded by heuristic register labeling and vanishes under label-noise\
  \ sensitivity analysis. Future research should prioritize gold-labeled spoken corpora.\n\n3. **Typology**: Word-order class\
  \ is a robust, large predictor of hazard-curve shape (β=−0.028, p=4.9e-25). Free-order languages exhibit flatter profiles,\
  \ consistent with theories linking morphological richness to dependency-length tolerance. Language families exhibit residual\
  \ structure beyond typology, though bootstrap CIs require larger samples for definitive conclusions.\n\nThis work opens\
  \ a new methodological avenue for quantitative typology, demonstrating that survival-analysis tools can be adapted to linguistic\
  \ problems with hidden censoring structures. It also serves as a cautionary example: apparent large-scale effects can be\
  \ artifacts of label quality, emphasizing the need for transparent data provenance in linguistic research.\n\n---\n\n##\
  \ References\n\n[1] Futrell, R., Mahowald, K., and Gibson, E. (2015). Large-scale evidence of dependency length minimization\
  \ in 37 languages. *Proceedings of the National Academy of Sciences*, 112(33), 10336–10341.\n\n[2] Ferrer-i-Cancho, R. and\
  \ Liu, H. (2013). The risks of mixing dependency lengths from sequences of different length. *Glottotheory*, 5, 143–155.\n\
  \n[3] Gerdes, K. (2026). The grammar does the work: Functional vs. lexical dependency length minimization across the UD\
  \ languages. *Proceedings of the Language Resources and Evaluation Conference*.\n\n[4] Temperley, D. (2007). Minimization\
  \ of dependency length in written English. *Cognition*, 105(2), 300–333.\n\n[5] Temperley, D. (2008). Dependency-length\
  \ minimization in natural and artificial languages. *Journal of Quantitative Linguistics*, 15(3), 256–282.\n\n[6] Liu, Z.\
  \ (2020). Mixed evidence for crosslinguistic dependency length minimization. *STUF—Language Typology and Universals*, 73(4),\
  \ 605–633.\n\n[7] Yadav, H., Mittal, S., and Husain, S. (2022). A reappraisal of dependency length minimization as a linguistic\
  \ universal. *Open Mind*, 6, 147–168.\n\n[8] Jaeger, T. F. and Wasow, T. (2010). Processing preference and language design.\
  \ *Annual Review of Linguistics*, 35, 245–268.\n\n[9] Dryer, M. S. (2013). Order of subject, object and verb. In *World\
  \ Atlas of Language Structures Online*. Max Planck Institute for Evolutionary Anthropology.\n\n[10] Yu, X., Falenska, A.,\
  \ and Kuhn, J. (2019). Dependency length minimization vs. word order constraints: An empirical study on 55 treebanks. In\
  \ *Proceedings of the First Workshop on Quantitative Syntax (Quasy, SyntaxFest 2019)*.\n\n[11] Nivre, J., Marneffe, M. de,\
  \ Ginter, F., Hajivc, J., Manning, C. D., Pyysalo, S., Schuster, S., Tyers, F. M., and Zeman, D. (2020). Universal dependencies\
  \ v2: An evergrowing multilingual treebank collection. In *Proceedings of the 12th Language Resources and Evaluation Conference\
  \ (LREC)*, pp. 4034–4043.\n"
summary: >-
  We apply survival-analysis methods to 14.56 million dependency arcs in Universal Dependencies to address the documented
  length-mixing confound in dependency-length research. The key findings are: (1) Methodological: survival analysis provides
  a principled, confound-robust framework for analyzing position-bounded syntactic data; (2) Register: on gold-labeled spoken/written
  pairs (3 languages), the register effect is non-significant (p=0.366), contradicting the front-loaded-hazard hypothesis,
  and the apparent effect in the full corpus is confounded by heuristic labeling; (3) Typology: word-order class is a robust,
  large predictor of hazard shape (p=4.9e-25), with free-order languages showing flatter profiles; (4) Family structure: language
  families exhibit residual heterogeneity beyond typological covariates, though bootstrap CIs require larger samples for definitive
  conclusions. This work demonstrates survival analysis as a novel tool for quantitative typology and underscores the importance
  of label quality in linguistic research.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
figure_type: data
title: Kaplan-Meier Survival Curves by Language and Register
caption: >-
  Non-parametric survival curves (1 minus cumulative hazard) for gold-labeled spoken vs. written dependency arcs across English,
  French, and Slovenian. Curves show the probability that an arc of length \textgreater d has not yet closed by distance d.
  Spoken (orange) and written (blue) curves largely overlap within each language, indicating no systematic register difference
  in arc-length distributions at gold-label quality.
image_gen_detailed_description: >-
  Three panels, one per language (English, French, Slovenian). Each panel shows two curves: spoken (orange) and written (blue)
  Kaplan-Meier survival curves. X-axis: arc distance d (tokens), range 0-20. Y-axis: S(d), survival probability (0.0-1.0).
  Spoken and written curves largely overlap or cross, showing no systematic separation. Curves decline steeply at short distances,
  leveling off after d=8-10. At d=10: S ≈ 0.2-0.3 for both registers in all languages. Legend: Spoken, Written. Sans-serif
  font, white background, no grid.
aspect_ratio: '16:9'
summary: >-
  Spoken and written registers show overlapping hazard profiles within each language, with no clear spoken-vs-written separation
  at gold-label quality.
figure_path: figures/fig1_v0.pdf

--- Item 2 ---
id: fig2
figure_type: data
title: 'Cox Coefficient Comparison: Register, Word Order, and Morphological Richness'
caption: >-
  Estimated Cox regression coefficients from the full-corpus model (350 treebanks, 14.56M arcs) for register (heuristic-labeled),
  word-order typology, and morphological richness. Point estimates and 95% confidence intervals shown. Register effect is
  small and label-noise-dependent (orange, significant in full corpus but confounded); word-order effect is large and highly
  significant (blue, p=4.9e-25); morphological richness is not significant (red, p=0.52).
image_gen_detailed_description: >-
  Horizontal bar plot. Three rows: register, word_order, morph_richness. Each row shows point estimate (dot) and 95% CI (horizontal
  line). Register (orange): point=-0.046, CI=[0.022, 0.069], p=1.1e-4. Word_order (blue): point=-0.028, CI=[-0.034, -0.023],
  p=4.9e-25. Morph_richness (red): point=0.0013, CI=[-0.003, 0.006], p=0.52. X-axis ranges -0.08 to +0.08. Zero-line marked.
  Legend optional. Sans-serif, white background.
aspect_ratio: '4:3'
summary: >-
  Word-order typology shows a large, highly significant effect; register and morphological richness effects are small and
  non-significant or label-dependent.
figure_path: figures/fig2_v0.pdf

--- Item 3 ---
id: fig3
figure_type: data
title: Family-Level Residual Hazard with Bootstrap Confidence Intervals
caption: >-
  Point estimates and 95% bootstrap confidence intervals for residual Nelson-Aalen cumulative hazard at d=10 across language
  families. Families are sorted by point estimate. Families with fewer than 2 treebanks (insufficient for bootstrap CI) are
  omitted. Wide CIs reflect small sample sizes; only families with ≥5 treebanks have narrow CIs. NW-Caucasian and Unclassified
  show clear positive residuals; Romance and Slavic show negative residuals. Most CIs overlap zero, suggesting family-level
  heterogeneity is modest after typological covariates are controlled.
image_gen_detailed_description: >-
  Horizontal dot-and-whisker plot. 12-15 families sorted by point estimate (low to high). Each family: dot=point estimate
  (mean bootstrapped h_10), whisker line=95% CI. X-axis: residual hazard (range -1.5 to +2.0). Zero-line marked. NW-Caucasian:
  point≈3.6, CI≈[3.15, 4.1]. Unclassified: point≈4.3, CI≈[3.8, 5.1]. Slavic: point≈-0.20, CI≈[-0.20, -0.20] (narrow, high
  precision). Romance: point≈-0.48, CI≈[-0.50, -0.46]. Most families (Indo-Aryan, Sino-Tibetan, Semitic, etc.) have overlapping
  CIs near zero. Font sans-serif, white background.
aspect_ratio: '16:9'
summary: >-
  Language families show substantial variation in residual hazard, but most confidence intervals overlap zero after typological
  covariates are controlled, suggesting family-level effects are modest.
figure_path: figures/fig3_v0.pdf
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/<the filename from its own `figure_path` above>} — INCLUDING the extension it actually has. Data figures are delivered as `.pdf` (vector, so their axis labels stay sharp) and concept figures as `.jpg`. Writing `.jpg` for a `.pdf` figure names a file that is not in figures/ and the build fails on it
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure}[placement], \includegraphics, \caption, \label, \end{figure} — one placement for every figure, see FLOAT PLACEMENT below. Constrain every \includegraphics with `width=\linewidth,height=0.85\textheight,keepaspectratio`. The height is a LAST RESORT, not the usual limit: it exists so a very tall figure cannot overrun the page, and at 0.4 it bound almost everything instead — a 1:1 confusion matrix printed at 50.9% and its 11 pt axis labels reached the page at 5.6 pt, below what any venue accepts. At 0.85 every ratio the paper prompt prescribes (21:9, 16:9, 4:3, 1:1) is limited by WIDTH, prints at 93% and keeps its text above 10 pt. Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

FLOAT PLACEMENT: every figure gets \begin{figure}[!htbp]. Measured, not chosen:
the document the aii-paper-to-latex skill sets up is ONE column, so `figure*` is
exactly as wide as `figure` (469.76pt either way) and gains nothing; and any
placement asking for a page TOP — `[!t]`, `[!tbp]` — floated the hero diagram above
the paper's own title on page 1, while `[!htbp]` did not. `[!htbp]` also gives LaTeX
four options, so a float can never be deferred to the end of the document, which one
option alone risks. Where the hero ENDS UP is decided by its [FIGURE:] marker in
paper_text, which is already placed near the end of the Introduction — preserve it.
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-13 13:19:23 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-08-13 13:19:25 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated vector PDFs and JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figures (vector `.pdf` for data figures, `.jpg` for concept figures) and a bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.pdf}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS `[!htbp]` — all four options, so a float can never be deferred to the end of the
  document, which `[t]` or `[h]` alone risks. Do not ask for a page TOP: `[!t]` and
  `[!tbp]` both floated a figure ABOVE the paper's own title on page 1, where `[!htbp]`
  on the same document did not. Where a figure lands is decided by where it is declared
  in the text
- Use `figure`, never `figure*`. This document class is ONE column, so `figure*` is exactly
  as wide as `figure` (469.76pt either way) and gains nothing, while restricting the float
  to a page top
- ALWAYS constrain with `width` and `keepaspectratio`. Add `height` only as a
  LAST RESORT against a very tall figure overrunning the page, and keep it
  generous — `0.85\textheight`. A tight height cap binds on ordinary figures
  and LaTeX then shrinks the TEXT with them: at `0.4\textheight` a square
  figure printed at 50.9%, putting 11 pt axis labels on the page at 5.6 pt.
  The figure generator measures legibility at the figure's OWN size, so it
  cannot see this happen
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/` — all figure images (pre-generated, copied into workspace). Data
  figures are `.pdf` (vector — LaTeX renders their text at page resolution, which
  is what keeps axis labels sharp in print); concept figures are `.jpg`. Use each
  file's OWN extension in `\includegraphics`; there is no conversion step.
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-08-13 13:19:25 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
