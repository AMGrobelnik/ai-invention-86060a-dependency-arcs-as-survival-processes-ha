# gen_plan_research_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_oQQwThF8kM-b` — Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_research_1` (terminal_claude_agent, claude-haiku-4-5)

### [1] CONFIG · 2026-08-13 12:19:27 UTC

```
model: claude-haiku-4-5 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_plan/gen_plan_research_1
```

### [2] SYSTEM-USER prompt · 2026-08-13 12:19:33 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: RESEARCH

RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings
</artifact_type_info>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>
</available_resources>

<time_budget>

The research executor has 3h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

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

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: research_iter2_dir3
type: research
objective: >-
  Clarify the novelty positioning by systematically reviewing survival-analysis and hazard-based modeling in historical linguistics
  (lexical replacement, grammaticalization, language change), confirming the boundary between our work and historical-ling
  precedent, and producing a refined novelty claim suitable for top-tier venues.
approach: >-
  Conduct targeted scholarly search for: (1) hazard models or survival-analysis applications in historical/diachronic linguistics
  (lexical replacement rates, grammaticalization as a survival process, phonological/morphological change trajectories over
  time), (2) position-dependent censoring or right-censoring concepts applied to linguistic data (census records, incomplete
  documentation, inherited constraints), (3) any prior synchronic applications of survival analysis to syntactic structure
  or dependency length (unlikely to find, but search explicitly). For each result, document: what linguistic phenomenon it
  models, how it uses survival-analysis machinery, what the event/censoring structure is, how temporal dynamics differ from
  our position-bounded static censoring. Articulate the clean boundary: historical-ling hazard models track temporal change
  over centuries (e.g., rate at which 'shall' replaces 'will', or when a morpheme leaves the language); our work models position-dependent
  structural censoring in a single synchronic state—a word near a sentence boundary cannot produce a long arc, exactly analogous
  to a patient enrolled late in a trial, but we are not modeling temporal dynamics. Conclude: our novelty positioning should
  be 'first application of survival analysis to synchronic dependency-length data at scale,' explicitly grounded in the historical-linguistics
  tradition but clearly distinct. Output: research_out.json with (a) catalog of historical-ling hazard models and how they
  differ, (b) refined novelty positioning statement (2–3 sentences) suitable for Related Work/Introduction, (c) confirmation
  that construct validity and field appropriateness of the survival-analysis framing for dependency arcs is sound and addresses
  a real, published confound (Ferrer-i-Cancho) rather than inventing a problem.
depends_on:
- id: art_2CDrgn6Hae3P
  label: iter-1 research and survival-analysis foundations
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for research artifacts:
  - cpu_light: 4 vCPUs, 16GB RAM — proofs, research, lightweight tasks (fallback: memory-optimized CPUs first (cpu3m → cpu5m), then GPU hosts last-ditch)

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
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
  "description": "Plan for a RESEARCH artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "question": {
      "default": "",
      "description": "The specific research question to investigate",
      "title": "Question",
      "type": "string"
    },
    "research_plan": {
      "description": "Step-by-step plan for web research to gather this research",
      "title": "Research Plan",
      "type": "string"
    },
    "explanation": {
      "description": "Why this research matters and what question it answers",
      "title": "Explanation",
      "type": "string"
    }
  },
  "required": [
    "title",
    "research_plan",
    "explanation"
  ],
  "title": "ResearchPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-08-13 12:19:33 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [4] ASSISTANT · 2026-08-13 12:19:51 UTC

```
Looking at this planning task, I need to create a detailed research plan that will guide the executor to investigate the novelty positioning of this survival-analysis approach to dependency arcs—specifically, clarifying how it differs from historical-linguistics precedent with hazard models.

Let me start by understanding what research needs to happen and what key sources exist in this space.
```

### [5] TOOL CALL — Skill · 2026-08-13 12:19:51 UTC

```
aii-web-research-tools
```

### [6] TOOL RESULT — Skill · 2026-08-13 12:19:51 UTC

```
{"success": true, "commandName": "aii-web-research-tools"}
```

### [7] ASSISTANT · 2026-08-13 12:19:57 UTC

```
Now let me conduct targeted research to understand what historical-linguistics work exists with hazard models, and verify the novelty boundary.
```

### [8] TOOL CALL — ToolSearch · 2026-08-13 12:19:57 UTC

```
{'query': 'select:WebSearch', 'max_results': 1}
```

### [9] TOOL RESULT — ToolSearch · 2026-08-13 12:19:57 UTC

```
{"matches": ["WebSearch"], "query": "select:WebSearch", "total_deferred_tools": 21}
```

### [10] TOOL CALL — WebSearch · 2026-08-13 12:19:59 UTC

```
hazard model language change grammaticalization
```

### [11] TOOL CALL — WebSearch · 2026-08-13 12:19:59 UTC

```
survival analysis historical linguistics lexical replacement
```

### [12] TOOL CALL — WebSearch · 2026-08-13 12:19:59 UTC

```
Ferrer-i-Cancho dependency length pooling confound
```

### [13] TOOL CALL — WebSearch · 2026-08-13 12:19:59 UTC

```
survival analysis syntax dependencies right-censoring
```

### [14] TOOL RESULT — WebSearch · 2026-08-13 12:20:05 UTC

```
{"query": "hazard model language change grammaticalization", "results": [{"tool_use_id": "srvtoolu_017KhndwnTNy4Vm99Y6uoh28", "content": [{"title": "Abstracts • Refining Grammaticalization • Department of Philosophy and Humanities", "url": "https://www.geisteswissenschaften.fu-berlin.de/en/v/Refining_Grammaticalization/Abstracts1/index.html"}, {"title": "(PDF) Modeling Language Change: The Pitfall of Grammaticalization", "url": "https://www.academia.edu/52024620/Modeling_Language_Change_The_Pitfall_of_Grammaticalization"}, {"title": "(PDF) Modeling Language Change: The Pitfall of Grammaticalization", "url": "https://www.researchgate.net/publication/305385641_Modeling_Language_Change_The_Pitfall_of_Grammaticalization"}, {"title": "Frequency patterns of semantic change: Corpus-based evidence of a   near-critical dynamics in language change", "url": "https://arxiv.org/pdf/1703.00203"}, {"title": "New Trends in Grammaticalization and Language Change | Edited by Sylvie Hancil, Tine Breban and José Vicente Lozano", "url": "https://benjamins.com/catalog/slcs.202"}, {"title": "Grammaticalization as Optimization Paul Kiparsky 2.1 Grammaticalization 2.1.1", "url": "https://web.stanford.edu/~kiparsky/Papers/yalegrammaticalization.pdf"}, {"title": "Grammaticalization and Semantic Reanalysis Regine Eckardt", "url": "https://semanticsarchive.net/Archive/GRmOWZmN/SemanticReanalysis.pdf"}]}, "I've performed a web search for \"hazard model language change grammaticalization.\" Here are the results:\n\nThe search results primarily focus on grammaticalization and modeling language change from various theoretical perspectives, including:\n\n1. **Network models of grammaticalization**: Research examines principles of network models relevant to language change, including that tokens of use are nodes in the language network, the structure allows for multiple default inheritance predicting gradience, and entrenchment of nodes is the product of successful use.\n\n2. **Grammaticalization frameworks**: Current models are claimed not to provide satisfactory accounts of grammaticalization (where words acquire grammatical status), leading researchers to introduce frameworks like the \"grammatheme\" to formalize mechanisms involved in grammaticalization.\n\n3. **Unidirectionality in grammaticalization**: The unidirectionality of grammaticalization may be comparable to the unidirectionality of lenition in phonological change—a better than chance occurrence in language change that admits exceptions.\n\n4. **Recent approaches**: New models such as constructionalization have been applied, with renewed interest in typological application of grammaticalization and cognitive motivations for unidirectionality.\n\nHowever, the search results don't contain specific information about \"hazard models\" applied to language change and grammaticalization. The results focus on other modeling approaches. If you're looking for research specifically on hazard rate models in linguistic change, you may need to search with more specific terminology or consult specialized linguistic literature on quantitative methods in historical linguistics."], "durationSeconds": 7.1294053889999995, "searchCount": 1}
```

