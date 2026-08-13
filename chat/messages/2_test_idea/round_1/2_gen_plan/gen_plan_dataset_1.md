# gen_plan_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_oQQwThF8kM-b` — Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_dataset_1` (terminal_claude_agent, claude-haiku-4-5)

### [1] CONFIG · 2026-08-13 11:33:19 UTC

```
model: claude-haiku-4-5 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1
```

### [2] SYSTEM-USER prompt · 2026-08-13 11:33:25 UTC

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
You are expanding an artifact direction of type: DATASET

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect
</artifact_type_info>

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

<time_budget>

The dataset executor has 6h total (including writing code, debugging, testing, and fixing errors).

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
  If each syntactic dependency arc is modeled as a censored time-to-event process — where the 'event' is the arc closing at
  distance d and the maximum possible distance is right-censored by the word's position in its sentence — then the resulting
  hazard function h(d) (the instantaneous risk that an arc of length ≥d closes at exactly d) is not flat or freely comparable
  across registers and typologies, as pooled mean-dependency-distance (MDD) statistics implicitly assume. Instead: (1) spoken
  registers show a front-loaded hazard (risk peaks at very short d and decays fast, i.e. a 'get-short-or-get-stuck' profile)
  relative to written registers of the same language, even after correcting for the sentence-length-mixing confound that pooled
  MDD comparisons are known to suffer from; (2) case-marking / free-word-order languages show flatter, lower-peak hazard curves
  than fixed-order languages, reflecting looser real-time commitment to short arcs; and (3) a shared-frailty Cox model with
  language family as the frailty (random-effect) group reveals specific families (identifiable from the fitted frailty terms)
  whose hazard shape deviates from their typological cluster's baseline, i.e. families that minimize dependency length through
  a mechanism decoupled from the word-order/morphology covariates that explain most other families.
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

id: dataset_iter1_dir2
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
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead
</artifact_executor_scope>

<artifact_planning_rules>
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for dataset artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

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
  "description": "Plan for a DATASET artifact.",
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
    "ideal_dataset_criteria": {
      "description": "What makes an ideal dataset for this purpose - size, format, content requirements",
      "title": "Ideal Dataset Criteria",
      "type": "string"
    },
    "dataset_search_plan": {
      "description": "Step-by-step plan for finding/creating this dataset - sources to check, fallback options",
      "title": "Dataset Search Plan",
      "type": "string"
    },
    "target_num_datasets": {
      "description": "How many individual datasets should be delivered. Count each dataset separately, not collections \u2014 a benchmark suite of N datasets counts as N. This controls how broadly the executor searches, so setting it too low will under-collect.",
      "title": "Target Num Datasets",
      "type": "integer"
    }
  },
  "required": [
    "title",
    "ideal_dataset_criteria",
    "dataset_search_plan",
    "target_num_datasets"
  ],
  "title": "DatasetPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [3] HUMAN-USER prompt · 2026-08-13 11:33:25 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [4] ASSISTANT · 2026-08-13 11:33:35 UTC

```
I'll plan this dataset for dependency-arc survival analysis. Let me start by reading the computational linguistics handbook since this is a core linguistics research task, then research the actual data sources and schema requirements.
```

### [5] TOOL CALL — Skill · 2026-08-13 11:33:35 UTC

```
aii-handbook-auto-computational-linguistics
```

### [6] TOOL RESULT — Skill · 2026-08-13 11:33:35 UTC

```
{"success": true, "commandName": "aii-handbook-auto-computational-linguistics"}
```

### [7] ASSISTANT · 2026-08-13 11:33:45 UTC

```
Now let me research the actual data sources for this dataset plan.
```

### [8] TOOL CALL — Skill · 2026-08-13 11:33:45 UTC

```
aii-web-tools
```

### [9] TOOL RESULT — Skill · 2026-08-13 11:33:45 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [10] TOOL CALL — Skill · 2026-08-13 11:33:45 UTC

```
aii-web-tools
```

### [11] TOOL RESULT — Skill · 2026-08-13 11:33:45 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [12] TOOL CALL — Skill · 2026-08-13 11:33:45 UTC

```
aii-web-tools
```

### [13] TOOL RESULT — Skill · 2026-08-13 11:33:45 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [14] ASSISTANT · 2026-08-13 11:33:47 UTC

```
Let me load the web tools and then research the data sources.
```

### [15] TOOL CALL — ToolSearch · 2026-08-13 11:33:47 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 5}
```

### [16] TOOL RESULT — ToolSearch · 2026-08-13 11:33:47 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 21}
```

### [17] ASSISTANT · 2026-08-13 11:33:53 UTC

```
Now let me search for the actual data sources and metadata resources I need to plan this dataset.
```

### [18] TOOL CALL — WebSearch · 2026-08-13 11:33:53 UTC

```
commul universal_dependencies huggingface dataset
```

### [19] TOOL CALL — WebSearch · 2026-08-13 11:33:53 UTC

```
universal dependencies spoken written register metadata genres
```

### [20] TOOL CALL — WebSearch · 2026-08-13 11:33:53 UTC

```
Glottolog language family database download API
```

### [21] TOOL CALL — WebSearch · 2026-08-13 11:33:53 UTC

```
WALS Grambank typological features word order morphology
```

### [22] TOOL RESULT — WebSearch · 2026-08-13 11:33:55 UTC

```
{"query": "commul universal_dependencies huggingface dataset", "results": [{"tool_use_id": "srvtoolu_0123j7gVJrehN93Bc9t3o3WP", "content": [{"title": "commul/universal_dependencies · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/commul/universal_dependencies"}, {"title": "Models - Hugging Face", "url": "https://huggingface.co/models?dataset=dataset:Universal+Dependencies"}, {"title": "albertvillanova/universal_dependencies · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/albertvillanova/universal_dependencies"}, {"title": "universal-dependencies/universal_dependencies · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/universal-dependencies/universal_dependencies"}, {"title": "Daily Papers - Hugging Face", "url": "https://huggingface.co/papers?q=Universal+Dependencies"}, {"title": "universal_dependencies.py · universal_dependencies at 7ecda5ec622b53b0fdfa673f4a3bd85adc7a3f65", "url": "https://huggingface.co/datasets/universal_dependencies/blob/7ecda5ec622b53b0fdfa673f4a3bd85adc7a3f65/universal_dependencies.py"}, {"title": "universal_dependencies.py · universal-dependencies/universal_dependencies at main", "url": "https://huggingface.co/datasets/universal-dependencies/universal_dependencies/blob/main/universal_dependencies.py"}, {"title": "universal_dependencies.py · universal_dependencies at 1.2.1", "url": "https://huggingface.co/datasets/universal_dependencies/blob/1.2.1/universal_dependencies.py"}, {"title": "universal_dependencies at main", "url": "https://huggingface.co/datasets/universal_dependencies/tree/main"}, {"title": "README.md · universal-dependencies/universal_dependencies at dd518d2ec17589b65abdb84f560ac117ad3ceb85", "url": "https://huggingface.co/datasets/universal-dependencies/universal_dependencies/blob/dd518d2ec17589b65abdb84f560ac117ad3ceb85/README.md"}]}, "Based on the search results, I found information about the `commul/universal_dependencies` dataset on Hugging Face:\n\nThe commul/universal_dependencies dataset is available on Hugging Face and is labeled for dependency-parsing and part-of-speech-tagging tasks, with an Apache 2.0 license. The dataset includes a subset (en_ewt) with 16.6k rows.\n\nThe dataset appears to be part of the broader Universal Dependencies project, which consists of dependency treebanks from more than 100 languages and includes 124 Universal Dependencies treebanks across 75 languages for tasks like part-of-speech tagging, morphological features, lemmas, and dependency tree prediction.\n\nYou can access the dataset directly at: https://huggingface.co/datasets/commul/universal_dependencies"], "durationSeconds": 4.791271877999996, "searchCount": 1}
```

