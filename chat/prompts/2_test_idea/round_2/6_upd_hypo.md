# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_oQQwThF8kM-b` — Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-13 13:05:37 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Dependency Length as a Survival Process
hypothesis: >-
  If each syntactic dependency arc is modeled as a right-censored time-to-event process — where the 'event' is the arc closing
  at distance d (arc_length == d) and censoring occurs precisely when the arc reaches its position-imposed maximum possible
  distance (arc_length == censoring_bound, the distance to the nearer sentence boundary) — then the resulting hazard function
  h(d) is not flat or freely comparable across registers and typologies, as pooled mean-dependency-distance (MDD) statistics
  implicitly assume, and this framing is now empirically validated at UD scale (350 treebanks, 14.56M arcs, 1.54% genuinely
  censored, 0 censoring-bound violations): the censored-hazard estimate is measurably robust to sentence-length-composition
  resampling where pooled-MDD ratios are not (Cox-coefficient SD ~0.0004 vs. 10-20x greater MDD variance across matched deciles).
  Building on this validated mechanism, three narrower and more specific claims remain to be established with adequate label
  quality and multiple-comparison control: (1) spoken registers show a front-loaded hazard (risk peaks at short d, decays
  fast) relative to written registers of the same language — but this must be estimated PRIMARILY on the small set of treebanks
  with genuinely gold-documented register (English-CHILDES/EWT, French-Rhapsodie/GSD, Slovenian-SST/SSJ; n_spoken=18,846 vs
  n_written=67,434), with the 350-treebank heuristic-labeled estimate (register β=+0.046, p=1.1e-4) reported only as a secondary,
  label-noise-sensitive robustness check, since the majority of the 350-treebank corpus lacks gold register annotation and
  defaults to metadata heuristics or a majority-written label; (2) case-marking / free-word-order languages show flatter,
  lower-peak hazard curves than fixed-order languages (word-order β=-0.028, p=4.9e-25, direction and significance already
  observed at full scale, but the covariate itself mixes a categorical Grambank class with a continuous empirical fallback
  on a single standardized scale and needs either separation into distinct terms or a demonstrated sensitivity analysis);
  and (3) a family-stratified Cox model (shared frailty, or the Nelson-Aalen residual-hazard proxy used so far) reveals specific
  language families whose hazard shape deviates from their typological cluster baseline — but a deviation only counts as established
  once residual hazards carry bootstrap confidence intervals and survive Benjamini-Hochberg correction across the ~32 families
  tested, since uncorrected multiple comparisons across that many small-to-large family samples (e.g. Dravidian's provisional
  +1.80 residual at n=18,353 arcs) are expected to produce spurious outliers by chance alone.
