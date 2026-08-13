# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `run_oQQwThF8kM-b` — Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_strat_1` (terminal_claude_agent, claude-haiku-4-5)

### [1] CONFIG · 2026-08-13 12:15:52 UTC

```
model: claude-haiku-4-5 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_strat/gen_strat_1
```

### [2] SYSTEM-USER prompt · 2026-08-13 12:15:58 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A strategy planner (Step 3.1: GEN_STRAT in the invention loop)

Each iteration of the invention loop runs: GEN_STRAT → GEN_PLAN → GEN_ART → GEN_PAPER_TEXT → REVIEW_PAPER → UPD_HYPO
Artifact types: RESEARCH (web search), EXPERIMENT (code), DATASET (data collection), EVALUATION (metrics), PROOF (Lean 4)
State persists across iterations: strategies, plans, artifacts, paper_texts (read from the run tree)

You received the hypothesis, iteration status (current + remaining), previous iteration's strategies, available artifact types, existing artifacts, and reviewer feedback.
Your strategy governs THIS iteration only. You define what artifacts to create NOW.

Focused strategy → efficient progress. Scattered strategy → wasted iteration.
</your_role>
</ai_inventor_context>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

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

<research_methodology>
Think like a researcher planning a study for a top venue.

- All strategies run in parallel and their artifacts combine into one pool. Together they must build toward a publishable paper — each strategy contributes a distinct, necessary piece. No strategy should be a standalone island.
- Ask yourself: what would a reviewer need to see? Proper baselines, controlled comparisons, ablations that isolate what matters. Plan artifacts that preempt reviewer objections.
- Depth over breadth. One well-designed experiment with proper controls beats five shallow ones.
- Match your evaluation to your claims. Measure what the hypothesis actually asserts.
- When results are weak or partial, vary the approach before writing it off. One failed method doesn't falsify the hypothesis.
- If iterations remain, think about what the NEXT iteration will need. Leave useful building blocks — datasets, baselines, preliminary results — that future strategies can build on, refine, or compare against.
</research_methodology>

<principles>
1. FOCUS ON NOVELTY - every strategy must lead to a genuinely novel contribution
2. MAXIMIZE PARALLELIZATION - all artifacts in your strategy run in parallel
3. BUILD ON EXISTING WORK - use completed artifacts from previous iterations, learn from failures
4. ITERATE ON THE METHOD - a negative result is about the approach, not the hypothesis. Try different methods, parameters, data, or formulations within the hypothesis bounds.
5. DIAGNOSE BEFORE DECIDING - before each iteration, review what worked, what didn't, and why. Use that to choose what to try next. Gaps are action items, not conclusions.
6. SET DEPENDENCIES WISELY - depends_on is a list of {id, label} objects referencing existing artifacts; each label is a short free-text type (a word or two, e.g. "dataset", "validates", "extends") that tags how the dep is used
7. PLAN FOR DEPENDENCIES - if an artifact depends on another (e.g. experiments need datasets), ensure prerequisites exist first or plan them this iteration for the next
</principles>

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

<hypothesis>
Your strategy should advance this hypothesis.

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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for study design, proper baselines, and the evaluation/validity norms this field demands.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<iteration_status>
Current iteration: 2 of 2
Remaining (including this one): 1
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: Survival Analysis Foundation for Dependency Minimization
objective: >-
  Establish and validate a survival-analysis framework for characterizing dependency-length distributions across UD treebanks,
  demonstrating that censored time-to-event modeling reveals linguistic patterns (register effects, typological contrasts,
  family heterogeneity) hidden from pooled-mean statistics, and is robust to the documented sentence-length-mixing confound.
rationale: >-
  The hypothesis proposes a novel methodological reframing—survival analysis for dependency arcs—that has never been applied
  to DLM research. This is methodological novelty. It directly addresses Ferrer-i-Cancho's published length-mixing confound
  with a statistically principled solution (censored modeling) rather than ad hoc normalization. Iteration 1 must (1) establish
  the data pipeline, (2) articulate construct validity (why is arc length a meaningful 'time-to-event' for language?), and
  (3) prove the method recovers known effects while revealing shape information inaccessible to pooled means. The field handbook
  warns against 'tape-measure' work—adding coverage without overturning assumptions—so validation against the known confound
  is essential. Early demonstration that hazard-based comparison is invariant to sentence-length composition, where pooled
  MDD is not, proves the method addresses a real problem.
artifact_directions:
- id: research_iter1_dir1
  type: research
  objective: >-
    Understand survival-analysis precedent in linguistics, deeply review DLM literature and its documented confounds, catalog
    UD treebanks suitable for register-level analysis, and establish the theoretical justification for modeling arc length
    as a censored time-to-event process.
  approach: >-
    Search scholarly literature for survival-analysis applications to linguistic or behavioral data with position-bounded
    maximums; deeply read Ferrer-i-Cancho et al. on length-mixing and recent cross-linguistic speech vs. writing DLM studies;
    catalog commul/universal_dependencies by modality and language coverage; synthesize why dependency arcs constitute a valid
    survival-analysis substrate—i.e., what makes 'has the arc closed by distance d, given it has not closed before d and could
    not exceed the sentence boundary' a meaningful conditional quantity rather than a degenerate one.
  depends_on: []
- id: dataset_iter1_dir2
  type: dataset
  objective: >-
    Assemble a complete, schema-validated dataset of dependency arcs from all UD treebanks, with arc-level features (observed
    length, position-bounded censoring bound), register/modality labels, typological covariates, and language-family groupings.
  approach: >-
    Download commul/universal_dependencies from HuggingFace; extract every dependency arc with computed arc length and position-imposed
    censoring bound (distance to nearer sentence boundary); label register/modality from treebank metadata (spoken vs. written)
    and manual UD documentation where available; integrate WALS and Grambank typological features (word order, morphological
    richness); use morphological feature counts from UD morphology table as proxy where typological databases lack coverage;
    attach Glottolog language-family labels; design schema with validation, splits (full/mini/preview), and explicit censoring-bound
    documentation; validate by spot-checking that censoring bounds align with sentence structure.
  depends_on: []
- id: experiment_iter1_dir3
  type: experiment
  objective: >-
    Implement Kaplan-Meier and Nelson-Aalen hazard estimation, fit semi-parametric Cox proportional-hazards model with covariates
    (register, word order, morphological richness) and language-family shared frailty, and validate robustness to the sentence-length-mixing
    confound by demonstrating invariance of hazard-based comparison under sentence-length resampling.
  approach: >-
    Fit non-parametric Kaplan-Meier and Nelson-Aalen hazard curves per treebank and per register (spoken vs. written within
    languages); fit semi-parametric Cox model with register, word-order, and morphological-richness as fixed effects and language
    family as shared-frailty random effect; extract and rank fitted frailty terms to identify families whose residual hazard
    deviates from typological cluster baseline. **Validation: robustness to sentence-length composition**—resample dependency
    arcs to match sentence-length distributions across register/language pairs, refit Cox model, demonstrate that hazard-based
    estimates (coefficients, curves) remain stable while pooled-MDD estimates shift (direct replication-with-correction of
    known confound). Cross-check that directional effects (spoken vs. written, word order, morphology) align with prior pooled-MDD
    literature, confirming the method recovers known patterns. Report all estimates with 95% confidence intervals and quantified
    uncertainty, not point values. Output hazard curves (both parametric and non-parametric), Cox coefficients with CIs, frailty
    term distributions, and robustness-check results.
  depends_on: []
expected_outcome: >-
  By end of iteration 1: (1) a grounded understanding of survival analysis as appropriate for dependent-arc data with position-bounded
  censoring, addressing field-level construct-validity standards [handbook]; (2) a complete, validated UD dataset with ~500k–2M
  dependency arcs across languages and registers, ready for downstream analysis; (3) empirical evidence that survival-based
  hazard modeling (a) recovers known DLM directional effects from literature, (b) reveals shape information (front-loaded
  vs. flat hazard) inaccessible to pooled means, (c) is robust to sentence-length-composition confound via explicit robustness
  checks (the critical validation), (d) reveals language-family heterogeneity via frailty structure. This foundation enables
  iteration 2 to deepen family-level analysis, conduct sensitivity studies, and write a comprehensive paper with full literature
  positioning.
summary: >-
  A methodologically grounded iteration-1 strategy establishing the survival-analysis framework for dependency-length research.
  Prioritizes construct validity and validation against known confounds over breadth. RESEARCH articulates theoretical justification;
  DATASET builds the data foundation; EXPERIMENT implements and validates the core method. All three run in parallel, producing
  a robust foundation for iteration 2 refinement and paper writing.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
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
out_dependency_files:
  file_list:
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
out_dependency_files:
  file_list:
  - data.py
  - full_data_out/full_data_out_1.json
  - full_data_out/full_data_out_2.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out/full_data_out_1.json
  - full_data_out/full_data_out_2.json
  - mini_data_out.json
  - preview_data_out.json

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
out_dependency_files:
  file_list:
  - method.py
  - full_method_out.json
  - mini_method_out.json
  - preview_method_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

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

</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

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

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 3 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool


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
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Strategy name in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-08-13 12:15:58 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [4] ASSISTANT · 2026-08-13 12:17:06 UTC

```
Looking at the reviewer feedback and current state, this is iteration 2 of 2 — the final iteration before paper submission. The feedback identifies three MAJOR evidentiary issues that must be fixed and several MINOR methodological refinements needed to meet publication standards for ACL/EMNLP/ComputLing.

Let me read the handbook first to ensure I'm grounding this in proper computational-linguistics standards.
```

### [5] TOOL CALL — Skill · 2026-08-13 12:17:06 UTC

```
aii-handbook-auto-computational-linguistics
```

### [6] TOOL RESULT — Skill · 2026-08-13 12:17:06 UTC

```
{"success": true, "commandName": "aii-handbook-auto-computational-linguistics"}
```

### [7] ASSISTANT · 2026-08-13 12:18:04 UTC

```
Now I'll develop the final iteration strategy. Based on the handbook, the reviewer critiques are fundamentally about **construct validity** (are your labels measuring what you claim?) and **measurement rigor** (are your statistical claims properly controlled and quantified?). These are not minor cleanups — they're central to whether the paper makes a sound claim.

The three-artifact strategy should focus on:

1. **EXPERIMENT** (re-run with methodological rigor) — Gold-label subsetting, bootstrap CIs, multiple-comparison correction
2. **EVALUATION** (comprehensive validation) — Effect-size standardization, data-provenance clarity, robustness checks  
3. **RESEARCH** (positioning refinement) — Historical-linguistics context for precise novelty claim

Let me write the JSON:
```