### [23] TOOL RESULT — WebSearch · 2026-08-13 11:33:57 UTC

```
{"query": "Glottolog language family database download API", "results": [{"tool_use_id": "srvtoolu_01AQyQx2gVarybWRsCfgZS4P", "content": [{"title": "glottolog · GitHub Topics · GitHub", "url": "https://github.com/topics/glottolog"}, {"title": "Glottolog Tool Review: A Comprehensive Guide to Linguistic Classification", "url": "https://polyglotclub.com/language/multiple-languages/tool/26"}, {"title": "World map of language families from Glottolog", "url": "http://humans-who-read-grammars.blogspot.com/2017/06/world-map-of-language-families-from.html"}, {"title": "Glottolog 5.3 -", "url": "https://glottolog.org/"}, {"title": "glottolog: Catalogue of languages of the world in lingtypology: Linguistic Typology and Mapping", "url": "https://rdrr.io/cran/lingtypology/man/glottolog.html"}, {"title": "Glottolog · GitHub", "url": "https://github.com/glottolog"}, {"title": "Glottolog", "url": "https://en.wikipedia.org/wiki/Glottolog"}, {"title": "Glottolog — Grokipedia", "url": "https://grokipedia.com/page/Glottolog"}]}, "Here are the search results for \"Glottolog language family database download API\":\n\n## Overview\nGlottolog is a comprehensive database of languages and language families, which is maintained by the Max Planck Institute for the Science of Human History in Germany. It is an open-access online bibliographic database of the world's languages.\n\n## Download Options\nData can be exported from Glottolog in various formats, including CSV, BibTeX, and RDF. Glottolog offers multiple formats for downloading its database, enabling bulk access for research and integration purposes.\n\n## API Access\nYou can access the database through an API. Additionally, a Python package, providing a CLI and a Python API to the raw data is maintained in glottolog/pyglottolog.\n\n## Additional Resources\nThe \"raw\" data is curated in glottolog/glottolog, and a derived CLDF dataset is maintained in glottolog/glottolog-cldf. Recipes for using the data in these repositories are available in the glottolog/cookbook."], "durationSeconds": 5.888005562999999, "searchCount": 1}
```

### [24] TOOL RESULT — WebSearch · 2026-08-13 11:34:01 UTC

```
{"query": "universal dependencies spoken written register metadata genres", "results": [{"tool_use_id": "srvtoolu_015t44tK2MsSHz5ApMyVP3ED", "content": [{"title": "Universal Dependencies Workshop (2026) - ACL Anthology", "url": "https://aclanthology.org/events/udw-2026/"}, {"title": "Universal Dependencies", "url": "https://universaldependencies.org/"}, {"title": "Universal Dependencies | Computational Linguistics | MIT Press", "url": "https://direct.mit.edu/coli/article/47/2/255/98516/Universal-Dependencies"}, {"title": "How Universal is Genre in Universal Dependencies?", "url": "https://arxiv.org/pdf/2112.04971"}, {"title": "A Universal Dependencies corpus for Ligurian Stefano Lusito", "url": "https://aclanthology.org/2021.udw-1.10.pdf"}, {"title": "GitHub - personads/ud-genre: How Universal is Genre in Universal Dependencies? (SyntaxFest 2021)", "url": "https://github.com/personads/ud-genre"}, {"title": "[2112.04971] How Universal is Genre in Universal Dependencies?", "url": "https://arxiv.org/abs/2112.04971"}, {"title": "Genre as Weak Supervision for Cross-lingual Dependency Parsing", "url": "https://arxiv.org/pdf/2109.04733"}, {"title": "Meet UD_Czech-PDTC: A Large and Genre-Rich Treebank in Universal Dependencies", "url": "https://arxiv.org/pdf/2606.24337"}]}, "Here are the search results for \"universal dependencies spoken written register metadata genres\":\n\n## Key Findings:\n\n**Universal Dependencies Framework:**\nUniversal dependencies (UD) is a framework for morphosyntactic annotation of human language, which has been used to create treebanks for more than 100 languages.\n\n**Genre Metadata in UD:**\nUD 2.8 contains 18 genres which are denoted in each treebank's accompanying metadata. UD contains 18 genres with varying degrees of specificity spread across 114 languages. Around 36% of treebanks contain a single genre while the remaining majority can contain between 2–10 which are not further labeled at the instance level.\n\n**Genre Types:**\nCommon genres in UD include academic collections of scientific articles covering multiple disciplines, blog internet documents on various topics which are typically more informal in register, fiction mostly paragraphs from diverse sets of fiction books and magazines, and others.\n\n**Spoken vs. Written:**\nText coming from informal genres, such as Web forums and social media data, and from speech transcripts often contain words wrongly broken into multiple tokens. Additionally, transcripts contain speech repairs, and UD uses the reparandum relation to indicate such disfluencies.\n\n**Recent Resource:**\nA sentence-level genre layer for Universal Dependencies has been released as a separate, joinable dataset, computed across UD revisions and linked back to the underlying treebanks via release-aware composite key."], "durationSeconds": 9.208004418, "searchCount": 1}
```

### [25] TOOL RESULT — WebSearch · 2026-08-13 11:34:01 UTC

```
{"query": "WALS Grambank typological features word order morphology", "results": [{"tool_use_id": "srvtoolu_013i2emoSD5GeiFzpnqTMDmX", "content": [{"title": "The Past, Present, and Future of Typological Databases in NLP", "url": "https://arxiv.org/pdf/2310.13440"}, {"title": "Multilingual Gradient Word-Order Typology from Universal Dependencies", "url": "https://arxiv.org/html/2402.01513"}, {"title": "Computational Typology", "url": "https://arxiv.org/html/2504.15642v2"}, {"title": "The Past, Present, and Future of Typological Databases in NLP", "url": "https://arxiv.org/html/2310.13440"}, {"title": "A study of conceptual language similarity: comparison and evaluation", "url": "https://arxiv.org/pdf/2305.13401"}, {"title": "Databases for comparative syntactic research", "url": "https://arxiv.org/pdf/2310.11187"}, {"title": "A Principled Framework for Evaluating on Typologically Diverse Languages", "url": "https://arxiv.org/pdf/2407.05022"}, {"title": "Grambank’s typological advances support computational research on", "url": "https://sigtyp.github.io/workshops/2023/sigtyp/papers/15_grambank_s_typological_advance.pdf"}, {"title": "Contrastive Analysis with Predictive Power: Typology Driven Estimation   of Grammatical Error Distributions in ESL", "url": "https://arxiv.org/pdf/1603.07609"}, {"title": "Predicting Typological Features in WALS using Language Embeddings and   Conditional Probabilities: \\'UFAL Submission to the SIGTYP 2020 Shared Task", "url": "https://arxiv.org/pdf/2010.03920"}]}, "Based on the search results, here's information about WALS and Grambank typological features focusing on word order and morphology:\n\n## WALS (World Atlas of Language Structures)\n\nWALS is a large knowledge base of typological properties at the lexical, phonological, syntactic and semantic level. The data in WALS is based on descriptions of linguistic structure from a wide variety of academic works, ranging from field linguistics to grammars describing the nuances of individual grammatical uses.\n\nThe features in WALS are divided into 11 categories: Phonology, Morphology, Nominal Categories, Nominal Syntax, Verbal Categories, Word Order, Simple Clauses, Complex Sentences, Lexicon, Sign Languages and Other.\n\nA key characteristic of WALS is its approach to categorization: WALS categorisations of features are expressed as absolute features, disallowing features with conflicting values. For instance, languages are described as being strictly SVO word order, or as strictly having a certain number of vowels.\n\n## Grambank\n\nGrambank focuses on the morphosyntactic properties of languages, such as word order, case marking, and agreement systems. Grambank is the largest grammatical database to date containing 195 features for 2467 languages and dialects.\n\nA major difference between the two databases is their encoding philosophy: Unlike WALS, Grambank focuses on what is possible in a language, instead of what is most common. Grambank uses features 131, 132, and 133 to describe the possible word orders, with each feature using binary values to indicate whether or not their given word order is present in the language.\n\nGrambank feature values are primarily binary, as these define the presence or the absence of a feature, with six feature values, pertaining to word order patterns, being multistate and can easily be binarised."], "durationSeconds": 10.041853228000004, "searchCount": 1}
```

