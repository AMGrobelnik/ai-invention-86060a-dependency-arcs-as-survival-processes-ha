# gen_paper_text — test_idea

> Phase: `invention_loop` · round 2 · `gen_paper_text`
> Run: `run_oQQwThF8kM-b` — Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-13 12:57:59 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A research paper writer (Step 3.4: GEN_PAPER_TEXT in the invention loop)

You received the hypothesis, all artifacts, the previous paper draft (if any), and reviewer feedback.
Write a complete paper draft with figure placeholders.

Publication-quality paper → strong contribution. Weak paper → wasted iteration.
</your_role>
</ai_inventor_context>

<research_methodology>
Write like a researcher drafting a paper, not a chatbot summarizing bullet points.

- Structure as a paper would: research question → methodology → results → analysis → limitations. Not a list of "we did X, then Y."
- Ground every claim in specific artifacts and specific numbers. "Results show improvement" is empty — state effect sizes, baselines, and conditions.
- Be honest about what worked, what didn't, and why. Don't spin failures as "future work."
- The paper's headline contribution should be a positive or surprising finding. Negative results are valuable context but should not be the primary narrative — lead with what works.
- Address reviewer feedback from previous iterations explicitly — show you've thought about each critique.
</research_methodology>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape. Two modes: general (default, broad web) and scholarly (peer-reviewed papers + citations) — pass mode=scholarly for prior-art, related-work, and citation lookups.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Length Across Speech and Writing

## Introduction

### The Problem: Measuring Syntactic Efficiency Under Confounding

A core finding in quantitative linguistics is that human language minimizes dependency length—the linear distance between syntactically related words [1]. Futrell et al. (2015) demonstrated this across 37 languages via pooled mean-dependency-distance (MDD) comparisons [1]. Yet a methodological critique, formalized by Ferrer-i-Cancho and Liu (2013), reveals a hidden confound: the empirical distribution of dependency lengths in a language is mathematically determined by that language's sentence-length distribution [2]. Specifically, if E[n] is the mean sentence length and dependencies are random, then E[d] = (1/3)(1 + E[n]) [2]. Two languages can differ in observed global MDD purely because one has longer sentences—not because one optimizes dependencies better within sentences. This confound is particularly severe when comparing speech and writing, which are known to differ in sentence length, or when comparing typologically distant language families.

Existing remedies—random baselines respecting sentence-length distribution, or explicit normalization by sentence length—address the mean but not the distributional shape. Yet shape carries information: a language might achieve the same mean dependency distance through either a "get-short-or-get-stuck" strategy (high risk of closure at short distances, then declining) or a more uniform distribution (steady risk across distances). These are functionally distinct cognitive and grammatical strategies, yet traditional MDD comparisons cannot distinguish them.

### Why This Matters: Spoken Language and Typology

Recent evidence suggests modality (speech vs. writing) and typology (word order, morphological richness) both shape dependency-length patterns. Dobrovoljc (2025), analyzing English and Slovenian, reports that spoken language exhibits fewer and less diverse syntactic structures than writing—potentially reflecting real-time production constraints [3]. Gerdes et al. (2026), studying 122 languages, show that functional dependencies (det, case, aux—grammar-driven) are universally short (~1.71 tokens), while lexical dependencies (nsubj, obj—processing-driven) are longer and highly variable across typology [4]. These findings suggest that hazard-curve shape should differ by modality and word-order class, but no methodology has characterized this distribution-level structure before.

### Why It's Hard: Statistical Confounding in Aggregated Data

The pooling problem is structural. In a language with two sentence-length classes (short and long), short sentences cannot produce long dependencies. Any aggregated statistic across both classes is mechanically influenced by the length-class ratio, independent of actual dependency-optimization preferences. Standard mixed-effects models, which condition on sentence length as a fixed effect, help but do not fully resolve the issue: position-dependent censoring (the fact that a token at position i < sentence-length/2 simply *cannot* produce a long arc) remains a discrete, structural constraint, not a linear shift.

### Why It Hasn't Been Solved

Biostatistics solved this problem decades ago via survival analysis, where right-censoring (known lower bounds on event times) is the standard tool [5]. A patient enrolled late in a trial has less follow-up time—not because they are "less healthy," but because of the trial structure. Arc length is identical: a word near a sentence boundary has less arc-length capacity—not because the language disfavors it, but because of the sentence structure. Yet survival analysis has never been applied to linguistic dependency data, despite perfect methodological fit. This represents a genuine gap between linguistic methodology and available statistical tools.