### [15] TOOL RESULT — WebSearch · 2026-08-13 12:20:05 UTC

```
{"query": "survival analysis historical linguistics lexical replacement", "results": [{"tool_use_id": "srvtoolu_01SNLt69zVUoufBoPNq99AuY", "content": [{"title": "Quantifying Cognitive Factors in Lexical Decline | Transactions of the Association for Computational Linguistics | MIT Press", "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00441/108934/Quantifying-Cognitive-Factors-in-Lexical-Decline"}, {"title": "Lexical borrowing in the Middle English period: a multi-domain analysis of semantic outcomes | English Language & Linguistics | Cambridge Core", "url": "https://www.cambridge.org/core/journals/english-language-and-linguistics/article/abs/lexical-borrowing-in-the-middle-english-period-a-multidomain-analysis-of-semantic-outcomes/B83A68089915746EC1B613C20761E985"}, {"title": "Survival and loss of Old English religious vocabulary between 1150 and 1350 | English Language & Linguistics | Cambridge Core", "url": "https://www.cambridge.org/core/journals/english-language-and-linguistics/article/survival-and-loss-of-old-english-religious-vocabulary-between-1150-and-1350/BA4EEFD39CCED022CB8A66093290FDC7"}, {"title": "Survival factors in the early Middle English lexicon | English Language & Linguistics | Cambridge Core", "url": "https://www.cambridge.org/core/journals/english-language-and-linguistics/article/survival-factors-in-the-early-middle-english-lexicon/50B9228A59E172A599D7FC367EE449B5"}, {"title": "What are the determinants of survival curves of words?: An evolutionary linguistics approach", "url": "https://benjamins.com/catalog/elt.00019.vel"}, {"title": "Survey of Computational Approaches to Lexical Semantic Change", "url": "https://arxiv.org/pdf/1811.06278"}, {"title": "What are the determinants of survival curves of words? | John Benjamins", "url": "https://www.jbe-platform.com/content/journals/10.1075/elt.00019.vel"}, {"title": "The structure of online social networks modulates the rate of lexical   change", "url": "https://arxiv.org/pdf/2104.05010"}, {"title": "What are the determinants of survival curves of words?: An evolutionary linguistics approach | Request PDF", "url": "https://www.researchgate.net/publication/347256820_What_are_the_determinants_of_survival_curves_of_words_An_evolutionary_linguistics_approach"}]}, "The search has returned several highly relevant results on survival analysis in historical linguistics and lexical replacement. Here's what the results show:\n\n## Survival Analysis in Historical Linguistics\n\nSurvival analysis has been applied to investigate what factors determine the lifespan of words. An evolutionary approach to historical linguistics can be enlightening when not only the mechanisms, but also the statistical methods are considered from neighboring disciplines.\n\n## Lexical Replacement\n\nLexical replacement is used about a lexeme being ousted by another synonymous lexeme over time. Vejdemo and Hörberg (2016) conducted a study of lexical replacement—a closely-related but narrower phenomenon than lexical decline—exploring similar semantic factors.\n\n## Research Findings\n\nResearch using survival analysis has identified several factors affecting word survival:\n\n- Lower frequency and phonetically longer lexemes suffer earlier deaths, and verbs turn out to have higher survival rates than adjectives and nouns.\n\n- In early Middle English lexicon studies, survival analysis revealed that geographical spread is the most important factor, usually in combination with particular suffixes.\n\n- Words are subject to various cognitive pressures that can influence their 'survival', and declining words tend to decrease in the diversity of their lexical contexts over time.\n\nThe research demonstrates how statistical methods borrowed from other disciplines can illuminate the mechanisms of lexical change and replacement in historical language evolution."], "durationSeconds": 7.211852538, "searchCount": 1}
```

### [16] TOOL RESULT — WebSearch · 2026-08-13 12:20:05 UTC

```
{"query": "Ferrer-i-Cancho dependency length pooling confound", "results": [{"tool_use_id": "srvtoolu_01J45V6TdFDkWdy9vExiVy6y", "content": [{"title": "Dependency distance minimization predicts compression Ramon Ferrer-i-Cancho", "url": "https://aclanthology.org/2021.quasy-1.4.pdf"}, {"title": "[PDF] Hubiness, length, crossings and their relationships in dependency trees | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/Hubiness,-length,-crossings-and-their-relationships-Ferrer-i-Cancho/2ebdb93599237ae67f5f16535d890ca3fc87fc52"}, {"title": "Crossings as a side effect of dependency lengths - Ferrer‐I‐Cancho - 2016 - Complexity - Wiley Online Library", "url": "https://onlinelibrary.wiley.com/doi/abs/10.1002/cplx.21810"}, {"title": "Crossings as a side effect of dependency lengths", "url": "https://arxiv.org/pdf/1508.06451"}, {"title": "Himanshu Yadav*, Samar Husain and Richard Futrell", "url": "https://sites.socsci.uci.edu/~rfutrell/papers/yadav2021dependency.pdf"}, {"title": "1 / 4 Dependency length minimization: Puzzles and Promises", "url": "https://arxiv.org/pdf/1509.04393"}, {"title": "(PDF) The placement of the head that maximizes predictability. An information theoretic approach", "url": "https://www.researchgate.net/publication/317229982_The_placement_of_the_head_that_maximizes_predictability_An_information_theoretic_approach"}, {"title": "Dependency distance minimization: a diachronic exploration of the effects of sentence length and dependency types | Humanities and Social Sciences Communications", "url": "https://www.nature.com/articles/s41599-022-01447-3"}]}, "Based on the search results, I found relevant information about Ferrer-i-Cancho's work on dependency length, though the specific term \"pooling confound\" wasn't explicitly mentioned in the results. Here's what I found:\n\n## Dependency Length Minimization (DDM)\n\nDependency distance is usually measured in words, but the distance of a dependency would be a function of the length of the words defining the dependency and that of the words in-between.\n\n## The Compression Prediction\n\nThe DDm principle predicts compression, whereby the mean word length has to be minimized. This connects to a potential confound: if dependency lengths vary partly due to word length differences across languages or contexts, this could affect measurements of dependency length minimization.\n\n## Hubiness and Dependency Length\n\nHubiness (the variance of degrees) plays a central role: the mean dependency length is bounded below by hubiness while the number of crossings is bounded above by hubiness. This suggests structural properties of dependency trees can create statistical relationships that might confound simpler interpretations of dependency length patterns.\n\nThe search results show Ferrer-i-Cancho's extensive work on how multiple structural factors in language (word lengths, tree structure variance, sentence length) interact with dependency length measurements, which appears relevant to understanding potential confounds in dependency length analysis."], "durationSeconds": 7.160564857999998, "searchCount": 1}
```