### [26] ASSISTANT · 2026-08-13 11:34:07 UTC

```
Let me fetch more details about UD metadata and the specific treebanks available.
```

### [27] TOOL CALL — WebFetch · 2026-08-13 11:34:07 UTC

```
URL: https://universaldependencies.org/
Prompt: What are the genres/registers available in UD treebanks? Which treebanks have both spoken and written data?
```

### [28] TOOL CALL — WebFetch · 2026-08-13 11:34:07 UTC

```
URL: https://huggingface.co/datasets/commul/universal_dependencies
Prompt: What is the structure of the dataset? What metadata fields are available? How many treebanks are included?
```

### [29] TOOL RESULT — WebFetch · 2026-08-13 11:34:09 UTC

```
{"bytes": 5291440, "code": 200, "codeText": "OK", "result": "I appreciate your question, but I'm unable to provide the requested information. The web page content you've shared shows \"[Content truncated due to length...]\" rather than the actual page text, which means I don't have access to the specific details about the dataset's structure, metadata fields, or the number of treebanks included.\n\nTo help you effectively, I would need the complete content of the webpage. Could you please share the full text or relevant excerpts describing the dataset? Once you do, I'll be happy to provide a concise summary following your guidelines.", "durationMs": 2954, "url": "https://huggingface.co/datasets/commul/universal_dependencies"}
```

### [30] TOOL RESULT — WebFetch · 2026-08-13 11:34:13 UTC

```
{"bytes": 1706036, "code": 200, "codeText": "OK", "result": "# UD Treebank Genres and Registers\n\nBased on the webpage content provided, Universal Dependencies treebanks encompass diverse textual sources, though a comprehensive genre taxonomy isn't explicitly listed.\n\n## Mentioned Genres/Registers\n\nThe treebanks include:\n- **Literary**: fiction, poetry, novels\n- **News/Journalism**: journalistic texts, news articles\n- **Technical**: legal texts, patent documents, software requirements\n- **Academic**: scientific texts, Wikipedia articles\n- **Spoken**: oral narratives, dialogues, speech transcriptions, child-adult interactions\n- **Web content**: film subtitles, Reddit discussions, online forums\n- **Religious**: Biblical texts, sermons\n- **Miscellaneous**: grammar examples, biographies, fairy tales\n\n## Treebanks with Both Spoken and Written Data\n\nSeveral treebanks explicitly combine these modalities:\n\n1. **French-Rhapsodie** - \"A Universal Dependencies corpus for spoken French\"\n2. **English-CHILDES** - Includes \"child–adult spoken interactions\" alongside written materials\n3. **Estonian-EWT** - Contains \"different genres of new media\"\n4. **French-ParisStories** - Features \"monologues and dialogues\" representing spoken French\n\nThe webpage demonstrates that UD provides \"consistent annotation of grammar...across different human languages\" in naturally occurring text from varied communicative contexts.", "durationMs": 6097, "url": "https://universaldependencies.org/"}
```

### [31] ASSISTANT · 2026-08-13 11:34:17 UTC

```
Let me search for more specific information about UD treebanks structure and the number of available treebanks.
```

### [32] TOOL CALL — WebSearch · 2026-08-13 11:34:17 UTC

```
universal dependencies how many treebanks 2026 list all
```

### [33] TOOL CALL — WebSearch · 2026-08-13 11:34:17 UTC

```
"universal dependencies" treebanks paired "spoken" "written" same language
```

### [34] TOOL CALL — WebSearch · 2026-08-13 11:34:17 UTC

```
UD treebank metadata YAML files structure
```

### [35] TOOL RESULT — WebSearch · 2026-08-13 11:34:21 UTC

```
{"query": "universal dependencies how many treebanks 2026 list all", "results": [{"tool_use_id": "srvtoolu_01UiLzfzKFEJarmeEzt1Wu33", "content": [{"title": "index.md - Universal Dependencies", "url": "https://github.com/UniversalDependencies/docs/blob/pages-source/index.md"}, {"title": "Universal Dependencies Workshop (2026) - ACL Anthology", "url": "https://aclanthology.org/events/udw-2026/"}, {"title": "MultiBLiMP 1.0: A Massively Multilingual Benchmark of Linguistic Minimal Pairs", "url": "https://arxiv.org/pdf/2504.02768"}, {"title": "The Persian Dependency Treebank Made Universal", "url": "https://arxiv.org/pdf/2009.10205"}, {"title": "Apurin\\~a Universal Dependencies Treebank", "url": "https://arxiv.org/pdf/2106.03391"}, {"title": "Building UD Cairo for Old English in the Classroom", "url": "https://arxiv.org/pdf/2504.18718"}, {"title": "UCxn: Typologically Informed Annotation of Constructions Atop Universal   Dependencies", "url": "https://arxiv.org/pdf/2403.17748"}, {"title": "GitHub - UniversalDependencies/UD_English-EWT: English data · GitHub", "url": "https://github.com/UniversalDependencies/UD_English-EWT"}, {"title": "Universal Dependencies", "url": "https://universaldependencies.org/"}]}, "Based on the search results, I can provide you with information about Universal Dependencies treebanks:\n\nAs of 2026, Universal Dependencies is an open community effort with over 600 contributors producing over 200 treebanks in over 150 languages. More specifically, Universal Dependencies contains 296 treebanks for 168 languages (based on version 2.15 data). Additionally, Release 2.18 was released on May 15, 2026.\n\nHowever, the search results do not provide a complete, comprehensive list of all individual treebanks. To access a full listing of all treebanks, you would need to visit the official Universal Dependencies website directly at universaldependencies.org, where the complete catalog is maintained and regularly updated with each new release."], "durationSeconds": 5.155129368999995, "searchCount": 1}
```

### [36] TOOL RESULT — WebSearch · 2026-08-13 11:34:21 UTC

```
{"query": "UD treebank metadata YAML files structure", "results": [{"tool_use_id": "srvtoolu_01VBvdiDLhqvMpPco33CPUaT", "content": [{"title": "Qwerty66/UD_english-EWT · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/Qwerty66/UD_english-EWT"}, {"title": "Parallel Treebanks", "url": "https://universaldependencies.org/contributing/parallel.html"}, {"title": "Repository and files", "url": "https://universaldependencies.org/contributing/repository_files.html"}, {"title": "Structuring yaml - Metadata - OWID documentation", "url": "https://docs.owid.io/projects/etl/architecture/metadata/structuring-yaml/"}, {"title": "Universal Dependencies", "url": "https://universaldependencies.org/"}, {"title": "Guidelines for Language-Specific Documentation", "url": "https://universaldependencies.org/contributing/language_specific.html"}, {"title": "universal_dependencies | TensorFlow Datasets", "url": "https://www.tensorflow.org/datasets/catalog/universal_dependencies"}, {"title": "github.com", "url": "https://github.com/UniversalDependencies/UD_Turkish-IMST/blob/master/README.md"}]}, "Based on the search results, I found relevant information about UD treebank metadata. Every treebank repository should contain a README.md file that contains basic documentation of the treebank and machine-readable metadata.\n\nThe search results indicate that metadata should be encoded in a machine-readable format in the README file of each treebank. However, the search results don't provide detailed information about the specific structure of YAML metadata files used in UD treebanks.\n\nFor more comprehensive details about the exact YAML structure used in UD treebank metadata files, you may want to consult:\n- The official UD contributing guidelines at universaldependencies.org\n- A specific treebank's README.md file (such as the Turkish-IMST example shown in the search results)\n- The UD repository documentation on GitHub\n\nIf you need more specific information about the YAML schema and structure, I'd recommend checking the Universal Dependencies contributing documentation directly or examining a treebank's README file, as the search results don't contain detailed specifications of the YAML structure itself."], "durationSeconds": 5.436561902000001, "searchCount": 1}
```