### Our Approach and Contributions

We reframe each dependency arc as a right-censored time-to-event object: arc length is the "duration," the position-imposed maximum is the "censoring bound," and the hazard function h(d) is the instantaneous risk of arc closure at distance d. Using Kaplan-Meier curves, Nelson-Aalen cumulative hazard, and stratified Cox proportional-hazards models, we estimate hazard-curve shape across 350 UD treebanks (14.56 million arcs), controlling for register (spoken/written), word-order typology, morphological richness, and language family. This approach eliminates the pooling confound, recovers distributional shape that mean-based statistics cannot report, and scales to large data.

### Summary of Contributions

1. **Methodological novelty**: First application of survival analysis to dependency-arc data [ARTIFACT:art_2CDrgn6Hae3P].
2. **Spoken-vs-written effect**: Registers show a front-loaded hazard profile (β=+0.046, p=1.1e-4) [ARTIFACT:art_d7jrBtmjm_7W].
3. **Typological effects**: Word-order class predicts hazard shape (β=-0.028, p=4.9e-25) [ARTIFACT:art_d7jrBtmjm_7W].
4. **Family-level heterogeneity**: Language families deviate from typological clusters (residuals up to ±1.8) [ARTIFACT:art_d7jrBtmjm_7W].
5. **Robustness validation**: Cox coefficients stable under sentence-length resampling; pooled MDD is not [ARTIFACT:art_d7jrBtmjm_7W].

---

## Related Work

### Dependency-Length Minimization as a Regularity

Futrell et al. (2015) established DLM as a cross-linguistic universal via large-scale comparison of 37 languages [1]. Subsequent work has expanded this to typologically diverse corpora (Gerdes et al., 122 languages, 2026) [4].

### The Length-Mixing Confound

Ferrer-i-Cancho and Liu (2013) proved that pooling dependency lengths across sentences of different lengths introduces a confound [2]. E[d] is mathematically determined by E[n] even under random arc placement.

### Speech vs. Writing in Syntax

Dobrovoljc (2025) reports spoken English and Slovenian contain fewer distinct syntactic structures than writing [3]. Jaeger and Wasow (2010) reviewed cognitive factors linking production constraints to dependency-length preferences [6].

### Functional vs. Lexical Dependency Types

Gerdes et al. (2026) show functional dependencies are universally short (~1.71 tokens) and invariant, while lexical dependencies are longer (~2.87 tokens) and typology-sensitive [4].

### Typology and Word Order

Word-order typology predicts syntactic structure (Dryer 2013, WALS). Free-order and head-final languages show different dependency patterns; morphological richness (case, agreement) correlates with word-order freedom.

### Survival Analysis in Linguistics

To our knowledge, survival analysis has not been applied to dependency-length or syntactic data. Time-to-event methods appear in psycholinguistic eye-tracking but operate on continuous reaction times, not position-bounded discrete counts. This work represents the first such application.

### Universal Dependencies Resources

UD (Nivre et al., 2020) is the largest cross-linguistic treebank collection [7]. Recent work leverages UD for typological studies, including speech/writing comparisons [3, 8].

---

## Methods

### Data and Censoring Structure

We extracted all dependency arcs from commul/universal_dependencies (HuggingFace) across 350 treebanks (UD v2.18, May 2026), yielding 14,560,338 arcs across 193 languages in 32 language families [7]. For each arc, we computed: (1) arc length d = |head_position − dependent_position|; (2) censoring bound c = max(dependent_position, sentence_length − dependent_position); (3) event indicator = 1 (all arcs observed). [ARTIFACT:art_V4iFzwfu7i49]

### Register Classification

Register was inferred per sentence from UD metadata (modality/channel tags, meta::genre fields). For treebanks without explicit metadata, we used curated name-based heuristics. This yielded 18,846 spoken arcs and 67,434 written arcs across matched language pairs (English, French, Italian, Ukrainian). [ARTIFACT:art_V4iFzwfu7i49]

### Typological Covariates

**Word order** was extracted from Grambank via Glottocode joins (verb-initial, verb-medial, verb-final). For missing values, we computed empirically: fraction of dependents preceding their head. **Morphological richness** was the mean number of UD morphological feature slots per token, scaled to [0,1]. Both covariates were standardized before Cox modeling.

### Statistical Models

#### Kaplan-Meier Survival Curves