### [17] TOOL RESULT — WebSearch · 2026-08-13 12:20:05 UTC

```
{"query": "survival analysis syntax dependencies right-censoring", "results": [{"tool_use_id": "srvtoolu_01MrHP1SqghyPq7MqK2wAccq", "content": [{"title": "Proximal Survival Analysis to Handle Dependent Right Censoring", "url": "https://arxiv.org/pdf/2208.07014"}, {"title": "Survival data analysis", "url": "https://www.karlin.mff.cuni.cz/~pesta/NMFM404/survival.html"}, {"title": "Introduction to Survival Analysis in R - OARC Stats - UCLA", "url": "https://stats.oarc.ucla.edu/wp-content/uploads/2025/02/survival_r_full.html"}, {"title": "PyDTS: A Python Package for Discrete-Time Survival Analysis with Competing Risks and Optional Penalization", "url": "https://arxiv.org/pdf/2204.05731"}, {"title": "Deep Copula-Based Survival Analysis for Dependent Censoring with   Identifiability Guarantees", "url": "https://arxiv.org/pdf/2312.15566"}, {"title": "Survival Data Simulation With the R Package rsurv", "url": "https://arxiv.org/pdf/2406.01750"}, {"title": "SurvLIMEpy: A Python package implementing SurvLIME", "url": "https://arxiv.org/pdf/2302.10571"}, {"title": "27 Survival analysis – The Epidemiologist R Handbook", "url": "https://www.epirhandbook.com/en/new_pages/survival_analysis.html"}, {"title": "9 Survival analysis and censored data | Modern Statistics with R", "url": "https://modernstatisticswithr.com/survivalchapter.html"}]}, "I've found several relevant sources on survival analysis with dependencies and right-censoring. Here's a summary of the key findings:\n\n## Right-Censoring Fundamentals\n\nRight-censoring is the most common type of censoring assumption dealt with in survival analysis. Survival data is right-censored when the time until the event of interest is greater than the observed time.\n\n## Independent vs. Dependent Censoring\n\nThe \"independent censoring\" assumption states that the event time and the censoring time are independent (T ⊥ C). The Kaplan-Meier estimator, the Nelson-Aalen estimator, and the logrank test are typically used to address right censoring in this case.\n\nHowever, proximal assumptions can be established to handle survival analysis in the presence of dependent right censoring, which addresses scenarios where the standard independence assumption doesn't hold.\n\n## Syntax in R\n\nCensoring is assumed to be right-censored unless otherwise specified with the type argument in the Surv() function. The Surv() function from the survival package is used to build a survival object from the follow-up time and event columns, producing an object that condenses the time information and whether the event of interest was observed.\n\nThe sources include research papers on handling dependent censoring, practical implementation guides for R, and Python packages for survival analysis simulation."], "durationSeconds": 7.093648896000002, "searchCount": 1}
```

### [18] ASSISTANT · 2026-08-13 12:20:13 UTC

```
Now let me fetch some of these key papers to understand the historical-linguistics precedent better.
```

### [19] TOOL CALL — ToolSearch · 2026-08-13 12:20:13 UTC

```
{'query': 'select:WebFetch', 'max_results': 1}
```

### [20] TOOL RESULT — ToolSearch · 2026-08-13 12:20:13 UTC

```
{"matches": ["WebFetch"], "query": "select:WebFetch", "total_deferred_tools": 21}
```

### [21] TOOL CALL — WebFetch · 2026-08-13 12:20:19 UTC

```
URL: https://arxiv.org/pdf/2104.05010
Prompt: What linguistic phenomenon is modeled as a survival process? How is the event defined? What is the censoring mechanism?
```

### [22] TOOL CALL — WebFetch · 2026-08-13 12:20:19 UTC

```
URL: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00441/108934/Quantifying-Cognitive-Factors-in-Lexical-Decline
Prompt: What is the event/outcome? How is time defined? How does this survival analysis approach differ from a simple mean comparison?
```

### [23] TOOL RESULT — WebFetch · 2026-08-13 12:20:19 UTC

```
{"bytes": 0, "code": 403, "codeText": "Forbidden", "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 293, "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00441/108934/Quantifying-Cognitive-Factors-in-Lexical-Decline"}
```

### [24] TOOL CALL — WebFetch · 2026-08-13 12:20:19 UTC

```
URL: https://arxiv.org/pdf/1509.04393
Prompt: What is the dependency length pooling problem? How does sentence length affect dependency length distributions?
```

### [25] TOOL RESULT — WebFetch · 2026-08-13 12:20:19 UTC

```
{"bytes": 1845251, "code": 200, "codeText": "OK", "result": "I appreciate your question, but I need to be direct: the content provided appears to be a corrupted or compressed PDF file that doesn't contain readable text. The material shows binary/encoded data rather than accessible linguistic or statistical content.\n\nWithout legible source material, I cannot accurately identify:\n- What linguistic phenomenon is modeled\n- How the event is defined\n- What censoring mechanism is employed\n\nTo provide the analysis you're requesting, I would need a readable document discussing survival analysis applied to language data. If you have an alternative version of this paper or a different source, I'd be happy to examine it and answer your questions while respecting the character limits and attribution guidelines you've outlined.\n\n[Binary content (application/pdf, 1.8MB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-oQQwThF8kM-b-3-invention-loop-iter-2-gen-plan-gen-plan-research-1/0d8c5a3b-2481-44b7-8e4d-82de7ba7d496/tool-results/webfetch-1786623615380-dipicp.pdf]", "durationMs": 4521, "url": "https://arxiv.org/pdf/2104.05010"}
```

### [26] TOOL RESULT — WebFetch · 2026-08-13 12:20:21 UTC

```
{"bytes": 342062, "code": 200, "codeText": "OK", "result": "I appreciate your request, but the document provided appears to be a PDF file encoded in binary format that doesn't render as readable text. The content shown consists of PDF structure metadata and compressed stream data rather than the actual article text.\n\nTo properly answer your questions about dependency length pooling and how sentence length affects dependency length distributions, I would need access to the readable text content of this document.\n\nCould you please:\n1. Provide the article text in a readable format (plain text, markdown, etc.), or\n2. Share the title/authors so I can reference the work appropriately, or\n3. Copy and paste the relevant sections discussing these topics?\n\nOnce I have readable content, I'll be happy to explain these linguistic concepts concisely with proper attribution.\n\n[Binary content (application/pdf, 334KB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-oQQwThF8kM-b-3-invention-loop-iter-2-gen-plan-gen-plan-research-1/0d8c5a3b-2481-44b7-8e4d-82de7ba7d496/tool-results/webfetch-1786623616420-6kzrmo.pdf]", "durationMs": 3706, "url": "https://arxiv.org/pdf/1509.04393"}
```

### [27] ASSISTANT · 2026-08-13 12:20:25 UTC

```
Let me search for more accessible sources and specific papers on these topics.
```

### [28] TOOL CALL — WebSearch · 2026-08-13 12:20:25 UTC

```
"What are the determinants of survival curves of words" Vejdemo
```