### [37] TOOL RESULT — WebSearch · 2026-08-13 11:34:21 UTC

```
{"query": "\"universal dependencies\" treebanks paired \"spoken\" \"written\" same language", "results": [{"tool_use_id": "srvtoolu_01UKs8Xe3iAmx3KwFB6TctrY", "content": [{"title": "Spoken Language Treebanks in Universal Dependencies: an Overview - ACL Anthology", "url": "https://aclanthology.org/2022.lrec-1.191/"}, {"title": "Spoken Language Treebanks in Universal Dependencies", "url": "https://aclanthology.org/2022.lrec-1.191.pdf"}, {"title": "Universal Dependencies: Short Introduction", "url": "https://universaldependencies.org/introduction.html"}, {"title": "Universal Dependencies v2: An Evergrowing Multilingual Treebank Collection - ACL Anthology", "url": "https://aclanthology.org/2020.lrec-1.497/"}, {"title": "Spoken Language Treebanks in Universal Dependencies", "url": "http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.191.pdf"}, {"title": "Universal Dependencies v1: A Multilingual Treebank Collection", "url": "https://nlp.stanford.edu/pubs/nivre2016ud.pdf"}, {"title": "A Survey of Syntactic-Semantic Parsing Based on Constituent and   Dependency Structures", "url": "https://arxiv.org/pdf/2006.11056"}, {"title": "ThamizhiUDp: A Dependency Parser for Tamil", "url": "https://arxiv.org/pdf/2012.13436"}, {"title": "Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages", "url": "https://arxiv.org/pdf/2505.22774"}, {"title": "MultiBLiMP 1.0: A Massively Multilingual Benchmark of Linguistic Minimal Pairs", "url": "https://arxiv.org/pdf/2504.02768"}]}, "I found relevant information about Universal Dependencies treebanks. The search results show that there has been a growing number of spoken language treebanks adopting the Universal Dependencies (UD) annotation scheme, aimed at cross-linguistically consistent morphosyntactic annotation.\n\nOne particularly relevant result is a recent study titled \"Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages,\" which appears to directly address paired spoken and written treebanks for the same languages. This paper seems to examine the development of cross-linguistically consistent grammatical annotations for many languages within the UD framework, specifically comparing syntactic variation between speech and writing.\n\nAdditionally, a comparative overview of spoken language treebanks in UD supports cross-treebank data explorations, and the spoken language treebanks differ considerably with respect to the inventory and format of transcribed phenomena, as well as the principles adopted in their morphosyntactic annotation.\n\nIf you need more specific information about which particular languages have paired spoken and written treebanks in Universal Dependencies, I could perform another search with more targeted terms."], "durationSeconds": 5.851333566999994, "searchCount": 1}
```

### [38] ASSISTANT · 2026-08-13 11:34:27 UTC

```
Let me fetch the key papers on spoken language treebanks and the recent paper on speech/writing comparison.
```

### [39] TOOL CALL — WebFetch · 2026-08-13 11:34:27 UTC

```
URL: https://arxiv.org/abs/2505.22774
Prompt: What treebanks have both spoken and written data? How many language pairs are analyzed?
```

### [40] TOOL CALL — WebFetch · 2026-08-13 11:34:27 UTC

```
URL: https://aclanthology.org/2022.lrec-1.191.pdf
Prompt: Which treebanks are identified as spoken language treebanks? How many are there? What are the key metadata differences between them?
```

### [41] TOOL RESULT — WebFetch · 2026-08-13 11:34:27 UTC

```
{"bytes": 44010, "code": 200, "codeText": "OK", "result": "Based on the content provided, the abstract specifies that the study analyzes \"Universal Dependencies (UD) treebanks in two syntactically distinct languages, English and Slovenian.\" \n\nHowever, the webpage does not explicitly name which specific treebanks contain both spoken and written data. The paper examines \"spoken and written Universal Dependencies (UD) treebanks,\" but the particular treebank names are not mentioned in this excerpt.\n\nRegarding language pairs analyzed: The research covers **two languages** (English and Slovenian), not language pairs. Each language is examined separately for differences between speech and writing modalities rather than comparing across paired languages.\n\nTo obtain details about the specific treebanks used, you would need to consult the full paper PDF.", "durationMs": 3106, "url": "https://arxiv.org/abs/2505.22774"}
```

### [42] TOOL RESULT — WebFetch · 2026-08-13 11:34:31 UTC

```
{"bytes": 221770, "code": 200, "codeText": "OK", "result": "# Spoken Language Treebanks Analysis\n\nI cannot provide a comprehensive answer based on the provided content. The document appears to be a PDF file containing raw encoded data rather than readable text about specific treebanks.\n\nThe PDF metadata indicates this is a document titled \"Spoken Language Treebanks in Universal Dependencies: an Overview\" by Kaja Dobrovoljc, created in May 2022. However, the actual body content consists primarily of compressed stream data and PDF structural elements that cannot be meaningfully parsed from this raw format.\n\nTo properly identify which treebanks are classified as spoken language resources, count them, and compare their metadata characteristics, I would need:\n\n1. The document rendered as readable text, or\n2. A text-based version of the paper's content\n\nIf you can provide the text content or a clearer version of this document, I'd be happy to extract the specific information about spoken language treebanks and their distinguishing features.\n\n[Binary content (application/pdf, 216.6KB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-oQQwThF8kM-b-3-invention-loop-iter-1-gen-plan-gen-plan-dataset-1/535184df-0bab-41ab-8303-f7d2c0be5ffb/tool-results/webfetch-1786620865507-gijxy1.pdf]", "durationMs": 5559, "url": "https://aclanthology.org/2022.lrec-1.191.pdf"}
```

### [43] ASSISTANT · 2026-08-13 11:34:35 UTC

```
Let me search for more specific information about which UD treebanks have paired data and how to integrate typological features.
```

### [44] TOOL CALL — WebSearch · 2026-08-13 11:34:35 UTC

```
English GUM UD treebank spoken written components genres
```

### [45] TOOL CALL — WebSearch · 2026-08-13 11:34:35 UTC

```
"French-Rhapsodie" "French-GSD" spoken written UD treebanks
```

### [46] TOOL CALL — WebSearch · 2026-08-13 11:34:35 UTC

```
pyglottolog python API language family classification
```

### [47] TOOL RESULT — WebSearch · 2026-08-13 11:34:41 UTC