For each (language, register) pair, we fit non-parametric Kaplan-Meier curves estimating S(d) = P(arc length ≥ d), revealing whether spoken and written registers differ in hazard profiles within a language.

#### Cox Proportional-Hazards Regression

We fit a stratified Cox model (lifelines v0.30.3+) with duration = arc_length, event = 1, covariates = register + word_order_scale + morph_scale, stratified by language family (32 families). The Cox partial-likelihood yields semi-parametric estimates of how covariates multiply the baseline risk. [ARTIFACT:art_d7jrBtmjm_7W]

Results: register β=+0.0456 (95% CI [0.0225, 0.0688], p=1.1e-4), word-order β=-0.0283 (CI [-0.0336, -0.0229], p=4.9e-25), morph β=+0.0013 (CI [-0.0028, 0.0055], p=0.52).

#### Family Residual Hazard

We computed per-family Nelson-Aalen cumulative hazard at d=10, compared to a word-order-matched cluster baseline, yielding residual-hazard scores. Dravidian showed the largest positive residual (+1.80, n=18,353 arcs). [ARTIFACT:art_d7jrBtmjm_7W]

### Robustness: Sentence-Length Resampling

We resampled arcs within censoring-bound decile strata (100 resamples) and refit the Cox model. Coefficients remained stable (SD < 0.003), while pooled-MDD ratios exhibited 10-20× greater variance, confirming survival-based estimates are robust to pooling confounds. [ARTIFACT:art_d7jrBtmjm_7W]

---

## Results

### Kaplan-Meier Curves by Language and Register

[FIGURE:fig1]

Spoken registers across English, French, Italian, and Ukrainian consistently show lower survival probability (higher cumulative hazard) at short distances compared to written registers within the same language. This pattern replicates cross-linguistically and persists after accounting for sentence-length composition. [ARTIFACT:art_d7jrBtmjm_7W]

### Cox Proportional-Hazards Coefficients

[FIGURE:fig2]

The register coefficient (β=+0.0456, p=1.1e-4) indicates spoken arcs have ~4.7% higher instantaneous hazard than written arcs, conditional on arc length distribution. This effect size is small but highly significant across 14.56M arcs and unconfounded by position-based censoring. The word-order coefficient (β=-0.0283, p=4.9e-25) indicates free-order languages have significantly lower hazard, consistent with the hypothesis that typological freedom permits longer arcs without processing cost. Morphological richness was not significant (p=0.52). [ARTIFACT:art_d7jrBtmjm_7W]

### Family-Level Residual Hazard Outliers

[FIGURE:fig3]

Among 32 language families, Dravidian shows the most pronounced positive residual hazard (+1.80), meaning arcs from Dravidian languages have substantially higher closure risk at d=10 than the head-final cluster baseline, even after controlling for word order and morphology. NW-Caucasian (+0.83) and Turkic (+0.63) also show notable positive residuals. Romance (-0.48), Iranian (-0.53), and Anatolian (-0.83) show lower-than-expected hazard. This family-level structure, not explainable by typological covariates, suggests distinct family-level optimization strategies. [ARTIFACT:art_d7jrBtmjm_7W]

### Robustness to Sentence-Length Confounding

[FIGURE:fig4]

Across 100 resamples within censoring-bound deciles, Cox regression coefficients showed negligible variance (SD register ≈ 0.0004, SD word-order ≈ 0.0003). Pooled-MDD ratios exhibited 10-20× greater variance across resamples (e.g., en_spoken/en_written MDD ratio ranged 0.93–1.08). This directly confirms survival-analysis estimates are robust to sentence-length composition, while pooled-mean comparisons are not. [ARTIFACT:art_d7jrBtmjm_7W]

### Cross-Check Against Prior Literature

The hypothesis predicts three directional effects: (1) spoken_front_loaded (positive register coef), (2) free_order_flatter (negative word-order coef), (3) family structure. All three are confirmed [ARTIFACT:art_d7jrBtmjm_7W]. Futrell et al. (2015) report all 37 languages minimize vs. random baseline [1]; we recover this. Gerdes et al. (2026) identify functional-vs-lexical split [4]; our Cox model stratified by deprel finds register effects larger for lexical (β=+0.062) than functional (β=+0.018) arcs. Dobrovoljc (2025) reports spoken syntax is simpler [3]; hazard-based measures confirm this reflects genuinely different arc-closure profiles.

---

## Discussion

### Findings in Context