### [29] TOOL CALL — WebSearch · 2026-08-13 12:20:25 UTC

```
Ferrer-i-Cancho "The risks of mixing dependency lengths"
```

### [30] TOOL CALL — WebSearch · 2026-08-13 12:20:25 UTC

```
dependency length spoken written register variation
```

### [31] TOOL RESULT — WebSearch · 2026-08-13 12:20:31 UTC

```
{"query": "\"What are the determinants of survival curves of words\" Vejdemo", "results": [{"tool_use_id": "srvtoolu_011Pru96neJmL7YWqHhXFTEc", "content": [{"title": "What are the determinants of survival curves of words?: An evolutionary linguistics approach | Request PDF", "url": "https://www.researchgate.net/publication/347256820_What_are_the_determinants_of_survival_curves_of_words_An_evolutionary_linguistics_approach"}, {"title": "What are the determinants of survival curves of words?: An evolutionary linguistics approach", "url": "https://benjamins.com/catalog/elt.00019.vel"}, {"title": "What are the determinants of survival curves of words? | John Benjamins", "url": "https://www.jbe-platform.com/content/journals/10.1075/elt.00019.vel?crawler=true"}, {"title": "Survival Curves in Statistics", "url": "https://www.jove.com/science-education/v/17616/survival-curves"}, {"title": "Survivorship curve", "url": "https://en.wikipedia.org/wiki/Survivorship_curve"}, {"title": "Quantifying Cognitive Factors in Lexical Decline | Transactions of the Association for Computational Linguistics | MIT Press", "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00441/108934/Quantifying-Cognitive-Factors-in-Lexical-Decline"}, {"title": "RULSurv: A probabilistic survival-based method for early censoring-aware   prediction of remaining useful life in ball bearings", "url": "https://arxiv.org/pdf/2405.01614"}]}, "Based on the search results, I found the research paper you're looking for. The study applies survival analysis to investigate what factors determine the lifespan of words, with a case study on post-classical Greek from the 4th century BC to the beginning of the 8th century AD.\n\nThe key findings regarding the determinants of word survival curves are:\n\n1. **Word Frequency**: Lower frequency lexemes suffer earlier deaths\n\n2. **Phonetic Length**: Phonetically longer lexemes suffer earlier deaths\n\n3. **Word Class**: Verbs turn out to have higher survival rates than adjectives and nouns\n\nThe research methodology employs survival analysis techniques including the Kaplan-Meier estimator and Cox proportional hazard model."], "durationSeconds": 6.112729143000004, "searchCount": 1}
```

### [32] TOOL RESULT — WebSearch · 2026-08-13 12:20:31 UTC

```
{"query": "Ferrer-i-Cancho \"The risks of mixing dependency lengths\"", "results": [{"tool_use_id": "srvtoolu_01MGU63PH11t2dJJtBXDZNYM", "content": [{"title": "[1304.3841] The risks of mixing dependency lengths from sequences of different length", "url": "https://arxiv.org/abs/1304.3841"}, {"title": "The risks of mixing dependency lengths from sequences of different   length", "url": "https://arxiv.org/pdf/1304.3841"}, {"title": "Factors Influencing Dependency Distance (Chapter 12) - Word Grammar, Cognition and Dependency", "url": "https://www.cambridge.org/core/books/abs/word-grammar-cognition-and-dependency/factors-influencing-dependency-distance/608109BDB35B9423AE335DB57ACB246F"}, {"title": "Quantitative relationship between distribution of sentence length and dependency distance in Spanish", "url": "https://www.degruyterbrill.com/document/doi/10.1515/lingvan-2024-0185/html"}, {"title": "Large-scale evidence of dependency length minimization in 37 languages | PNAS", "url": "https://www.pnas.org/doi/10.1073/pnas.1502134112"}, {"title": "Non-crossing Dependencies: Least Effort, Not Grammar | SpringerLink", "url": "https://link.springer.com/chapter/10.1007/978-3-662-47238-5_10"}, {"title": "Crossings as a side effect of dependency lengths - Ferrer‐I‐Cancho - 2016 - Complexity - Wiley Online Library", "url": "https://onlinelibrary.wiley.com/doi/abs/10.1002/cplx.21810"}, {"title": "Glottotheory Volume 5, Issue 2", "url": "https://www.degruyterbrill.com/journal/key/glot/5/2/html?lang=en"}, {"title": "A Reappraisal of Dependency Length Minimization as a Linguistic Universal - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9692064/"}, {"title": "Ramon FERRER-I-CANCHO | Tenured associate professor | Computer Science | Polytechnic University of Catalonia, Barcelona | UPC | Department of Computer Science | Research profile - Page 2", "url": "https://www.researchgate.net/profile/Ramon-Ferrer-I-Cancho/2"}]}, "I found the paper you're looking for. Here's what I found:\n\n\"The risks of mixing dependency lengths from sequences of different length\" is a paper by Ramon Ferrer-i-Cancho and Haitao Liu examining the common practice in language research of mixing dependency lengths from sequences of different length.\n\nThe paper shows that the empirical distribution of dependency lengths of sentences of the same length differs from that of sentences of varying length, and the distribution of dependency lengths depends on sentence length for both real sentences and under the null hypothesis that dependencies connect vertices located in random positions of the sequence.\n\nThis suggests that certain results, such as the distribution of syntactic dependency lengths mixing dependencies from sentences of varying length, could be a mere consequence of that mixing.\n\nFurthermore, differences in the global averages of dependency length for two different languages do not simply imply that one language optimizes dependency lengths better than the other because those differences could be due to differences in the distribution of sentence lengths and other factors.\n\nThe paper was published in Glottotheory in 2014 and is available on arXiv at https://arxiv.org/abs/1304.3841."], "durationSeconds": 5.802619409999999, "searchCount": 1}
```

### [33] TOOL RESULT — WebSearch · 2026-08-13 12:20:31 UTC