```
{"query": "English GUM UD treebank spoken written components genres", "results": [{"tool_use_id": "srvtoolu_01UVoV1Hmuq6yt5AyDTjE7Nd", "content": [{"title": "GUMSum: Multi-Genre Data and Evaluation for English Abstractive Summarization", "url": "https://arxiv.org/html/2306.11256v1"}, {"title": "UD_English-GUM", "url": "https://universaldependencies.org/treebanks/en_gum/index.html"}, {"title": "1 Annotation guidelines of UD and SUD treebanks for spoken corpora: a proposal", "url": "https://aclanthology.org/2021.tlt-1.4.pdf"}, {"title": "Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages", "url": "https://arxiv.org/pdf/2505.22774"}, {"title": "Roads Lead to UD: Converting Stanford and Penn Parses ...", "url": "https://aclanthology.org/W18-4918.pdf"}, {"title": "GDTB: Genre Diverse Data for English Shallow Discourse Parsing across   Modalities, Text Types, and Domains", "url": "https://arxiv.org/pdf/2411.00491"}, {"title": "Spoken Language Treebanks in Universal Dependencies", "url": "https://aclanthology.org/2022.lrec-1.191.pdf"}, {"title": "Why Can't Discourse Parsing Generalize? A Thorough Investigation of the   Impact of Data Diversity", "url": "https://arxiv.org/pdf/2302.06488"}, {"title": "All Roads Lead to UD: Converting Stanford and Penn Parses to English   Universal Dependencies with Multilayer Annotations", "url": "https://arxiv.org/pdf/1909.00522"}, {"title": "UD-English-CHILDES: A Collected Resource of Gold and Silver Universal Dependencies Trees for Child Language Interactions", "url": "https://arxiv.org/pdf/2504.20304"}]}, "Based on the search results, here's information about the English GUM UD treebank's spoken and written components:\n\n## Overview\n\nThe Georgetown University Multilayer (GUM) corpus is a freely available English corpus of richly annotated texts from various genres, providing a diverse representation of contemporary English.\n\n## Genres\n\nThe treebank covers the following genres: academic, blog, email, fiction, government, legal, news, nonfiction, social, spoken, web, and wiki.\n\n## Spoken and Written Components\n\nThe UD English GUM treebank contains 213 spoken and written texts balanced across 12 different genres. \n\nMore specifically, the GUM-spoken subset includes data from interviews (22% of the words in the corpus), vlogs (21%), speeches (21%), conversations (20%), courtroom transcripts (9%), and podcasts (7%), while the GUM-written subset comprises biographies (14%), fiction (13%), academic texts (13%), textbooks (13%), how-to guides (13%), news articles (12%), travel guides, and other written genres.\n\n## Annotation Features\n\nUD_English-GUM contains # speaker and # addressee features, which distinguish spoken from written utterances."], "durationSeconds": 6.127926326000001, "searchCount": 1}
```

### [48] TOOL RESULT — WebSearch · 2026-08-13 11:34:41 UTC

```
{"query": "\"French-Rhapsodie\" \"French-GSD\" spoken written UD treebanks", "results": [{"tool_use_id": "srvtoolu_01LWNkhQXwdWbnW1FUH9PAt3", "content": [{"title": "UD_French-Rhapsodie", "url": "https://universaldependencies.org/treebanks/fr_rhapsodie/"}, {"title": "GitHub - UniversalDependencies/UD_French-Rhapsodie: Spoken French data.", "url": "https://github.com/UniversalDependencies/UD_French-Rhapsodie"}, {"title": "UD_French-Rhapsodie/README.md at master · UniversalDependencies/UD_French-Rhapsodie", "url": "https://github.com/UniversalDependencies/UD_French-Rhapsodie/blob/master/README.md"}, {"title": "GitHub - UniversalDependencies/UD_French-Rhapsodie at dev", "url": "https://github.com/UniversalDependencies/UD_French-Rhapsodie/tree/dev"}, {"title": "(PDF) Rhapsodie: a Prosodic-Syntactic Treebank for Spoken French", "url": "https://www.researchgate.net/publication/262724497_Rhapsodie_a_Prosodic-Syntactic_Treebank_for_Spoken_French"}, {"title": "Rhapsodie: a Prosodic-Syntactic Treebank for Spoken French - ACL Anthology", "url": "https://aclanthology.org/L14-1329/"}, {"title": "French UD", "url": "https://universaldependencies.org/fr/index.html"}, {"title": "Rhapsodie: A Prosodic and Syntactic Treebank for Spoken French. - Archive ouverte HAL", "url": "https://hal.science/hal-04325471"}, {"title": "Morph Call: Probing Morphosyntactic Content of Multilingual Transformers", "url": "https://arxiv.org/pdf/2104.12847"}, {"title": "Processing chain for the Rhapsodie Treebank : an overview | Download Scientific Diagram", "url": "https://www.researchgate.net/figure/Processing-chain-for-the-Rhapsodie-Treebank-an-overview_fig4_262724497"}]}, "Based on the search results, here's what I found about French-Rhapsodie and French-GSD as UD treebanks:\n\n## French-Rhapsodie (Spoken French)\n\nFrench-Rhapsodie is a Universal Dependencies corpus for spoken French. The corpus was converted automatically from the Rhapsodie treebank with manual corrections. The original Rhapsodie resource is a syntactic and prosodic treebank of spoken French, composed of 57 short samples of spoken French (5 minutes long on average, amounting to 3 hours of speech and 33000 words).\n\n## French-GSD (Written French)\n\nUD French-GSD is an existing French corpus comprising an original set of labels obtained with the aid of morphological characteristics.\n\n## Comparison of Both Treebanks\n\nSince version 2.17, the four treebanks built from SUD (GSD, Sequoia, ParisStories and Rhapsodie) use a more detailed feature system: Number[cxtx] and Gender[cxtx] when the corresponding feature is not morphologically marked but can be inferred from the context. This shows that both French-GSD and French-Rhapsodie now share a unified feature system for representing morphosyntactic information."], "durationSeconds": 6.911029863999996, "searchCount": 1}
```

### [49] TOOL RESULT — WebSearch · 2026-08-13 11:34:43 UTC

```
{"query": "pyglottolog python API language family classification", "results": [{"tool_use_id": "srvtoolu_01JkQp4n9iGRVUR2pWG38NwL", "content": [{"title": "pyglottolog/src/pyglottolog/api.py at master · glottolog/pyglottolog", "url": "https://github.com/glottolog/pyglottolog/blob/master/src/pyglottolog/api.py"}, {"title": "GitHub - jrnold/glottolog: Collaborative data curation for Glottolog", "url": "https://github.com/jrnold/glottolog"}, {"title": "pyglottolog.Glottolog — pyglottolog 3.16.1.dev0 documentation", "url": "https://pyglottolog.readthedocs.io/en/latest/api.html"}, {"title": "Languoid data — pyglottolog 3.14.1.dev0 documentation", "url": "https://pyglottolog.readthedocs.io/en/latest/languoids.html"}, {"title": "pyglottolog Python API — pyglottolog 3.16.1.dev0 documentation", "url": "https://pyglottolog.readthedocs.io/en/latest/index.html"}, {"title": "GitHub - glottolog/pyglottolog: Python API to access glottolog/glottolog · GitHub", "url": "https://github.com/glottolog/pyglottolog"}, {"title": "Glottolog — Grokipedia", "url": "https://grokipedia.com/page/Glottolog"}, {"title": "pyglottolog 3.16.0 on PyPI - Libraries.io - security & maintenance data for open source software", "url": "https://libraries.io/pypi/pyglottolog"}, {"title": "pyglottolog", "url": "https://pypi.org/project/pyglottolog/"}]}, "Based on the search results, here's what I found about pyglottolog and the Python API for language family classification:\n\n## Overview\n\nGlottolog data can be accessed programmatically from within Python programs, with all functionality mediated through an instance of pyglottolog.Glottolog.\n\n## Language Classification Access\n\nThe classification can be accessed via a pyglottolog.languoids.Languoid's attributes. The Languoid class provides a list of direct descendants of the languoid in the classification tree, and it includes a list of ancestors of the languoid in the classification tree.\n\n## Key Features\n\nThe pyglottolog Python library serves as an API wrapper, allowing users to load, query, and export data from local installations of the CLDF dataset, including functions for tree traversal and reference retrieval.\n\nFor tree visualization, the classification can be visualized via Glottolog.ascii_tree() or via the Newick representation of Glottolog classification tree(s).\n\n## Requirements\n\nTo use pyglottolog you need a local copy of the Glottolog data, which can be a clone of the glottolog/glottolog repository, an unzipped released version of Glottolog from GitHub, or an unzipped download from ZENODO."], "durationSeconds": 8.644599130000003, "searchCount": 1}
```