### [8] TOOL CALL — Write · 2026-08-13 12:18:04 UTC

```
File: /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_strat/.terminal_claude_agent_struct_out.json

{
  "strategies": [
    {
      "title": "Construct Validity and Statistical Rigor for Final Evidence",
      "objective": "Convert iter-1's methodological foundation into publication-ready evidence by fixing three critical validity issues: (1) re-fit the Cox model on genuinely gold-labeled spoken/written data only as the primary finding, with heuristic-labeled full corpus as secondary robustness check with explicit label-noise sensitivity bounds; (2) add bootstrap confidence intervals for all family-level residual hazards and apply Benjamini-Hochberg correction across 32 comparisons, reporting only families surviving correction; (3) provide explicit, reconciled data-provenance documentation so readers know exactly which statistics came from which treebank subset and which annotation source.",
      "rationale": "Iteration 1 produced a methodologically novel result (survival-analysis reframing of dependency arcs, correctly handling position-bounded censoring) but the evidence for two key claims—spoken-vs-written register effect and language-family outliers—relies on noisy/heuristic labels and lacks multiple-comparison control. Reviewer feedback identifies these as threats to construct validity (the headline register finding is mostly from treebanks with no gold annotation of modality, only heuristic defaults) and statistical validity (32 family comparisons reported without correction, inviting spurious top-rank artifacts). The computational-linguistics field handbook emphasizes that construct validity and measurement rigor are load-bearing for publication in top venues; a capability claim must define its construct, operationalize it clearly, and report uncertainty. This iteration must repair these foundations: restrict the primary spoken-vs-written claim to the small, gold-labeled subset (English, French, Slovenian pairs); add label-noise sensitivity analysis to bound the impact of heuristic labels on the full-corpus secondary finding; compute bootstrap CIs for family residuals and apply Benjamini-Hochberg correction; clarify data provenance with explicit tables. This is not exploratory work—it is targeted validation of iter-1's results to publication-readiness standards.",
      "artifact_directions": [
        {
          "type": "experiment",
          "objective": "Re-run the survival-analysis pipeline on gold-labeled spoken/written data as the primary analysis, with three methodological refinements: (1) restrict spoken-vs-written Cox fit to English/French/Slovenian matched pairs (genuinely gold-annotated) as PRIMARY finding, (2) compute 1000-replicate bootstrap for family residuals and apply Benjamini-Hochberg correction across 32 families as PRIMARY ranking (not just point estimates), (3) add label-noise sensitivity: re-fit the full-corpus secondary model after randomly flipping 5%/10%/20% of heuristic register labels to bound how much the full-corpus register coefficient could be noise-driven.",
          "approach": "Load the curated dataset (art_V4iFzwfu7i49) and filter to the small gold-labeled subset: English CHILDES/EWT, French Rhapsodie/GSD, Slovenian SST/SSJ pairs (documented as genuinely gold-annotated in iter-1 dataset artifact). Fit a primary Cox proportional-hazards model on this subset with register + standardized word-order + standardized morphological-richness as covariates, stratified by language family (note: family count will be smaller; stratify if n_families >= 5, else use family as fixed effect). Compute 1000-replicate bootstrap on family residuals (sample arcs with replacement, refit family-level Nelson-Aalen cumulative hazard at d=10), extract bootstrap confidence intervals (2.5th, 97.5th percentile), and apply Benjamini-Hochberg FDR correction across all 32 families using the point estimates. Report only families with BH-adjusted p < 0.05 as confirmed outliers. For the secondary analysis (full 350-treebank corpus with heuristic labels), fit a second Cox model and report its coefficients with CIs; then conduct 3 sensitivity runs where register labels are corrupted by randomly flipping 5%, 10%, 20% of the 'heuristic' rows (determined from a flag in the dataset), refit Cox, and plot how coefficients shift with label-corruption rate. For word-order operationalization robustness: fit Cox models under three variants: (A) categorical Grambank verb-order only (84% coverage), (B) empirical continuous fraction-of-dependents-before-head only (100% coverage), (C) both as separate terms (Grambank categorical + empirical continuous as interaction term or parallel terms). Report coefficients for register and family effects under all three variants to confirm they are stable across operationalization choices. Additionally, compute random-baseline null distribution: for a random sample of 50k arcs, permute head positions uniformly within sentence and compute null hazard curves; overlay observed vs. null on a figure to directly demonstrate (not just assert) that the observed hazard deviates from random, as required for the 'recovery' of Futrell et al. Explicit data provenance: in method_out.json metadata, tag every result with its source (gold-subset-cox, full-corpus-cox, gold-subset-bootstrap, sensitivity-5pct, etc.) and include a provenance table documenting the exact row counts, treebank sources, and annotation sources for each statistic. Output: method_out.json with (1) primary Cox fit on gold subset with 95% bootstrap CIs, (2) BH-corrected family rankings with bootstrap CIs and adjusted p-values, (3) secondary full-corpus Cox with label-noise sensitivity curves, (4) word-order operationalization variants comparison, (5) random-baseline null comparison, (6) explicit provenance metadata for every reported statistic.",
          "depends_on": [
            {
              "id": "art_V4iFzwfu7i49",
              "label": "gold-labeled dataset"
            }
          ]
        },
        {
          "type": "evaluation",
          "objective": "Comprehensively validate the experiment results by computing effect sizes in linguistically meaningful units, reconciling data provenance across 28-treebank vs. 350-treebank pipelines, and verifying that key methodological choices (word-order operationalization, register definition, sentence-length robustness) are robust to reasonable perturbations.",
          "approach": "Generate four sets of validation results: (1) **Effect-size standardization**: For the primary register coefficient (β from gold-subset Cox), compute the median arc-length reduction that the spoken-language penalty implies at the median arc-length observed in the data. Express this in terms of a percentile of the between-language variance in the same coefficient across the 350 treebanks (e.g., 'the register effect of 0.046 corresponds to a 0.5-token median arc-length reduction, which places it at the X-th percentile of between-language variance'). This grounds the effect size in linguistic units. (2) **Data-provenance reconciliation table**: Create a table with one row per reported statistic (register coefficient, word-order coefficient, family outlier rankings, robustness-check delta, etc.) documenting whether it came from: [a] 28-treebank curated dataset, [b] 350-treebank full extraction, [c] gold-labeled subset only (English/French/Slovenian), [d] secondary heuristic-label run. Include row counts, treebank names, and annotation sources. This resolves the paper's ambiguity about which numbers come from which pipeline. (3) **Cross-checks and literature recovery**: Compare new experiment results against iter-1 artifact (art_d7jrBtmjm_7W) for numerical stability (e.g., register coefficient iter-1 vs. iter-2, difference should be small since only the label-quality subset is changing); compute register effect stratified by dependency-type (functional vs. lexical) and compare against Gerdes et al.'s finding that functional deps are universally short (~1.71) and lexical deps are longer and typology-variable (expect register effect to be larger for lexical); recompute pooled-MDD ratios under same sentence-length resampling as Cox to directly demonstrate pooled-MDD variance is 10-20× larger than Cox-coefficient variance (the core robustness claim). (4) **Methodological transparency**: Generate a full audit trail showing: how gold-label treebanks were identified and validated (list the three with sources), how word-order variants were compared (all three operationalizations fitted to identical data subsets), how label-noise sensitivity was parameterized (5%/10%/20% random flips on 'heuristic' rows), and how bootstrap replicates were generated (sampling with replacement, number of replicates, random seed for reproducibility). Output: eval_out.json with tables, figures, and interpretive guidance for the paper; include effect-size quantile information, provenance table, literature-recovery statistics, and methodological audit trail.",
          "depends_on": [
            {
              "id": "art_d7jrBtmjm_7W",
              "label": "iter-1 results for comparison and baseline"
            }
          ]
        },
        {
          "type": "research",
          "objective": "Clarify the novelty positioning by systematically reviewing survival-analysis and hazard-based modeling in historical linguistics (lexical replacement, grammaticalization, language change), confirming the boundary between our work and historical-ling precedent, and producing a refined novelty claim suitable for top-tier venues.",
          "approach": "Conduct targeted scholarly search for: (1) hazard models or survival-analysis applications in historical/diachronic linguistics (lexical replacement rates, grammaticalization as a survival process, phonological/morphological change trajectories over time), (2) position-dependent censoring or right-censoring concepts applied to linguistic data (census records, incomplete documentation, inherited constraints), (3) any prior synchronic applications of survival analysis to syntactic structure or dependency length (unlikely to find, but search explicitly). For each result, document: what linguistic phenomenon it models, how it uses survival-analysis machinery, what the event/censoring structure is, how temporal dynamics differ from our position-bounded static censoring. Articulate the clean boundary: historical-ling hazard models track temporal change over centuries (e.g., rate at which 'shall' replaces 'will', or when a morpheme leaves the language); our work models *position-dependent structural censoring in a single synchronic state* — a word near a sentence boundary cannot produce a long arc, exactly analogous to a patient enrolled late in a trial, but we are not modeling temporal dynamics. Conclude: our novelty positioning should be 'first application of survival analysis to synchronic dependency-length data at scale,' explicitly grounded in the historical-linguistics tradition but clearly distinct. Output: research_out.json with (a) catalog of historical-ling hazard models and how they differ, (b) refined novelty positioning statement (2–3 sentences) suitable for Related Work/Introduction, (c) confirmation that construct validity and field appropriateness of the survival-analysis framing for dependency arcs is sound and addresses a real, published confound (Ferrer-i-Cancho) rather than inventing a problem.",
          "depends_on": [
            {
              "id": "art_2CDrgn6Hae3P",
              "label": "iter-1 research and survival-analysis foundations"
            }
          ]
        }
      ],
      "expected_outcome": "By end of iteration 2, we will have: (1) a corrected survival-analysis pipeline with primary findings on a small, rigorously defined gold-labeled spoken/written subset (n_spoken ≈18.8k, n_written ≈67.4k from English/French/Slovenian) including register Cox coefficient with 95% bootstrap CI and explicit construct definition; family-level residual-hazard rankings with bootstrap CIs and Benjamini-Hochberg multiple-comparison correction (reporting only families surviving BH threshold); and a secondary full-corpus finding with explicit label-noise sensitivity bounds showing how much the register coefficient could shift if heuristic labels have noise; (2) comprehensive validation showing effect sizes in linguistically meaningful units (tokens/median-shift), explicit data-provenance reconciliation documenting which statistics came from which treebank subset and annotation source, and robustness of key methodological choices (word-order operationalization, sentence-length resampling, random-baseline comparison) to reasonable perturbations; (3) a refined novelty claim—'first application to synchronic dependency-length data'—grounded in historical-linguistics context and clearly distinguished from temporal hazard models. These three artifacts eliminate all MAJOR reviewer critiques (construct validity of register finding, multiple-comparison problem in family rankings, data-provenance confusion) and address MINOR concerns (word-order operationalization, Futrell recovery demonstration, effect-size interpretation, novelty precision). The result is a publication-ready empirical foundation meeting top-tier journal standards for construct validity, statistical rigor, and transparency.",
      "summary": "This strategy directly addresses reviewer feedback by retrofitting iter-1's results with proper construct validity (gold-labeled subset only for spoken-vs-written), statistical rigor (bootstrap CIs, Benjamini-Hochberg correction), and transparency (explicit data-provenance documentation). The goal is not new discovery but rigorous validation of iter-1's foundation to ACL/EMNLP/ComputLing publication standards. Three parallel artifacts re-run the analysis with refinements, validate all methodological choices, and refine the novelty positioning to be precise and grounded in field-appropriate historical context."
    }
  ]
}
```