```
{"query": "dependency length spoken written register variation", "results": [{"tool_use_id": "srvtoolu_01KXQDLfcM61K82aP6RouZ2j", "content": [{"title": "Dependency lengths in speech and writing: A cross-linguistic comparison", "url": "https://aclanthology.org/2021.scil-1.36.pdf"}, {"title": "Variation in Language and Cohesion across Written and Spoken Registers", "url": "https://escholarship.org/content/qt7d8631cr/qt7d8631cr_noSplash_1baa0b228787a2bfb598aaa2ab63d544.pdf"}, {"title": "Register Variation: A Corpus Approach 175 9 Register Variation:", "url": "https://www.blackwellpublishing.com/content/bpl_images/content_store/WWW_Content/9780631205951/009.pdf"}, {"title": "Glottometrics 51, 2021 39 A Multi-dimensional Approach to Register Variations", "url": "https://glottometrics.iqla.org/wp-content/uploads/2022/03/2021_51_393.pdf"}, {"title": "Register variation in spoken British English: the case of verb-forming", "url": "https://centaur.reading.ac.uk/67310/3/16036%20Laws%20&%20Ryder%20[finalised%2005.02.18]_with_pre-proof_header.pdf"}, {"title": "The risks of mixing dependency lengths from sequences of different   length", "url": "https://arxiv.org/pdf/1304.3841"}, {"title": "A scale of conceptual orality and literacy: Automatic text   categorization in the tradition of \"N\\\"ahe und Distanz\"", "url": "https://arxiv.org/pdf/2502.03252"}, {"title": "Variation between Different Discourse Types: Literate vs. Oral", "url": "https://aclanthology.org/W19-1407.pdf"}, {"title": "The Distribution of Dependency Distance and Hierarchical Distance in Contemporary Written Japanese and Its Influencing Factors", "url": "https://arxiv.org/pdf/2504.21421"}]}, "Based on the search results, here's what I found on dependency length in relation to spoken, written, and register variation:\n\n## Dependency Length Across Spoken and Written Registers\n\nResearch has found differences in dependency lengths between spoken and written registers, with some languages showing longer spoken dependencies than written dependencies (French, Russian, Italian; English showed no difference).\n\n## Register Variation and Discourse Style\n\nA key cross-linguistic finding from multi-dimensional (MD) studies is that spoken registers and 'oral' written registers rely on clausal discourse styles with dense use of dependent clauses, while written registers and 'literate' spoken registers rely on phrasal discourse styles with dense use of phrasal modifiers embedded in noun phrases.\n\n## Dependency Distance Patterns\n\nResearch testing hypotheses about dependency distance across 20 languages found that adjacent dependencies account for the highest proportion among all languages, suggesting that the human language parser prefers linear orders that minimize average dependency distance.\n\nThe research suggests that dependency length is an important linguistic feature that varies systematically across spoken and written registers, with implications for understanding the fundamental differences between these discourse modes."], "durationSeconds": 5.521368036, "searchCount": 1}
```

### [34] ASSISTANT · 2026-08-13 12:20:39 UTC

```
Now let me search for recent DLM methodology papers to understand current best practices and related work.
```

### [35] TOOL CALL — WebSearch · 2026-08-13 12:20:39 UTC

```
dependency length minimization 2024 2025 2026 methodology
```

### [36] TOOL CALL — WebSearch · 2026-08-13 12:20:39 UTC

```
Dobrovoljc dependency length spoken written
```

### [37] TOOL CALL — WebSearch · 2026-08-13 12:20:39 UTC

```
Gerdes functional lexical dependency length
```

### [38] TOOL RESULT — WebSearch · 2026-08-13 12:20:45 UTC

```
{"query": "Dobrovoljc dependency length spoken written", "results": [{"tool_use_id": "srvtoolu_01S9yCVjH9V2hBfQFwmZEcTr", "content": [{"title": "Kaja Dobrovoljc - ACL Anthology", "url": "https://aclanthology.org/people/kaja-dobrovoljc/"}, {"title": "Kaja Dobrovoljc Jozef Stefan Institute ...", "url": "https://universaldependencies.org/udw18/PDFs/34_Paper.pdf"}, {"title": "(PDF) The Universal Dependencies Treebank for Slovenian", "url": "https://www.researchgate.net/publication/318739675_The_Universal_Dependencies_Treebank_for_Slovenian"}, {"title": "Proceedings of the Second Workshop on Universal Dependencies (UDW 2018) - ACL Anthology", "url": "https://aclanthology.org/volumes/W18-60/"}, {"title": "Kaja Dobrovoljc Counting trees: A treebank-driven exploration of syntactic", "url": "https://arxiv.org/pdf/2505.22774"}, {"title": "Fine-grained Controllable Text Generation through In-context Learning   with Feedback", "url": "https://arxiv.org/pdf/2406.11338"}, {"title": "The Universal Dependencies Treebank of Spoken Slovenian - ACL Anthology", "url": "https://aclanthology.org/L16-1248/"}, {"title": "GitHub - UniversalDependencies/UD_Slovenian-SST", "url": "https://github.com/UniversalDependencies/UD_Slovenian-SST/tree/master"}]}, "Based on the search results, here's what I found about Dobrovoljc's work on dependency length in spoken versus written language:\n\nDobrovoljc's analysis of the Slovenian treebanks confirms significant syntactic differences between spoken and written language modalities, with spoken data consisting of shorter and more elliptic sentences, less and simpler nominal phrases, and more relations marking disfluencies, interaction, deixis and modality.\n\nDobrovoljc and colleagues found that dependency parsing systems achieve considerably lower performance parsing spoken language data compared to written data, and they investigated which speech-specific phenomena undermine parsing performance using the Spoken Slovenian Treebank. \n\nTheir results showed that utterance segmentation is the most prominent cause of low parsing performance, and both parsers performed better on normalized transcriptions with basic prosody markers and excluding disfluencies.\n\nThe research demonstrates that dependency structures in spoken language are notably shorter and simpler than those in written language, which is relevant to understanding how dependency length varies across modalities."], "durationSeconds": 5.858591163999997, "searchCount": 1}
```

### [39] TOOL RESULT — WebSearch · 2026-08-13 12:20:47 UTC

```
{"query": "dependency length minimization 2024 2025 2026 methodology", "results": [{"tool_use_id": "srvtoolu_01AAXec8QBwfZcYAxARwNXXW", "content": [{"title": "Dependency length minimization in natural and artificial grammars | Request PDF", "url": "https://www.researchgate.net/publication/220469436_Dependency_length_minimization_in_natural_and_artificial_grammars"}, {"title": "Large-scale evidence of dependency length minimization in 37 languages", "url": "https://www.pnas.org/doi/pdf/10.1073/pnas.1502134112"}, {"title": "Dependency distance minimization: a diachronic exploration of the effects of sentence length and dependency types | Humanities and Social Sciences Communications", "url": "https://www.nature.com/articles/s41599-022-01447-3"}, {"title": "Mean Dependency Distance (MDD) in Linguistics", "url": "https://www.emergentmind.com/topics/mean-dependency-distance-mdd"}, {"title": "The Grammar Does the Work: Functional vs. Lexical Dependency Length Minimization Across Universal Dependencies", "url": "https://arxiv.org/pdf/2607.01899"}, {"title": "1 / 4 Dependency length minimization: Puzzles and Promises", "url": "https://arxiv.org/pdf/1509.04393"}, {"title": "Does Dependency Locality Predict Non-canonical Word Order in Hindi?", "url": "https://arxiv.org/pdf/2405.07730"}, {"title": "A Reappraisal of Dependency Length Minimization as a Linguistic Universal", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9692064/"}, {"title": "A Reappraisal of Dependency Length Minimization as a Linguistic Universal | Open Mind | MIT Press", "url": "https://direct.mit.edu/opmi/article/doi/10.1162/opmi_a_00060/112598/A-Reappraisal-of-Dependency-Length-Minimization-as"}, {"title": "A Reappraisal of Dependency Length Minimization as a Linguistic Universal - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9692064/"}]}, "Based on the web search results, here's what I found about dependency length minimization methodology from 2024-2026:\n\n## Recent Research on Dependency Length Minimization\n\nRecent studies in 2025-2026 have explored how dependency distance minimization (DDM) reflects different strategies of sentence organization to meet the universal constraint of working memory. Research has found that Chinese objects tend to be much shorter than English objects, and that unlike in English, Chinese subjects and objects tend to have similar lengths when their information status is controlled.\n\n## Current Methodological Approaches\n\nDependency Length Minimization (DLM) has a rich empirical history, with Liu (2008) proposing Mean Dependency Distance (MDD) as a metric of language comprehension difficulty. Three principles that minimize dependency length have been identified: consistent branching direction, shorter dependent phrases being closer to the head, and opposite-branching of one-word phrases.\n\nA standard methodology involves conducting cross-linguistic corpus studies where real trees attested in dependency treebanks are compared with random baseline trees that match the real trees in certain properties.\n\n## Recent Developments (2024-2025)\n\nFuture research areas identified include empirical derivation of chunk-size distributions, development of multi-level chunking algorithms, and integration of human processing experiments linking reaction times to MDD. More fine-grained models factoring non-uniform, multi-tier chunking, and cross-linguistic predicate valency distributions are expected to refine predictions."], "durationSeconds": 7.556338191999996, "searchCount": 1}
```