We have demonstrated that survival-analysis methods provide a principled, confound-robust framework for characterizing dependency-length distributions. The spoken-vs-written effect (β=+0.0456) is modest but highly significant and robust to confounding. The word-order effect (β=-0.0283) is stronger and shows clear typological interpretation. Family-level structure (residuals up to ±1.8) reveals language-family-specific mechanisms beyond typological covariates.

### Methodological Advantages and Limitations

**Advantages:** Eliminates pooling confound via explicit censoring. Recovers hazard-curve shape, not just central tendency. Scales to large data (14.56M arcs in ~134 seconds). Naturally accommodates stratification without ad hoc normalization.

**Limitations:** Cannot distinguish "true" vs. structural censoring; all UD arcs are observed. Register classification relies on metadata inconsistently annotated across treebanks; only 3 of 28 focused treebanks have gold-annotated spoken/written splits. Morphological richness proxy is crude; Grambank/WALS coverage is incomplete (84% of arcs). Family-level frailty effects estimated via stratification, not explicit random-effect frailty (lifelines lacks native support). Sample size for spoken/written comparison is modest (4 language pairs; n_spoken=18,846).

### Functional Interpretation

The front-loaded hazard in spoken language aligns with cognitive theories of real-time production [6]. Speakers must commit to syntactic relations quickly to maintain fluency. Written language permits longer dependency chains. Typological effects (free-order languages showing flatter hazard) suggest morphological marking licenses longer dependencies by reducing real-time ambiguity.

### Future Directions

1. Stratification by dependency type within survival framework to quantify whether register/typology effects differ by dependency role.
2. Explicit frailty modeling using Bayesian Cox models to estimate family-level variance.
3. Temporal dynamics: sentence-position effects and inter-clausal dependencies.
4. Language change: historical corpora to track hazard-profile shifts.

---

## Conclusion

We have introduced survival analysis to the study of dependency-length minimization, treating arc length as a right-censored time-to-event outcome. This eliminates the sentence-length-pooling confound and recovers hazard-curve shape information unavailable to mean-based statistics.

Our analysis of 14.56 million arcs across 350 UD treebanks confirms three core hypotheses: (1) spoken language shows front-loaded hazard (β=+0.046, p=1.1e-4), consistent with real-time production; (2) word-order typology predicts hazard shape (β=-0.028, p=4.9e-25), with free-order languages showing flatter profiles; (3) language families exhibit residual structure not explained by typological covariates.

This work opens a new methodological avenue for quantitative typology, demonstrating that survival-analysis tools can be adapted to linguistic problems with hidden censoring structures. Future work should extend this framework to finer-grained dependency types, explicit Bayesian frailty modeling, and diachronic analysis.

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (rigor) The Methods section states the event indicator is '1 (all arcs observed)' and the Limitations section repeats 'all UD arcs are observed' — but this directly contradicts both the paper's own Results ('1.54% censored') and the actual code in method.py, which computes event = 1 if arc_length < censoring_bound else 0 (i.e., a genuine right-censoring rule, not a trivial always-observed indicator). As written, the paper's description of its own central mechanism is self-contradictory and does not match the artifact it cites.
  Action: Correct the Methods text to state the actual censoring rule (event=0, i.e. censored, precisely when an arc reaches its position-imposed maximum, arc_length == censoring_bound; this occurs for 1.54% of arcs), and remove or correct the false 'all arcs are observed' statement in Limitations. Add one worked example (a token near a sentence boundary whose arc is censored) to make the mechanism concrete.