### [9] TOOL RESULT — Write · 2026-08-13 12:18:04 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_strat/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Construct Validity and Statistical Rigor for Final Evidence\",\n      \"objective\": \"Convert iter-1's methodological foundation into publication-ready evidence by fixing three critical validity issues: (1) re-fit the Cox model on genuinely gold-labeled spoken/written data only as the primary finding, with heuristic-labeled full corpus as secondary robustness check with explicit label-noise sensitivity bounds; (2) add bootstrap confidence intervals for all family-level residual hazards and apply Benjamini-Hochberg correction across 32 comparisons, reporting only families surviving correction; (3) provide explicit, reconciled data-provenance documentation so readers know exactly which statistics came from which treebank subset and which annotation source.\",\n      \"rationale\": \"Iteration 1 produced a methodologically novel result (survival-analysis reframing of dependency arcs, correctly handling position-bounded censoring) but the evidence for two key claims—spoken-vs-written register effect and language-family outliers—relies on noisy/heuristic labels and lacks multiple-comparison control. Reviewer feedback identifies these as threats to construct validity (the headline register finding is mostly from treebanks with no gold annotation of modality, only heuristic defaults) and statistical validity (32 family comparisons reported without correction, inviting spurious top-rank artifacts). The computational-linguistics field handbook emphasizes that construct validity and measurement rigor are load-bearing for publication in top venues; a capability claim must define its construct, operationalize it clearly, and report uncertainty. This iteration must repair these foundations: restrict the primary spoken-vs-written claim to the small, gold-labeled subset (English, French, Slovenian pairs); add label-noise sensitivity analysis to bound the impact of heuristic labels on the full-corpus secondary finding; compute bootstrap CIs for family residuals and apply Benjamini-Hochberg correction; clarify data provenance with explicit tables. This is not exploratory work—it is targeted validation of iter-1's results to publication-readiness standards.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Re-run the survival-analysis pipeline on gold-labeled spoken/written data as the primary analysis, with three methodological refinements: (1) restrict spoken-vs-written Cox fit to English/French/Slovenian matched pairs (genuinely gold-annotated) as PRIMARY finding, (2) compute 1000-replicate bootstrap for family residuals and apply Benjamini-Hochberg correction across 32 families as PRIMARY ranking (not just point estimates), (3) add label-noise sensitivity: re-fit the full-corpus secondary model after randomly flipping 5%/10%/20% of heuristic register labels to bound how much the full-corpus register coefficient could be noise-driven.\",\n          \"approach\": \"Load the curated dataset (art_V4iFzwfu7i49) and filter to the small gold-labeled subset: English CHILDES/EWT, French Rhapsodie/GSD, Slovenian SST/SSJ pairs (documented as genuinely gold-annotated in iter-1 dataset artifact). Fit a primary Cox proportional-hazards model on this subset with register + standardized word-order + standardized morphological-richness as covariates, stratified by language family (note: family count will be smaller; stratify if n_families >= 5, else use family as fixed effect). Compute 1000-replicate bootstrap on family residuals (sample arcs with replacement, refit family-level Nelson-Aalen cumulative hazard at d=10), extract bootstrap confidence intervals (2.5th, 97.5th percentile), and apply Benjamini-Hochberg FDR correction across all 32 families using the point estimates. Report only families with BH-adjusted p < 0.05 as confirmed outliers. For the secondary analysis (full 350-treebank corpus with heuristic labels), fit a second Cox model and report its coefficients with CIs; then conduct 3 sensitivity runs where register labels are corrupted by randomly flipping 5%, 10%, 20% of the 'heuristic' rows (determined from a flag in the dataset), refit Cox, and plot how coefficients shift with label-corruption rate. For word-order operationalization robustness: fit Cox models under three variants: (A) categorical Grambank verb-order only (84% coverage), (B) empirical continuous fraction-of-dependents-before-head only (100% coverage), (C) both as separate terms (Grambank categorical + empirical continuous as interaction term or parallel terms). Report coefficients for register and family effects under all three variants to confirm they are stable across operationalization choices. Additionally, compute random-baseline null distribution: for a random sample of 50k arcs, permute head positions uniformly within sentence and compute null hazard curves; overlay observed vs. null on a figure to directly demonstrate (not just assert) that the observed hazard deviates from random, as required for the 'recovery' of Futrell et al. Explicit data provenance: in method_out.json metadata, tag every result with its source (gold-subset-cox, full-corpus-cox, gold-subset-bootstrap, sensitivity-5pct, etc.) and include a provenance table documenting the exact row counts, treebank sources, and annotation sources for each statistic. Output: method_out.json with (1) primary Cox fit on gold subset with 95% bootstrap CIs, (2) BH-corrected family rankings with bootstrap CIs and adjusted p-values, (3) secondary full-corpus Cox with label-noise sensitivity curves, (4) word-order operationalization variants comparison, (5) random-baseline null comparison, (6) explicit provenance metadata for every reported statistic.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_V4iFzwfu7i49\",\n              \"label\": \"gold-labeled dataset\"\n            }\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Comprehensively validate the experiment results by computing effect sizes in linguistically meaningful units, reconciling data provenance across 28-treebank vs. 350-treebank pipelines, and verifying that key methodological choices (word-order operationalization, register definition, sentence-length robustness) are robust to reasonable perturbations.\",\n          \"approach\": \"Generate four sets of validation results: (1) **Effect-size standardization**: For the primary register coefficient (β from gold-subset Cox), compute the median arc-length reduction that the spoken-language penalty implies at the median arc-length observed in the data. Express this in terms of a percentile of the between-language variance in the same coefficient across the 350 treebanks (e.g., 'the register effect of 0.046 corresponds to a 0.5-token median arc-length reduction, which places it at the X-th percentile of between-language variance'). This grounds the effect size in linguistic units. (2) **Data-provenance reconciliation table**: Create a table with one row per reported statistic (register coefficient, word-order coefficient, family outlier rankings, robustness-check delta, etc.) documenting whether it came from: [a] 28-treebank curated dataset, [b] 350-treebank full extraction, [c] gold-labeled subset only (English/French/Slovenian), [d] secondary heuristic-label run. Include row counts, treebank names, and annotation sources. This resolves the paper's ambiguity about which numbers come from which pipeline. (3) **Cross-checks and literature recovery**: Compare new experiment results against iter-1 artifact (art_d7jrBtmjm_7W) for numerical stability (e.g., register coefficient iter-1 vs. iter-2, difference should be small since only the label-quality subset is changing); compute register effect stratified by dependency-type (functional vs. lexical) and compare against Gerdes et al.'s finding that functional deps are universally short (~1.71) and lexical deps are longer and typology-variable (expect register effect to be larger for lexical); recompute pooled-MDD ratios under same sentence-length resampling as Cox to directly demonstrate pooled-MDD variance is 10-20× larger than Cox-coefficient variance (the core robustness claim). (4) **Methodological transparency**: Generate a full audit trail showing: how gold-label treebanks were identified and validated (list the three with sources), how word-order variants were compared (all three operationalizations fitted to identical data subsets), how label-noise sensitivity was parameterized (5%/10%/20% random flips on 'heuristic' rows), and how bootstrap replicates were generated (sampling with replacement, number of replicates, random seed for reproducibility). Output: eval_out.json with tables, figures, and interpretive guidance for the paper; include effect-size quantile information, provenance table, literature-recovery statistics, and methodological audit trail.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_d7jrBtmjm_7W\",\n              \"label\": \"iter-1 results for comparison and baseline\"\n            }\n          ]\n        },\n        {\n          \"type\": \"research\",\n          \"objective\": \"Clarify the novelty positioning by systematically reviewing survival-analysis and hazard-based modeling in historical linguistics (lexical replacement, grammaticalization, language change), confirming the boundary between our work and historical-ling precedent, and producing a refined novelty claim suitable for top-tier venues.\",\n          \"approach\": \"Conduct targeted scholarly search for: (1) hazard models or survival-analysis applications in historical/diachronic linguistics (lexical replacement rates, grammaticalization as a survival process, phonological/morphological change trajectories over time), (2) position-dependent censoring or right-censoring concepts applied to linguistic data (census records, incomplete documentation, inherited constraints), (3) any prior synchronic applications of survival analysis to syntactic structure or dependency length (unlikely to find, but search explicitly). For each result, document: what linguistic phenomenon it models, how it uses survival-analysis machinery, what the event/censoring structure is, how temporal dynamics differ from our position-bounded static censoring. Articulate the clean boundary: historical-ling hazard models track temporal change over centuries (e.g., rate at which 'shall' replaces 'will', or when a morpheme leaves the language); our work models *position-dependent structural censoring in a single synchronic state* — a word near a sentence boundary cannot produce a long arc, exactly analogous to a patient enrolled late in a trial, but we are not modeling temporal dynamics. Conclude: our novelty positioning should be 'first application of survival analysis to synchronic dependency-length data at scale,' explicitly grounded in the historical-linguistics tradition but clearly distinct. Output: research_out.json with (a) catalog of historical-ling hazard models and how they differ, (b) refined novelty positioning statement (2–3 sentences) suitable for Related Work/Introduction, (c) confirmation that construct validity and field appropriateness of the survival-analysis framing for dependency arcs is sound and addresses a real, published confound (Ferrer-i-Cancho) rather than inventing a problem.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_2CDrgn6Hae3P\",\n              \"label\": \"iter-1 research and survival-analysis foundations\"\n            }\n          ]\n        }\n      ],\n      \"expected_outcome\": \"By end of iteration 2, we will have: (1) a corrected survival-analysis pipeline with primary findings on a small, rigorously defined gold-labeled spoken/written subset (n_spoken ≈18.8k, n_written ≈67.4k from English/French/Slovenian) including register Cox coefficient with 95% bootstrap CI and explicit construct definition; family-level residual-hazard rankings with bootstrap CIs and Benjamini-Hochberg multiple-comparison correction (reporting only families surviving BH threshold); and a secondary full-corpus finding with explicit label-noise sensitivity bounds showing how much the register coefficient could shift if heuristic labels have noise; (2) comprehensive validation showing effect sizes in linguistically meaningful units (tokens/median-shift), explicit data-provenance reconciliation documenting which statistics came from which treebank subset and annotation source, and robustness of key methodological choices (word-order operationalization, sentence-length resampling, random-baseline comparison) to reasonable perturbations; (3) a refined novelty claim—'first application to synchronic dependency-length data'—grounded in historical-linguistics context and clearly distinguished from temporal hazard models. These three artifacts eliminate all MAJOR reviewer critiques (construct validity of register finding, multiple-comparison problem in family rankings, data-provenance confusion) and address MINOR concerns (word-order operationalization, Futrell recovery demonstration, effect-size interpretation, novelty precision). The result is a publication-ready empirical foundation meeting top-tier journal standards for construct validity, statistical rigor, and transparency.\",\n      \"summary\": \"This strategy directly addresses reviewer feedback by retrofitting iter-1's results with proper construct validity (gold-labeled subset only for spoken-vs-written), statistical rigor (bootstrap CIs, Benjamini-Hochberg correction), and transparency (explicit data-provenance documentation). The goal is not new discovery but rigorous validation of iter-1's foundation to ACL/EMNLP/ComputLing publication standards. Three parallel artifacts re-run the analysis with refinements, validate all methodological choices, and refine the novelty positioning to be precise and grounded in field-appropriate historical context.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [10] ASSISTANT · 2026-08-13 12:18:10 UTC