motivation: >-
  Dependency-length minimization (DLM) is one of computational linguistics' most replicated regularities, but nearly every
  study — including recent spoken-vs-written and functional-vs-lexical UD studies — characterizes it through summary statistics
  (mean dependency distance, MDD ratios against random baselines) computed on dependency lengths pooled across sentences of
  different lengths. This pooling is a documented methodological hazard in the field: the distribution of dependency lengths
  differs mechanically between sentences of different lengths, so pooled comparisons between languages or registers can reflect
  nothing more than differences in sentence-length distributions. Existing corrections (normalizing by sentence length, comparing
  against random-linearization baselines) are partial fixes to a problem that biostatistics solved generally decades ago:
  when the maximum observable value of a quantity is bounded by a covariate (here, a word's distance to its sentence boundary),
  the correct tool is a censored time-to-event model, not a pooled mean. Reframing dependency arcs as survival objects turns
  the confound into the covariate structure of the model, and yields a full curve (the hazard function) instead of a single
  ratio — recovering shape information (front-loaded vs. flat risk, monotonic vs. non-monotonic hazard) that MDD-based statistics
  structurally cannot see, and giving typology and language-family effects a principled multi-level home via frailty terms
  rather than post-hoc grouping of means.
assumptions:
- >-
  UD/SUD dependency trees (via HuggingFace commul/universal_dependencies) provide, for each token, a well-defined linear position
  and head position from which an arc length and its position-bounded maximum possible length (the censoring bound) can both
  be computed deterministically.
- >-
  A sufficient number of UD treebanks contain both a spoken and a written subcorpus of the same language (e.g. French-Rhapsodie/GSD,
  Slovenian-SST/SSJ, English-GUM strands, Cantonese-HK, Komi-Zyrian) to support matched within-language register comparison
  rather than only cross-language comparison.
- >-
  Treating each dependency arc's length as a discrete time-to-event outcome (with censoring at the boundary-imposed maximum)
  is a valid reframing — i.e., arc length is generated by a process for which 'has the arc closed by distance d, given it
  has not closed before d and could not exceed the sentence-boundary bound' is a meaningful conditional quantity, not a degenerate
  one.
- >-
  Standard survival-analysis software (lifelines / scikit-survival, pure Python) can fit non-parametric hazard curves (Kaplan-Meier
  / Nelson-Aalen) and semi-parametric shared-frailty Cox models at UD-scale (tens of thousands to low millions of arcs) within
  available CPU compute.
- >-
  Genealogical family labels (as curated by UD/Glottolog metadata) provide a defensible grouping variable for the frailty
  term, i.e. within-family arcs share more unmodeled hazard-shape similarity than across-family arcs on average.
investigation_approach: >-
  Using commul/universal_dependencies on HuggingFace, extract every UD and, where paired, SUD-style dependency arc across
  all treebanks with a machine-parseable genre/modality tag (spoken vs. written) and known word-order/morphological-richness
  typological features (from WALS/Grambank where available, else UD morphological feature counts as a proxy). For each arc,
  compute observed length d and the position-imposed maximum possible length (censoring bound) from the token's distance to
  the nearer sentence boundary. Fit (a) non-parametric Kaplan-Meier/Nelson-Aalen hazard curves per treebank and per register
  within language, (b) a semi-parametric Cox proportional-hazards model with register, word-order class, and a morphological-richness
  covariate as fixed effects and language family as a shared frailty (random effect) term, and (c) compare fitted frailty
  terms across families to flag those whose residual hazard shape (after covariates) departs from their typological cluster.
  Validate the reframing against the known sentence-length-mixing confound by showing the hazard-based comparison is invariant
  to sentence-length composition where the pooled-MDD comparison is not (a direct, quantitative replication-with-correction
  of the pooling risk already flagged in prior DLM methodology). Cross-check spoken-vs-written and typology findings against
  the closest existing pooled-mean results (Cross-linguistic speech/writing DLM studies, and recent functional-vs-lexical
  UD DLM work) to confirm the hazard-based method recovers known directional effects while adding shape information those
  methods cannot report.
success_criteria: >-
  CONFIRMS the hypothesis if: (1) spoken-register hazard curves are measurably front-loaded relative to matched written-register
  curves within the same language for a majority of language pairs with paired spoken/written UD data, after the censoring
  correction, with the effect surviving a sentence-length-composition robustness check (i.e., hazard shape differs even when
  pooled MDD would not, or differs more than pooled MDD suggests); (2) word-order/morphology covariates in the Cox model show
  a consistent, statistically supported direction (free-order languages flatter/lower-peak hazard) with confidence intervals
  excluding zero; (3) the fitted frailty terms identify at least one family whose residual (covariate-adjusted) hazard shape
  is a clear outlier relative to its typological cluster, replicable when refit on a held-out subset of that family's treebanks.
  DISCONFIRMS or narrows the hypothesis if hazard curves are statistically indistinguishable from what pooled MDD/random-baseline
  comparisons already predict (i.e., the survival reframing adds no shape information beyond a rescaled mean), if the spoken/written
  effect disappears entirely once censoring is corrected (suggesting the previously reported effect WAS the pooling artifact),
  or if frailty terms show no family-level structure beyond what word order and morphology already explain (i.e., no deviating
  families exist once typology is controlled).
related_works:
- >-
  Futrell, Mahowald & Gibson, 'Large-scale evidence of dependency length minimization' (PNAS 2015) — establishes DLM across
  37 languages via pooled mean dependency length vs. random-baseline comparison; the proposed work replaces the pooled-mean/baseline-ratio
  statistic with a censored hazard function that recovers distributional shape and is explicitly designed to be robust to
  the sentence-length-mixing artifact this line of work does not correct for.
- >-
  Ferrer-i-Cancho & colleagues, 'The risks of mixing dependency lengths from sequences of different length' — identifies the
  exact confound (pooling dependency lengths across sentences of different lengths distorts cross-language/register comparison)
  that motivates this hypothesis; that paper diagnoses the problem, this hypothesis imports a general-purpose statistical
  solution (censored survival modeling) from biostatistics rather than proposing an ad hoc normalization.
- >-
  Cross-linguistic study of dependency lengths in speech vs. writing (SCiL 2021) — compares spoken and written MDD across
  languages using pooled/normalized means and finds inconsistent directional effects (e.g., longer spoken dependencies in
  French/Russian/Italian, no difference in English); this hypothesis re-examines the same spoken/written contrast with a hazard-shape
  lens that can distinguish 'same mean, different shape' patterns the mean-based comparison cannot see, and tests whether
  the inconsistency is itself a pooling artifact.
- >-
  'The Grammar Does the Work: Functional vs. Lexical Dependency Length Minimization Across Universal Dependencies' (2026,
  UD/SUD 2.14-2.17, 122 languages) — decomposes DLM variance into functional vs. lexical dependency-type contributions using
  variance-decomposition/mixed-effects methods; this hypothesis instead decomposes variance in the shape of the length distribution
  itself (hazard curve) via a survival/frailty model, a orthogonal axis (event-time shape, not source-of-variance-by-dependency-type)
  that has not been applied to any dependency-length dataset in the literature we could locate.
- >-
  Petrini et al., 'The distribution of syntactic dependency distances' (2022) — fits exponential/two-regime parametric families
  to the marginal p(d) distribution; this hypothesis instead estimates the conditional hazard h(d | not yet closed, structurally
  censored at the boundary) non-parametrically via Kaplan-Meier/Cox, which is a different (and, for censored, boundary-bounded
  count data, more standard) object than a marginal-distribution fit and naturally incorporates position-dependent censoring
  that parametric marginal fits do not model.
inspiration: >-
  METHODOLOGICAL transfer from biostatistics/epidemiology: survival analysis (Kaplan-Meier estimators, Cox proportional-hazards
  regression, shared-frailty models) was built specifically to handle outcomes whose maximum observable value is bounded by
  a covariate (a patient's follow-up time) and where hazard-shape, not just mean survival time, carries scientific information.
  Dependency arcs have the identical structure — a word near a sentence boundary simply cannot produce a long arc, exactly
  analogous to a patient enrolled late in a trial being 'censored' rather than truly event-free — yet computational-linguistics
  DLM studies have never adopted the corresponding tool, instead using pooled means and ad hoc normalizations that the field's
  own methodology papers (Ferrer-i-Cancho on length-mixing) flag as risky. The 'language family as frailty group' framing
  is a direct import of the population-genetics/biostatistics idea of unobserved cluster-level heterogeneity (the same statistical
  object used for hospital-level effects in multi-center trials or subpopulation effects in genetic epidemiology), repurposed
  here as a principled way to let language-family membership contribute its own random effect on hazard shape after typological
  covariates are controlled — rather than being folded into a single fixed-effect grouping variable as in current mixed-effects
  DLM work.
terms:
- term: Dependency length (arc length)
  definition: >-
    The linear distance, in tokens, between a syntactic head and its dependent in a UD-annotated sentence; the primary quantity
    DLM research studies.
- term: Right-censoring
  definition: >-
    A survival-analysis concept where the true event time is unknown but is known to be at least as large as an observed bound;
    here, a word's true 'preferred' arc length is bounded from above by its distance to the sentence boundary, so long arcs
    near a boundary are structurally impossible rather than dispreferred.
- term: Hazard function h(d)
  definition: >-
    The instantaneous probability that an arc of length ≥ d closes exactly at d, conditional on not having closed before d;
    captures the shape of risk across d, unlike a single mean or ratio statistic.
- term: Kaplan-Meier / Nelson-Aalen estimator
  definition: >-
    Standard non-parametric estimators of the survival function / cumulative hazard from censored time-to-event data, used
    here to estimate arc-length hazard curves without assuming a parametric family.
- term: Cox proportional-hazards model
  definition: >-
    A semi-parametric regression model for censored time-to-event data that estimates how covariates (here: register, word
    order, morphological richness) multiplicatively shift the baseline hazard, without requiring the baseline hazard's functional
    form to be specified.
- term: Shared frailty model
  definition: >-
    An extension of the Cox model that adds a group-level random effect (the 'frailty') shared by all observations in a cluster
    — here, all arcs from treebanks belonging to the same language family — to capture unobserved cluster-level heterogeneity
    in hazard after fixed-effect covariates are controlled.
- term: Dependency length minimization (DLM)
  definition: >-
    The hypothesis, and associated empirical regularity, that language users and grammars prefer word orders that keep syntactically
    related words close together in the linear string.
- term: Length-mixing confound
  definition: >-
    The documented methodological risk that pooling dependency lengths across sentences of different lengths can produce spurious
    or distorted cross-language/register comparisons, because the length distribution is itself a function of sentence length.
summary: >-
  This hypothesis reframes each dependency arc in a UD-parsed sentence as a censored time-to-event object — closing at some
  distance d, with a maximum possible distance bounded by the word's position in the sentence — and applies survival-analysis
  tools (Kaplan-Meier hazard curves, Cox models with language-family frailty) to characterize dependency-length minimization
  across UD treebanks, testing whether spoken registers show a distinctively front-loaded hazard shape and which language
  families deviate from their typological cluster once word order and morphology are controlled.
_relation_rationale: >-
  Mechanism confirmed at scale; narrows claims to gold labels + adds required corrections.
_confidence_delta: increased
_key_changes:
- >-
  Confirmed the core censoring mechanism is real and correctly implemented (event=1 iff arc_length<censoring_bound, 1.54%
  censored, 0 bound violations) — the paper text's 'all arcs observed' claim was a writing error, not a modeling one; hypothesis
  now states the mechanism precisely.
- >-
  Robustness-to-pooling claim upgraded to well-supported: Cox coefficients stable under sentence-length resampling (SD~0.0004)
  vs. pooled-MDD 10-20x more variable — this is now a demonstrated, not merely hoped-for, advantage of the reframing.
- >-
  Downgraded the spoken-vs-written headline claim from a full-350-treebank estimate to primarily a gold-labeled-subset claim
  (only 3/350 treebanks have genuine gold register annotation), per reviewer's construct-validity critique; full-corpus estimate
  now secondary/heuristic-dependent.
- >-
  Added an explicit requirement for bootstrap CIs and Benjamini-Hochberg correction on family-level residual-hazard rankings
  before any family is claimed to be a genuine typological outlier, since 32 uncorrected comparisons make spurious top hits
  likely.
- >-
  Flagged the word-order covariate's categorical/continuous mixing (Grambank class vs. empirical fallback merged into one
  standardized scale) as needing resolution via separate terms or a sensitivity check.
- >-
  Softened implicit novelty scope: retained 'first application to synchronic dependency-length data' framing rather than an
  unqualified first-ever survival-analysis-in-linguistics claim (historical-linguistics hazard models for lexical replacement/grammaticalization
  exist and are adjacent).
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

--- Item 1 ---
id: art_2CDrgn6Hae3P
type: research
title: Survival Analysis Foundations for Dependency Arc Modeling Across UD Treebanks
summary: >-
  This artifact conducts exhaustive research establishing the theoretical, methodological, and empirical foundations for applying
  survival analysis to dependency-arc modeling in Universal Dependencies treebanks. The investigation addresses six components:
  (1) **The Length-Mixing Confound**: Documents Ferrer-i-Cancho & Liu's (2013) proof that pooled dependency-length means are
  mathematically determined by sentence-length distributions, creating a confound that invalidates cross-language/register
  comparisons. Survival analysis eliminates this by treating position-bounded arc length as right-censored. (2) **Survival-Analysis
  Precedent**: Conducts a systematic search finding NO prior linguistic applications of survival analysis, despite perfect
  methodological fit—identifying this as genuine methodological novelty. (3) **UD Treebank Catalog**: Identifies and catalogs
  at least 12 fully-spoken UD treebanks (Slovenian-SST, Norwegian-NynorskLIA, English-GUM, French-Rhapsodie, Cantonese-HK,
  Naija-NSC, and 6 others) and 4-6 language pairs with paired spoken/written data, sourcing typological metadata from WALS,
  Grambank, and Glottolog. (4) **Recent DLM Findings**: Synthesizes Dobrovoljc (2025) showing spoken language has fewer/less-diverse
  syntactic structures than writing, and Gerdes et al. (2026) proving dependency-type (functional vs. lexical) partitions
  DLM into two distinct regimes (grammar-driven functional: ~1.71 tokens; processing-driven lexical: ~2.87 tokens, typology-variable).
  (5) **Technical Feasibility**: Confirms Python's lifelines library supports Kaplan-Meier, stratified Cox proportional hazards,
  and scales to 100k+ observations; stratification handles language-family effects when frailty unavailable. (6) **Theoretical
  Justification**: Proves rigorously that arc length qualifies as a valid right-censored time-to-event outcome—position-bounded
  just as patient follow-up time is enrollment-bounded—with all survival-analysis assumptions satisfied. Concludes: all components
  are sound, novel, feasible, and ready for implementation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_V4iFzwfu7i49
type: dataset
title: UD Dependency Arcs with Survival-Analysis Features
summary: >-
  ud_arcs_curated: 114,480 dependency-arc records extracted from 28 Universal Dependencies v2.18 treebanks (commul/universal_dependencies
  on HuggingFace) spanning 20+ ISO-639-3 languages and 13 top-level Glottolog families, built for survival-analysis modeling
  of dependency-length minimization (does spoken register minimize arc length more than written?). Each row is one token's
  dependency arc with: arc_length (|token_id - head_id|, 0 for root), censoring_bound (= max(token_id, sentence_length - token_id),
  the position-bounded maximum arc length structurally possible from that token's position -- documented and verified with
  0 violations of arc_length <= censoring_bound across all 114,480 rows), register (spoken/written/academic/news/fiction/web/other,
  sourced from each treebank's own documented provenance -- e.g. en_childes/fr_rhapsodie/sl_sst are spoken, en_ewt/fr_gsd/sl_ssj
  are written gold-matched pairs; en_gum's 12 genres resolved per-sentence via commul/ud_genre bootstrapped labels since GUM
  itself is mixed-register), language_code/name, family_id + family_path (Glottolog CLDF, glottolog/glottolog-cldf GitHub),
  word_order_type (Grambank CLDF verb-initial/medial/final, resolved via a Glottocode join since Grambank's own ISO639P3code
  column is empty in the 2.18 snapshot -- covers 84% of rows, e.g. correctly recovers SOV for Japanese/Korean/Turkish/Basque/Tamil,
  SVO for English/French/Russian/Chinese, VSO for Arabic), morph_richness_proxy (0-1 scalar: mean UD morphological feature-slots
  per token / 8, clipped) with morph_richness_data_source='UD_proxy' throughout (WALS lookup was not implemented; Grambank/UD_proxy
  sourcing is transparent per-field). A second candidate dataset, ud_arcs_genre_labeled (same schema but register from commul/ud_genre's
  bootstrapped 18-genre classifier applied to all 28 treebanks rather than only the 3 gold-documented spoken/written pairs),
  was built and compared but NOT selected: its own dataset card states these labels 'are not authoritative gold annotations,'
  which is unacceptable noise for the register contrast this experiment hinges on -- ud_arcs_curated's smaller but gold-labeled
  spoken n=18,846 (vs written n=67,434) across matched within-language pairs (en_childes/en_ewt/en_gum, fr_rhapsodie/fr_gsd,
  sl_sst/sl_ssj) gives a methodologically cleaner test. Data is a treebank-stratified random subsample (120,000-per-dataset-build
  cap before final stratification) of the full 6,132,347-arc extraction from all 28 curated treebanks (0 censoring violations
  found in either the full or sampled extraction); downstream experiment code can call build_ud_arcs_curated() in data.py
  directly on the full manifest for the complete corpus if a larger sample is needed. Output is schema-valid against exp_sel_data_out.json,
  split into 2 shards of ~50MB each (full 101.5MB single file exceeded the 100MB artifact limit). Known limitation: only 3
  of 28 treebanks have genuinely gold-documented spoken register (en_childes, fr_rhapsodie, sl_sst); the rest default to a
  single treebank-level register inferred from each treebank's UD documentation page, not per-sentence.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_d7jrBtmjm_7W
type: experiment
title: Dependency Lengths as Survival Curves in UD
summary: >-
  Implements a full survival-analysis pipeline over commul/universal_dependencies (all 350 treebank configs, 14.56M dependency
  arcs) that reframes each head-dependent arc length as a right-censored time-to-event object: arc_length = |head_pos - dep_pos|,
  censoring_bound = max(distance-to-left-edge, distance-to-right-edge), event = 1 if arc_length < censoring_bound. This removes
  the mechanical sentence-length confound that plagues the standard pooled mean-dependency-distance (MDD) baseline used in
  prior dependency-length-minimization literature, which is implemented side-by-side as predict_baseline_pooled_mdd in every
  example for direct comparison against the survival-hazard estimate (predict_survival_hazard_median). Register (spoken/written/sign)
  is classified per sentence from CoNLL-U comment metadata (modality/channel tags, meta::genre values) with a curated name-based
  fallback (Rhapsodie, CHILDES, ESL-spoken, KIParla, ParlaMint) and a majority-written default, documented as a limitation.
  Language family is assigned via a static genealogical lookup table (Indo-European branches, Uralic, Semitic, Sino-Tibetan,
  Turkic, etc.) built from established typological classification. Word-order class and morphological richness are computed
  empirically per treebank directly from the parsed data (fraction of dependents preceding their head; unique morphological
  feature strings per token) rather than fetched from WALS/Glottolog, avoiding external API fragility. Kaplan-Meier survival
  curves are fit per (language, register) pair (198 curves), Nelson-Aalen cumulative/instantaneous hazard per treebank (350
  curves), and a stratified Cox proportional-hazards model (register + standardized word-order + standardized morphological-richness
  covariates, stratified by language family as a frailty substitute) is fit on a 300k-arc subsample with automatic penalizer
  escalation and near-constant-covariate dropping for numerical robustness. Family-level residual-hazard ranking implements
  the PyMC-frailty fallback (empirical-Bayes-lite): per-family Nelson-Aalen cumulative hazard at d=10 is compared against
  a word-order-matched typological-cluster baseline, yielding a residual-hazard outlier ranking across 32 families. A sentence-length-resampling
  robustness check (censoring-bound-decile-balanced resampling, since raw per-arc sentence length is not retained) compares
  Cox-coefficient stability against pooled-MDD-ratio instability for the 4 languages with both spoken and written treebanks
  (English, French, Italian, Ukrainian), directly testing the hypothesis that hazard-based estimates are robust to the sentence-length
  confound while pooled MDD is not. All results (KM/NA curves, Cox coefficients with 95% CIs and p-values, family outlier
  rankings, robustness deltas, literature cross-check directions, and an explicit hypothesis-verdict block) are written to
  method_out.json following the exp_gen_sol_out schema: one example per treebank (input=treebank description, output=JSON
  survival summary, metadata_language/family/register/word_order_score/morph_richness, predict_baseline_pooled_mdd vs predict_survival_hazard_median),
  with the corpus-level statistical results (Cox model, frailty ranking, robustness, cross-check, hypothesis verdict) in the
  top-level metadata object. On the full run: 350/350 treebanks processed, 14,560,338 arcs (1.54% censored), Cox model converged
  with register coef=+0.046 (95% CI [0.022, 0.069], p=1.1e-4, higher hazard/front-loaded for spoken), word-order coef=-0.028
  (95% CI [-0.034,-0.023], p=4.9e-25), robustness check CONFIRMED (Cox-stable, MDD-unstable) for the tested language pairs,
  and all four hypothesis-verdict flags (spoken_front_loaded, word_order_effect, family_deviance_exists, robustness_to_sent_length)
  returned CONFIRMED. Runtime ~134s for the full corpus after download.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 4 ---
id: art_AC8BwlWvA3iR
type: experiment
in_dependencies:
- id: art_V4iFzwfu7i49
  label: gold-labeled dataset
title: Does spoken language shorten dependency links?
summary: >-
  This experiment implements a censored survival-analysis pipeline over 114,480 Universal Dependencies dependency-arc records
  (28 treebanks, 20+ languages, 13 Glottolog families) to test whether spoken register minimizes dependency-arc length more
  than written register, and how word-order typology and morphological richness interact with that pattern. The core method
  (method.py) fits Cox proportional-hazards models where duration=arc_length and event=1 iff arc_length is strictly below
  its position-bounded censoring_bound (an arc that hits the maximum length structurally possible from its token's position
  is treated as censored, not as a fully observed outcome) -- the correct treatment for position-bounded dependency distances,
  which a naive analysis would silently miss. A baseline logistic regression on a median-dichotomized (long/short) arc length,
  ignoring censoring entirely, is fit on identical covariates for direct comparison. The pipeline covers: (1) a primary Cox
  fit on the gold-labeled spoken/written subset (en_childes/en_ewt, fr_rhapsodie/fr_gsd, sl_sst/sl_ssj; n=25,710 in this stratified
  sample) with robust cluster-by-language standard errors (adapted from the planned shared-frailty-by-family since the gold
  subset is 100% Indo-European in this sample, so family has zero variance there); (2) 500-replicate stratified bootstrap
  of family-level Nelson-Aalen cumulative-hazard-at-d=10 residuals (relative to the pooled corpus) across all 13 families
  present in the full corpus, with Benjamini-Hochberg FDR correction to flag confirmed family-level outliers; (3) a secondary
  Cox fit on the full 114,480-arc corpus with family as a fixed effect and mixed gold+heuristic register labels; (4) label-noise
  sensitivity analysis flipping 5/10/20% of heuristically-labeled register values and re-fitting; (5) three word-order operationalization
  variants (categorical Grambank word_order_type, an ordinal linear proxy, and a register-by-word-order interaction) run on
  the full corpus, since the gold subset also has zero word-order variance (all six gold treebanks are verb-medial/SVO) --
  both of these deviations from the artifact plan are documented in the output's deviations_from_plan field; and (6) a random-head-permutation
  null baseline (heads reassigned uniformly within sentence-length bounds) compared via Nelson-Aalen curves and AUC difference
  against the observed data. All Cox fits use a small ridge penalizer for numerical stability under near-collinear typology
  covariates. Key results from the executed run: the censoring-aware primary Cox fit finds NO significant register effect
  on the gold subset (register_spoken beta=-0.032, HR=0.968, p=0.366), while the censoring-naive baseline logistic regression
  on the identical data DOES find a significant effect (beta=0.076, OR=1.079, p=0.006) -- a direct empirical demonstration
  that ignoring position-bounded censoring can manufacture spurious register effects; the full-corpus secondary Cox (mixed
  gold+heuristic labels, family fixed effects) is directionally consistent but only marginal (p=0.063); label-noise sensitivity
  shows the register coefficient staying small and stable in sign as 0/5/10/20% of heuristic labels are flipped; word-order
  variants A/B/C agree the register effect is small and non-significant regardless of operationalization; the family-level
  bootstrap flags 8 of 13 families as BH-significant outliers in position-relative hazard, i.e. substantial residual heterogeneity
  by language family after accounting for register; and the random-head-permutation null shows a large, clear separation from
  the observed data (mean arc length 3.38 observed vs. 8.77 under random head reassignment, Nelson-Aalen AUC difference 78.8),
  confirming strong general dependency-length minimization even though the specific spoken-vs-written contrast is weak in
  this sample. Output follows the exp_gen_sol_out schema: one dataset of 54 examples, each tagged metadata_analysis_type (primary_cox_fit,
  primary_baseline_logit, family_bootstrap_ranking, full_corpus_cox, label_noise_sensitivity, word_order_variant, random_permutation_null,
  model_coefficient) with full nested statistics in metadata_full_result. Downstream paper-writing steps should read metadata_full_result
  off each example for exact coefficients, CIs, p-values, and BH-adjusted significance flags rather than parsing the human-readable
  output/input strings.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_fgt7JgoWQP-k
type: evaluation
in_dependencies:
- id: art_d7jrBtmjm_7W
  label: iter-1 results for comparison and baseline
title: Stress-Testing the Spoken-vs-Written Dependency Model
summary: >-
  Validates the iter-1 survival-hazard reframing of UD dependency-arc lengths (register Cox coef=+0.046, 350 treebanks, 14.56M
  arcs) through four blocks, executed in eval.py against a genuine fresh re-download of 11 treebanks (723,819 arcs: the 3
  gold-register pairs en_childes/en_ewt, fr_rhapsodie/fr_gsd, sl_sst/sl_ssj, plus the 4 spoken/written robustness pairs en/fr/it/uk).
  (1) Effect-size standardization: HR=exp(0.046)=1.047, translating to a 0.082-token reduction in median arc length at the
  corpus-pooled median (1.85 tokens), placing the effect at the 25th percentile of a 4-language cross-language distribution
  of register log-mean-arc-length contrasts. (2) Data-provenance reconciliation: a 22-row provenance_table.csv documenting
  every reported statistic's source pipeline, n_arcs, n_treebanks, annotation source, and quality flag (6 gold_standard, 3
  heuristic_dependent, 13 mostly_reliable rows). (3) Cross-checks: gold-subset-only register coefficient (0.112) vs iter-1's
  full-corpus coefficient (0.046) differs by 146% (fails the plan's 5% tolerance -- an honest finding, not the originally-envisioned
  iter1-vs-iter2 diff, since no separate iter2 artifact exists to compare against); functional-dependency register coefficient
  (0.027) vs lexical (0.122) gives a 4.53x lexical/functional ratio, consistent with Gerdes et al.'s expected pattern; and
  a genuine 30-repeat censoring-bound-decile-balanced resample per language pair (not iter-1's single draw) gives a pooled
  Cox-vs-MDD variance ratio of only ~1.3x, sharply contradicting iter-1's claimed 10-20x -- this is the evaluation's most
  consequential finding and should be reported as a disconfirmation of the robustness-magnitude claim (the qualitative COX_STABLE/MDD_SHIFTS
  direction may still hold but the quantitative ratio does not survive proper repeated resampling). (4) Methodological transparency
  audit (audit_trail.md): documents the 3 genuine gold-label treebank pairs with citations and sample token counts; notes
  only ONE word-order operationalization exists in iter-1 (no second measure to cross-validate against, reported as an honest
  gap); label-noise sensitivity at 0/5/10/20% flips on heuristic-labeled treebanks (it_kiparlaforest/it_parlamint/uk_parlamint
  spoken side, it_isdt/uk_iu majority-written default side) shows the coefficient and its significance are unstable even at
  5% noise; and a block-bootstrap (500 replicates, seed=20260813, resampling treebanks not individual arcs) adds confidence
  intervals to the family-outlier ranking that iter-1 never computed. All numeric results are in eval_out.json (schema-validated
  against exp_eval_sol_out, metrics_agg + 45 per-example rows tagged by validation block) with full/mini/preview size variants
  generated. Downstream paper-writing steps should foreground the variance-ratio contradiction and the large gold-subset delta
  as the two central robustness caveats, not just the confirmatory functional/lexical and provenance results.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

--- Item 6 ---
id: art_vrYpy-2sRrjb
type: research
in_dependencies:
- id: art_2CDrgn6Hae3P
  label: iter-1 research and survival-analysis foundations
title: 'Survival Analysis for Synchronic Dependency Arcs: Novelty & Confound Resolution'
summary: >-
  Comprehensive investigation of novelty positioning for applying survival analysis to synchronic dependency-arc data in Universal
  Dependencies treebanks. Key findings: (1) **No prior synchronic applications exist**: Despite systematic searching of peer-reviewed
  literature and arXiv, no previous applications of Kaplan-Meier, Cox proportional hazards, or survival-analysis methods to
  synchronic dependency-length data were found. Historical-linguistics applications exist only for diachronic phenomena (word
  replacement, grammaticalization). (2) **The Ferrer-i-Cancho confound is real and unresolved**: Ferrer-i-Cancho & Liu (2014)
  rigorously proved that pooled mean dependency distance E[d] is mathematically determined by sentence-length distribution
  E[n], meaning cross-language DLM comparisons using global metrics are unreliable. This confound is documented and acknowledged
  but remains unsolved in current practice—researchers use stratified E[d|n] but not formal survival-analysis frameworks.
  (3) **Why survival analysis is the solution**: Position-bounded arc length in dependency data is structurally isomorphic
  to right-censoring in survival analysis. A word at position p cannot produce arcs longer than (n-p). Stratified Cox proportional
  hazards automatically control for sentence-length composition, making coefficients invariant to sentence-length resampling
  in ways pooled means are not. (4) **Recent field evidence supports positioning**: Gerdes et al. (2026, LREC) demonstrate
  two distinct DLM regimes (grammar-driven functional dependencies: mean 1.71; processing-driven lexical: mean 2.87, σ=0.63),
  supporting typological variation analysis. Futrell et al. (2015, PNAS) established large-scale DLM evidence using length-stratified
  means. Dobrovoljc (2025) shows spoken language has fewer/less-diverse syntactic structures. (5) **Clear boundary with historical-linguistics
  precedent**: Historical applications model word disappearance across centuries (diachronic, calendar time, behavioral event).
  Synchronic survival analysis models structural constraint in a single snapshot (synchronic, position in sentence, censoring
  as structural boundary). These are categorically distinct phenomena using the same statistical machinery. (6) **All six
  components validated**: Theoretical justification (arc length is right-censored), methodological novelty (no prior synchronic
  applications), confound documentation (Ferrer-i-Cancho), technical feasibility (Python lifelines scales to 100k+), typological
  coverage (12+ spoken UD treebanks available), field readiness (DLM is active research receptive to methodological improvements).
  Conclusion: Applying survival analysis to synchronic dependency-arc data is a genuine first—methodologically novel, addressing
  a documented unresolved confound, clearly bounded against historical-linguistics precedent, and ready for top-tier submission
  (ACL, EMNLP, Computational Linguistics).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

id: art_AC8BwlWvA3iR
type: experiment
in_dependencies:
- id: art_V4iFzwfu7i49
  label: gold-labeled dataset
title: Does spoken language shorten dependency links?
summary: >-
  This experiment implements a censored survival-analysis pipeline over 114,480 Universal Dependencies dependency-arc records
  (28 treebanks, 20+ languages, 13 Glottolog families) to test whether spoken register minimizes dependency-arc length more
  than written register, and how word-order typology and morphological richness interact with that pattern. The core method
  (method.py) fits Cox proportional-hazards models where duration=arc_length and event=1 iff arc_length is strictly below
  its position-bounded censoring_bound (an arc that hits the maximum length structurally possible from its token's position
  is treated as censored, not as a fully observed outcome) -- the correct treatment for position-bounded dependency distances,
  which a naive analysis would silently miss. A baseline logistic regression on a median-dichotomized (long/short) arc length,
  ignoring censoring entirely, is fit on identical covariates for direct comparison. The pipeline covers: (1) a primary Cox
  fit on the gold-labeled spoken/written subset (en_childes/en_ewt, fr_rhapsodie/fr_gsd, sl_sst/sl_ssj; n=25,710 in this stratified
  sample) with robust cluster-by-language standard errors (adapted from the planned shared-frailty-by-family since the gold
  subset is 100% Indo-European in this sample, so family has zero variance there); (2) 500-replicate stratified bootstrap
  of family-level Nelson-Aalen cumulative-hazard-at-d=10 residuals (relative to the pooled corpus) across all 13 families
  present in the full corpus, with Benjamini-Hochberg FDR correction to flag confirmed family-level outliers; (3) a secondary
  Cox fit on the full 114,480-arc corpus with family as a fixed effect and mixed gold+heuristic register labels; (4) label-noise
  sensitivity analysis flipping 5/10/20% of heuristically-labeled register values and re-fitting; (5) three word-order operationalization
  variants (categorical Grambank word_order_type, an ordinal linear proxy, and a register-by-word-order interaction) run on
  the full corpus, since the gold subset also has zero word-order variance (all six gold treebanks are verb-medial/SVO) --
  both of these deviations from the artifact plan are documented in the output's deviations_from_plan field; and (6) a random-head-permutation
  null baseline (heads reassigned uniformly within sentence-length bounds) compared via Nelson-Aalen curves and AUC difference
  against the observed data. All Cox fits use a small ridge penalizer for numerical stability under near-collinear typology
  covariates. Key results from the executed run: the censoring-aware primary Cox fit finds NO significant register effect
  on the gold subset (register_spoken beta=-0.032, HR=0.968, p=0.366), while the censoring-naive baseline logistic regression
  on the identical data DOES find a significant effect (beta=0.076, OR=1.079, p=0.006) -- a direct empirical demonstration
  that ignoring position-bounded censoring can manufacture spurious register effects; the full-corpus secondary Cox (mixed
  gold+heuristic labels, family fixed effects) is directionally consistent but only marginal (p=0.063); label-noise sensitivity
  shows the register coefficient staying small and stable in sign as 0/5/10/20% of heuristic labels are flipped; word-order
  variants A/B/C agree the register effect is small and non-significant regardless of operationalization; the family-level
  bootstrap flags 8 of 13 families as BH-significant outliers in position-relative hazard, i.e. substantial residual heterogeneity
  by language family after accounting for register; and the random-head-permutation null shows a large, clear separation from
  the observed data (mean arc length 3.38 observed vs. 8.77 under random head reassignment, Nelson-Aalen AUC difference 78.8),
  confirming strong general dependency-length minimization even though the specific spoken-vs-written contrast is weak in
  this sample. Output follows the exp_gen_sol_out schema: one dataset of 54 examples, each tagged metadata_analysis_type (primary_cox_fit,
  primary_baseline_logit, family_bootstrap_ranking, full_corpus_cox, label_noise_sensitivity, word_order_variant, random_permutation_null,
  model_coefficient) with full nested statistics in metadata_full_result. Downstream paper-writing steps should read metadata_full_result
  off each example for exact coefficients, CIs, p-values, and BH-adjusted significance flags rather than parsing the human-readable
  output/input strings.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_fgt7JgoWQP-k
type: evaluation
in_dependencies:
- id: art_d7jrBtmjm_7W
  label: iter-1 results for comparison and baseline
title: Stress-Testing the Spoken-vs-Written Dependency Model
summary: >-
  Validates the iter-1 survival-hazard reframing of UD dependency-arc lengths (register Cox coef=+0.046, 350 treebanks, 14.56M
  arcs) through four blocks, executed in eval.py against a genuine fresh re-download of 11 treebanks (723,819 arcs: the 3
  gold-register pairs en_childes/en_ewt, fr_rhapsodie/fr_gsd, sl_sst/sl_ssj, plus the 4 spoken/written robustness pairs en/fr/it/uk).
  (1) Effect-size standardization: HR=exp(0.046)=1.047, translating to a 0.082-token reduction in median arc length at the
  corpus-pooled median (1.85 tokens), placing the effect at the 25th percentile of a 4-language cross-language distribution
  of register log-mean-arc-length contrasts. (2) Data-provenance reconciliation: a 22-row provenance_table.csv documenting
  every reported statistic's source pipeline, n_arcs, n_treebanks, annotation source, and quality flag (6 gold_standard, 3
  heuristic_dependent, 13 mostly_reliable rows). (3) Cross-checks: gold-subset-only register coefficient (0.112) vs iter-1's
  full-corpus coefficient (0.046) differs by 146% (fails the plan's 5% tolerance -- an honest finding, not the originally-envisioned
  iter1-vs-iter2 diff, since no separate iter2 artifact exists to compare against); functional-dependency register coefficient
  (0.027) vs lexical (0.122) gives a 4.53x lexical/functional ratio, consistent with Gerdes et al.'s expected pattern; and
  a genuine 30-repeat censoring-bound-decile-balanced resample per language pair (not iter-1's single draw) gives a pooled
  Cox-vs-MDD variance ratio of only ~1.3x, sharply contradicting iter-1's claimed 10-20x -- this is the evaluation's most
  consequential finding and should be reported as a disconfirmation of the robustness-magnitude claim (the qualitative COX_STABLE/MDD_SHIFTS
  direction may still hold but the quantitative ratio does not survive proper repeated resampling). (4) Methodological transparency
  audit (audit_trail.md): documents the 3 genuine gold-label treebank pairs with citations and sample token counts; notes
  only ONE word-order operationalization exists in iter-1 (no second measure to cross-validate against, reported as an honest
  gap); label-noise sensitivity at 0/5/10/20% flips on heuristic-labeled treebanks (it_kiparlaforest/it_parlamint/uk_parlamint
  spoken side, it_isdt/uk_iu majority-written default side) shows the coefficient and its significance are unstable even at
  5% noise; and a block-bootstrap (500 replicates, seed=20260813, resampling treebanks not individual arcs) adds confidence
  intervals to the family-outlier ranking that iter-1 never computed. All numeric results are in eval_out.json (schema-validated
  against exp_eval_sol_out, metrics_agg + 45 per-example rows tagged by validation block) with full/mini/preview size variants
  generated. Downstream paper-writing steps should foreground the variance-ratio contradiction and the large gold-subset delta
  as the two central robustness caveats, not just the confirmatory functional/lexical and provenance results.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json

id: art_vrYpy-2sRrjb
type: research
in_dependencies:
- id: art_2CDrgn6Hae3P
  label: iter-1 research and survival-analysis foundations
title: 'Survival Analysis for Synchronic Dependency Arcs: Novelty & Confound Resolution'
summary: >-
  Comprehensive investigation of novelty positioning for applying survival analysis to synchronic dependency-arc data in Universal
  Dependencies treebanks. Key findings: (1) **No prior synchronic applications exist**: Despite systematic searching of peer-reviewed
  literature and arXiv, no previous applications of Kaplan-Meier, Cox proportional hazards, or survival-analysis methods to
  synchronic dependency-length data were found. Historical-linguistics applications exist only for diachronic phenomena (word
  replacement, grammaticalization). (2) **The Ferrer-i-Cancho confound is real and unresolved**: Ferrer-i-Cancho & Liu (2014)
  rigorously proved that pooled mean dependency distance E[d] is mathematically determined by sentence-length distribution
  E[n], meaning cross-language DLM comparisons using global metrics are unreliable. This confound is documented and acknowledged
  but remains unsolved in current practice—researchers use stratified E[d|n] but not formal survival-analysis frameworks.
  (3) **Why survival analysis is the solution**: Position-bounded arc length in dependency data is structurally isomorphic
  to right-censoring in survival analysis. A word at position p cannot produce arcs longer than (n-p). Stratified Cox proportional
  hazards automatically control for sentence-length composition, making coefficients invariant to sentence-length resampling
  in ways pooled means are not. (4) **Recent field evidence supports positioning**: Gerdes et al. (2026, LREC) demonstrate
  two distinct DLM regimes (grammar-driven functional dependencies: mean 1.71; processing-driven lexical: mean 2.87, σ=0.63),
  supporting typological variation analysis. Futrell et al. (2015, PNAS) established large-scale DLM evidence using length-stratified
  means. Dobrovoljc (2025) shows spoken language has fewer/less-diverse syntactic structures. (5) **Clear boundary with historical-linguistics
  precedent**: Historical applications model word disappearance across centuries (diachronic, calendar time, behavioral event).
  Synchronic survival analysis models structural constraint in a single snapshot (synchronic, position in sentence, censoring
  as structural boundary). These are categorically distinct phenomena using the same statistical machinery. (6) **All six
  components validated**: Theoretical justification (arc length is right-censored), methodological novelty (no prior synchronic
  applications), confound documentation (Ferrer-i-Cancho), technical feasibility (Python lifelines scales to 100k+), typological
  coverage (12+ spoken UD treebanks available), field readiness (DLM is active research receptive to methodological improvements).
  Conclusion: Applying survival analysis to synchronic dependency-arc data is a genuine first—methodologically novel, addressing
  a documented unresolved confound, clearly bounded against historical-linguistics precedent, and ready for top-tier submission
  (ACL, EMNLP, Computational Linguistics).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies

## 1. Introduction

### Problem: Measuring Syntactic Dependency Structure Under Confounding

A foundational empirical finding in quantitative linguistics is that human languages organize words to minimize the linear distance between syntactically related elements—a regularity termed dependency length minimization (DLM) [1]. Futrell et al. (2015) demonstrated this phenomenon across 37 languages by comparing global mean dependency distance (MDD) against random baselines [1]. Yet a rigorous methodological critique, formalized by Ferrer-i-Cancho and Liu (2013), reveals a hidden confound: the empirical distribution of dependency lengths is mathematically determined by the sentence-length distribution [2]. Specifically, even under random arc placement, shorter sentences mechanically produce shorter arcs. This structural confound is particularly severe when comparing across languages, registers, or typological classes that differ in sentence length—or when comparing speech and writing, which are known to differ substantially in syntactic complexity.

Existing remedies—stratified comparisons, random baselines that respect sentence-length distributions, or explicit normalization—address the mean but not the distributional shape. Yet shape carries information: a language might achieve a given mean dependency distance through either a "get-short-or-get-stuck" strategy (high closure probability at short distances, then rapid decay) or through a more uniform distribution (steady closure risk across distances). These represent functionally distinct grammatical and cognitive strategies, yet traditional pooled-mean comparisons cannot distinguish them.

### Why This Matters

Recent evidence suggests both register (speech vs. writing) and typology (word order, morphological richness) shape dependency-length patterns. Gerdes et al. (2026), analyzing 122 languages in Universal Dependencies, identify two distinct DLM regimes: functional dependencies (grammar-driven: ~1.71 tokens mean, invariant across languages) and lexical dependencies (processing-driven: ~2.87 tokens mean, highly variable by typology) [3]. This decomposition suggests that hazard-curve shape—not just central tendency—should differ by register and word-order class. Yet no methodology has characterized distributional shape at UD scale before.

A broader issue: the pooling problem is structural and unresolved in practice. Researchers apply stratified statistics but rarely adopt formal statistical tools designed precisely for this scenario: right-censored time-to-event modeling. A word at position *i* in a sentence of length *n* simply cannot produce arcs longer than min(*i* − 1, *n* − *i*)—a hard structural boundary, not a soft preference. Biostatistics has solved this problem generically for decades through survival analysis, yet it has never been applied to linguistic dependency data.

### Why It's Hard: The Pooling Confound is Structural

Consider a language with two sentence-length classes: short (*n* = 5) and long (*n* = 15). Short sentences cannot produce long arcs. Any pooled summary of arc lengths across both classes is mechanically influenced by the class ratio, independent of dependency-optimization preferences. Standard methods (conditioning on sentence length as a fixed effect, or stratified comparison) provide partial corrections but do not fully eliminate the discrete, structural nature of the censoring: a token at position *i* < *n*/2 has less capacity for long arcs, independent of any linguistic mechanism. This is not a linear confound resolvable through regression adjustment; it is a censoring mechanism.

### Our Approach and Contribution

We reformulate each dependency arc as a right-censored time-to-event outcome: arc length is the "duration," the position-imposed maximum is the "censoring bound," and the hazard function *h(d)* is the instantaneous risk of arc closure at distance *d*. Using non-parametric Kaplan-Meier curves and semi-parametric Cox models stratified by language family, we analyze 14.56 million arcs across 350 UD treebanks. This approach eliminates the pooling confound by treating the sentence-boundary constraint as a design component of the model, not an artifact to be normalized away.

**Key findings:**
1. **Methodological novelty**: First application of survival analysis to synchronic dependency-arc data, resolving the documented length-mixing confound [ARTIFACT:art_2CDrgn6Hae3P].
2. **Register analysis with label-quality caveats**: On gold-labeled spoken/written pairs, the register effect is not significant (β=−0.032, p=0.366) [ARTIFACT:art_AC8BwlWvA3iR]. The apparent effect in the full 350-treebank corpus (β=+0.046, p=1.1e-4) is confounded by heuristic register labeling; label-noise sensitivity analysis shows the effect vanishes under 20% label perturbation [ARTIFACT:art_fgt7JgoWQP-k].
3. **Typological effects**: Word-order class predicts hazard shape robustly (β=−0.028, p=4.9e-25), with free-order languages exhibiting flatter hazard profiles [ARTIFACT:art_d7jrBtmjm_7W].
4. **Family-level heterogeneity**: Language families show substantial residual hazard structure beyond typological covariates; bootstrap confidence intervals are provided for families with sufficient data [ARTIFACT:art_fgt7JgoWQP-k].
5. **Robustness to confounding**: Cox regression coefficients are stable under sentence-length-composition resampling (SD ~ 0.005), whereas pooled-MDD ratios show ~1.3× greater variance [ARTIFACT:art_fgt7JgoWQP-k].

---

## 2. Related Work

### Dependency-Length Minimization as a Linguistic Universal

Futrell et al. (2015) established DLM across 37 typologically diverse languages via large-scale pooled-mean comparison [1]. Subsequent work has expanded this to broader UD corpora and refined the decomposition by dependency type. Temperley (2007, 2008) demonstrated DLM in written English and artificial grammars [4, 5]. Recent meta-analyses have questioned the universality of DLM; Liu (2020) reports mixed evidence across language families, suggesting typological moderation [6].

### The Length-Mixing Confound

Ferrer-i-Cancho and Liu (2013) proved that pooled MDD is mathematically determined by sentence-length distribution: even under random arc placement, *E[d]* ≈ (1/3)(1 + *E[n]*) [2]. This confound is acknowledged but remains unresolved in practice. Researchers apply stratified statistics but do not use formal censored-data methods. Yadav et al. (2022) reappraised DLM as a universal, noting the confound as a methodological concern but not proposing a solution [7].

### Functional vs. Lexical Dependencies

Gerdes et al. (2026) demonstrate that DLM operates through two distinct mechanisms: functional dependencies (determiners, case markers, auxiliaries) are universally short (~1.71 tokens) and invariant, while lexical dependencies (subjects, objects, core arguments) are longer (~2.87 tokens) and typology-sensitive [3]. This decomposition supports the hypothesis that grammar-driven (functional) and processing-driven (lexical) dependencies operate under different optimization pressures.

### Speech vs. Writing in Syntax

Recent comparative work (e.g., Dobrovoljc 2025, cited in the hypothesis) reports that spoken language exhibits fewer distinct syntactic structures than writing, potentially reflecting real-time production constraints. However, cross-linguistic spoken/written comparisons using mean-based statistics have yielded mixed results, with some languages showing longer spoken dependencies [8]. Our survival-analysis approach permits us to distinguish "same mean, different shape" patterns that mean-based comparisons cannot resolve.

### Typology and Word Order

Word-order typology predicts syntactic structure broadly (Dryer 2013, WALS) [9]. Free-order and head-final languages permit different dependency distances; morphological richness (case, agreement) correlates with word-order freedom. Yu et al. (2019) studied DLM vs. word order on 55 treebanks, finding interactions, but without the censoring correction [10].

### Survival Analysis in Linguistics

Survival-analysis methods (Kaplan-Meier, Cox regression, frailty models) have not been applied to synchronic dependency-length or other discrete, position-bounded linguistic data. Historical linguistics employs hazard-function concepts for diachronic phenomena (lexical replacement rates, grammaticalization timescales), but these operate on calendar time, not linear position within an utterance. This work represents the first adaptation of survival methods to the synchronic, position-bounded structure of syntactic dependency arcs [ARTIFACT:art_vrYpy-2sRrjb].

### Universal Dependencies

Nivre et al. (2020) describe the UD annotation scheme and resource collection [11]. UD provides consistent head-dependent relations across 193 languages and 32 language families [ARTIFACT:art_V4iFzwfu7i49], enabling large-scale typological study.

---

## 3. Methods

### The Survival-Analysis Reframing

We treat each dependency arc as a right-censored time-to-event outcome:
- **Duration** (*T*): the observed arc length, *T = |head_position − dependent_position|*
- **Event**: arc closure at exactly distance *d* (indicator = 1 for all observed arcs)
- **Censoring bound** (*C*): the position-imposed maximum arc length, *C = max(dependent_position, sentence_length − dependent_position)*
- **Censoring indicator** (*δ*): *δ = 1* if *T < C* (arc did not reach boundary); *δ = 0* if *T = C* (arc reached boundary, censored)

Across the 14.56 million arcs analyzed, 1.54% are censored—arcs that reach their structural maximum. This censoring is not missing data; it is a design component reflecting sentence boundaries as hard constraints. Standard survival-analysis tools then estimate the hazard function *h(d)*, the instantaneous risk that an arc of length ≥ *d* closes exactly at *d*, conditional on not yet closing and being structurally possible.

#### Why Survival Analysis Fits

The reframing satisfies all survival-analysis assumptions: (1) independence of censoring and outcome (sentence boundaries are deterministic, not selective); (2) identifiability of the hazard (arcs near sentence boundaries have reduced capacity, not reduced preference); (3) no competing risks (arc closure is the only event). Position-bounded arc length is isomorphic to patient follow-up time in a trial: a patient enrolled late is censored not because they are "less healthy," but because the trial structure limits observation time. Similarly, a word near a sentence boundary cannot produce long arcs, independent of language-specific preferences.

### Data Source and Censoring Structure

We extracted all dependency arcs from commul/universal_dependencies on HuggingFace, UD v2.18 (May 2026), across all 350 treebank configurations. This yielded 14,560,338 arcs spanning 193 languages in 32 language families. For each arc, we computed arc_length (*d*), censoring_bound (*c*), and event indicator (*δ*) from CoNLL-U head/dependent positions. **Verification**: 0 censoring-bound violations were found (all *d* ≤ *c*), confirming the reframing's validity. [ARTIFACT:art_V4iFzwfu7i49]

### Data Provenance and Register Classification

Register (spoken vs. written) labeling employs two distinct pipelines, which we distinguish:

**Pipeline A: Gold-labeled subset** (28 treebanks, n=114,480 arcs)
- Three language pairs with genuine gold-documented spoken/written splits:
  - English: en_childes (CHILDES corpus, child-directed speech transcripts) vs en_ewt (written web text)
  - French: fr_rhapsodie (Prosodic Corpus of French, transcribed speech) vs fr_gsd (written text)
  - Slovenian: sl_sst (Slovenian Spoken Spontaneous Treebank, transcribed speech) vs sl_ssj (written standard Slovenian)
- Register labels inferred from treebank metadata (modality/channel tags) and curated name-based matching against known gold-spoken treebanks.
- Primary Cox analysis restricts to this subset to avoid label-quality confounding.

**Pipeline B: Full 350-treebank heuristic-labeled extraction** (n=14,560,338 arcs)
- Register inferred per sentence from UD metadata tags (modality, channel fields) where present, else per-treebank heuristic labels (majority-written default for unknown treebanks).
- Only 3 of 350 treebanks have true gold-documented spoken registers; 347 rely on heuristics.
- Reported as a secondary, label-noise-dependent finding; label-noise sensitivity analysis quantifies the risk [ARTIFACT:art_fgt7JgoWQP-k].

[ARTIFACT:art_fgt7JgoWQP-k]

### Typological Covariates

**Word order** was extracted via two sources:
1. **Grambank**: categorical verb position (V-initial, V-medial, V-final) via Glottocode join, covering 84% of arcs.
2. **Empirical fallback**: for remaining 16%, fraction of dependents preceding their head, computed directly from UD parsed data.
For Cox modeling, we used the empirical continuous measure (fraction preceding) as the primary operationalization for consistency [ARTIFACT:art_fgt7JgoWQP-k].

**Morphological richness**: mean number of UD morphological feature slots per token, scaled to [0,1]. Both covariates were standardized (mean 0, SD 1) before fitting.

### Statistical Models

#### Primary Analysis: Gold-Labeled Subset
Cox proportional-hazards regression on 25,710 arcs from gold-labeled spoken/written pairs (n_spoken=12,855, n_written=12,855, matched by language). Covariates: register, standardized morph_richness. Standard errors clustered by language (6 language codes) to account for within-language correlation. No family-level frailty in the primary model since the gold subset is 100% Indo-European.

**Results**: register_spoken β=−0.032 (95% CI [−0.102, 0.037], p=0.366), morph_richness_std β=−0.082 (95% CI [−0.103, −0.061], p=4.5e-14). Concordance: 0.519.

Interpretation: On gold-labeled data, spoken registers do NOT show significantly higher (or lower) hazard than written registers. The negative coefficient (HR = 0.968) suggests, if anything, spoken arcs are slightly more likely to persist longer—opposite the hypothesis of front-loaded closure in speech [ARTIFACT:art_AC8BwlWvA3iR].

#### Secondary Analysis: Full 350-Treebank Heuristic-Labeled
Cox proportional-hazards regression on 300k-arc subsample (stratified random sample within each language family, family-stratified to capture family-level baseline hazard). Covariates: register (heuristic labels), word_order_scale, morph_richness_std, with small ridge penalizer (α=0.01) for numerical stability.

**Results**: register β=+0.046 (95% CI [0.022, 0.069], p=1.1e-4), word_order β=−0.028 (95% CI [−0.034, −0.023], p=4.9e-25), morph_richness β=+0.0013 (CI [−0.003, 0.006], p=0.52) [ARTIFACT:art_d7jrBtmjm_7W].

The register effect is statistically significant at the 14.56M-arc scale, but label-noise sensitivity analysis shows it becomes non-significant when heuristic labels are perturbed (β → 0.005 at 20% label noise, p=0.157) [ARTIFACT:art_fgt7JgoWQP-k]. This suggests the full-corpus effect is confounded by label assignment method.

#### Robustness: Sentence-Length-Composition Resampling
For the four languages with both spoken and written treebanks (English, French, Italian, Ukrainian), we performed 30-repeat stratified resampling within censoring-bound deciles to control for sentence-length composition. Within each decile, we resampled arcs with replacement and refit the Cox model.

**Results**:
- Cox coefficient SD across 30 resamples per language: 0.004–0.006 (highly stable)
- Pooled-MDD ratio SD across resamples: ~0.006–0.009 (comparable or slightly lower variance)
- Pooled variance ratio (MDD/Cox): 1.31× (sharply contradicting the originally-claimed 10–20× advantage)

Qualitatively, Cox coefficients remain stable under resampling, while pooled-MDD ratios shift more; quantitatively, the robustness advantage is modest [ARTIFACT:art_fgt7JgoWQP-k].

#### Family-Level Heterogeneity
We computed per-family Nelson-Aalen cumulative hazard at *d*=10 across all 14.56M arcs, compared to a word-order-matched cluster baseline, yielding residual-hazard scores. For families with ≥2 treebanks in the sample, we ran 500-replicate block bootstrap (resampling treebanks within family) to generate 95% confidence intervals. Benjamini-Hochberg FDR correction applied across all families tested.

**Results**: Most families show wide, overlapping confidence intervals. NW-Caucasian shows a clear positive residual (point est. 3.62, CI [3.15–4.09]), and Unclassified (polyglot collection) and Indo-Aryan show substantial positive residuals. However, only families with ≥3 treebanks in the bootstrap sample have meaningful CIs; singleton families cannot be reliably ranked [ARTIFACT:art_fgt7JgoWQP-k].

---

## 4. Results

### Primary Finding: No Significant Register Effect at Gold-Label Quality

[FIGURE:fig1]

Kaplan-Meier survival curves for gold-labeled English, French, and Slovenian show substantial overlap between spoken and written hazard profiles within each language. The primary Cox model on this subset yields a non-significant register coefficient (β=−0.032, p=0.366). This directly contradicts the hypothesis that spoken language exhibits front-loaded hazard; instead, the gold-labeled data show no systematic register difference in arc-length distribution.

### Secondary Finding: Apparent Register Effect in Full Corpus is Label-Confounded

In the full 350-treebank corpus with heuristic labels, a statistically significant register effect emerges (β=+0.046, p=1.1e-4). However, this effect is fragile. Label-noise sensitivity analysis shows:

- 0% label noise: β=0.011, p=0.004 (significant)
- 5% label noise: β=0.007, p=0.054 (marginal)
- 10% label noise: β=0.013, p=0.0009 (significant)
- 20% label noise: β=0.005, p=0.157 (non-significant)

At 20% perturbation—a plausible noise rate for heuristic labels applied to 347 of 350 treebanks—the effect vanishes. This suggests the full-corpus effect is driven by label assignment bias, not genuine register differences [ARTIFACT:art_fgt7JgoWQP-k].

### Strong Typological Effect: Word Order

[FIGURE:fig2]

The word-order coefficient (β=−0.028, p=4.9e-25) is large and highly significant. Free-order languages (low fraction of dependents preceding head) exhibit lower hazard, meaning arcs are less likely to close at short distances—they have flatter, lower-peak hazard curves. Fixed-order languages (high fraction preceding) show steeper hazard, with closure concentrated at shorter distances.

Effect size: A one-standard-deviation increase in word-order scale (from fixed to free) corresponds to a hazard ratio of exp(−0.028) = 0.972, a 2.8% decrease in instantaneous closure risk. While the percentage is small, the effect spans an entire typological dimension and is observed across 14.56 million arcs.

Functional vs. lexical stratification: Functional dependencies (articles, case markers) show weaker register effects (β=0.027, CI [0.018–0.036], p=1.6e-8) than lexical dependencies (β=0.122, CI [0.115–0.129], p=2.7e-257), a 4.5× ratio consistent with Gerdes et al. [3] [ARTIFACT:art_fgt7JgoWQP-k].

### Family-Level Structure

[FIGURE:fig3]

Language families show substantial heterogeneity in residual hazard after word-order and morphological-richness covariates are controlled. Bootstrap CIs are wide for most families (singleton or small-sample families), but a few show consistent positive or negative residuals. NW-Caucasian shows notably elevated hazard relative to its typological cluster, while Romance, Slavic, and Indo-Aryan show lower-than-expected hazard.

Interpretation: Family-level deviations suggest language families have distinct grammatical or processing strategies that go beyond word-order typology alone. However, sample-size constraints limit the strength of these claims; replication on larger family-level samples is necessary [ARTIFACT:art_fgt7JgoWQP-k].

### Cross-Check Against Futrell et al. and Gerdes et al.

The hypothesis predicted recovery of Futrell et al. (2015)'s finding that all 37 languages minimize dependency length vs. random baseline. A random-head-permutation null (heads reassigned uniformly within sentence-length bounds) yields mean arc length 8.77 vs. 3.38 observed, a clear and large separation (Nelson-Aalen AUC difference 78.8) [ARTIFACT:art_AC8BwlWvA3iR]. This replicates Futrell's directional result: DLM is strong and consistent across our 350-treebank sample.

The functional/lexical split is confirmed: functional dependencies (β=0.027) show weaker language effects than lexical dependencies (β=0.122), consistent with Gerdes et al.'s hypothesis that grammar-driven dependencies are universal while processing-driven dependencies are typologically variable [ARTIFACT:art_fgt7JgoWQP-k].

---

## 5. Discussion

### Methodological Contribution: Survival Analysis as a Confound-Resolution Tool

The primary contribution of this work is methodological: survival-analysis methods provide a principled, built-in solution to the length-mixing confound that has long plagued dependency-length research. By treating sentence-boundary constraints as censoring (not as a regression predictor to normalize away), we eliminate the mechanical confound at its source. This reframing is not novel to dependency data—biostatistics has used it for decades—but its application to synchronic linguistic data is, to our knowledge, unprecedented [ARTIFACT:art_vrYpy-2sRrjb].

The robustness check partially validates this advantage: Cox coefficients are more stable under sentence-length-composition resampling than pooled-MDD ratios. However, the quantitative advantage (1.3× variance ratio, not 10–20×) is more modest than originally hypothesized, suggesting the confound's practical impact may be smaller in some regimes than others.

### The Register Finding: A Cautionary Tale on Label Quality

Our analysis reveals a stark contrast between gold-labeled and heuristic-labeled registers:
- **Gold-labeled subset** (*n*=25,710, 3 languages): β=−0.032, p=0.366 (not significant).
- **Full-corpus heuristic labels** (*n*=14.56M, 350 treebanks): β=+0.046, p=1.1e-4 (significant, but label-noise-dependent).

This 146% discrepancy and label-noise sensitivity are significant findings in themselves. They demonstrate that register effects in dependency-length research are highly sensitive to annotation quality. For future work, we recommend:
1. Prioritize gold-labeled spoken/written corpora (CHILDES, Rhapsodie, SST, etc.) over heuristic labeling.
2. Explicitly model label uncertainty, rather than treating register as a fixed covariate.
3. Report both gold-labeled and heuristic results, with transparent quality flags.

Our honest finding is that **spoken language does not show significantly front-loaded dependency hazard at gold-label quality**. The apparent effect in the full corpus is confounded by label assignment bias. This does not invalidate the register hypothesis; rather, it underscores that the hypothesis needs cleaner data to test.

### Typological Effects: Robust and Large

The word-order effect (β=−0.028, p=4.9e-25) survives all robustness checks and operationalization variants. Free-order languages exhibit flatter, lower-peak hazard, consistent with the idea that morphological marking (case, agreement) permits longer dependencies without real-time ambiguity. This is a genuine typological signal. Effect size, while a 2.8% hazard decrease per SD, is meaningfully large at the 14.56M-arc scale and aligns with linguistic theory.

### Family-Level Structure: Tentative and Exploratory

Language families show residual heterogeneity, but bootstrap CIs are wide for most families due to limited treebank coverage. NW-Caucasian emerges as an outlier, but this is based on a small sample (*n*_treebanks = 2). We caution against over-interpreting family rankings without larger, more balanced language-family samples in UD.

### Limitations

1. **Register labeling**: Only 3 of 350 treebanks have gold-documented spoken/written splits. The primary register analysis is restricted to these 3 languages, limiting generalizability. The full-corpus heuristic-labeled estimate is confounded by label noise.

2. **Word-order operationalization**: The primary covariate is empirical (fraction of dependents preceding head), not categorical (Grambank/WALS). While this ensures consistency, it differs from typological classifications linguists may prefer. A future sensitivity analysis should compare against Grambank categorical classes.

3. **Family-level frailty**: We use stratification and post-hoc residual ranking as proxies for family-level frailty, rather than explicit random-effect frailty modeling (which lifelines does not natively support). Bayesian methods (e.g., PyMC) would provide more rigorous family-level inference.

4. **Functional vs. lexical stratification**: Register effects are larger for lexical dependencies (β=0.122) than functional (β=0.027). The functional-dependency hypothesis—that grammar-driven dependencies are universal—is supported, but the analysis does not deeply examine *why* lexical dependencies show larger register variance. Deeper linguistic modeling (e.g., by argument structure, semantic role) could refine this.

5. **Sample-size asymmetry**: Spoken arcs are far fewer than written (12,855 vs. 12,855 in gold subset, but 18,846 vs. 67,434 in full corpus across all languages). Small spoken samples in many languages limit power for language-specific register effects.

---

## 6. Conclusion

We have introduced survival-analysis methods to the study of dependency-length minimization, treating arc length as a right-censored time-to-event outcome. This reframes the documented sentence-length-pooling confound as a design component of the model, rather than a statistical hazard to be normalized away.

Our analysis of 14.56 million arcs across 350 UD treebanks yields three findings:

1. **Methodological**: Survival analysis provides a confound-robust framework for quantitative typology. Cox regression coefficients are stable under sentence-length-composition resampling, validating the reframing's utility.

2. **Register**: On gold-labeled spoken/written pairs, no significant register effect emerges (β=−0.032, p=0.366). The apparent effect in the full corpus (β=+0.046) is confounded by heuristic register labeling and vanishes under label-noise sensitivity analysis. Future research should prioritize gold-labeled spoken corpora.

3. **Typology**: Word-order class is a robust, large predictor of hazard-curve shape (β=−0.028, p=4.9e-25). Free-order languages exhibit flatter profiles, consistent with theories linking morphological richness to dependency-length tolerance. Language families exhibit residual structure beyond typology, though bootstrap CIs require larger samples for definitive conclusions.

This work opens a new methodological avenue for quantitative typology, demonstrating that survival-analysis tools can be adapted to linguistic problems with hidden censoring structures. It also serves as a cautionary example: apparent large-scale effects can be artifacts of label quality, emphasizing the need for transparent data provenance in linguistic research.

---

## References

[1] Futrell, R., Mahowald, K., and Gibson, E. (2015). Large-scale evidence of dependency length minimization in 37 languages. *Proceedings of the National Academy of Sciences*, 112(33), 10336–10341.

[2] Ferrer-i-Cancho, R. and Liu, H. (2013). The risks of mixing dependency lengths from sequences of different length. *Glottotheory*, 5, 143–155.

[3] Gerdes, K. (2026). The grammar does the work: Functional vs. lexical dependency length minimization across the UD languages. *Proceedings of the Language Resources and Evaluation Conference*.

[4] Temperley, D. (2007). Minimization of dependency length in written English. *Cognition*, 105(2), 300–333.

[5] Temperley, D. (2008). Dependency-length minimization in natural and artificial languages. *Journal of Quantitative Linguistics*, 15(3), 256–282.

[6] Liu, Z. (2020). Mixed evidence for crosslinguistic dependency length minimization. *STUF—Language Typology and Universals*, 73(4), 605–633.

[7] Yadav, H., Mittal, S., and Husain, S. (2022). A reappraisal of dependency length minimization as a linguistic universal. *Open Mind*, 6, 147–168.

[8] Jaeger, T. F. and Wasow, T. (2010). Processing preference and language design. *Annual Review of Linguistics*, 35, 245–268.

[9] Dryer, M. S. (2013). Order of subject, object and verb. In *World Atlas of Language Structures Online*. Max Planck Institute for Evolutionary Anthropology.

[10] Yu, X., Falenska, A., and Kuhn, J. (2019). Dependency length minimization vs. word order constraints: An empirical study on 55 treebanks. In *Proceedings of the First Workshop on Quantitative Syntax (Quasy, SyntaxFest 2019)*.

[11] Nivre, J., Marneffe, M. de, Ginter, F., Hajivc, J., Manning, C. D., Pyysalo, S., Schuster, S., Tyers, F. M., and Zeman, D. (2020). Universal dependencies v2: An evergrowing multilingual treebank collection. In *Proceedings of the 12th Language Resources and Evaluation Conference (LREC)*, pp. 4034–4043.

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (rigor) The primary Cox model's concordance index (0.519) is reported in the Methods results line but never interpreted or flagged as a limitation anywhere in Results, Discussion, or Limitations. A concordance of 0.519 is only marginally above the 0.5 value expected from an uninformative model — it indicates that register + morphological richness together have almost no ability to rank-order which of two arcs will close first at the individual-arc level, even though the population-level register coefficient is (correctly) reported as non-significant. This matters especially for the secondary/full-corpus model, where a formally 'significant' register coefficient (p=1.1e-4) driven by 14.56M arcs could similarly coexist with near-chance individual discrimination, and the paper does not report or discuss concordance for that model at all.
  Action: Report concordance (or an equivalent discrimination statistic) for both the primary and secondary Cox models, and add explicit interpretive text distinguishing 'statistically detectable population-level coefficient' from 'individually informative model.' This should temper language like 'robust to confounding' in the Discussion, which currently reads as claiming more than a near-chance-concordance model with a marginal effect size supports.
- [MINOR] (evidence) Gerdes et al. (2026) — the functional-vs-lexical decomposition the paper relies on as an independent cross-check and cites four times as supporting evidence — is dated to a future LREC (2026) proceedings and its exact title/venue cannot be independently verified against a public, indexed record from this review. The paper additionally cites it inconsistently as both single-author 'Gerdes, K. (2026)' in the reference list and 'Gerdes et al. (2026)' throughout the body text, which itself signals the citation was not checked against the actual publication metadata.
  Action: Verify the exact author list, venue, and year of the Gerdes citation against a DOI/ACL-anthology or arXiv record before camera-ready, and make the in-text and reference-list author forms consistent. If the paper cannot be independently verified as existing/accepted, either soften reliance on it as a load-bearing cross-check or clearly flag it as a preprint/forthcoming work.
- [MINOR] (clarity) Limitations point 5 states 'Spoken arcs are far fewer than written (12,855 vs. 12,855 in gold subset, but 18,846 vs. 67,434 in full corpus across all languages)' — the first clause reports equal counts (12,855 vs. 12,855) as evidence of imbalance, which is self-contradictory as written; only the second clause (18,846 vs. 67,434, referring to the unmatched Pipeline-A corpus before Cox-model stratified sampling) actually demonstrates the imbalance being described.
  Action: Rewrite to state plainly that the gold-subset Cox analysis is deliberately balanced by design (12,855/12,855 via matched sampling), while the underlying raw Pipeline-A extraction from which it was drawn is imbalanced (18,846 spoken vs. 67,434 written), and that the imbalance concern applies to any future work using the raw pipeline rather than to the reported Cox estimate itself.
- [MINOR] (evidence) The word-order effect is simultaneously described as 'small' (2.8% hazard-ratio decrease) and 'meaningfully large' within the same Discussion paragraph, and no calibration point is given for what a linguistically meaningful hazard-ratio shift would look like in this domain — unlike the register effect, which the companion evaluation artifact translates into a concrete 0.082-token median-arc-length shift and a percentile within a cross-language effect-size distribution. Readers cannot tell whether the word-order effect is linguistically large or merely statistically detectable at n=14.56M, the same criticism the paper itself levels at typical DLM literature.
  Action: Apply the same effect-size standardization already used for the register effect (median-arc-length-shift translation, or percentile against a comparable cross-linguistic distribution) to the word-order coefficient, and remove or justify the 'meaningfully large' characterization with that calibration rather than an unanchored qualitative claim.
- [MINOR] (evidence) The aggregate secondary-Cox register coefficient (β=+0.046, full corpus) and the deprel-stratified functional (β=0.027) / lexical (β=0.122) register coefficients reported later in Results are never explicitly reconciled — a reader cannot tell whether the aggregate is a weighted mixture of the two strata, whether the strata were fit on the same sample as the aggregate model, or why the lexical-only coefficient (0.122) is nearly 3x the reported aggregate.
  Action: Add one sentence in Results clarifying the relationship between the pooled and deprel-stratified register coefficients (e.g., stating the pooled estimate reflects the arc-count-weighted mixture of the two, and reporting the functional/lexical arc-count split used) so the numbers are legible as a coherent decomposition rather than three independent claims.
- [MINOR] (scope) The title continues to frame the contribution as characterizing dependency lengths 'Across Universal Dependencies' generally, but the paper's most decisive positive finding is the word-order/typology result, while the register component of the title's implicit framing (speech vs. writing, foregrounded heavily in the Introduction's motivating narrative) is the one result the paper itself disconfirms at gold-label quality. The current title/abstract balance may lead readers to expect a stronger register story than the paper ultimately delivers.
  Action: Consider whether the abstract's opening framing could shift weight toward the methodological contribution and the word-order finding as primary, with the register finding explicitly framed as a cautionary case study on label quality — this would better match the paper's actual evidentiary strength distribution and reduce the risk of a reviewer feeling the title over-promises on speech/writing content that the paper itself walks back.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-13 13:05:37 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SYSTEM-USER prompt · 2026-08-13 13:06:15 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Same censoring frame; register claim downgraded to disconfirmed/cautionary, word-order promoted to primary evidence-backed result.' is too long (at most 120 characters, got 130)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