- [MAJOR] (evidence) The flagship spoken-vs-written finding (register β=+0.0456, p=1.1e-4) is fit on a corpus where only 3 of 350 treebanks have gold-documented spoken register (per the experiment artifact's own stated limitation); the remaining treebanks are labeled via metadata heuristics or a 'majority-written default'. A Cox coefficient built mostly on noisy/defaulted labels, reported with p=1.1e-4 from a huge N, conflates statistical significance (driven by sample size) with construct validity (driven by label quality). The paper's Discussion calls this effect 'robust to confounding' without addressing label reliability, which is a distinct and more serious threat to validity than the pooling confound the paper set out to solve.
  Action: Re-run the register-specific Cox coefficient restricted to the gold-labeled subset only (English/French/Slovenian pairs, n≈18,846 vs. 67,434) and report that as the primary register estimate, with the full-350-treebank estimate reported as a secondary, heuristic-label-dependent robustness check rather than the headline number. Report a label-noise sensitivity analysis (e.g., re-fit after randomly flipping X% of heuristic register labels) to bound how much the effect could be an artifact of the majority-written default.
- [MAJOR] (evidence) 32 language families are ranked by residual hazard at d=10 and the top three (Dravidian +1.80, NW-Caucasian +0.83, Turkic +0.63) are reported as 'notable' without any multiple-comparison correction or confidence interval on the residual itself, despite testing 32 families. With 32 comparisons, some large residuals are expected under noise alone, especially for small families (Dravidian n=18,353 arcs is one of the smaller family samples relative to Indo-European branches).
  Action: Report bootstrap or analytic confidence intervals for each family's residual hazard, apply a Benjamini-Hochberg correction across the 32 comparisons, and explicitly state how many families remain significant after correction. If Dravidian survives, strengthen the claim; if not, reframe as suggestive/exploratory rather than a confirmed finding.
- [MINOR] (novelty) The claim 'survival analysis has never been applied to linguistic dependency data' (and 'time-to-event methods appear in psycholinguistic eye-tracking but operate on continuous reaction times') is plausible but stated with more confidence than the search process supports — the supplementary research artifact describes only a 'systematic search' without listing what was searched or what near-misses were found (e.g., hazard/survival models have been used for language change and lexical attrition in historical linguistics, which is adjacent but not cited or ruled out).
  Action: Either broaden the novelty search to explicitly address historical-linguistics hazard models (e.g., work on lexical replacement rates, grammaticalization as survival processes) and cite/distinguish from them, or soften the novelty claim to 'first application to synchronic dependency-length data' rather than an unqualified first-ever claim.
- [MAJOR] (clarity) The paper uses two different datasets interchangeably without clearly distinguishing them: a 28-treebank gold-curated dataset (114,480 sampled rows / 6.13M full extraction) and a 350-treebank direct-from-HuggingFace extraction (14.56M arcs) used for the headline Cox/KM/Nelson-Aalen results. It is not clear from the paper text which numbers (e.g., n_spoken=18,846) come from which pipeline, or whether the 'curated, gold-labeled register' dataset was used for the headline Cox fit at all, given the Cox model is described as running on 'all 350 treebank configs.'
  Action: Add an explicit 'Data provenance' subsection in Methods stating exactly which pipeline (curated-28 vs. full-350) produced which reported statistic, and reconcile the n=18,846/67,434 spoken/written counts with the 14.56M-arc full run.
- [MINOR] (methodology) Word-order typology is operationalized inconsistently: primary source is Grambank's categorical verb-initial/medial/final class (via Glottocode join, covering 84% of arcs), with a continuous empirical fallback (fraction of dependents preceding their head) for the remaining 16% — these are then merged into a single standardized 'word_order_scale' covariate for the Cox model without explaining how a categorical class and a continuous ratio are placed on the same standardized scale.
  Action: Either restrict the covariate to the empirical continuous measure throughout (dropping the categorical/Grambank source for consistency) or explicitly model word order as separate categorical dummy + continuous residual terms, and report a sensitivity analysis showing the Cox coefficient is stable under either choice.
- [MINOR] (evidence) The Cross-Check subsection claims to 'recover' Futrell et al. (2015)'s finding that all 37 languages minimize dependency length vs. a random baseline, and to confirm Gerdes et al. (2026)'s functional-vs-lexical split, but no actual comparison statistic (e.g., a random-baseline hazard curve, or a stratified-by-deprel effect-size comparison table) is shown for the Futrell claim — only the deprel-stratified register coefficients (β=0.062 lexical vs. 0.018 functional) are reported for Gerdes.
  Action: For the Futrell comparison, compute and report a random-arc-placement null hazard curve (analogous to the paper's own random-baseline logic in Related Work) alongside the observed hazard curve, so 'we recover this' is a demonstrated result rather than an assertion.
- [MINOR] (scope) The paper positions itself as characterizing 'syntactic length across speech and writing' broadly, but the spoken-vs-written comparison is limited to 4 language pairs (English, French, Italian, Ukrainian) despite the corpus spanning 193 languages — the title and abstract's framing ('Across Speech and Writing') somewhat overstates the breadth of the register analysis relative to the typology/family analysis, which does span the full corpus.
  Action: Either expand the register comparison to more matched pairs if UD v2.18 has additional spoken/written pairs beyond the 4 used, or adjust the title/abstract to more precisely reflect that the register finding is a 4-pair case study nested within a 350-treebank typological survey.
- [MINOR] (clarity) The effect-size framing throughout (register β=+0.0456 described as '~4.7% higher instantaneous hazard') would benefit from an explicit comparison to what effect size would be practically meaningful in this domain — a reader cannot tell from the paper whether a 4.7% hazard increase is linguistically large or negligible relative to, e.g., the magnitude of within-language variance across sentences.
  Action: Report a standardized effect size (e.g., in terms of median survival distance shift, or percentile of the between-language variance in the same coefficient) so readers can calibrate whether the register effect is linguistically meaningful, not just statistically detectable at n=14.56M.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

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
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 6 research artifacts across all iterations.

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
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

id: art_AC8BwlWvA3iR
title: Does spoken language shorten dependency links?
type: experiment
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

id: art_fgt7JgoWQP-k
title: Stress-Testing the Spoken-vs-Written Dependency Model
type: evaluation
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

id: art_vrYpy-2sRrjb
title: 'Survival Analysis for Synchronic Dependency Arcs: Novelty & Confound Resolution'
type: research
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
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

FIGURE TYPE — set `figure_type` on every figure. One test decides it: does the figure plot numbers?
  "data"    — a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling
              laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically
              from the values you supply, so every bar is exactly the height of its number.
  "concept" — a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything
              with no underlying dataset. Drawn by an image model.
If the figure has real numbers behind it, ALWAYS use "data". An image model only approximates
values: the bars come back close to, but not equal to, the numbers you asked for, and nothing
downstream detects it.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison — plots numbers, so a data figure):
  {"id": "fig3", "title": "Performance Comparison", "figure_type": "data", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. Categories: PostgreSQL, Bao, RLQOpt. One series 'Latency'. Values: 4.6, 2.8, 2.0 seconds. Errors: 0.8, 0.5, 0.3. X-axis label 'Optimizer'. Y-axis label 'Latency (s)', range 0-5.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero — no dataset, so a concept figure):
  {"id": "fig1", "title": "System Architecture", "figure_type": "concept", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description. For a "data" figure, list the values per series
plus the axis labels and units; the renderer needs the numbers themselves, not a description of
what they look like.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
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
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "figure_type": {
          "description": "Which generator draws this figure. Decide by ONE test: does the figure plot numbers? 'data' \u2014 a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically from the numbers, so every bar is exactly the height of its value. 'concept' \u2014 a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything with no underlying dataset. When a figure has real numbers behind it, ALWAYS choose 'data': an image model only approximates values, producing bars that disagree with their own labels.",
          "enum": [
            "data",
            "concept"
          ],
          "title": "Figure Type",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "The generator's ONLY input \u2014 it cannot read files. For figure_type='data': every numeric value to plot, per series, with axis labels and units, category names, and what the figure has to make the reader see \u2014 the comparison, trend, trade-off or distribution that is the point. Name a chart type only if you actually want a specific one: the figure generator reads its own catalogue of chart types and picks the one that fits, so an enumeration here would only go stale as that catalogue grows. For figure_type='concept': the composition \u2014 what appears where, colours, labels, and what to leave out.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "aspect_ratio": {
          "default": "21:9",
          "description": "Shape of the figure. '21:9' for architecture diagrams / pipelines / flow charts (the paper's hero diagram is usually one of these), '16:9' for side-by-side comparisons and multi-panel results, '4:3' for dense charts, '1:1' for heatmaps / confusion matrices / scatter plots, '3:4' or '9:16' for vertical layouts.",
          "enum": [
            "1:1",
            "4:3",
            "3:2",
            "16:9",
            "21:9",
            "3:4",
            "9:16"
          ],
          "title": "Aspect Ratio",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "figure_type",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-13 12:57:59 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-08-13 12:58:39 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-08-13 12:58:39 UTC

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

### [5] SKILL-INPUT — aii-web-tools · 2026-08-13 12:58:56 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: free-first web search (general or scholarly, Serper fallback), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — free-first web search (keyless general/scholarly engines,
   Serper fallback), html2text + PyMuPDF for fetch, and regex grep over the full
   document text. They work without any built-in web tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (free-first: general or scholarly)

```bash
# general web (default): keyless engines (ddgs, marginalia); Serper only if they miss
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
# scholarly mode: OpenAlex + Crossref (DOIs, citation counts)
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation" --mode scholarly
```

Returns ranked title / URL / snippet lines. `--mode general` (default) uses
keyless general engines; `--mode scholarly` uses academic APIs. Both fall back
to Serper (paid) only when the free engines miss. Use search first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````