```
Perfect. I've generated the final iteration strategy as JSON. Let me verify it's properly formatted and complete:
```

### [11] TOOL CALL — Read · 2026-08-13 12:18:10 UTC

```
/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_strat/.terminal_claude_agent_struct_out.json
```

### [12] TOOL RESULT — Read · 2026-08-13 12:18:10 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_strat/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Construct Validity and Statistical Rigor for Final Evidence\",\n      \"objective\": \"Convert iter-1's methodological foundation into publication-ready evidence by fixing three critical validity issues: (1) re-fit the Cox model on genuinely gold-labeled spoken/written data only as the primary finding, with heuristic-labeled full corpus as secondary robustness check with explicit label-noise sensitivity bounds; (2) add bootstrap confidence intervals for all family-level residual hazards and apply Benjamini-Hochberg correction across 32 comparisons, reporting only families surviving correction; (3) provide explicit, reconciled data-provenance documentation so readers know exactly which statistics came from which treebank subset and which annotation source.\",\n      \"rationale\": \"Iteration 1 produced a methodologically novel result (survival-analysis reframing of dependency arcs, correctly handling position-bounded censoring) but the evidence for two key claims—spoken-vs-written register effect and language-family outliers—relies on noisy/heuristic labels and lacks multiple-comparison control. Reviewer feedback identifies these as threats to construct validity (the headline register finding is mostly from treebanks with no gold annotation of modality, only heuristic defaults) and statistical validity (32 family comparisons reported without correction, inviting spurious top-rank artifacts). The computational-linguistics field handbook emphasizes that construct validity and measurement rigor are load-bearing for publication in top venues; a capability claim must define its construct, operationalize it clearly, and report uncertainty. This iteration must repair these foundations: restrict the primary spoken-vs-written claim to the small, gold-labeled subset (English, French, Slovenian pairs); add label-noise sensitivity analysis to bound the impact of heuristic labels on the full-corpus secondary finding; compute bootstrap CIs for family residuals and apply Benjamini-Hochberg correction; clarify data provenance with explicit tables. This is not exploratory work—it is targeted validation of iter-1's results to publication-readiness standards.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Re-run the survival-analysis pipeline on gold-labeled spoken/written data as the primary analysis, with three methodological refinements: (1) restrict spoken-vs-written Cox fit to English/French/Slovenian matched pairs (genuinely gold-annotated) as PRIMARY finding, (2) compute 1000-replicate bootstrap for family residuals and apply Benjamini-Hochberg correction across 32 families as PRIMARY ranking (not just point estimates), (3) add label-noise sensitivity: re-fit the full-corpus secondary model after randomly flipping 5%/10%/20% of heuristic register labels to bound how much the full-corpus register coefficient could be noise-driven.\",\n          \"approach\": \"Load the curated dataset (art_V4iFzwfu7i49) and filter to the small gold-labeled subset: English CHILDES/EWT, French Rhapsodie/GSD, Slovenian SST/SSJ pairs (documented as genuinely gold-annotated in iter-1 dataset artifact). Fit a primary Cox proportional-hazards model on this subset with register + standardized word-order + standardized morphological-richness as covariates, stratified by language family (note: family count will be smaller; stratify if n_families >= 5, else use family as fixed effect). Compute 1000-replicate bootstrap on family residuals (sample arcs with replacement, refit family-level Nelson-Aalen cumulative hazard at d=10), extract bootstrap confidence intervals (2.5th, 97.5th percentile), and apply Benjamini-Hochberg FDR correction across all 32 families using the point estimates. Report only families with BH-adjusted p < 0.05 as confirmed outliers. For the secondary analysis (full 350-treebank corpus with heuristic labels), fit a second Cox model and report its coefficients with CIs; then conduct 3 sensitivity runs where register labels are corrupted by randomly flipping 5%, 10%, 20% of the 'heuristic' rows (determined from a flag in the dataset), refit Cox, and plot how coefficients shift with label-corruption rate. For word-order operationalization robustness: fit Cox models under three variants: (A) categorical Grambank verb-order only (84% coverage), (B) empirical continuous fraction-of-dependents-before-head only (100% coverage), (C) both as separate terms (Grambank categorical + empirical continuous as interaction term or parallel terms). Report coefficients for register and family effects under all three variants to confirm they are stable across operationalization choices. Additionally, compute random-baseline null distribution: for a random sample of 50k arcs, permute head positions uniformly within sentence and compute null hazard curves; overlay observed vs. null on a figure to directly demonstrate (not just assert) that the observed hazard deviates from random, as required for the 'recovery' of Futrell et al. Explicit data provenance: in method_out.json metadata, tag every result with its source (gold-subset-cox, full-corpus-cox, gold-subset-bootstrap, sensitivity-5pct, etc.) and include a provenance table documenting the exact row counts, treebank sources, and annotation sources for each statistic. Output: method_out.json with (1) primary Cox fit on gold subset with 95% bootstrap CIs, (2) BH-corrected family rankings with bootstrap CIs and adjusted p-values, (3) secondary full-corpus Cox with label-noise sensitivity curves, (4) word-order operationalization variants comparison, (5) random-baseline null comparison, (6) explicit provenance metadata for every reported statistic.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_V4iFzwfu7i49\",\n              \"label\": \"gold-labeled dataset\"\n            }\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Comprehensively validate the experiment results by computing effect sizes in linguistically meaningful units, reconciling data provenance across 28-treebank vs. 350-treebank pipelines, and verifying that key methodological choices (word-order operationalization, register definition, sentence-length robustness) are robust to reasonable perturbations.\",\n          \"approach\": \"Generate four sets of validation results: (1) **Effect-size standardization**: For the primary register coefficient (β from gold-subset Cox), compute the median arc-length reduction that the spoken-language penalty implies at the median arc-length observed in the data. Express this in terms of a percentile of the between-language variance in the same coefficient across the 350 treebanks (e.g., 'the register effect of 0.046 corresponds to a 0.5-token median arc-length reduction, which places it at the X-th percentile of between-language variance'). This grounds the effect size in linguistic units. (2) **Data-provenance reconciliation table**: Create a table with one row per reported statistic (register coefficient, word-order coefficient, family outlier rankings, robustness-check delta, etc.) documenting whether it came from: [a] 28-treebank curated dataset, [b] 350-treebank full extraction, [c] gold-labeled subset only (English/French/Slovenian), [d] secondary heuristic-label run. Include row counts, treebank names, and annotation sources. This resolves the paper's ambiguity about which numbers come from which pipeline. (3) **Cross-checks and literature recovery**: Compare new experiment results against iter-1 artifact (art_d7jrBtmjm_7W) for numerical stability (e.g., register coefficient iter-1 vs. iter-2, difference should be small since only the label-quality subset is changing); compute register effect stratified by dependency-type (functional vs. lexical) and compare against Gerdes et al.'s finding that functional deps are universally short (~1.71) and lexical deps are longer and typology-variable (expect register effect to be larger for lexical); recompute pooled-MDD ratios under same sentence-length resampling as Cox to directly demonstrate pooled-MDD variance is 10-20× larger than Cox-coefficient variance (the core robustness claim). (4) **Methodological transparency**: Generate a full audit trail showing: how gold-label treebanks were identified and validated (list the three with sources), how word-order variants were compared (all three operationalizations fitted to identical data subsets), how label-noise sensitivity was parameterized (5%/10%/20% random flips on 'heuristic' rows), and how bootstrap replicates were generated (sampling with replacement, number of replicates, random seed for reproducibility). Output: eval_out.json with tables, figures, and interpretive guidance for the paper; include effect-size quantile information, provenance table, literature-recovery statistics, and methodological audit trail.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_d7jrBtmjm_7W\",\n              \"label\": \"iter-1 results for comparison and baseline\"\n            }\n          ]\n        },\n        {\n          \"type\": \"research\",\n          \"objective\": \"Clarify the novelty positioning by systematically reviewing survival-analysis and hazard-based modeling in historical linguistics (lexical replacement, grammaticalization, language change), confirming the boundary between our work and historical-ling precedent, and producing a refined novelty claim suitable for top-tier venues.\",\n          \"approach\": \"Conduct targeted scholarly search for: (1) hazard models or survival-analysis applications in historical/diachronic linguistics (lexical replacement rates, grammaticalization as a survival process, phonological/morphological change trajectories over time), (2) position-dependent censoring or right-censoring concepts applied to linguistic data (census records, incomplete documentation, inherited constraints), (3) any prior synchronic applications of survival analysis to syntactic structure or dependency length (unlikely to find, but search explicitly). For each result, document: what linguistic phenomenon it models, how it uses survival-analysis machinery, what the event/censoring structure is, how temporal dynamics differ from our position-bounded static censoring. Articulate the clean boundary: historical-ling hazard models track temporal change over centuries (e.g., rate at which 'shall' replaces 'will', or when a morpheme leaves the language); our work models *position-dependent structural censoring in a single synchronic state* — a word near a sentence boundary cannot produce a long arc, exactly analogous to a patient enrolled late in a trial, but we are not modeling temporal dynamics. Conclude: our novelty positioning should be 'first application of survival analysis to synchronic dependency-length data at scale,' explicitly grounded in the historical-linguistics tradition but clearly distinct. Output: research_out.json with (a) catalog of historical-ling hazard models and how they differ, (b) refined novelty positioning statement (2–3 sentences) suitable for Related Work/Introduction, (c) confirmation that construct validity and field appropriateness of the survival-analysis framing for dependency arcs is sound and addresses a real, published confound (Ferrer-i-Cancho) rather than inventing a problem.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_2CDrgn6Hae3P\",\n              \"label\": \"iter-1 research and survival-analysis foundations\"\n            }\n          ]\n        }\n      ],\n      \"expected_outcome\": \"By end of iteration 2, we will have: (1) a corrected survival-analysis pipeline with primary findings on a small, rigorously defined gold-labeled spoken/written subset (n_spoken ≈18.8k, n_written ≈67.4k from English/French/Slovenian) including register Cox coefficient with 95% bootstrap CI and explicit construct definition; family-level residual-hazard rankings with bootstrap CIs and Benjamini-Hochberg multiple-comparison correction (reporting only families surviving BH threshold); and a secondary full-corpus finding with explicit label-noise sensitivity bounds showing how much the register coefficient could shift if heuristic labels have noise; (2) comprehensive validation showing effect sizes in linguistically meaningful units (tokens/median-shift), explicit data-provenance reconciliation documenting which statistics came from which treebank subset and annotation source, and robustness of key methodological choices (word-order operationalization, sentence-length resampling, random-baseline comparison) to reasonable perturbations; (3) a refined novelty claim—'first application to synchronic dependency-length data'—grounded in historical-linguistics context and clearly distinguished from temporal hazard models. These three artifacts eliminate all MAJOR reviewer critiques (construct validity of register finding, multiple-comparison problem in family rankings, data-provenance confusion) and address MINOR concerns (word-order operationalization, Futrell recovery demonstration, effect-size interpretation, novelty precision). The result is a publication-ready empirical foundation meeting top-tier journal standards for construct validity, statistical rigor, and transparency.\",\n      \"summary\": \"This strategy directly addresses reviewer feedback by retrofitting iter-1's results with proper construct validity (gold-labeled subset only for spoken-vs-written), statistical rigor (bootstrap CIs, Benjamini-Hochberg correction), and transparency (explicit data-provenance documentation). The goal is not new discovery but rigorous validation of iter-1's foundation to ACL/EMNLP/ComputLing publication standards. Three parallel artifacts re-run the analysis with refinements, validate all methodological choices, and refine the novelty positioning to be precise and grounded in field-appropriate historical context.\"\n    }\n  ]\n}\n", "numLines": 47, "startLine": 1, "totalLines": 47}}
```

### [13] ASSISTANT · 2026-08-13 12:18:24 UTC

```
## Summary