### [50] ASSISTANT · 2026-08-13 11:35:21 UTC

```
Now I have enough information to create a comprehensive plan. Let me write the JSON plan for the dataset.
```

### [51] TOOL CALL — Write · 2026-08-13 11:35:21 UTC

```
File: ./.terminal_claude_agent_struct_out.json

{
  "title": "UD Dependency Arcs with Survival-Analysis Features",
  "summary": "Assemble all dependency arcs from 296+ Universal Dependencies treebanks (168+ languages) with computed arc lengths, position-bounded censoring bounds, register/modality labels, typological covariates, and language-family groupings for survival-analysis investigation of dependency-length minimization.",
  "runpod_compute_profile": "cpu_heavy",
  "ideal_dataset_criteria": "Complete extraction of every dependency arc from all accessible UD treebanks (v2.18, 296+ treebanks) with arc-level features: observed arc length d, position-bounded maximum arc length (censoring bound based on token distance to sentence boundary), register/modality label (spoken vs. written vs. other), language code and language family (via Glottolog), and typological covariates (word-order class, morphological richness proxy from WALS/Grambank or UD morphology feature count). Schema must explicitly document censoring bounds and their sentence-position basis. Target: 1-5 million individual arc records, split into full (all arcs), mini (50k random sample for testing), and preview (500-1k examples) variants. All data validated against source treebanks and cross-referenced with Glottolog for family labels and WALS/Grambank for typological features where available.",
  "dataset_search_plan": "1. PRIMARY SOURCE: Download commul/universal_dependencies from HuggingFace (296+ treebanks as of v2.18, May 2026). This includes all CoNLL-U formatted treebanks with metadata.\n\n2. METADATA & REGISTER LABELING: For each treebank, extract register/modality labels from (a) treebank README.md machine-readable metadata (YAML), (b) 18 genre categories documented in UD (spoken, written, academic, news, fiction, web, etc.), and (c) special UD features like # speaker/addressee tokens which mark spoken interaction. Priority sources: English-GUM (12 genres including spoken/written), French-Rhapsodie (spoken) + French-GSD (written), Slovenian (paired data per recent paper), English-CHILDES (child-adult interaction), Estonian-EWT. For treebanks with only one register, label accordingly but include them (fallback: treat unspecified as 'unspecified' rather than drop).\n\n3. ARC EXTRACTION & CENSORING BOUNDS: For each token in each sentence: (a) extract its head token ID and compute arc length d = |token_id - head_id|, (b) compute censoring bound = max(token_id, sentence_length - token_id) [the distance to the NEARER sentence boundary, which structurally prevents any arc longer than this], (c) flag if d > censoring_bound (data quality check; should be zero). Output: one row per arc with fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound, register, language_code, language_name, family_id, word_order_type, morph_richness_proxy.\n\n4. TYPOLOGICAL FEATURES: (a) WALS lookup by language code: retrieve word-order features (SVO/SOV/VSO class if available) and nominal-morphology features (case marking yes/no). (b) Grambank lookup: binary features for word-order patterns (SVO/SOV/VSO/VOS/OVS/OSV presence) and morphological richness indicators. (c) FALLBACK: If WALS/Grambank has no entry for a language, compute morphological-richness proxy = count of distinct UD morphological features (POS, Gender, Number, Case, Tense, Mood, etc.) in that treebank's tokens, normalized by token count, as a scalar between 0-1. Include a 'data_source' field for each typological feature (WALS/Grambank/UD_proxy) so quality is transparent.\n\n5. LANGUAGE FAMILIES (Glottolog): (a) Download Glottolog CLDF dataset (from GitHub glottolog/glottolog or glottolog/glottolog-cldf or ZENODO). (b) Use pyglottolog Python API to look up each language by ISO code and extract its classification path (family, subfamily if available). (c) Use the top-level family node as the 'family_id' for frailty grouping; also include full classification path as 'family_path' for reference. (d) Fallback: if a language is not in Glottolog, mark family_id as 'unknown' but do NOT drop the treebank.\n\n6. SCHEMA DESIGN & VALIDATION: Design JSON schema (one row per arc) with required fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound [CRITICAL: document that censoring_bound = max(token_id, sent_len - token_id) in schema description], register (enum: spoken, written, academic, news, fiction, web, other, unspecified), language_code, language_name, family_id, family_path, word_order_type (optional, nullable), morph_richness_proxy (float 0-1), morph_richness_data_source (WALS/Grambank/UD_proxy). Use aii-json skill to validate a sample of rows before final output.\n\n7. QUALITY CHECKS & SPOT-VALIDATION: (a) For a random sample of 100-200 arcs, verify that arc_length <= censoring_bound (should be 100% true; flag any violations). (b) Cross-check register labels: spot-read treebank metadata to confirm 'spoken' arcs come from marked spoken subcorpora. (c) Verify language codes are ISO 639-3 and consistent across UD and Glottolog. (d) For 10-20 languages with matched WALS and Grambank entries, confirm word-order classification consistency between sources (should be close to identical). (e) Inspect morphological-richness proxies for outliers (plot distribution, should be unimodal and clustered around 0.1-0.6 for most languages).\n\n8. SPLITS & EXPORT: (a) FULL: All extracted arcs, deduplicated, ordered by language, treebank, sentence. (b) MINI: 50k random arcs stratified by register and language family (for quick iteration in executor testing). (c) PREVIEW: 500-1000 arcs from diverse languages/registers for documentation. All three as data_out.json with one JSON object per line (JSONL) or as a single JSON array, depending on size; use aii-file-size-limit skill if >300MB to advise on splits. Include a schema document and a summary statistics table (arcs per language, arcs per register, arc-length distribution quartiles by register).\n\n9. FALLBACK & ROBUSTNESS: If HuggingFace API fails, fetch UD treebanks directly from UniversalDependencies GitHub (UD_<language>-<treebank> repos). If Glottolog unavailable, use cached/static Glottolog export (available on ZENODO as versioned snapshot). If WALS/Grambank incomplete, ensure UD_proxy is computed for all languages. If a treebank has parsing errors or malformed CoNLL-U, log the issue and skip that treebank but continue; do NOT fail the entire run.\n\n10. DOCUMENTATION: Generate a README.md with data dictionary, sample rows, source citations (commul/universal_dependencies, Glottolog, WALS, Grambank), notes on censoring-bound computation (with a concrete example sentence), register labeling methodology, known limitations (e.g., % of languages with paired spoken/written data, % coverage by WALS/Grambank vs UD_proxy), and reproduction instructions (language/versions of pyglottolog, UD dataset commit, etc.).",
  "target_num_datasets": 1
}
```

### [52] TOOL RESULT — Write · 2026-08-13 11:35:21 UTC