### [40] TOOL RESULT — WebSearch · 2026-08-13 12:20:47 UTC

```
{"query": "Gerdes functional lexical dependency length", "results": [{"tool_use_id": "srvtoolu_01JjP3zkFhguBE4vz3Hk5b1S", "content": [{"title": "The Grammar Does the Work: Functional vs. Lexical Dependency Length Minimization Across Universal Dependencies", "url": "https://arxiv.org/pdf/2607.01899"}, {"title": "Computation and Language Jul 2026", "url": "https://arxiv.org/list/cs.CL/current?skip=90&show=25"}, {"title": "Dependency Locality as an Explanatory Principle for Word Order | Request PDF", "url": "https://www.researchgate.net/publication/342350601_Dependency_locality_as_an_explanatory_principle_for_word_order"}, {"title": "Dependency structures and lexicalized grammars", "url": "https://www.researchgate.net/publication/298070505_Dependency_structures_and_lexicalized_grammars"}, {"title": "Dependency locality as an explanatory principle for word order", "url": "https://tedlab.mit.edu/tedlab_website/researchpapers/Futrell_Levy_Gibson_2020.pdf"}, {"title": "A Reappraisal of Dependency Length Minimization as a Linguistic Universal - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9692064/"}, {"title": "International Conference on Dependency Linguistics", "url": "https://depling.org/proceedingsDepling2011/papers/proceedingsDepling2011.pdf"}, {"title": "Kim Gerdes", "url": "https://gerdes.fr/"}]}, "Based on the search results, here's what I found about Gerdes' work on functional and lexical dependency length:\n\nKim Gerdes conducted research on dependency length minimization (DLM), a well-documented processing universal, showing that previous studies report a single mean dependency distance per language, obscuring variation across syntactic relation types.\n\nHis analysis examined 122 languages in UD and SUD (version 2.17), showing that DLM operates on two distinct levels.\n\nThe key findings distinguish between two types of dependencies:\n\n1. **Functional Dependencies**: Grammar-driven optimization targets functional dependencies (det, case, aux), which are universally short (mean 1.71, σ = 0.33) and invariant across typologically diverse languages.\n\n2. **Lexical Dependencies**: Processing-driven optimization operates on lexical dependencies (nsubj, obj, obl), which are longer (mean 2.87), highly variable (σ = 0.63), and constrained by word-order typology.\n\nGerdes concludes that \"the grammar does the work\" of minimization by scaffolding sentences with local functional attachments, leaving processing pressures to determine the ordering of lexical heads. This research was presented at the Ninth Workshop on Universal Dependencies (UDW 2026) in May 2026."], "durationSeconds": 7.855962073000002, "searchCount": 1}
```

### [41] ASSISTANT · 2026-08-13 12:21:23 UTC

```
Perfect! I now have a clear picture of the landscape. Let me write a comprehensive, actionable research plan for the executor.
```

### [42] TOOL CALL — Write · 2026-08-13 12:21:23 UTC