I've generated the final iteration strategy for this computational-linguistics research on dependency-length minimization. The strategy directly addresses the three MAJOR reviewer critiques and several MINOR concerns that stand between iter-1's foundation and publication readiness.

**Strategy: "Construct Validity and Statistical Rigor for Final Evidence"**

**The Core Issue:** Iteration 1 produced methodologically novel work (survival-analysis reframing of dependency arcs, correct handling of position-bounded censoring) but has two critical evidence problems:
1. **Construct validity threat**: The spoken-vs-written register effect comes mostly from treebanks with heuristic/defaulted labels (only 3 of 350 have gold annotation)
2. **Statistical validity threat**: Family-level outlier rankings lack multiple-comparison control across 32 families

The computational-linguistics field handbook makes clear that these are load-bearing for top-tier publication: construct validity (does your measure operationalize what you claim?) and measurement rigor (proper uncertainty quantification, correction for multiple comparisons) are non-negotiable for a capability claim.

**Three Parallel Artifacts:**

1. **EXPERIMENT** (re-run with rigor):
   - Primary finding: Cox model fit ONLY on gold-labeled spoken/written pairs (English CHILDES/EWT, French Rhapsodie/GSD, Slovenian SST/SSJ)
   - Bootstrap CIs (1000 replicates) for all family residual hazards
   - Benjamini-Hochberg correction across 32 family comparisons; report only survivors
   - Label-noise sensitivity: re-fit with 5%/10%/20% label corruption to bound impact
   - Word-order operationalization variants (categorical vs. continuous vs. both)
   - Random-baseline comparison to directly demonstrate "recovery" of Futrell et al.
   - Explicit data-provenance tags on every statistic

2. **EVALUATION** (comprehensive validation):
   - Effect-size standardization: median arc-length reduction in linguistic units, expressed as percentile of between-language variance
   - Data-provenance reconciliation table showing which stats came from which treebank subset
   - Cross-checks: numerical stability vs. iter-1, dependency-type stratification (Gerdes et al. recovery), pooled-MDD variance comparison
   - Methodological audit trail: gold-label identification, word-order variant comparison, label-noise parameterization, bootstrap reproducibility

3. **RESEARCH** (novelty positioning):
   - Systematic search for hazard models in historical linguistics (lexical replacement, grammaticalization, language change)
   - Clear boundary articulation: our work is synchronic position-bounded censoring, not temporal dynamics
   - Refined novelty claim: "first application to synchronic dependency-length data" (precise, grounded, defensible)

**Expected Outcome:** Publication-ready evidence with proper construct validity, statistical rigor, and transparency meeting ACL/EMNLP/ComputLing standards. All MAJOR critiques resolved, MINOR concerns addressed.

The JSON is ready at `./.terminal_claude_agent_struct_out.json`.
```

### [14] SYSTEM-USER prompt · 2026-08-13 12:18:26 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [15] ASSISTANT · 2026-08-13 12:19:14 UTC

```
I see the issue — I wrote to the wrong directory. The current working directory is the `gen_strat_1` subdirectory. Let me write the file to the correct location:
```

### [16] TOOL CALL — Write · 2026-08-13 12:19:14 UTC

```
File: /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json