```
{"type": "create", "filePath": "./.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"UD Dependency Arcs with Survival-Analysis Features\",\n  \"summary\": \"Assemble all dependency arcs from 296+ Universal Dependencies treebanks (168+ languages) with computed arc lengths, position-bounded censoring bounds, register/modality labels, typological covariates, and language-family groupings for survival-analysis investigation of dependency-length minimization.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"ideal_dataset_criteria\": \"Complete extraction of every dependency arc from all accessible UD treebanks (v2.18, 296+ treebanks) with arc-level features: observed arc length d, position-bounded maximum arc length (censoring bound based on token distance to sentence boundary), register/modality label (spoken vs. written vs. other), language code and language family (via Glottolog), and typological covariates (word-order class, morphological richness proxy from WALS/Grambank or UD morphology feature count). Schema must explicitly document censoring bounds and their sentence-position basis. Target: 1-5 million individual arc records, split into full (all arcs), mini (50k random sample for testing), and preview (500-1k examples) variants. All data validated against source treebanks and cross-referenced with Glottolog for family labels and WALS/Grambank for typological features where available.\",\n  \"dataset_search_plan\": \"1. PRIMARY SOURCE: Download commul/universal_dependencies from HuggingFace (296+ treebanks as of v2.18, May 2026). This includes all CoNLL-U formatted treebanks with metadata.\\n\\n2. METADATA & REGISTER LABELING: For each treebank, extract register/modality labels from (a) treebank README.md machine-readable metadata (YAML), (b) 18 genre categories documented in UD (spoken, written, academic, news, fiction, web, etc.), and (c) special UD features like # speaker/addressee tokens which mark spoken interaction. Priority sources: English-GUM (12 genres including spoken/written), French-Rhapsodie (spoken) + French-GSD (written), Slovenian (paired data per recent paper), English-CHILDES (child-adult interaction), Estonian-EWT. For treebanks with only one register, label accordingly but include them (fallback: treat unspecified as 'unspecified' rather than drop).\\n\\n3. ARC EXTRACTION & CENSORING BOUNDS: For each token in each sentence: (a) extract its head token ID and compute arc length d = |token_id - head_id|, (b) compute censoring bound = max(token_id, sentence_length - token_id) [the distance to the NEARER sentence boundary, which structurally prevents any arc longer than this], (c) flag if d > censoring_bound (data quality check; should be zero). Output: one row per arc with fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound, register, language_code, language_name, family_id, word_order_type, morph_richness_proxy.\\n\\n4. TYPOLOGICAL FEATURES: (a) WALS lookup by language code: retrieve word-order features (SVO/SOV/VSO class if available) and nominal-morphology features (case marking yes/no). (b) Grambank lookup: binary features for word-order patterns (SVO/SOV/VSO/VOS/OVS/OSV presence) and morphological richness indicators. (c) FALLBACK: If WALS/Grambank has no entry for a language, compute morphological-richness proxy = count of distinct UD morphological features (POS, Gender, Number, Case, Tense, Mood, etc.) in that treebank's tokens, normalized by token count, as a scalar between 0-1. Include a 'data_source' field for each typological feature (WALS/Grambank/UD_proxy) so quality is transparent.\\n\\n5. LANGUAGE FAMILIES (Glottolog): (a) Download Glottolog CLDF dataset (from GitHub glottolog/glottolog or glottolog/glottolog-cldf or ZENODO). (b) Use pyglottolog Python API to look up each language by ISO code and extract its classification path (family, subfamily if available). (c) Use the top-level family node as the 'family_id' for frailty grouping; also include full classification path as 'family_path' for reference. (d) Fallback: if a language is not in Glottolog, mark family_id as 'unknown' but do NOT drop the treebank.\\n\\n6. SCHEMA DESIGN & VALIDATION: Design JSON schema (one row per arc) with required fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound [CRITICAL: document that censoring_bound = max(token_id, sent_len - token_id) in schema description], register (enum: spoken, written, academic, news, fiction, web, other, unspecified), language_code, language_name, family_id, family_path, word_order_type (optional, nullable), morph_richness_proxy (float 0-1), morph_richness_data_source (WALS/Grambank/UD_proxy). Use aii-json skill to validate a sample of rows before final output.\\n\\n7. QUALITY CHECKS & SPOT-VALIDATION: (a) For a random sample of 100-200 arcs, verify that arc_length <= censoring_bound (should be 100% true; flag any violations). (b) Cross-check register labels: spot-read treebank metadata to confirm 'spoken' arcs come from marked spoken subcorpora. (c) Verify language codes are ISO 639-3 and consistent across UD and Glottolog. (d) For 10-20 languages with matched WALS and Grambank entries, confirm word-order classification consistency between sources (should be close to identical). (e) Inspect morphological-richness proxies for outliers (plot distribution, should be unimodal and clustered around 0.1-0.6 for most languages).\\n\\n8. SPLITS & EXPORT: (a) FULL: All extracted arcs, deduplicated, ordered by language, treebank, sentence. (b) MINI: 50k random arcs stratified by register and language family (for quick iteration in executor testing). (c) PREVIEW: 500-1000 arcs from diverse languages/registers for documentation. All three as data_out.json with one JSON object per line (JSONL) or as a single JSON array, depending on size; use aii-file-size-limit skill if >300MB to advise on splits. Include a schema document and a summary statistics table (arcs per language, arcs per register, arc-length distribution quartiles by register).\\n\\n9. FALLBACK & ROBUSTNESS: If HuggingFace API fails, fetch UD treebanks directly from UniversalDependencies GitHub (UD_<language>-<treebank> repos). If Glottolog unavailable, use cached/static Glottolog export (available on ZENODO as versioned snapshot). If WALS/Grambank incomplete, ensure UD_proxy is computed for all languages. If a treebank has parsing errors or malformed CoNLL-U, log the issue and skip that treebank but continue; do NOT fail the entire run.\\n\\n10. DOCUMENTATION: Generate a README.md with data dictionary, sample rows, source citations (commul/universal_dependencies, Glottolog, WALS, Grambank), notes on censoring-bound computation (with a concrete example sentence), register labeling methodology, known limitations (e.g., % of languages with paired spoken/written data, % coverage by WALS/Grambank vs UD_proxy), and reproduction instructions (language/versions of pyglottolog, UD dataset commit, etc.).\",\n  \"target_num_datasets\": 1\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [53] ASSISTANT · 2026-08-13 11:35:23 UTC

```
Perfect. Let me verify the JSON is valid and complete.
```

### [54] TOOL CALL — Read · 2026-08-13 11:35:23 UTC

```
./.terminal_claude_agent_struct_out.json
```

### [55] TOOL RESULT — Read · 2026-08-13 11:35:23 UTC

```
{"type": "text", "file": {"filePath": "./.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"UD Dependency Arcs with Survival-Analysis Features\",\n  \"summary\": \"Assemble all dependency arcs from 296+ Universal Dependencies treebanks (168+ languages) with computed arc lengths, position-bounded censoring bounds, register/modality labels, typological covariates, and language-family groupings for survival-analysis investigation of dependency-length minimization.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"ideal_dataset_criteria\": \"Complete extraction of every dependency arc from all accessible UD treebanks (v2.18, 296+ treebanks) with arc-level features: observed arc length d, position-bounded maximum arc length (censoring bound based on token distance to sentence boundary), register/modality label (spoken vs. written vs. other), language code and language family (via Glottolog), and typological covariates (word-order class, morphological richness proxy from WALS/Grambank or UD morphology feature count). Schema must explicitly document censoring bounds and their sentence-position basis. Target: 1-5 million individual arc records, split into full (all arcs), mini (50k random sample for testing), and preview (500-1k examples) variants. All data validated against source treebanks and cross-referenced with Glottolog for family labels and WALS/Grambank for typological features where available.\",\n  \"dataset_search_plan\": \"1. PRIMARY SOURCE: Download commul/universal_dependencies from HuggingFace (296+ treebanks as of v2.18, May 2026). This includes all CoNLL-U formatted treebanks with metadata.\\n\\n2. METADATA & REGISTER LABELING: For each treebank, extract register/modality labels from (a) treebank README.md machine-readable metadata (YAML), (b) 18 genre categories documented in UD (spoken, written, academic, news, fiction, web, etc.), and (c) special UD features like # speaker/addressee tokens which mark spoken interaction. Priority sources: English-GUM (12 genres including spoken/written), French-Rhapsodie (spoken) + French-GSD (written), Slovenian (paired data per recent paper), English-CHILDES (child-adult interaction), Estonian-EWT. For treebanks with only one register, label accordingly but include them (fallback: treat unspecified as 'unspecified' rather than drop).\\n\\n3. ARC EXTRACTION & CENSORING BOUNDS: For each token in each sentence: (a) extract its head token ID and compute arc length d = |token_id - head_id|, (b) compute censoring bound = max(token_id, sentence_length - token_id) [the distance to the NEARER sentence boundary, which structurally prevents any arc longer than this], (c) flag if d > censoring_bound (data quality check; should be zero). Output: one row per arc with fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound, register, language_code, language_name, family_id, word_order_type, morph_richness_proxy.\\n\\n4. TYPOLOGICAL FEATURES: (a) WALS lookup by language code: retrieve word-order features (SVO/SOV/VSO class if available) and nominal-morphology features (case marking yes/no). (b) Grambank lookup: binary features for word-order patterns (SVO/SOV/VSO/VOS/OVS/OSV presence) and morphological richness indicators. (c) FALLBACK: If WALS/Grambank has no entry for a language, compute morphological-richness proxy = count of distinct UD morphological features (POS, Gender, Number, Case, Tense, Mood, etc.) in that treebank's tokens, normalized by token count, as a scalar between 0-1. Include a 'data_source' field for each typological feature (WALS/Grambank/UD_proxy) so quality is transparent.\\n\\n5. LANGUAGE FAMILIES (Glottolog): (a) Download Glottolog CLDF dataset (from GitHub glottolog/glottolog or glottolog/glottolog-cldf or ZENODO). (b) Use pyglottolog Python API to look up each language by ISO code and extract its classification path (family, subfamily if available). (c) Use the top-level family node as the 'family_id' for frailty grouping; also include full classification path as 'family_path' for reference. (d) Fallback: if a language is not in Glottolog, mark family_id as 'unknown' but do NOT drop the treebank.\\n\\n6. SCHEMA DESIGN & VALIDATION: Design JSON schema (one row per arc) with required fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound [CRITICAL: document that censoring_bound = max(token_id, sent_len - token_id) in schema description], register (enum: spoken, written, academic, news, fiction, web, other, unspecified), language_code, language_name, family_id, family_path, word_order_type (optional, nullable), morph_richness_proxy (float 0-1), morph_richness_data_source (WALS/Grambank/UD_proxy). Use aii-json skill to validate a sample of rows before final output.\\n\\n7. QUALITY CHECKS & SPOT-VALIDATION: (a) For a random sample of 100-200 arcs, verify that arc_length <= censoring_bound (should be 100% true; flag any violations). (b) Cross-check register labels: spot-read treebank metadata to confirm 'spoken' arcs come from marked spoken subcorpora. (c) Verify language codes are ISO 639-3 and consistent across UD and Glottolog. (d) For 10-20 languages with matched WALS and Grambank entries, confirm word-order classification consistency between sources (should be close to identical). (e) Inspect morphological-richness proxies for outliers (plot distribution, should be unimodal and clustered around 0.1-0.6 for most languages).\\n\\n8. SPLITS & EXPORT: (a) FULL: All extracted arcs, deduplicated, ordered by language, treebank, sentence. (b) MINI: 50k random arcs stratified by register and language family (for quick iteration in executor testing). (c) PREVIEW: 500-1000 arcs from diverse languages/registers for documentation. All three as data_out.json with one JSON object per line (JSONL) or as a single JSON array, depending on size; use aii-file-size-limit skill if >300MB to advise on splits. Include a schema document and a summary statistics table (arcs per language, arcs per register, arc-length distribution quartiles by register).\\n\\n9. FALLBACK & ROBUSTNESS: If HuggingFace API fails, fetch UD treebanks directly from UniversalDependencies GitHub (UD_<language>-<treebank> repos). If Glottolog unavailable, use cached/static Glottolog export (available on ZENODO as versioned snapshot). If WALS/Grambank incomplete, ensure UD_proxy is computed for all languages. If a treebank has parsing errors or malformed CoNLL-U, log the issue and skip that treebank but continue; do NOT fail the entire run.\\n\\n10. DOCUMENTATION: Generate a README.md with data dictionary, sample rows, source citations (commul/universal_dependencies, Glottolog, WALS, Grambank), notes on censoring-bound computation (with a concrete example sentence), register labeling methodology, known limitations (e.g., % of languages with paired spoken/written data, % coverage by WALS/Grambank vs UD_proxy), and reproduction instructions (language/versions of pyglottolog, UD dataset commit, etc.).\",\n  \"target_num_datasets\": 1\n}\n", "numLines": 9, "startLine": 1, "totalLines": 9}}
```

### [56] ASSISTANT · 2026-08-13 11:35:42 UTC

```
Excellent! I've created a detailed, actionable plan for the dataset. Here's what the plan covers:

## Plan Summary

**Title**: UD Dependency Arcs with Survival-Analysis Features

**Core deliverable**: A complete dataset of 1–5 million dependency arcs from all 296+ Universal Dependencies treebanks, with arc-level features (observed length, position-bounded censoring bound, register labels, typological covariates, language families) designed for survival-analysis investigation of dependency-length minimization.

**Key plan components**:

1. **Data sources**: 
   - Primary: `commul/universal_dependencies` on HuggingFace (v2.18, 296+ treebanks)
   - Typological features: WALS, Grambank, UD morphology as fallback proxy
   - Language families: Glottolog (via pyglottolog API)

2. **Arc extraction with censoring bounds**: 
   - For each token: compute arc length and censoring bound = `max(token_id, sentence_length - token_id)`
   - This captures the structural constraint that a word near a sentence boundary cannot produce long arcs
   - Critical for the survival-analysis reframing

3. **Register/modality labeling**:
   - Extract from UD metadata (18 genre categories)
   - Identify paired treebanks (English-GUM, French-Rhapsodie+GSD, Slovenian, etc.)
   - Fallback: label as "unspecified" rather than drop

4. **Typological integration**:
   - Word order: SVO/SOV/VSO class from WALS or Grambank
   - Morphological richness: from WALS/Grambank or computed as UD feature count proxy (0–1 normalized)
   - Track data source for transparency

5. **Quality validation**:
   - Verify arc_length ≤ censoring_bound (should be 100%)
   - Cross-check register labels with metadata
   - Validate language codes (ISO 639-3) consistency
   - Test word-order classification consistency between WALS/Grambank

6. **Output format**:
   - Full dataset: all arcs ordered by language/treebank
   - Mini: 50k stratified sample for testing
   - Preview: 500–1k examples for documentation
   - JSON schema with explicit censoring-bound documentation
   - README with data dictionary, reproduction instructions, known limitations

7. **Robustness fallbacks**: If HuggingFace fails, use GitHub direct. If Glottolog/WALS/Grambank incomplete, fall back to UD morphology or mark as unknown. Skip malformed treebanks but continue.

**Compute profile**: `cpu_heavy` (4 vCPU, 32GB RAM) — processing millions of arcs and cross-referencing with external databases.

**Target**: 1 integrated dataset (not multiple separate datasets).

The plan is grounded in actual data availability (I researched commul/UD, Glottolog, WALS, Grambank, and identified specific treebanks with paired spoken/written data like English-GUM and French-Rhapsodie) and calibrated for your reviewer's expertise in UD and computational typology.

---

**Sources:**
- [commul/universal_dependencies on HuggingFace](https://huggingface.co/datasets/commul/universal_dependencies)
- [Universal Dependencies Main Site](https://universaldependencies.org/)
- [Spoken Language Treebanks Overview (ACL 2022)](https://aclanthology.org/2022.lrec-1.191/)
- [Counting Trees: Speech/Writing Variation Study (2505.22774)](https://arxiv.org/pdf/2505.22774)
- [English-GUM Treebank](https://universaldependencies.org/treebanks/en_gum/index.html)
- [French-Rhapsodie (Spoken French)](https://universaldependencies.org/treebanks/fr_rhapsodie/)
- [pyglottolog Python API](https://pyglottolog.readthedocs.io/en/latest/api.html)
- [Typological Databases in NLP Survey](https://arxiv.org/pdf/2310.13440)
```