```
File: /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json

{
  "title": "Survival Analysis Novelty Positioning in Linguistics",
  "summary": "Systematically investigate survival-analysis and hazard-based modeling in historical linguistics, clarify the boundary between historical-change precedent and our synchronic dependency-arc model, and produce refined novelty positioning suitable for top venues.",
  "runpod_compute_profile": "cpu_light",
  "question": "What is the precise novelty positioning of applying survival analysis to synchronic dependency-arc data? How does our work differ from historical-linguistics precedent with hazard models? Does survival analysis address a real, documented confound in current DLM methodology?",
  "research_plan": "**Phase 1: Map Historical-Linguistics Survival Analysis Precedent**\n\n1. Confirm and catalog survival-analysis applications in historical linguistics:\n   - Search: 'survival analysis historical linguistics' + 'lexical replacement' + 'word survival curves'\n   - Fetch key papers (especially arXiv:0000/v1 versions when available):\n     * Vejdemo & Hörberg (2016) on determinants of word survival curves (post-classical Greek, 4th century BC–8th century AD)\n     * Papers on lexical decline, word death, and cognitive factors in word loss\n     * Any papers on grammaticalization rates or phonological/morphological change trajectories\n   - For each paper, document:\n     * What linguistic phenomenon is modeled as a survival process?\n     * How is the 'event' defined? (e.g., 'word disappears from use')\n     * What is the time variable? (calendar time: centuries, decades, years)\n     * What is the censoring mechanism? (incomplete documentation, data ends before word dies)\n     * What survival-analysis machinery is used? (Kaplan-Meier, Cox, frailty?)\n     * What are the predictors/covariates? (word frequency, phonetic length, word class, etc.)\n     * What is the scientific question being answered?\n\n2. Identify at least 3–5 distinct historical-linguistics survival-analysis applications and summarize their event/censoring/time structure in a table.\n\n**Phase 2: Verify the Ferrer-i-Cancho Confound Is Real and Unaddressed**\n\n1. Fetch and deeply read Ferrer-i-Cancho & Liu (2014): 'The risks of mixing dependency lengths from sequences of different length' (arXiv:1304.3841):\n   - Extract: What is the exact mathematical problem they identify?\n   - What do they prove about how sentence-length distribution affects pooled mean dependency distance?\n   - Do they propose or recommend a solution? (If yes, what? If no, note the gap.)\n   - Is this confound acknowledged in subsequent DLM literature?\n\n2. Search for and fetch 3–5 recent DLM papers (2022–2026) from the hypothesis's related works or recent literature:\n   - Dobrovoljc (2025): Spoken language syntactic properties\n   - Gerdes et al. (2026): 'The Grammar Does the Work: Functional vs. Lexical Dependency Length Minimization'\n   - Futrell et al. (2015): 'Large-scale evidence of dependency length minimization' (PNAS baseline)\n   - Any papers on cross-linguistic/register DLM comparisons\n   - For each, ask: Do they address or correct for the Ferrer-i-Cancho confound? Do they use pooled means or a more sophisticated model? Do they acknowledge the length-mixing risk?\n\n3. Synthesize: Is the confound documented but unresolved in current practice? Or have other methods already solved it?\n\n**Phase 3: Search Explicitly for Synchronic Survival-Analysis Applications to Syntax/Dependencies**\n\n1. Conduct targeted searches for any prior applications of survival analysis or hazard models to synchronic syntactic data:\n   - Search: 'survival analysis syntax' + 'hazard model dependency' + 'censoring syntactic data'\n   - Search: 'Kaplan-Meier' + 'Cox model' + 'proportional hazards' + 'linguistic'\n   - Search: 'right-censoring' + 'structural constraint' + 'language'\n   - If papers appear, fetch and assess: Are they measuring something temporal (diachronic) or static (synchronic)? How do they handle the position/boundary constraint?\n\n2. Expected outcome: Unlikely to find any published applications to synchronic dependency data. Document evidence of this null search as a positive finding (confirms novelty).\n\n**Phase 4: Articulate the Clean Boundary**\n\n1. Create a comparison table with rows = historical-linguistics hazard models vs. our dependency-arc model, and columns:\n   - Linguistic phenomenon being modeled\n   - Event definition\n   - Time/process variable\n   - Censoring mechanism\n   - Methodological motivation\n   - Temporal scope (diachronic vs. synchronic)\n   - Data structure (time-series across centuries vs. a single snapshot)\n\n2. Write a 2–3 sentence novelty claim articulating:\n   - Why historical-linguistics hazard models are not a precedent for our work (they model temporal change; we model position-dependent structural constraints in a single state)\n   - What gap in current DLM methodology we fill (survival analysis corrects the Ferrer-i-Cancho confound that other methods do not address)\n   - Our positioning: 'First application of survival analysis to synchronic dependency-length data at scale, addressing a documented methodological confound in DLM research.'\n\n**Phase 5: Verify Construct Validity**\n\n1. Fetch Ferrer-i-Cancho (2021): 'Dependency distance minimization predicts compression' or a recent Ferrer-i-Cancho survey to understand current discourse on dependency-length confounds.\n\n2. Document: Does the survival-analysis framing genuinely solve the pooling problem? How?\n   - Answer: By treating position-bounded arc length as right-censored (word near boundary cannot produce long arc), the model explicitly controls for sentence-length composition. Cox coefficients should be invariant to sentence-length resampling where pooled means are not.\n   - This addresses Ferrer-i-Cancho's critique: it makes the confound explicit rather than ignoring it.\n\n**Phase 6: Synthesis and Output**\n\n1. Compile research_out.json with keys:\n   - 'historical_linguistics_catalog': List of 3–5 survival-analysis applications with event/censoring/time structure for each\n   - 'confound_analysis': Documented evidence that Ferrer-i-Cancho's length-mixing confound is real, published, and unaddressed by current DLM methods (with citations)\n   - 'synchronic_search_results': Explicit statement that no prior synchronic survival-analysis applications to dependencies were found (with search terms used)\n   - 'novelty_positioning_statement': Refined 2–3 sentence claim for Related Work/Introduction\n   - 'boundary_table': CSV or JSON table contrasting historical-ling hazard models vs. our model\n   - 'construct_validity_summary': How survival analysis corrects the Ferrer-i-Cancho confound\n\n2. Write research_report.md with:\n   - Executive summary (200 words): The landscape of hazard modeling in linguistics, the documented length-mixing confound, and how our work fills the gap\n   - Main sections: Historical precedent, the confound, novelty confirmation, boundary articulation\n   - Conclusion: Refined positioning and readiness for top-tier submission\n\n**Execution Notes:**\n- Use scholarly search mode where available to prioritize peer-reviewed literature\n- For arXiv papers, prefer to fetch the published/journal version when available\n- When papers are behind paywalls or un-fetchable, document the title/authors/venue and note 'abstract only' or 'title/venue confirmed'\n- If a paper's full text is inaccessible, synthesize from title, abstract, and search snippets, but flag the limitation\n- Cross-check findings across at least 2–3 sources before claiming a fact (e.g., 'Ferrer-i-Cancho's confound is unaddressed')\n- If novelty appears less clear than expected (e.g., if someone already applied survival analysis to synchronic data), document that honestly and adjust the positioning accordingly",
  "explanation": "This research clarifies the novelty positioning of applying survival analysis to synchronic dependency arcs by (1) mapping what historical-linguistics precedent exists with hazard models (lexical replacement, grammaticalization), (2) confirming the Ferrer-i-Cancho length-mixing confound is a documented, unresolved problem in current DLM methodology, (3) verifying no prior synchronic applications of survival analysis to dependency data exist, and (4) articulating a clean boundary between temporal change (historical linguistics) and position-dependent structural constraints (our work). The output is a refined novelty statement suitable for ACL/EMNLP/CL venues, anchored in documented methodology gaps and field precedent rather than unsupported claims. This addresses the reviewer's construct-validity critique and grounds the work in the historical-linguistics tradition while clarifying its distinct contribution to synchronic dependency-length research."
}
```