{
  "strategies": [
    {
      "title": "Construct Validity and Statistical Rigor for Final Evidence",
      "objective": "Convert iter-1's methodological foundation into publication-ready evidence by fixing three critical validity issues: (1) re-fit the Cox model on genuinely gold-labeled spoken/written data only as the primary finding, with heuristic-labeled full corpus as secondary robustness check with explicit label-noise sensitivity bounds; (2) add bootstrap confidence intervals for all family-level residual hazards and apply Benjamini-Hochberg correction across 32 comparisons, reporting only families surviving correction; (3) provide explicit, reconciled data-provenance documentation so readers know exactly which statistics came from which treebank subset and which annotation source.",
      "rationale": "Iteration 1 produced a methodologically novel result (survival-analysis reframing of dependency arcs, correctly handling position-bounded censoring) but the evidence for two key claims—spoken-vs-written register effect and language-family outliers—relies on noisy/heuristic labels and lacks multiple-comparison control. Reviewer feedback identifies these as threats to construct validity (the headline register finding is mostly from treebanks with no gold annotation of modality, only heuristic defaults) and statistical validity (32 family comparisons reported without correction, inviting spurious top-rank artifacts). The computational-linguistics field handbook emphasizes that construct validity and measurement rigor are load-bearing for publication in top venues; a capability claim must define its construct, operationalize it clearly, and report uncertainty. This iteration must repair these foundations: restrict the primary spoken-vs-written claim to the small, gold-labeled subset (English, French, Slovenian pairs); add label-noise sensitivity analysis to bound the impact of heuristic labels on the full-corpus secondary finding; compute bootstrap CIs for family residuals and apply Benjamini-Hochberg correction; clarify data provenance with explicit tables. This is not exploratory work—it is targeted validation of iter-1's results to publication-readiness standards.",
      "artifact_directions": [
        {
          "type": "experiment",
          "objective": "Re-run the survival-analysis pipeline on gold-labeled spoken/written data as the primary analysis, with three methodological refinements: (1) restrict spoken-vs-written Cox fit to English/French/Slovenian matched pairs (genuinely gold-annotated) as PRIMARY finding, (2) compute 1000-replicate bootstrap for family residuals and apply Benjamini-Hochberg correction across 32 families as PRIMARY ranking (not just point estimates), (3) add label-noise sensitivity: re-fit the full-corpus secondary model after randomly flipping 5%/10%/20% of heuristic register labels to bound how much the full-corpus register coefficient could be noise-driven.",
          "approach": "Load the curated dataset (art_V4iFzwfu7i49) and filter to the small gold-labeled subset: English CHILDES/EWT, French Rhapsodie/GSD, Slovenian SST/SSJ pairs (documented as genuinely gold-annotated in iter-1 dataset artifact). Fit a primary Cox proportional-hazards model on this subset with register + standardized word-order + standardized morphological-richness as covariates, stratified by language family (note: family count will be smaller; stratify if n_families >= 5, else use family as fixed effect). Compute 1000-replicate bootstrap on family residuals (sample arcs with replacement, refit family-level Nelson-Aalen cumulative hazard at d=10), extract bootstrap confidence intervals (2.5th, 97.5th percentile), and apply Benjamini-Hochberg FDR correction across all 32 families using the point estimates. Report only families with BH-adjusted p < 0.05 as confirmed outliers. For the secondary analysis (full 350-treebank corpus with heuristic labels), fit a second Cox model and report its coefficients with CIs; then conduct 3 sensitivity runs where register labels are corrupted by randomly flipping 5%, 10%, 20% of the 'heuristic' rows (determined from a flag in the dataset), refit Cox, and plot how coefficients shift with label-corruption rate. For word-order operationalization robustness: fit Cox models under three variants: (A) categorical Grambank verb-order only (84% coverage), (B) empirical continuous fraction-of-dependents-before-head only (100% coverage), (C) both as separate terms (Grambank categorical + empirical continuous as interaction term or parallel terms). Report coefficients for register and family effects under all three variants to confirm they are stable across operationalization choices. Additionally, compute random-baseline null distribution: for a random sample of 50k arcs, permute head positions uniformly within sentence and compute null hazard curves; overlay observed vs. null on a figure to directly demonstrate (not just assert) that the observed hazard deviates from random, as required for the 'recovery' of Futrell et al. Explicit data provenance: in method_out.json metadata, tag every result with its source (gold-subset-cox, full-corpus-cox, gold-subset-bootstrap, sensitivity-5pct, etc.) and include a provenance table documenting the exact row counts, treebank sources, and annotation sources for each statistic. Output: method_out.json with (1) primary Cox fit on gold subset with 95% bootstrap CIs, (2) BH-corrected family rankings with bootstrap CIs and adjusted p-values, (3) secondary full-corpus Cox with label-noise sensitivity curves, (4) word-order operationalization variants comparison, (5) random-baseline null comparison, (6) explicit provenance metadata for every reported statistic.",
          "depends_on": [
            {
              "id": "art_V4iFzwfu7i49",
              "label": "gold-labeled dataset"
            }
          ]
        },
        {
          "type": "evaluation",
          "objective": "Comprehensively validate the experiment results by computing effect sizes in linguistically meaningful units, reconciling data provenance across 28-treebank vs. 350-treebank pipelines, and verifying that key methodological choices (word-order operationalization, register definition, sentence-length robustness) are robust to reasonable perturbations.",
          "approach": "Generate four sets of validation results: (1) Effect-size standardization: For the primary register coefficient (beta from gold-subset Cox), compute the median arc-length reduction that the spoken-language penalty implies at the median arc-length observed in the data. Express this in terms of a percentile of the between-language variance in the same coefficient across the 350 treebanks (e.g., 'the register effect of 0.046 corresponds to a 0.5-token median arc-length reduction, which places it at the X-th percentile of between-language variance'). This grounds the effect size in linguistic units. (2) Data-provenance reconciliation table: Create a table with one row per reported statistic (register coefficient, word-order coefficient, family outlier rankings, robustness-check delta, etc.) documenting whether it came from: [a] 28-treebank curated dataset, [b] 350-treebank full extraction, [c] gold-labeled subset only (English/French/Slovenian), [d] secondary heuristic-label run. Include row counts, treebank names, and annotation sources. This resolves the paper's ambiguity about which numbers come from which pipeline. (3) Cross-checks and literature recovery: Compare new experiment results against iter-1 artifact (art_d7jrBtmjm_7W) for numerical stability (e.g., register coefficient iter-1 vs. iter-2, difference should be small since only the label-quality subset is changing); compute register effect stratified by dependency-type (functional vs. lexical) and compare against Gerdes et al.'s finding that functional deps are universally short (~1.71) and lexical deps are longer and typology-variable (expect register effect to be larger for lexical); recompute pooled-MDD ratios under same sentence-length resampling as Cox to directly demonstrate pooled-MDD variance is 10-20x larger than Cox-coefficient variance (the core robustness claim). (4) Methodological transparency: Generate a full audit trail showing: how gold-label treebanks were identified and validated (list the three with sources), how word-order variants were compared (all three operationalizations fitted to identical data subsets), how label-noise sensitivity was parameterized (5%/10%/20% random flips on 'heuristic' rows), and how bootstrap replicates were generated (sampling with replacement, number of replicates, random seed for reproducibility). Output: eval_out.json with tables, figures, and interpretive guidance for the paper; include effect-size quantile information, provenance table, literature-recovery statistics, and methodological audit trail.",
          "depends_on": [
            {
              "id": "art_d7jrBtmjm_7W",
              "label": "iter-1 results for comparison and baseline"
            }
          ]
        },
        {
          "type": "research",
          "objective": "Clarify the novelty positioning by systematically reviewing survival-analysis and hazard-based modeling in historical linguistics (lexical replacement, grammaticalization, language change), confirming the boundary between our work and historical-ling precedent, and producing a refined novelty claim suitable for top-tier venues.",
          "approach": "Conduct targeted scholarly search for: (1) hazard models or survival-analysis applications in historical/diachronic linguistics (lexical replacement rates, grammaticalization as a survival process, phonological/morphological change trajectories over time), (2) position-dependent censoring or right-censoring concepts applied to linguistic data (census records, incomplete documentation, inherited constraints), (3) any prior synchronic applications of survival analysis to syntactic structure or dependency length (unlikely to find, but search explicitly). For each result, document: what linguistic phenomenon it models, how it uses survival-analysis machinery, what the event/censoring structure is, how temporal dynamics differ from our position-bounded static censoring. Articulate the clean boundary: historical-ling hazard models track temporal change over centuries (e.g., rate at which 'shall' replaces 'will', or when a morpheme leaves the language); our work models position-dependent structural censoring in a single synchronic state—a word near a sentence boundary cannot produce a long arc, exactly analogous to a patient enrolled late in a trial, but we are not modeling temporal dynamics. Conclude: our novelty positioning should be 'first application of survival analysis to synchronic dependency-length data at scale,' explicitly grounded in the historical-linguistics tradition but clearly distinct. Output: research_out.json with (a) catalog of historical-ling hazard models and how they differ, (b) refined novelty positioning statement (2–3 sentences) suitable for Related Work/Introduction, (c) confirmation that construct validity and field appropriateness of the survival-analysis framing for dependency arcs is sound and addresses a real, published confound (Ferrer-i-Cancho) rather than inventing a problem.",
          "depends_on": [
            {
              "id": "art_2CDrgn6Hae3P",
              "label": "iter-1 research and survival-analysis foundations"
            }
          ]
        }
      ],
      "expected_outcome": "By end of iteration 2, we will have: (1) a corrected survival-analysis pipeline with primary findings on a small, rigorously defined gold-labeled spoken/written subset (n_spoken approximately 18.8k, n_written approximately 67.4k from English/French/Slovenian) including register Cox coefficient with 95% bootstrap CI and explicit construct definition; family-level residual-hazard rankings with bootstrap CIs and Benjamini-Hochberg multiple-comparison correction (reporting only families surviving BH threshold); and a secondary full-corpus finding with explicit label-noise sensitivity bounds showing how much the register coefficient could shift if heuristic labels have noise; (2) comprehensive validation showing effect sizes in linguistically meaningful units (tokens/median-shift), explicit data-provenance reconciliation documenting which statistics came from which treebank subset and annotation source, and robustness of key methodological choices (word-order operationalization, sentence-length resampling, random-baseline comparison) to reasonable perturbations; (3) a refined novelty claim—'first application to synchronic dependency-length data'—grounded in historical-linguistics context and clearly distinguished from temporal hazard models. These three artifacts eliminate all MAJOR reviewer critiques (construct validity of register finding, multiple-comparison problem in family rankings, data-provenance confusion) and address MINOR concerns (word-order operationalization, Futrell recovery demonstration, effect-size interpretation, novelty precision). The result is a publication-ready empirical foundation meeting top-tier journal standards for construct validity, statistical rigor, and transparency.",
      "summary": "This strategy directly addresses reviewer feedback by retrofitting iter-1's results with proper construct validity (gold-labeled subset only for spoken-vs-written), statistical rigor (bootstrap CIs, Benjamini-Hochberg correction), and transparency (explicit data-provenance documentation). The goal is not new discovery but rigorous validation of iter-1's foundation to ACL/EMNLP/ComputLing publication standards. Three parallel artifacts re-run the analysis with refinements, validate all methodological choices, and refine the novelty positioning to be precise and grounded in field-appropriate historical context."
    }
  ]
}
```

### [17] TOOL RESULT — Write · 2026-08-13 12:19:14 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Construct Validity and Statistical Rigor for Final Evidence\",\n      \"objective\": \"Convert iter-1's methodological foundation into publication-ready evidence by fixing three critical validity issues: (1) re-fit the Cox model on genuinely gold-labeled spoken/written data only as the primary finding, with heuristic-labeled full corpus as secondary robustness check with explicit label-noise sensitivity bounds; (2) add bootstrap confidence intervals for all family-level residual hazards and apply Benjamini-Hochberg correction across 32 comparisons, reporting only families surviving correction; (3) provide explicit, reconciled data-provenance documentation so readers know exactly which statistics came from which treebank subset and which annotation source.\",\n      \"rationale\": \"Iteration 1 produced a methodologically novel result (survival-analysis reframing of dependency arcs, correctly handling position-bounded censoring) but the evidence for two key claims—spoken-vs-written register effect and language-family outliers—relies on noisy/heuristic labels and lacks multiple-comparison control. Reviewer feedback identifies these as threats to construct validity (the headline register finding is mostly from treebanks with no gold annotation of modality, only heuristic defaults) and statistical validity (32 family comparisons reported without correction, inviting spurious top-rank artifacts). The computational-linguistics field handbook emphasizes that construct validity and measurement rigor are load-bearing for publication in top venues; a capability claim must define its construct, operationalize it clearly, and report uncertainty. This iteration must repair these foundations: restrict the primary spoken-vs-written claim to the small, gold-labeled subset (English, French, Slovenian pairs); add label-noise sensitivity analysis to bound the impact of heuristic labels on the full-corpus secondary finding; compute bootstrap CIs for family residuals and apply Benjamini-Hochberg correction; clarify data provenance with explicit tables. This is not exploratory work—it is targeted validation of iter-1's results to publication-readiness standards.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Re-run the survival-analysis pipeline on gold-labeled spoken/written data as the primary analysis, with three methodological refinements: (1) restrict spoken-vs-written Cox fit to English/French/Slovenian matched pairs (genuinely gold-annotated) as PRIMARY finding, (2) compute 1000-replicate bootstrap for family residuals and apply Benjamini-Hochberg correction across 32 families as PRIMARY ranking (not just point estimates), (3) add label-noise sensitivity: re-fit the full-corpus secondary model after randomly flipping 5%/10%/20% of heuristic register labels to bound how much the full-corpus register coefficient could be noise-driven.\",\n          \"approach\": \"Load the curated dataset (art_V4iFzwfu7i49) and filter to the small gold-labeled subset: English CHILDES/EWT, French Rhapsodie/GSD, Slovenian SST/SSJ pairs (documented as genuinely gold-annotated in iter-1 dataset artifact). Fit a primary Cox proportional-hazards model on this subset with register + standardized word-order + standardized morphological-richness as covariates, stratified by language family (note: family count will be smaller; stratify if n_families >= 5, else use family as fixed effect). Compute 1000-replicate bootstrap on family residuals (sample arcs with replacement, refit family-level Nelson-Aalen cumulative hazard at d=10), extract bootstrap confidence intervals (2.5th, 97.5th percentile), and apply Benjamini-Hochberg FDR correction across all 32 families using the point estimates. Report only families with BH-adjusted p < 0.05 as confirmed outliers. For the secondary analysis (full 350-treebank corpus with heuristic labels), fit a second Cox model and report its coefficients with CIs; then conduct 3 sensitivity runs where register labels are corrupted by randomly flipping 5%, 10%, 20% of the 'heuristic' rows (determined from a flag in the dataset), refit Cox, and plot how coefficients shift with label-corruption rate. For word-order operationalization robustness: fit Cox models under three variants: (A) categorical Grambank verb-order only (84% coverage), (B) empirical continuous fraction-of-dependents-before-head only (100% coverage), (C) both as separate terms (Grambank categorical + empirical continuous as interaction term or parallel terms). Report coefficients for register and family effects under all three variants to confirm they are stable across operationalization choices. Additionally, compute random-baseline null distribution: for a random sample of 50k arcs, permute head positions uniformly within sentence and compute null hazard curves; overlay observed vs. null on a figure to directly demonstrate (not just assert) that the observed hazard deviates from random, as required for the 'recovery' of Futrell et al. Explicit data provenance: in method_out.json metadata, tag every result with its source (gold-subset-cox, full-corpus-cox, gold-subset-bootstrap, sensitivity-5pct, etc.) and include a provenance table documenting the exact row counts, treebank sources, and annotation sources for each statistic. Output: method_out.json with (1) primary Cox fit on gold subset with 95% bootstrap CIs, (2) BH-corrected family rankings with bootstrap CIs and adjusted p-values, (3) secondary full-corpus Cox with label-noise sensitivity curves, (4) word-order operationalization variants comparison, (5) random-baseline null comparison, (6) explicit provenance metadata for every reported statistic.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_V4iFzwfu7i49\",\n              \"label\": \"gold-labeled dataset\"\n            }\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Comprehensively validate the experiment results by computing effect sizes in linguistically meaningful units, reconciling data provenance across 28-treebank vs. 350-treebank pipelines, and verifying that key methodological choices (word-order operationalization, register definition, sentence-length robustness) are robust to reasonable perturbations.\",\n          \"approach\": \"Generate four sets of validation results: (1) Effect-size standardization: For the primary register coefficient (beta from gold-subset Cox), compute the median arc-length reduction that the spoken-language penalty implies at the median arc-length observed in the data. Express this in terms of a percentile of the between-language variance in the same coefficient across the 350 treebanks (e.g., 'the register effect of 0.046 corresponds to a 0.5-token median arc-length reduction, which places it at the X-th percentile of between-language variance'). This grounds the effect size in linguistic units. (2) Data-provenance reconciliation table: Create a table with one row per reported statistic (register coefficient, word-order coefficient, family outlier rankings, robustness-check delta, etc.) documenting whether it came from: [a] 28-treebank curated dataset, [b] 350-treebank full extraction, [c] gold-labeled subset only (English/French/Slovenian), [d] secondary heuristic-label run. Include row counts, treebank names, and annotation sources. This resolves the paper's ambiguity about which numbers come from which pipeline. (3) Cross-checks and literature recovery: Compare new experiment results against iter-1 artifact (art_d7jrBtmjm_7W) for numerical stability (e.g., register coefficient iter-1 vs. iter-2, difference should be small since only the label-quality subset is changing); compute register effect stratified by dependency-type (functional vs. lexical) and compare against Gerdes et al.'s finding that functional deps are universally short (~1.71) and lexical deps are longer and typology-variable (expect register effect to be larger for lexical); recompute pooled-MDD ratios under same sentence-length resampling as Cox to directly demonstrate pooled-MDD variance is 10-20x larger than Cox-coefficient variance (the core robustness claim). (4) Methodological transparency: Generate a full audit trail showing: how gold-label treebanks were identified and validated (list the three with sources), how word-order variants were compared (all three operationalizations fitted to identical data subsets), how label-noise sensitivity was parameterized (5%/10%/20% random flips on 'heuristic' rows), and how bootstrap replicates were generated (sampling with replacement, number of replicates, random seed for reproducibility). Output: eval_out.json with tables, figures, and interpretive guidance for the paper; include effect-size quantile information, provenance table, literature-recovery statistics, and methodological audit trail.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_d7jrBtmjm_7W\",\n              \"label\": \"iter-1 results for comparison and baseline\"\n            }\n          ]\n        },\n        {\n          \"type\": \"research\",\n          \"objective\": \"Clarify the novelty positioning by systematically reviewing survival-analysis and hazard-based modeling in historical linguistics (lexical replacement, grammaticalization, language change), confirming the boundary between our work and historical-ling precedent, and producing a refined novelty claim suitable for top-tier venues.\",\n          \"approach\": \"Conduct targeted scholarly search for: (1) hazard models or survival-analysis applications in historical/diachronic linguistics (lexical replacement rates, grammaticalization as a survival process, phonological/morphological change trajectories over time), (2) position-dependent censoring or right-censoring concepts applied to linguistic data (census records, incomplete documentation, inherited constraints), (3) any prior synchronic applications of survival analysis to syntactic structure or dependency length (unlikely to find, but search explicitly). For each result, document: what linguistic phenomenon it models, how it uses survival-analysis machinery, what the event/censoring structure is, how temporal dynamics differ from our position-bounded static censoring. Articulate the clean boundary: historical-ling hazard models track temporal change over centuries (e.g., rate at which 'shall' replaces 'will', or when a morpheme leaves the language); our work models position-dependent structural censoring in a single synchronic state—a word near a sentence boundary cannot produce a long arc, exactly analogous to a patient enrolled late in a trial, but we are not modeling temporal dynamics. Conclude: our novelty positioning should be 'first application of survival analysis to synchronic dependency-length data at scale,' explicitly grounded in the historical-linguistics tradition but clearly distinct. Output: research_out.json with (a) catalog of historical-ling hazard models and how they differ, (b) refined novelty positioning statement (2–3 sentences) suitable for Related Work/Introduction, (c) confirmation that construct validity and field appropriateness of the survival-analysis framing for dependency arcs is sound and addresses a real, published confound (Ferrer-i-Cancho) rather than inventing a problem.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_2CDrgn6Hae3P\",\n              \"label\": \"iter-1 research and survival-analysis foundations\"\n            }\n          ]\n        }\n      ],\n      \"expected_outcome\": \"By end of iteration 2, we will have: (1) a corrected survival-analysis pipeline with primary findings on a small, rigorously defined gold-labeled spoken/written subset (n_spoken approximately 18.8k, n_written approximately 67.4k from English/French/Slovenian) including register Cox coefficient with 95% bootstrap CI and explicit construct definition; family-level residual-hazard rankings with bootstrap CIs and Benjamini-Hochberg multiple-comparison correction (reporting only families surviving BH threshold); and a secondary full-corpus finding with explicit label-noise sensitivity bounds showing how much the register coefficient could shift if heuristic labels have noise; (2) comprehensive validation showing effect sizes in linguistically meaningful units (tokens/median-shift), explicit data-provenance reconciliation documenting which statistics came from which treebank subset and annotation source, and robustness of key methodological choices (word-order operationalization, sentence-length resampling, random-baseline comparison) to reasonable perturbations; (3) a refined novelty claim—'first application to synchronic dependency-length data'—grounded in historical-linguistics context and clearly distinguished from temporal hazard models. These three artifacts eliminate all MAJOR reviewer critiques (construct validity of register finding, multiple-comparison problem in family rankings, data-provenance confusion) and address MINOR concerns (word-order operationalization, Futrell recovery demonstration, effect-size interpretation, novelty precision). The result is a publication-ready empirical foundation meeting top-tier journal standards for construct validity, statistical rigor, and transparency.\",\n      \"summary\": \"This strategy directly addresses reviewer feedback by retrofitting iter-1's results with proper construct validity (gold-labeled subset only for spoken-vs-written), statistical rigor (bootstrap CIs, Benjamini-Hochberg correction), and transparency (explicit data-provenance documentation). The goal is not new discovery but rigorous validation of iter-1's foundation to ACL/EMNLP/ComputLing publication standards. Three parallel artifacts re-run the analysis with refinements, validate all methodological choices, and refine the novelty positioning to be precise and grounded in field-appropriate historical context.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [18] ASSISTANT · 2026-08-13 12:19:16 UTC

```
Perfect. I've written the strategy JSON to the correct location. Let me verify it's valid:
```

### [19] TOOL CALL — Read · 2026-08-13 12:19:16 UTC

```
/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json
```

### [20] TOOL RESULT — Read · 2026-08-13 12:19:18 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_strat/gen_strat_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"strategies\": [\n    {\n      \"title\": \"Construct Validity and Statistical Rigor for Final Evidence\",\n      \"objective\": \"Convert iter-1's methodological foundation into publication-ready evidence by fixing three critical validity issues: (1) re-fit the Cox model on genuinely gold-labeled spoken/written data only as the primary finding, with heuristic-labeled full corpus as secondary robustness check with explicit label-noise sensitivity bounds; (2) add bootstrap confidence intervals for all family-level residual hazards and apply Benjamini-Hochberg correction across 32 comparisons, reporting only families surviving correction; (3) provide explicit, reconciled data-provenance documentation so readers know exactly which statistics came from which treebank subset and which annotation source.\",\n      \"rationale\": \"Iteration 1 produced a methodologically novel result (survival-analysis reframing of dependency arcs, correctly handling position-bounded censoring) but the evidence for two key claims—spoken-vs-written register effect and language-family outliers—relies on noisy/heuristic labels and lacks multiple-comparison control. Reviewer feedback identifies these as threats to construct validity (the headline register finding is mostly from treebanks with no gold annotation of modality, only heuristic defaults) and statistical validity (32 family comparisons reported without correction, inviting spurious top-rank artifacts). The computational-linguistics field handbook emphasizes that construct validity and measurement rigor are load-bearing for publication in top venues; a capability claim must define its construct, operationalize it clearly, and report uncertainty. This iteration must repair these foundations: restrict the primary spoken-vs-written claim to the small, gold-labeled subset (English, French, Slovenian pairs); add label-noise sensitivity analysis to bound the impact of heuristic labels on the full-corpus secondary finding; compute bootstrap CIs for family residuals and apply Benjamini-Hochberg correction; clarify data provenance with explicit tables. This is not exploratory work—it is targeted validation of iter-1's results to publication-readiness standards.\",\n      \"artifact_directions\": [\n        {\n          \"type\": \"experiment\",\n          \"objective\": \"Re-run the survival-analysis pipeline on gold-labeled spoken/written data as the primary analysis, with three methodological refinements: (1) restrict spoken-vs-written Cox fit to English/French/Slovenian matched pairs (genuinely gold-annotated) as PRIMARY finding, (2) compute 1000-replicate bootstrap for family residuals and apply Benjamini-Hochberg correction across 32 families as PRIMARY ranking (not just point estimates), (3) add label-noise sensitivity: re-fit the full-corpus secondary model after randomly flipping 5%/10%/20% of heuristic register labels to bound how much the full-corpus register coefficient could be noise-driven.\",\n          \"approach\": \"Load the curated dataset (art_V4iFzwfu7i49) and filter to the small gold-labeled subset: English CHILDES/EWT, French Rhapsodie/GSD, Slovenian SST/SSJ pairs (documented as genuinely gold-annotated in iter-1 dataset artifact). Fit a primary Cox proportional-hazards model on this subset with register + standardized word-order + standardized morphological-richness as covariates, stratified by language family (note: family count will be smaller; stratify if n_families >= 5, else use family as fixed effect). Compute 1000-replicate bootstrap on family residuals (sample arcs with replacement, refit family-level Nelson-Aalen cumulative hazard at d=10), extract bootstrap confidence intervals (2.5th, 97.5th percentile), and apply Benjamini-Hochberg FDR correction across all 32 families using the point estimates. Report only families with BH-adjusted p < 0.05 as confirmed outliers. For the secondary analysis (full 350-treebank corpus with heuristic labels), fit a second Cox model and report its coefficients with CIs; then conduct 3 sensitivity runs where register labels are corrupted by randomly flipping 5%, 10%, 20% of the 'heuristic' rows (determined from a flag in the dataset), refit Cox, and plot how coefficients shift with label-corruption rate. For word-order operationalization robustness: fit Cox models under three variants: (A) categorical Grambank verb-order only (84% coverage), (B) empirical continuous fraction-of-dependents-before-head only (100% coverage), (C) both as separate terms (Grambank categorical + empirical continuous as interaction term or parallel terms). Report coefficients for register and family effects under all three variants to confirm they are stable across operationalization choices. Additionally, compute random-baseline null distribution: for a random sample of 50k arcs, permute head positions uniformly within sentence and compute null hazard curves; overlay observed vs. null on a figure to directly demonstrate (not just assert) that the observed hazard deviates from random, as required for the 'recovery' of Futrell et al. Explicit data provenance: in method_out.json metadata, tag every result with its source (gold-subset-cox, full-corpus-cox, gold-subset-bootstrap, sensitivity-5pct, etc.) and include a provenance table documenting the exact row counts, treebank sources, and annotation sources for each statistic. Output: method_out.json with (1) primary Cox fit on gold subset with 95% bootstrap CIs, (2) BH-corrected family rankings with bootstrap CIs and adjusted p-values, (3) secondary full-corpus Cox with label-noise sensitivity curves, (4) word-order operationalization variants comparison, (5) random-baseline null comparison, (6) explicit provenance metadata for every reported statistic.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_V4iFzwfu7i49\",\n              \"label\": \"gold-labeled dataset\"\n            }\n          ]\n        },\n        {\n          \"type\": \"evaluation\",\n          \"objective\": \"Comprehensively validate the experiment results by computing effect sizes in linguistically meaningful units, reconciling data provenance across 28-treebank vs. 350-treebank pipelines, and verifying that key methodological choices (word-order operationalization, register definition, sentence-length robustness) are robust to reasonable perturbations.\",\n          \"approach\": \"Generate four sets of validation results: (1) Effect-size standardization: For the primary register coefficient (beta from gold-subset Cox), compute the median arc-length reduction that the spoken-language penalty implies at the median arc-length observed in the data. Express this in terms of a percentile of the between-language variance in the same coefficient across the 350 treebanks (e.g., 'the register effect of 0.046 corresponds to a 0.5-token median arc-length reduction, which places it at the X-th percentile of between-language variance'). This grounds the effect size in linguistic units. (2) Data-provenance reconciliation table: Create a table with one row per reported statistic (register coefficient, word-order coefficient, family outlier rankings, robustness-check delta, etc.) documenting whether it came from: [a] 28-treebank curated dataset, [b] 350-treebank full extraction, [c] gold-labeled subset only (English/French/Slovenian), [d] secondary heuristic-label run. Include row counts, treebank names, and annotation sources. This resolves the paper's ambiguity about which numbers come from which pipeline. (3) Cross-checks and literature recovery: Compare new experiment results against iter-1 artifact (art_d7jrBtmjm_7W) for numerical stability (e.g., register coefficient iter-1 vs. iter-2, difference should be small since only the label-quality subset is changing); compute register effect stratified by dependency-type (functional vs. lexical) and compare against Gerdes et al.'s finding that functional deps are universally short (~1.71) and lexical deps are longer and typology-variable (expect register effect to be larger for lexical); recompute pooled-MDD ratios under same sentence-length resampling as Cox to directly demonstrate pooled-MDD variance is 10-20x larger than Cox-coefficient variance (the core robustness claim). (4) Methodological transparency: Generate a full audit trail showing: how gold-label treebanks were identified and validated (list the three with sources), how word-order variants were compared (all three operationalizations fitted to identical data subsets), how label-noise sensitivity was parameterized (5%/10%/20% random flips on 'heuristic' rows), and how bootstrap replicates were generated (sampling with replacement, number of replicates, random seed for reproducibility). Output: eval_out.json with tables, figures, and interpretive guidance for the paper; include effect-size quantile information, provenance table, literature-recovery statistics, and methodological audit trail.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_d7jrBtmjm_7W\",\n              \"label\": \"iter-1 results for comparison and baseline\"\n            }\n          ]\n        },\n        {\n          \"type\": \"research\",\n          \"objective\": \"Clarify the novelty positioning by systematically reviewing survival-analysis and hazard-based modeling in historical linguistics (lexical replacement, grammaticalization, language change), confirming the boundary between our work and historical-ling precedent, and producing a refined novelty claim suitable for top-tier venues.\",\n          \"approach\": \"Conduct targeted scholarly search for: (1) hazard models or survival-analysis applications in historical/diachronic linguistics (lexical replacement rates, grammaticalization as a survival process, phonological/morphological change trajectories over time), (2) position-dependent censoring or right-censoring concepts applied to linguistic data (census records, incomplete documentation, inherited constraints), (3) any prior synchronic applications of survival analysis to syntactic structure or dependency length (unlikely to find, but search explicitly). For each result, document: what linguistic phenomenon it models, how it uses survival-analysis machinery, what the event/censoring structure is, how temporal dynamics differ from our position-bounded static censoring. Articulate the clean boundary: historical-ling hazard models track temporal change over centuries (e.g., rate at which 'shall' replaces 'will', or when a morpheme leaves the language); our work models position-dependent structural censoring in a single synchronic state—a word near a sentence boundary cannot produce a long arc, exactly analogous to a patient enrolled late in a trial, but we are not modeling temporal dynamics. Conclude: our novelty positioning should be 'first application of survival analysis to synchronic dependency-length data at scale,' explicitly grounded in the historical-linguistics tradition but clearly distinct. Output: research_out.json with (a) catalog of historical-ling hazard models and how they differ, (b) refined novelty positioning statement (2–3 sentences) suitable for Related Work/Introduction, (c) confirmation that construct validity and field appropriateness of the survival-analysis framing for dependency arcs is sound and addresses a real, published confound (Ferrer-i-Cancho) rather than inventing a problem.\",\n          \"depends_on\": [\n            {\n              \"id\": \"art_2CDrgn6Hae3P\",\n              \"label\": \"iter-1 research and survival-analysis foundations\"\n            }\n          ]\n        }\n      ],\n      \"expected_outcome\": \"By end of iteration 2, we will have: (1) a corrected survival-analysis pipeline with primary findings on a small, rigorously defined gold-labeled spoken/written subset (n_spoken approximately 18.8k, n_written approximately 67.4k from English/French/Slovenian) including register Cox coefficient with 95% bootstrap CI and explicit construct definition; family-level residual-hazard rankings with bootstrap CIs and Benjamini-Hochberg multiple-comparison correction (reporting only families surviving BH threshold); and a secondary full-corpus finding with explicit label-noise sensitivity bounds showing how much the register coefficient could shift if heuristic labels have noise; (2) comprehensive validation showing effect sizes in linguistically meaningful units (tokens/median-shift), explicit data-provenance reconciliation documenting which statistics came from which treebank subset and annotation source, and robustness of key methodological choices (word-order operationalization, sentence-length resampling, random-baseline comparison) to reasonable perturbations; (3) a refined novelty claim—'first application to synchronic dependency-length data'—grounded in historical-linguistics context and clearly distinguished from temporal hazard models. These three artifacts eliminate all MAJOR reviewer critiques (construct validity of register finding, multiple-comparison problem in family rankings, data-provenance confusion) and address MINOR concerns (word-order operationalization, Futrell recovery demonstration, effect-size interpretation, novelty precision). The result is a publication-ready empirical foundation meeting top-tier journal standards for construct validity, statistical rigor, and transparency.\",\n      \"summary\": \"This strategy directly addresses reviewer feedback by retrofitting iter-1's results with proper construct validity (gold-labeled subset only for spoken-vs-written), statistical rigor (bootstrap CIs, Benjamini-Hochberg correction), and transparency (explicit data-provenance documentation). The goal is not new discovery but rigorous validation of iter-1's foundation to ACL/EMNLP/ComputLing publication standards. Three parallel artifacts re-run the analysis with refinements, validate all methodological choices, and refine the novelty positioning to be precise and grounded in field-appropriate historical context.\"\n    }\n  ]\n}\n", "numLines": 47, "startLine": 1, "totalLines": 47}}
```