### [43] TOOL RESULT — Write · 2026-08-13 12:21:23 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_2/gen_plan/gen_plan_research_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Survival Analysis Novelty Positioning in Linguistics\",\n  \"summary\": \"Systematically investigate survival-analysis and hazard-based modeling in historical linguistics, clarify the boundary between historical-change precedent and our synchronic dependency-arc model, and produce refined novelty positioning suitable for top venues.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"question\": \"What is the precise novelty positioning of applying survival analysis to synchronic dependency-arc data? How does our work differ from historical-linguistics precedent with hazard models? Does survival analysis address a real, documented confound in current DLM methodology?\",\n  \"research_plan\": \"**Phase 1: Map Historical-Linguistics Survival Analysis Precedent**\\n\\n1. Confirm and catalog survival-analysis applications in historical linguistics:\\n   - Search: 'survival analysis historical linguistics' + 'lexical replacement' + 'word survival curves'\\n   - Fetch key papers (especially arXiv:0000/v1 versions when available):\\n     * Vejdemo & Hörberg (2016) on determinants of word survival curves (post-classical Greek, 4th century BC–8th century AD)\\n     * Papers on lexical decline, word death, and cognitive factors in word loss\\n     * Any papers on grammaticalization rates or phonological/morphological change trajectories\\n   - For each paper, document:\\n     * What linguistic phenomenon is modeled as a survival process?\\n     * How is the 'event' defined? (e.g., 'word disappears from use')\\n     * What is the time variable? (calendar time: centuries, decades, years)\\n     * What is the censoring mechanism? (incomplete documentation, data ends before word dies)\\n     * What survival-analysis machinery is used? (Kaplan-Meier, Cox, frailty?)\\n     * What are the predictors/covariates? (word frequency, phonetic length, word class, etc.)\\n     * What is the scientific question being answered?\\n\\n2. Identify at least 3–5 distinct historical-linguistics survival-analysis applications and summarize their event/censoring/time structure in a table.\\n\\n**Phase 2: Verify the Ferrer-i-Cancho Confound Is Real and Unaddressed**\\n\\n1. Fetch and deeply read Ferrer-i-Cancho & Liu (2014): 'The risks of mixing dependency lengths from sequences of different length' (arXiv:1304.3841):\\n   - Extract: What is the exact mathematical problem they identify?\\n   - What do they prove about how sentence-length distribution affects pooled mean dependency distance?\\n   - Do they propose or recommend a solution? (If yes, what? If no, note the gap.)\\n   - Is this confound acknowledged in subsequent DLM literature?\\n\\n2. Search for and fetch 3–5 recent DLM papers (2022–2026) from the hypothesis's related works or recent literature:\\n   - Dobrovoljc (2025): Spoken language syntactic properties\\n   - Gerdes et al. (2026): 'The Grammar Does the Work: Functional vs. Lexical Dependency Length Minimization'\\n   - Futrell et al. (2015): 'Large-scale evidence of dependency length minimization' (PNAS baseline)\\n   - Any papers on cross-linguistic/register DLM comparisons\\n   - For each, ask: Do they address or correct for the Ferrer-i-Cancho confound? Do they use pooled means or a more sophisticated model? Do they acknowledge the length-mixing risk?\\n\\n3. Synthesize: Is the confound documented but unresolved in current practice? Or have other methods already solved it?\\n\\n**Phase 3: Search Explicitly for Synchronic Survival-Analysis Applications to Syntax/Dependencies**\\n\\n1. Conduct targeted searches for any prior applications of survival analysis or hazard models to synchronic syntactic data:\\n   - Search: 'survival analysis syntax' + 'hazard model dependency' + 'censoring syntactic data'\\n   - Search: 'Kaplan-Meier' + 'Cox model' + 'proportional hazards' + 'linguistic'\\n   - Search: 'right-censoring' + 'structural constraint' + 'language'\\n   - If papers appear, fetch and assess: Are they measuring something temporal (diachronic) or static (synchronic)? How do they handle the position/boundary constraint?\\n\\n2. Expected outcome: Unlikely to find any published applications to synchronic dependency data. Document evidence of this null search as a positive finding (confirms novelty).\\n\\n**Phase 4: Articulate the Clean Boundary**\\n\\n1. Create a comparison table with rows = historical-linguistics hazard models vs. our dependency-arc model, and columns:\\n   - Linguistic phenomenon being modeled\\n   - Event definition\\n   - Time/process variable\\n   - Censoring mechanism\\n   - Methodological motivation\\n   - Temporal scope (diachronic vs. synchronic)\\n   - Data structure (time-series across centuries vs. a single snapshot)\\n\\n2. Write a 2–3 sentence novelty claim articulating:\\n   - Why historical-linguistics hazard models are not a precedent for our work (they model temporal change; we model position-dependent structural constraints in a single state)\\n   - What gap in current DLM methodology we fill (survival analysis corrects the Ferrer-i-Cancho confound that other methods do not address)\\n   - Our positioning: 'First application of survival analysis to synchronic dependency-length data at scale, addressing a documented methodological confound in DLM research.'\\n\\n**Phase 5: Verify Construct Validity**\\n\\n1. Fetch Ferrer-i-Cancho (2021): 'Dependency distance minimization predicts compression' or a recent Ferrer-i-Cancho survey to understand current discourse on dependency-length confounds.\\n\\n2. Document: Does the survival-analysis framing genuinely solve the pooling problem? How?\\n   - Answer: By treating position-bounded arc length as right-censored (word near boundary cannot produce long arc), the model explicitly controls for sentence-length composition. Cox coefficients should be invariant to sentence-length resampling where pooled means are not.\\n   - This addresses Ferrer-i-Cancho's critique: it makes the confound explicit rather than ignoring it.\\n\\n**Phase 6: Synthesis and Output**\\n\\n1. Compile research_out.json with keys:\\n   - 'historical_linguistics_catalog': List of 3–5 survival-analysis applications with event/censoring/time structure for each\\n   - 'confound_analysis': Documented evidence that Ferrer-i-Cancho's length-mixing confound is real, published, and unaddressed by current DLM methods (with citations)\\n   - 'synchronic_search_results': Explicit statement that no prior synchronic survival-analysis applications to dependencies were found (with search terms used)\\n   - 'novelty_positioning_statement': Refined 2–3 sentence claim for Related Work/Introduction\\n   - 'boundary_table': CSV or JSON table contrasting historical-ling hazard models vs. our model\\n   - 'construct_validity_summary': How survival analysis corrects the Ferrer-i-Cancho confound\\n\\n2. Write research_report.md with:\\n   - Executive summary (200 words): The landscape of hazard modeling in linguistics, the documented length-mixing confound, and how our work fills the gap\\n   - Main sections: Historical precedent, the confound, novelty confirmation, boundary articulation\\n   - Conclusion: Refined positioning and readiness for top-tier submission\\n\\n**Execution Notes:**\\n- Use scholarly search mode where available to prioritize peer-reviewed literature\\n- For arXiv papers, prefer to fetch the published/journal version when available\\n- When papers are behind paywalls or un-fetchable, document the title/authors/venue and note 'abstract only' or 'title/venue confirmed'\\n- If a paper's full text is inaccessible, synthesize from title, abstract, and search snippets, but flag the limitation\\n- Cross-check findings across at least 2–3 sources before claiming a fact (e.g., 'Ferrer-i-Cancho's confound is unaddressed')\\n- If novelty appears less clear than expected (e.g., if someone already applied survival analysis to synchronic data), document that honestly and adjust the positioning accordingly\",\n  \"explanation\": \"This research clarifies the novelty positioning of applying survival analysis to synchronic dependency arcs by (1) mapping what historical-linguistics precedent exists with hazard models (lexical replacement, grammaticalization), (2) confirming the Ferrer-i-Cancho length-mixing confound is a documented, unresolved problem in current DLM methodology, (3) verifying no prior synchronic applications of survival analysis to dependency data exist, and (4) articulating a clean boundary between temporal change (historical linguistics) and position-dependent structural constraints (our work). The output is a refined novelty statement suitable for ACL/EMNLP/CL venues, anchored in documented methodology gaps and field precedent rather than unsupported claims. This addresses the reviewer's construct-validity critique and grounds the work in the historical-linguistics tradition while clarifying its distinct contribution to synchronic dependency-length research.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [44] ASSISTANT · 2026-08-13 12:21:35 UTC

```
Perfect! I've completed a detailed, actionable research plan that will guide the executor through investigating the novelty positioning of this work. Here's what the plan accomplishes:

## Plan Summary

**Objective:** Clarify how the survival-analysis approach to dependency arcs differs from historical-linguistics precedent and confirm it addresses a real, unresolved methodological gap.

**Key Components:**

1. **Phase 1: Map Historical-Linguistics Hazard-Model Precedent** — Identifies and catalogs existing survival-analysis applications (lexical replacement, word death, grammaticalization) to understand their event/censoring/time structure (which focuses on *temporal change* over centuries).

2. **Phase 2: Verify the Ferrer-i-Cancho Confound** — Confirms the length-mixing problem is documented, real, and currently unaddressed in DLM methodology.

3. **Phase 3: Explicit Synchronic Search** — Conducts targeted searches to verify no prior synchronic applications of survival analysis to dependency data exist (likely finding nothing—evidence of novelty).

4. **Phase 4: Articulate the Clean Boundary** — Creates a comparison table showing how our work (synchronic, position-bounded censoring) differs from historical-ling models (temporal, document-incompleteness censoring).

5. **Phase 5: Verify Construct Validity** — Confirms that survival analysis genuinely solves the pooling problem Ferrer-i-Cancho identified.

6. **Phase 6: Synthesis** — Produces a refined 2–3 sentence novelty statement plus supporting documentation.

**Expected Output:** 
- `research_out.json` with catalog of historical-ling models, confound analysis, novelty positioning, and boundary table
- `research_report.md` with full synthesis suitable for an ACL/EMNLP/CL audience

**Why This Matters:** The plan grounds the novelty claim in documented precedent and unresolved gaps rather than speculation, directly addressing the reviewer's construct-validity critique.

The plan is now ready at `./.terminal_claude_agent_struct_out.json` for the executor agent to follow.
```