### [21] ASSISTANT · 2026-08-13 12:19:23 UTC

```
Done. The strategy JSON is now complete and valid at `.terminal_claude_agent_struct_out.json`. 

**Summary of the generated strategy:**

This final-iteration strategy directly addresses all three MAJOR reviewer critiques through three parallel, focused artifacts:

1. **EXPERIMENT** — Re-run survival analysis with:
   - Primary finding on gold-labeled data only (English/French/Slovenian pairs, ~86k arcs)
   - Bootstrap CIs and Benjamini-Hochberg correction for family residuals
   - Label-noise sensitivity analysis (5%/10%/20% corruption bounds)
   - Word-order operationalization variants
   - Random-baseline null comparison

2. **EVALUATION** — Comprehensive validation:
   - Effect-size standardization in linguistic units
   - Data-provenance reconciliation table
   - Cross-checks against iter-1 and literature (Gerdes, Futrell)
   - Methodological audit trail

3. **RESEARCH** — Novelty positioning:
   - Historical-linguistics hazard models review
   - Refined claim: "first application to synchronic dependency-length data"
   - Clear boundary from temporal/diachronic models

The strategy converts iteration 1's methodological foundation into publication-ready evidence meeting ACL/EMNLP/ComputLing standards for construct validity, statistical rigor, and transparency.
```
