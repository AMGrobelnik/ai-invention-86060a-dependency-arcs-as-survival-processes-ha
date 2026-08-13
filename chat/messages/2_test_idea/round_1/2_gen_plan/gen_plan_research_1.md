# gen_plan_research_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_oQQwThF8kM-b` — Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_research_1` (terminal_claude_agent, claude-haiku-4-5)

### [1] CONFIG · 2026-08-13 11:33:19 UTC

```
model: claude-haiku-4-5 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_plan/gen_plan_research_1
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

id: research_iter1_dir1
type: research
objective: >-
  Understand survival-analysis precedent in linguistics, deeply review DLM literature and its documented confounds, catalog
  UD treebanks suitable for register-level analysis, and establish the theoretical justification for modeling arc length as
  a censored time-to-event process.
approach: >-
  Search scholarly literature for survival-analysis applications to linguistic or behavioral data with position-bounded maximums;
  deeply read Ferrer-i-Cancho et al. on length-mixing and recent cross-linguistic speech vs. writing DLM studies; catalog
  commul/universal_dependencies by modality and language coverage; synthesize why dependency arcs constitute a valid survival-analysis
  substrate—i.e., what makes 'has the arc closed by distance d, given it has not closed before d and could not exceed the
  sentence boundary' a meaningful conditional quantity rather than a degenerate one.
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

### [3] HUMAN-USER prompt · 2026-08-13 11:33:25 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [4] ASSISTANT · 2026-08-13 11:33:41 UTC

```
I'll create a detailed research plan for understanding survival-analysis precedent in linguistics, reviewing DLM literature, cataloging UD treebanks, and establishing the theoretical justification for modeling dependency arcs as censored time-to-event processes.

Let me search the relevant literature and documentation to make this plan concrete and actionable.
```

### [5] TOOL CALL — Skill · 2026-08-13 11:33:41 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-08-13 11:33:41 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — Skill · 2026-08-13 11:33:41 UTC

```
aii-web-tools
```

### [8] TOOL RESULT — Skill · 2026-08-13 11:33:41 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [9] TOOL CALL — Skill · 2026-08-13 11:33:41 UTC

```
aii-web-tools
```

### [10] TOOL RESULT — Skill · 2026-08-13 11:33:41 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [11] TOOL CALL — Skill · 2026-08-13 11:33:41 UTC

```
aii-web-tools
```

### [12] TOOL RESULT — Skill · 2026-08-13 11:33:41 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [13] TOOL CALL — Skill · 2026-08-13 11:33:41 UTC

```
aii-web-tools
```

### [14] TOOL RESULT — Skill · 2026-08-13 11:33:41 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [15] ASSISTANT · 2026-08-13 11:33:45 UTC

```
I need to load the built-in web research tools first. Let me fetch their schemas:
```

### [16] TOOL CALL — ToolSearch · 2026-08-13 11:33:45 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 2}
```

### [17] TOOL RESULT — ToolSearch · 2026-08-13 11:33:45 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 21}
```

### [18] ASSISTANT · 2026-08-13 11:33:51 UTC

```
Now I'll conduct targeted searches to gather the key information needed for the research plan.
```

### [19] TOOL CALL — WebSearch · 2026-08-13 11:33:51 UTC

```
Ferrer-i-Cancho dependency length mixing confound sentence length
```

### [20] TOOL CALL — WebSearch · 2026-08-13 11:33:51 UTC

```
cross-linguistic dependency length minimization spoken written speech PNAS
```

### [21] TOOL CALL — WebSearch · 2026-08-13 11:33:51 UTC

```
universal dependencies treebanks genre spoken written modality HuggingFace
```

### [22] TOOL CALL — WebSearch · 2026-08-13 11:33:51 UTC

```
survival analysis Kaplan-Meier censoring time-to-event linguistics behavioral data
```

### [23] TOOL CALL — WebSearch · 2026-08-13 11:33:51 UTC

```
Cox proportional hazards shared frailty random effects language family typology
```

### [24] TOOL RESULT — WebSearch · 2026-08-13 11:33:57 UTC

```
{"query": "cross-linguistic dependency length minimization spoken written speech PNAS", "results": [{"tool_use_id": "srvtoolu_01X4kjBnWuRTMTX3Lo3VzNE1", "content": [{"title": "Large-scale evidence of dependency length minimization in 37 languages | PNAS", "url": "https://www.pnas.org/doi/full/10.1073/pnas.1502134112"}, {"title": "Cross-linguistic Dependency Length Minimization in scientific language | John Benjamins", "url": "https://www.jbe-platform.com/content/journals/10.1075/lic.00038.kri"}, {"title": "Large-scale evidence of dependency length minimization in 37 languages - PubMed", "url": "https://pubmed.ncbi.nlm.nih.gov/26240370/"}, {"title": "(PDF) Large-scale evidence of dependency length minimization in 37 languages", "url": "https://www.researchgate.net/publication/280692970_Large-scale_evidence_of_dependency_length_minimization_in_37_languages"}, {"title": "Cross-Linguistic Analysis of Memory Load in Sentence Comprehension: Linear Distance and Structural Density", "url": "https://arxiv.org/pdf/2509.20916"}, {"title": "Large-scale evidence of dependency length minimization in 37 languages", "url": "https://www.pnas.org/doi/pdf/10.1073/pnas.1502134112"}, {"title": "Large-scale evidence of dependency length minimization in 37 languages - ADS", "url": "https://ui.adsabs.harvard.edu/abs/2015PNAS..11210336F/abstract"}, {"title": "Correction for Futrell et al., Large-scale evidence of dependency length minimization in 37 languages | PNAS", "url": "https://www.pnas.org/doi/10.1073/pnas.1520071112"}]}, "Based on the search results, I found relevant information about cross-linguistic dependency length minimization:\n\n## Main Study\n\nThe primary research provides large-scale, quantitative, cross-linguistic evidence for a universal syntactic property of languages: that dependency lengths are shorter than chance. The principle being studied is that dependency length—the distance between syntactically related words in a sentence—is minimized.\n\nThe study was authored by Richard Futrell and colleagues from the Department of Brain and Cognitive Sciences at MIT and was published in PNAS in 2015 (volume 112, issue 33).\n\n## Key Findings\n\nThe work supports long-standing ideas that speakers prefer word orders with short dependency lengths and that languages do not enforce word orders with long dependency lengths. Dependency length minimization is well motivated because it allows for more efficient parsing and generation of natural language.\n\n## Relevance to Spoken and Written Speech\n\nWhile the search results reference the main PNAS study on 37 languages, they also indicate related research exploring these patterns in different registers. For instance, other work has examined whether scientific English and German minimize the length of syntactic dependency relations in the Late Modern period (ca. 1650–1900)."], "durationSeconds": 7.072016158000002, "searchCount": 1}
```

### [25] TOOL RESULT — WebSearch · 2026-08-13 11:33:57 UTC

```
{"query": "Ferrer-i-Cancho dependency length mixing confound sentence length", "results": [{"tool_use_id": "srvtoolu_01LXt6bpuZYLwfLo5BeX9kaU", "content": [{"title": "Glottotheory Volume 5, Issue 2", "url": "https://www.degruyterbrill.com/journal/key/glot/5/2/html?lang=en"}, {"title": "Large-scale evidence of dependency length minimization in 37 languages | PNAS", "url": "https://www.pnas.org/doi/10.1073/pnas.1502134112"}, {"title": "The risks of mixing dependency lengths from sequences of different   length", "url": "https://arxiv.org/pdf/1304.3841"}, {"title": "[1304.3841] The risks of mixing dependency lengths from sequences of different length", "url": "https://arxiv.org/abs/1304.3841"}, {"title": "\b Glottotheory 2014; 5(2): 143 – 155 Ramon Ferrer-i-Cancho and Haitao Liu", "url": "https://upcommons.upc.edu/bitstream/handle/2117/28279/Ferrer-i-Cancho_and_Liu_Glottotheory_2014.pdf"}, {"title": "Dependency length minimization: Puzzles and Promises", "url": "https://arxiv.org/pdf/1509.04393"}, {"title": "The effects of sentence length on dependency distance, dependency direction and the implications–Based on a parallel English–Chinese dependency treebank - ScienceDirect", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0388000115000418"}, {"title": "Quantitative relationship between distribution of sentence length and dependency distance in Spanish", "url": "https://www.degruyterbrill.com/document/doi/10.1515/lingvan-2024-0185/html"}, {"title": "A Reappraisal of Dependency Length Minimization as a Linguistic Universal - PMC", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9692064/"}, {"title": "Reply to the commentary \"Be careful when assuming the obvious\", by P.   Alday", "url": "https://arxiv.org/pdf/1412.7186"}]}, "Based on the search results, here's what I found about Ferrer-i-Cancho's work on dependency length and the mixing confound with sentence length:\n\n## Key Findings\n\nMixing dependency lengths from sequences of different length is a common practice in language research, but the empirical distribution of dependency lengths of sentences of the same length differs from that of sentences of varying length.\n\n## The Core Issue\n\nThe distribution of dependency lengths depends on sentence length for real sentences and also under the null hypothesis that dependencies connect vertices located in random positions of the sequence. This is significant because certain results, such as the distribution of syntactic dependency lengths mixing dependencies from sentences of varying length, could be a mere consequence of that mixing.\n\n## Implications for Language Comparison\n\nDifferences in the global averages of dependency length (mixing lengths from sentences of varying length) for two different languages do not simply imply a priori that one language optimizes dependency lengths better than the other because those differences could be due to differences in the distribution of sentence lengths and other factors.\n\n## Methodological Recommendation\n\nTo reduce confounds, it is convenient to not include sequences with less than three elements in mixtures of dependency length information from sentences of varying length.\n\nThis work by Ferrer-i-Cancho and Liu highlights an important methodological issue in computational linguistics research—that the confounding of sentence length must be carefully controlled for when analyzing syntactic dependency structures across languages."], "durationSeconds": 8.884587963999998, "searchCount": 1}
```

### [26] TOOL RESULT — WebSearch · 2026-08-13 11:33:57 UTC

```
{"query": "universal dependencies treebanks genre spoken written modality HuggingFace", "results": [{"tool_use_id": "srvtoolu_01MirhmNxdffG2cJzL8GQGsd", "content": [{"title": "Daily Papers - Hugging Face", "url": "https://huggingface.co/papers?q=Universal+Dependencies"}, {"title": "Counting trees: a treebank-driven exploration of syntactic variation in speech and writing across languages", "url": "https://www.degruyterbrill.com/document/doi/10.1515/cllt-2025-0046/html?lang=en"}, {"title": "Universal Dependencies", "url": "https://universaldependencies.org/"}, {"title": "Genre as Weak Supervision for Cross-lingual Dependency Parsing", "url": "https://arxiv.org/pdf/2109.04733"}, {"title": "Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages", "url": "https://arxiv.org/pdf/2505.22774"}, {"title": "Spoken Language Treebanks in Universal Dependencies", "url": "https://aclanthology.org/2022.lrec-1.191.pdf"}, {"title": "Universal Dependencies v1: A Multilingual Treebank Collection", "url": "https://nlp.stanford.edu/pubs/nivre2016ud.pdf"}, {"title": "Paper page - Universal Dependencies v2: An Evergrowing Multilingual Treebank Collection", "url": "https://huggingface.co/papers/2004.10643"}, {"title": "Universal Dependencies v2", "url": "https://aclanthology.org/2020.lrec-1.497.pdf"}, {"title": "Data-driven Parsing Evaluation for Child-Parent Interactions", "url": "https://arxiv.org/pdf/2209.13778"}]}, "I've found comprehensive information about Universal Dependencies treebanks, their genre and modality characteristics. Here are the key findings:\n\n## Universal Dependencies Overview\n\nUniversal Dependencies is an open community effort to create cross-linguistically consistent treebank annotation for many languages within a dependency-based lexicalist framework. The annotation consists of a linguistically motivated word segmentation; a morphological layer comprising lemmas, universal part-of-speech tags, and standardized morphological features; and a syntactic layer focusing on syntactic relations between predicates, arguments and modifiers.\n\n## Genre Coverage\n\nMost treebanks are constituted of different genres, with newswire quite present, and other genres well represented in several languages such as web data (reviews, blogs), fiction and legal documents.\n\n## Spoken vs. Written Modality\n\nThere's a significant imbalance in the treebank data: Of the 228 treebanks in the latest version of UD (v2.10), only 12 are treebanks of fully spoken data, while the rest focus on different genres within the written domain.\n\nRecent research has examined this modality distinction: GUM-spoken subset includes data from interviews, vlogs, speeches, conversations, courtroom transcripts, and podcasts, while the GUM-written subset comprises biographies, fiction, academic texts, textbooks, how-to guides, news articles, and travel guides.\n\nThere has been a growing number of spoken language treebanks adopting the Universal Dependencies annotation scheme, aimed at cross-linguistically consistent morphosyntactic annotation."], "durationSeconds": 8.252311135, "searchCount": 1}
```

### [27] TOOL RESULT — WebSearch · 2026-08-13 11:33:57 UTC

```
{"query": "Cox proportional hazards shared frailty random effects language family typology", "results": [{"tool_use_id": "srvtoolu_01NUjqn6xhEJ1UmDVAmkzQSy", "content": [{"title": "Shared Frailty Models Based on Cancer Data", "url": "https://arxiv.org/pdf/2112.10986"}, {"title": "A Tutorial on Multilevel Survival Analysis: Methods, Models and Applications - Austin - 2017 - International Statistical Review - Wiley Online Library", "url": "https://onlinelibrary.wiley.com/doi/full/10.1111/insr.12214"}, {"title": "A Cox Model with Shared Frailty", "url": "https://grodri.github.io/survival/frailtyr"}, {"title": "The shared weighted Lindley frailty model for cluster failure time data", "url": "https://arxiv.org/pdf/2206.12973"}, {"title": "General Semiparametric Shared Frailty Model Estimation and Simulation   with frailtySurv", "url": "https://arxiv.org/pdf/1702.06407"}, {"title": "coxme: Mixed Effects Cox Models version 2.2-22 from CRAN", "url": "https://rdrr.io/cran/coxme/"}, {"title": "Generalized inverse-Gaussian frailty models with application to TARGET   neuroblastoma data", "url": "https://arxiv.org/pdf/2004.01292"}, {"title": "Rethinking Individual Risk and Aggregation in Survival Analysis: A Latent Mechanism Framework", "url": "https://arxiv.org/pdf/2603.24276"}, {"title": "Classification Algorithm for High Dimensional Protein Markers in   Time-course Data", "url": "https://arxiv.org/pdf/1907.12853"}, {"title": "Laplacian-P-splines for shared Gamma frailty models applied to clustered right-censored time-to-event data", "url": "https://arxiv.org/pdf/2605.12092"}]}, "I've completed the web search for your query. Here are the key findings:\n\n**Overview of Cox Proportional Hazards with Shared Frailty and Random Effects:**\n\nThe frailty model is a random effect model for time to event data which is an extension of the Cox's proportional hazards model. Clayton (1978) introduced a random effect term into the proportional hazards model, known as the shared frailty model, which includes a latent random variable that comprises the unobservable dependency between members of a cluster.\n\n**Shared Frailty Models:**\n\nThese models are described as shared frailty models because the same random effect is shared by all subjects within the same cluster. The frailty has a multiplicative effect on the hazard, and given the observed covariates and unobserved frailty, the survival times within a cluster are assumed independent.\n\n**Common Applications:**\n\nOften, the assumption of independent and identically distributed observations is violated when survival times are clustered or depend on unobserved covariates, such as from geographical clustering, subjects sharing common genes, or other unobserved predispositions.\n\n**Frailty Distributions:**\n\nThe gamma and log-normal distributions are most commonly used for frailty terms.\n\nThe search results focus primarily on statistical methodology and medical/biological applications. The results do not contain specific information about applications to language family typology, which would be a more specialized area combining survival analysis with linguistic classification."], "durationSeconds": 7.425973732999999, "searchCount": 1}
```

### [28] TOOL RESULT — WebSearch · 2026-08-13 11:33:59 UTC

```
{"query": "survival analysis Kaplan-Meier censoring time-to-event linguistics behavioral data", "results": [{"tool_use_id": "srvtoolu_01HrFLxwaA7C51jpuVXpVKZg", "content": [{"title": "Methods to Analyse Time-to-Event Data: The Kaplan-Meier Survival Curve", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8478547/"}, {"title": "Survival analysis—time-to-event data and censoring | Nature Methods", "url": "https://www.nature.com/articles/s41592-022-01563-7"}, {"title": "Clinicians' Interpretation and Preferences for Survival Data Visualisation: A Pre-Post Study Comparing Kaplan-Meier and Mean Residual Life Plots", "url": "https://arxiv.org/pdf/2511.08332"}, {"title": "Phase III Study of Trifluridine/Tipiracil With and Without Bevacizumab in Refractory Metastatic Colorectal Cancer Patients", "url": "https://cdn.clinicaltrials.gov/large-docs/87/NCT04737187/SAP_001.pdf"}, {"title": "Study of Efficacy and Safety of CTL019 in Adult DLBCL Patients", "url": "https://cdn.clinicaltrials.gov/large-docs/48/NCT02445248/SAP_001.pdf"}, {"title": "Time-To-Event (TTE) Data Analysis | Columbia Public Health | Columbia University Mailman School of Public Health", "url": "https://www.publichealth.columbia.edu/research/population-health-methods/time-event-data-analysis"}, {"title": "Reconstruct Kaplan--Meier Estimator as M-estimator and Its Confidence   Band", "url": "https://arxiv.org/pdf/2011.10240"}, {"title": "STOPPER CHINA:With Tandem Microspheres in the Treatment of Localized Hepatocellular Carcinoma", "url": "https://cdn.clinicaltrials.gov/large-docs/55/NCT03113955/SAP_001.pdf"}, {"title": "CleanSurvival: Automated data preprocessing for time-to-event models using reinforcement learning", "url": "https://arxiv.org/pdf/2502.03946"}]}, "I've performed the web search with your query. The results provide substantial information about survival analysis, Kaplan-Meier methods, and censoring in time-to-event data. Here's what I found:\n\n## Key Findings\n\n**Survival Analysis and Time-to-Event Data:**\nSurvival analysis, also referred to as time-to-event data analysis, is the analysis of data in the form of times from a well-defined time origin until the occurrence of some particular event or end point. Time-to-event analysis is one of the most important methodologies used in clinical and epidemiological research to address etiological and prognostic hypotheses.\n\n**Kaplan-Meier Method:**\nThe Kaplan-Meier analysis is the most used method in both observational and interventional studies. The Kaplan-Meier method is based on conditional probabilities calculations and enables to compute non-parametric estimates of the survival function.\n\n**Censoring:**\nThe concept of censoring includes right censoring, interval censoring, and left censoring. The distinct feature of survival data is censoring, wherein the event of interest has not been observed for all subjects during the study period.\n\n**Broader Applications:**\nEvents may range from biological outcomes such as death, remission, or relapse, to engineering failures, time to default in finance, or germination in agriculture.\n\n**Note:** The search results focus primarily on medical and clinical applications of these methods. The results don't specifically address applications to linguistics or behavioral data, which were part of your original query."], "durationSeconds": 8.779778677000001, "searchCount": 1}
```

### [29] ASSISTANT · 2026-08-13 11:34:05 UTC

```
Now let me fetch the key papers to get more specific technical details:
```

### [30] TOOL CALL — WebFetch · 2026-08-13 11:34:05 UTC

```
URL: https://arxiv.org/abs/1304.3841
Prompt: What is the core confound in dependency length mixing? What examples are given? What corrections do they suggest?
```

### [31] TOOL CALL — WebFetch · 2026-08-13 11:34:05 UTC

```
URL: https://aclanthology.org/2022.lrec-1.191.pdf
Prompt: Which UD treebanks contain spoken data? How many? What is their coverage by language?
```

### [32] TOOL CALL — WebFetch · 2026-08-13 11:34:05 UTC

```
URL: https://arxiv.org/pdf/2505.22774
Prompt: What are the key findings about syntactic variation in speech vs writing? Which language pairs have paired spoken/written treebanks?
```

### [33] TOOL CALL — WebFetch · 2026-08-13 11:34:05 UTC

```
URL: https://www.pnas.org/doi/full/10.1073/pnas.1502134112
Prompt: What methodology does Futrell et al. use? How do they normalize for sentence length? What are the main statistical findings?
```

### [34] TOOL RESULT — WebFetch · 2026-08-13 11:34:05 UTC

```
{"bytes": 0, "code": 403, "codeText": "Forbidden", "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 295, "url": "https://www.pnas.org/doi/full/10.1073/pnas.1502134112"}
```

### [35] TOOL RESULT — WebFetch · 2026-08-13 11:34:07 UTC

```
{"bytes": 43119, "code": 200, "codeText": "OK", "result": "# Core Confound in Dependency Length Mixing\n\n**The Primary Issue:**\n\nThe paper identifies that \"the empirical distribution of dependency lengths of sentences of the same length differs from that of sentences of varying length.\" This means combining dependency lengths across sentences of different sizes creates statistical artifacts.\n\n**Key Examples:**\n\nThe authors demonstrate that this problem occurs both in real language data and under null hypothesis conditions (where dependencies connect randomly positioned vertices). This suggests observed patterns in mixed-length datasets might reflect sampling methodology rather than genuine linguistic properties.\n\n**Suggested Corrections:**\n\nRather than mixing dependencies from sentences of varying lengths, the authors recommend:\n\n1. **Separate analyses by sentence length** to reveal true distributional patterns\n2. **Account for sentence length distribution differences** when comparing languages, since variations in global averages \"could be due to differences in the distribution of sentence lengths and other factors\"\n3. **Recognize that cross-language comparisons** cannot simply assume one language optimizes dependencies better without controlling for these confounds\n\nThe core insight is that sentence length acts as a confounding variable that distorts aggregate findings about syntactic dependency optimization.", "durationMs": 4409, "url": "https://arxiv.org/abs/1304.3841"}
```

### [36] TOOL RESULT — WebFetch · 2026-08-13 11:34:07 UTC

```
{"bytes": 221770, "code": 200, "codeText": "OK", "result": "I apologize, but the provided content is a PDF file in raw binary/encoded format that I cannot properly parse or extract readable text from. The document appears to be about \"Spoken Language Treebanks in Universal Dependencies: an Overview\" based on the metadata, but the actual content is not accessible in a readable form.\n\nTo answer your questions about:\n- Which UD treebanks contain spoken data\n- How many such treebanks exist\n- Their language coverage\n\nI would need the document in a format I can read (such as plain text, HTML, or properly rendered PDF content). Could you provide the document in an alternative format, or share the specific information you're looking for from this paper?\n\n[Binary content (application/pdf, 216.6KB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-oQQwThF8kM-b-3-invention-loop-iter-1-gen-plan-gen-plan-research-1/d080fb08-09ee-4a4d-8d50-6eb8d7066ffd/tool-results/webfetch-1786620843567-ynae8r.pdf]", "durationMs": 4290, "url": "https://aclanthology.org/2022.lrec-1.191.pdf"}
```

### [37] TOOL RESULT — WebFetch · 2026-08-13 11:34:09 UTC

```
{"bytes": 1544246, "code": 200, "codeText": "OK", "result": "I appreciate your question, but I need to be honest: the content provided appears to be a corrupted or heavily compressed PDF file with unreadable binary data. The text extracted contains fragmented, garbled information that doesn't form coherent passages about syntactic variation or treebanks.\n\nTo properly answer your questions about:\n- Key findings on speech vs. writing syntactic differences\n- Language pairs with paired spoken/written treebanks\n\nI would need access to a legible academic source document. The current material doesn't contain interpretable information on these topics.\n\nIf you have a specific linguistic paper or resource on this subject, I'd be happy to analyze it and provide the concise, properly-quoted response you're seeking.\n\n[Binary content (application/pdf, 1.5MB) also saved to /root/.claude/projects/-ai-inventor-aii-data-runs-run-oQQwThF8kM-b-3-invention-loop-iter-1-gen-plan-gen-plan-research-1/d080fb08-09ee-4a4d-8d50-6eb8d7066ffd/tool-results/webfetch-1786620843665-qfx384.pdf]", "durationMs": 3747, "url": "https://arxiv.org/pdf/2505.22774"}
```

### [38] ASSISTANT · 2026-08-13 11:34:13 UTC

```
Let me search for more accessible resources on UD treebanks and the recent spoken/written studies:
```

### [39] TOOL CALL — WebSearch · 2026-08-13 11:34:13 UTC

```
"Counting trees" speech writing syntactic variation UD treebanks arxiv
```

### [40] TOOL CALL — WebSearch · 2026-08-13 11:34:13 UTC

```
UD treebanks list spoken genre GUM French Slovenian Cantonese
```

### [41] TOOL CALL — WebSearch · 2026-08-13 11:34:13 UTC

```
lifelines Python library survival analysis Kaplan-Meier Cox frailty
```

### [42] TOOL CALL — WebFetch · 2026-08-13 11:34:13 UTC

```
URL: https://universaldependencies.org/
Prompt: List all treebanks with spoken or genre metadata. What modality tags exist?
```

### [43] TOOL RESULT — WebSearch · 2026-08-13 11:34:15 UTC

```
{"query": "\"Counting trees\" speech writing syntactic variation UD treebanks arxiv", "results": [{"tool_use_id": "srvtoolu_01N83HeMQC4wozsytYG36FTW", "content": [{"title": "Counting trees: a treebank-driven exploration of syntactic variation in speech and writing across languages", "url": "https://www.degruyterbrill.com/document/doi/10.1515/cllt-2025-0046/html"}, {"title": "(PDF) Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages", "url": "https://www.researchgate.net/publication/392204301_Counting_trees_A_treebank-driven_exploration_of_syntactic_variation_in_speech_and_writing_across_languages"}, {"title": "Kaja Dobrovoljc Counting trees: A treebank-driven exploration of syntactic", "url": "https://arxiv.org/pdf/2505.22774"}, {"title": "The UD-NewsCrawl Treebank: Reflections and Challenges from a Large-scale Tagalog Syntactic Annotation Project", "url": "https://arxiv.org/html/2505.20428"}, {"title": "Treebank — Grokipedia", "url": "https://grokipedia.com/page/Treebank"}, {"title": "arxiv.org", "url": "https://arxiv.org/abs/2505.22774"}]}, "I found the research paper you're looking for! Here's what I found:\n\nThe paper \"Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages\" presents a novel treebank-driven approach to comparing syntactic structures in speech and writing using dependency-parsed corpora, adopting a fully inductive, bottom-up method to define syntactic structures as delexicalized dependency (sub)trees extracted from spoken and written Universal Dependencies (UD) treebanks in English and Slovenian.\n\nFor each corpus, the researchers analyze the size, diversity, and distribution of syntactic inventories, their overlap across modalities, and the structures most characteristic of speech.\n\nThe results show that across both languages, spoken corpora contain fewer and less diverse syntactic structures than their written counterparts, with the overlap between spoken and written syntactic inventories being very limited—most structures attested in speech do not occur in writing, pointing to modality-specific preferences in syntactic organization.\n\nThe paper is authored by Kaja Dobrovoljc and was submitted to arXiv on May 28, 2025 (arXiv:2505.22774)."], "durationSeconds": 4.793712994000002, "searchCount": 1}
```

### [44] TOOL RESULT — WebSearch · 2026-08-13 11:34:17 UTC

```
{"query": "UD treebanks list spoken genre GUM French Slovenian Cantonese", "results": [{"tool_use_id": "srvtoolu_016jW5LB9uHRrxtBiJmcvZcK", "content": [{"title": "1 Annotation guidelines of UD and SUD treebanks for spoken corpora: a proposal", "url": "https://aclanthology.org/2021.tlt-1.4.pdf"}, {"title": "Spoken Language Treebanks in Universal Dependencies", "url": "https://aclanthology.org/2022.lrec-1.191.pdf"}, {"title": "Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages", "url": "https://arxiv.org/pdf/2505.22774"}, {"title": "Universal Dependencies", "url": "https://universaldependencies.org/"}, {"title": "Text Annotation · NLP with R and UDPipe", "url": "https://bnosac.github.io/udpipe/docs/doc2.html"}, {"title": "UCxn: Typologically Informed Annotation of Constructions Atop Universal   Dependencies", "url": "https://arxiv.org/pdf/2403.17748"}, {"title": "UD_English-GUM", "url": "https://universaldependencies.org/treebanks/en_gum/index.html"}, {"title": "UD-English-CHILDES: A Collected Resource of Gold and Silver Universal Dependencies Trees for Child Language Interactions", "url": "https://arxiv.org/pdf/2504.20304"}, {"title": "Distilling Efficient Language-Specific Models for Cross-Lingual Transfer", "url": "https://arxiv.org/pdf/2306.01709"}, {"title": "Treebanking user-generated content: a UD based overview of guidelines, corpora and unified recommendations | Language Resources and Evaluation | Springer Nature Link", "url": "https://link.springer.com/article/10.1007/s10579-022-09581-9"}]}, "Based on the search results, here's information about UD treebanks with spoken genre data, including the specific languages you mentioned:\n\n## UD Treebanks with Spoken Genre\n\nUD_English-GUM contains spoken data with speaker and addressee features, and the GUM treebank covers multiple genres including academic, blog, email, fiction, government, legal, news, nonfiction, social, spoken, web, and wiki.\n\nUD_Polish-LFG contains a feature marking genre as spoken (prepared) to distinguish the spoken data. Additionally, there is a spoken French UD treebank.\n\nFor the other languages you mentioned, UD_Slovenian-SST and UD_Cantonese-HK are treebanks of spoken languages. More specifically, the Cantonese treebank consists of film subtitles and of legislative proceedings of Hong Kong.\n\nThe search results also indicate that among the UD v2.9 treebanks with mixed written and spoken data are English GUM, along with several others including Polish LFG and Scottish Gaelic ARCOSG."], "durationSeconds": 6.609797079000003, "searchCount": 1}
```

### [45] TOOL RESULT — WebFetch · 2026-08-13 11:34:19 UTC

```
{"bytes": 1706036, "code": 200, "codeText": "OK", "result": "# Treebanks with Spoken or Genre Metadata\n\nBased on the document, several treebanks are explicitly marked with metadata indicating spoken language or specific genres:\n\n## Spoken Language Treebanks\n- **French-Rhapsodie**: \"A Universal Dependencies corpus for spoken French\"\n- **English-CHILDES**: Utterances from \"child–adult spoken interactions in English\"\n- **Gorontalo-BungoLoLombi**: \"modern spoken Gorontalo\"\n- **French-ParisStories**: \"oral French collected and transcribed\"\n\n## Genre-Specific Treebanks\n- **English-ESLSpok**: Spoken second language English from transcripts\n- **Bavarian-MaiBaam**: \"diverse text genres (wiki articles and discussions, grammar examples, fiction, and commands)\"\n- **Chinese-Beginner**: \"variety of text genres\" for learner levels\n\n## Modality Tags\n\nThe document does not explicitly define a standardized set of modality tags. However, treebanks are distinguished using icon symbols (Ⓛ, Ⓟ, Ⓕ, Ⓔ, ✘) that appear to indicate special characteristics like \"Lemmas,\" \"Parallel,\" \"Fused,\" \"Enhanced,\" or other properties, though the legend isn't clearly provided in this excerpt.\n\nMost genre/modality information appears embedded in descriptive text rather than through consistent metadata tags.", "durationMs": 6501, "url": "https://universaldependencies.org/"}
```

### [46] TOOL RESULT — WebSearch · 2026-08-13 11:34:19 UTC

```
{"query": "lifelines Python library survival analysis Kaplan-Meier Cox frailty", "results": [{"tool_use_id": "srvtoolu_015bWVSWm7eNJaCjWLcd2Mm3", "content": [{"title": "‘Lifelines’ Python Library: The Key to Effective Survival Analysis | by daython3 | Medium", "url": "https://medium.com/@daython3/lifelines-python-library-the-key-to-effective-survival-analysis-b048ac974395"}, {"title": "Overview about Survival Analysis in Python with the ‘lifelines’ Library | by Roland Nagy | Medium", "url": "https://medium.com/@rolandnagydata/overview-about-survival-analysis-in-python-with-the-lifelines-library-eb84f84a86c6"}, {"title": "Frailty and Survival Regression Models — PyMC example gallery", "url": "https://www.pymc.io/projects/examples/en/latest/survival_analysis/frailty_models.html"}, {"title": "More examples and recipes — lifelines 0.30.3 documentation", "url": "https://lifelines.readthedocs.io/en/latest/Examples.html"}, {"title": "lifelines/docs/Examples.rst at master · CamDavidsonPilon/lifelines", "url": "https://github.com/CamDavidsonPilon/lifelines/blob/master/docs/Examples.rst"}, {"title": "lifelines — lifelines 0.30.3 documentation", "url": "https://lifelines.readthedocs.io/"}, {"title": "lifelines — lifelines 0.30.0 documentation - Read the Docs", "url": "https://lifelines.readthedocs.io/en/latest/"}, {"title": "GitHub - CamDavidsonPilon/lifelines: Survival analysis in Python · GitHub", "url": "https://github.com/CamDavidsonPilon/lifelines"}, {"title": "Quickstart — lifelines 0.30.3 documentation", "url": "https://lifelines.readthedocs.io/en/latest/Quickstart.html"}, {"title": "Survival analysis in Julia", "url": "https://github.com/topics/kaplan-meier?o=desc&s=stars"}]}, "Here are the search results for the lifelines Python library and survival analysis:\n\n## Overview\n\nLifelines is a complete survival analysis library, written in pure Python. The lifelines library in Python provides a powerful and easy-to-use suite of tools for survival analysis.\n\n## Key Features\n\nThe library offers easy installation, internal plotting methods, a simple and intuitive API, and handles right, left and interval censored data.\n\n## Main Survival Analysis Techniques\n\nThe library implements several important methods:\n\n1. **Kaplan-Meier Estimator**: A non-parametric method to estimate the survival function from lifetime data.\n\n2. **Cox Proportional Hazards Model**: A semi-parametric model to evaluate the effect of several variables on survival.\n\n3. **Nelson-Aalen Fitter**: Similar functionality exists for the NelsonAalenFitter, which exposes a cumulative_hazard_ instead of a survival_function_.\n\n4. **Parametric Models**: Lifelines has builtin parametric models, for example, Weibull, Log-Normal, Log-Logistic, and more.\n\n## Handling Survival Data\n\nThe library deals with time durations that are strictly positive, measuring the time until an event of interest occurs, and addresses the challenge of censoring, where some individuals may not experience the event during the observation period.\n\nThe library is available on GitHub at CamDavidsonPilon/lifelines with comprehensive documentation and examples."], "durationSeconds": 7.190209520999997, "searchCount": 1}
```

### [47] ASSISTANT · 2026-08-13 11:34:25 UTC

```
Let me fetch more details from the key papers:
```

### [48] TOOL CALL — WebFetch · 2026-08-13 11:34:25 UTC

```
URL: https://arxiv.org/abs/2505.22774
Prompt: What language pairs have paired spoken/written UD treebanks? What specific corpora are analyzed? What are the main findings about speech vs writing?
```

### [49] TOOL CALL — WebFetch · 2026-08-13 11:34:25 UTC

```
URL: https://lifelines.readthedocs.io/en/latest/
Prompt: What models does lifelines support? Does it support shared frailty models? What is the API for Cox regression with random effects?
```

### [50] TOOL CALL — WebSearch · 2026-08-13 11:34:25 UTC

```
HuggingFace datasets universal_dependencies commul download treebanks
```

### [51] TOOL CALL — WebSearch · 2026-08-13 11:34:25 UTC

```
dependency length minimization typology word order free-order language
```

### [52] TOOL RESULT — WebFetch · 2026-08-13 11:34:27 UTC

```
{"bytes": 3956, "code": 200, "codeText": "OK", "result": "Based on the provided content, I cannot answer your questions about specific models or shared frailty support.\n\nThe webpage states that lifelines \"contains the most popular parametric, semi-parametric and non-parametric models\" and handles various censoring types, but it doesn't enumerate which particular models are included or whether shared frailty models are supported.\n\nThe documentation sections listed mention \"Survival regression\" and \"Custom regression models,\" but the actual content of those pages isn't provided here. To find information about Cox regression with random effects or frailty models, you would need to consult the full documentation at the links referenced on this page, particularly the API Reference or the Survival Regression section.", "durationMs": 3123, "url": "https://lifelines.readthedocs.io/en/latest/"}
```

### [53] TOOL RESULT — WebFetch · 2026-08-13 11:34:27 UTC

```
{"bytes": 44010, "code": 200, "codeText": "OK", "result": "# Analysis of \"Counting trees\" Paper\n\n## Language Pairs and Corpora\n\nThe abstract specifies that the study examines **English and Slovenian**, described as \"two syntactically distinct languages.\" The research uses \"spoken and written Universal Dependencies (UD) treebanks\" for these languages, though the abstract doesn't name specific corpus versions.\n\n## Main Findings on Speech vs. Writing\n\nThe research reveals several key contrasts:\n\n1. **Structural Diversity**: \"Spoken corpora contain fewer and less diverse syntactic structures than their written counterparts\" across both languages studied.\n\n2. **Limited Overlap**: Most strikingly, \"the overlap between spoken and written syntactic inventories is very limited: most structures attested in speech do not occur in writing,\" indicating modality-specific syntactic preferences.\n\n3. **Speech-Specific Patterns**: The keyness analysis identified structures in speech \"associated with interactivity, context-grounding, and economy of expression\"—reflecting how real-time conversation differs from planned written composition.\n\n4. **Cross-Linguistic Consistency**: The study found \"consistent cross-linguistic preferences for certain structural types across modalities,\" suggesting universal patterns in how speech and writing differ syntactically.\n\nThe framework offers a scalable, language-independent methodology for examining syntactic variation across different corpora.", "durationMs": 4416, "url": "https://arxiv.org/abs/2505.22774"}
```

### [54] TOOL RESULT — WebSearch · 2026-08-13 11:34:29 UTC

```
{"query": "HuggingFace datasets universal_dependencies commul download treebanks", "results": [{"tool_use_id": "srvtoolu_014oyYGHCxPKdKsy3Xi9p8mv", "content": [{"title": "commul/universal_dependencies · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/commul/universal_dependencies"}, {"title": "Continual Learning in Recurrent Neural Networks", "url": "https://arxiv.org/pdf/2006.12109"}, {"title": "Universal Dependencies", "url": "https://universaldependencies.org/"}, {"title": "universal_dependencies | TensorFlow Datasets", "url": "https://www.tensorflow.org/datasets/catalog/universal_dependencies"}, {"title": "universal-dependencies/universal_dependencies · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/universal-dependencies/universal_dependencies"}, {"title": "Cross-Linguistic Syntactic Difference in Multilingual BERT: How Good is   It and How Does It Affect Transfer?", "url": "https://arxiv.org/pdf/2212.10879"}, {"title": "Daily Papers - Hugging Face", "url": "https://huggingface.co/papers?q=Universal+Dependencies"}, {"title": "albertvillanova/universal_dependencies · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/albertvillanova/universal_dependencies"}, {"title": "Universal Dependencies according to BERT: both more specific and more   general", "url": "https://arxiv.org/pdf/2004.14620"}, {"title": "README.md · universal-dependencies/universal_dependencies at c76366e40bc6dfc1324005f10416e3112719a12b", "url": "https://huggingface.co/datasets/universal-dependencies/universal_dependencies/blob/c76366e40bc6dfc1324005f10416e3112719a12b/README.md"}]}, "Based on the search results, I found information about Universal Dependencies datasets on Hugging Face:\n\nThere are multiple Universal Dependencies dataset options available on Hugging Face:\n\n1. **universal-dependencies/universal_dependencies** - A dataset on Hugging Face\n\n2. **commul/universal_dependencies** - A Hugging Face dataset described as part of their journey to advance and democratize artificial intelligence through open source and open science\n\n3. **albertvillanova/universal_dependencies** - Another variant available on Hugging Face\n\nThe search results indicate that the Universal Dependencies dataset on Hugging Face includes annotations for 92 languages with various treebank configurations, including multilinguality support.\n\nFor more detailed information about how to download and use these treebanks, you can visit the dataset pages directly on Hugging Face at:\n- `huggingface.co/datasets/commul/universal_dependencies`\n- `huggingface.co/datasets/universal-dependencies/universal_dependencies`\n\nThese datasets contain dependency-annotated treebanks that can be used for NLP tasks like parsing and part-of-speech tagging."], "durationSeconds": 5.412736777999991, "searchCount": 1}
```

### [55] TOOL RESULT — WebSearch · 2026-08-13 11:34:31 UTC

```
{"query": "dependency length minimization typology word order free-order language", "results": [{"tool_use_id": "srvtoolu_016rf7kAGtpH17Aov3PMfX7b", "content": [{"title": "Dependency Locality as an Explanatory Principle for Word Order | Request PDF", "url": "https://www.researchgate.net/publication/342350601_Dependency_locality_as_an_explanatory_principle_for_word_order"}, {"title": "Large-scale evidence of dependency length minimization in 37 languages | PNAS", "url": "https://www.pnas.org/doi/10.1073/pnas.1502134112"}, {"title": "The placement of the head that maximizes predictability. An information   theoretic approach", "url": "https://arxiv.org/pdf/1705.09932"}, {"title": "The Crosslinguistic Relationship between Ordering Flexibility and", "url": "https://aclanthology.org/2021.scil-1.24.pdf"}, {"title": "Word Order Typology Interacts With Linguistic Complexity: A Cross‐Linguistic Corpus Study - Yadav - 2020 - Cognitive Science - Wiley Online Library", "url": "https://onlinelibrary.wiley.com/doi/full/10.1111/cogs.12822"}, {"title": "Generalized Optimal Linear Orders", "url": "https://arxiv.org/pdf/2108.10692"}, {"title": "Dependency-length minimization and its limits: A possible", "url": "https://www.diva-portal.org/smash/get/diva2:1712963/FULLTEXT01.pdf"}, {"title": "Dependency length minimization vs. word order constraints", "url": "https://aclanthology.org/W19-7911.pdf"}, {"title": "Bounds of the sum of edge lengths in linear arrangements of trees", "url": "https://arxiv.org/pdf/2006.14069"}]}, "Here are the search results for your query on dependency length minimization, typology, word order, and free-order languages:\n\n**Key Findings:**\n\nDependency length minimization (DLM) is a well-documented processing universal, and research has shown this principle operates differently across languages depending on their word-order typology.\n\nGrammar-driven optimization targets functional dependencies (det, case, aux), which are universally short and invariant across typologically diverse languages, while processing-driven optimization operates on lexical dependencies (nsubj, obj, obl), which are longer, highly variable, and constrained by word-order typology.\n\nHead-final languages tend to have longer dependency length as compared to other languages, suggesting that word-order typology plays a significant role in how dependency length minimization manifests across languages.\n\nSpeakers prefer word orders with short dependency lengths and languages do not enforce word orders with long dependency lengths, because dependency length minimization allows for more efficient parsing and generation of natural language.\n\nThe relationship between word-order freedom and dependency length minimization appears complex, with dependency-length minimization being inversely correlated with the overall presence of head-final dependencies after controlling for harmony and conditioning on dependency types."], "durationSeconds": 6.777059710000001, "searchCount": 1}
```

### [56] ASSISTANT · 2026-08-13 11:34:35 UTC

```
Let me get more specific information about the HuggingFace dataset structure:
```

### [57] TOOL CALL — WebFetch · 2026-08-13 11:34:35 UTC

```
URL: https://huggingface.co/datasets/commul/universal_dependencies
Prompt: What treebanks are available? How can you access genre/modality metadata? What fields are in the dataset?
```

### [58] TOOL CALL — WebSearch · 2026-08-13 11:34:35 UTC

```
lifelines CoxPHFitter frailty shared random effects documentation
```

### [59] TOOL RESULT — WebFetch · 2026-08-13 11:34:37 UTC

```
{"bytes": 5291440, "code": 200, "codeText": "OK", "result": "I appreciate your question, but I notice the web page content you've referenced appears to be truncated or missing. The section marked \"[Content truncated due to length...]\" means I don't have the actual information needed to answer your questions about:\n\n- Which treebanks are available\n- How to access genre/modality metadata\n- What fields exist in the dataset\n\nTo provide accurate information following your guidelines, I would need the complete web page content. Could you please share the full text or a working link to the resource you're asking about? Once you provide the complete content, I'll be happy to give you a concise answer with properly formatted quotes (under 125 characters each) and paraphrased explanations.", "durationMs": 3472, "url": "https://huggingface.co/datasets/commul/universal_dependencies"}
```

### [60] TOOL RESULT — WebSearch · 2026-08-13 11:34:41 UTC

```
{"query": "lifelines CoxPHFitter frailty shared random effects documentation", "results": [{"tool_use_id": "srvtoolu_0149sHzrqbLH8NyEumhYR7z2", "content": [{"title": "Code Lifespan Survival Analysis (CLSA): Predicting the Survival of Source Code Lines Using AST-Aware Mining", "url": "https://arxiv.org/pdf/2606.04993"}, {"title": "A Cox Model with Shared Frailty", "url": "https://grodri.github.io/survival/frailtyr"}, {"title": "frailty: Random effects terms in survival: Survival Analysis", "url": "https://rdrr.io/cran/survival/man/frailty.html"}, {"title": "Laplacian-P-splines for shared Gamma frailty models applied to clustered right-censored time-to-event data", "url": "https://arxiv.org/pdf/2605.12092"}, {"title": "Survival regression — lifelines 0.30.3 documentation", "url": "https://lifelines.readthedocs.io/en/latest/Survival%20Regression.html"}, {"title": "Shared Frailty Methods for Complex Survival Data: A Review of Recent   Advances", "url": "https://arxiv.org/pdf/2205.05322"}, {"title": "CoxPHFitter — lifelines 0.30.0 documentation", "url": "https://lifelines.readthedocs.io/en/stable/fitters/regression/CoxPHFitter.html"}, {"title": "frailty Random effects terms", "url": "https://www.rdocumentation.org/packages/survival/versions/3.8-3/topics/frailty"}, {"title": "CoxPHFitter — lifelines 0.30.3 documentation - Read the Docs", "url": "https://lifelines.readthedocs.io/en/latest/fitters/regression/CoxPHFitter.html"}]}, "Based on the search results, I found documentation on lifelines' CoxPHFitter. The implementation of the Cox model in lifelines is under CoxPHFitter. The official lifelines documentation shows the basic usage of CoxPHFitter, including methods like `fit()`, `print_summary()`, and visualization functions.\n\nHowever, the search results do not contain specific documentation about frailty models, shared random effects, or how to implement these features in CoxPHFitter. While the results discuss frailty models in general and their implementation in R's survival package, they don't show the corresponding functionality in lifelines' CoxPHFitter.\n\nTo find information specifically about frailty models in lifelines, you may want to:\n1. Check the official lifelines documentation directly at https://lifelines.readthedocs.io/\n2. Look at the lifelines GitHub repository for examples or open issues related to frailty models\n3. Check if there's a separate class for shared frailty models in lifelines (such as CoxTimeVaryingFitter or similar)\n\nThe search results suggest that while R's survival package has built-in frailty functions, the lifelines documentation retrieved here focuses on stratification and penalization features rather than frailty terms."], "durationSeconds": 6.044147935000001, "searchCount": 1}
```

### [61] ASSISTANT · 2026-08-13 11:35:43 UTC

```
Now I have enough information to create a detailed research plan. Let me write it out:
```

### [62] TOOL CALL — Write · 2026-08-13 11:35:43 UTC

```
File: /tmp/claude-0/-ai-inventor-aii-data-runs-run-oQQwThF8kM-b-3-invention-loop-iter-1-gen-plan-gen-plan-research-1/d080fb08-09ee-4a4d-8d50-6eb8d7066ffd/scratchpad/research_plan_output.json

{
  "title": "Survival Analysis Foundations for Dependency Arc Modeling",
  "summary": "Research foundational literature on survival analysis precedent in linguistics, the DLM length-mixing confound, spoken-vs-written register variation in UD treebanks, and theoretical justification for modeling dependency arcs as right-censored time-to-event processes.",
  "runpod_compute_profile": "cpu_light",
  "question": "Can dependency arcs in UD treebanks be rigorously modeled as censored time-to-event processes using survival-analysis tools, and what is the precedent in linguistics for this approach?",
  "explanation": "The hypothesis proposes a novel methodological reframing of dependency-length minimization (DLM) using survival analysis. Current DLM research uses pooled mean dependency distances, which conflate sentence-length effects with genuine linguistic preferences—a documented confound (Ferrer-i-Cancho et al., 2013). Survival analysis (Kaplan-Meier, Cox models with frailty) is the standard biostatistical tool for data whose maximum observable value is bounded by a covariate (here, word position → censoring bound). This research establishes the theoretical and empirical foundation for importing this methodology: (1) confirming the length-mixing confound and its implications, (2) surveying how survival analysis has been applied to behavioral/linguistic data with position-bounded outcomes, (3) cataloging which UD treebanks contain paired spoken/written data and typological metadata, and (4) articulating why modeling arc length as a time-to-event outcome is a valid reframing. This foundation justifies the later implementation step.",
  "research_plan": "## Research Plan: Survival-Analysis Foundations for Dependency Arc Modeling\n\n### PART 1: Confirm the Methodological Problem (Length-Mixing Confound)\n\n**Objective**: Deeply understand and document Ferrer-i-Cancho et al.'s identified length-mixing confound and its specific implications for cross-language/register comparisons.\n\n**Searches**:\n1. Ferrer-i-Cancho & Liu (2013) \"The risks of mixing dependency lengths from sequences of different length\" (arXiv:1304.3841):\n   - What exactly is the mathematical/statistical mechanism of the confound? (distortion in mean, variance, shape?)\n   - What examples do they show (which language pairs, which direction does confound bias?)\n   - What corrections do they recommend, and why are they partial fixes?\n   - How does sentence-length distribution differ across languages/registers?\n\n2. Follow-up DLM papers citing Ferrer-i-Cancho (search: \"dependency length mixing\", \"sentence length confound DLM\"):\n   - How have subsequent studies tried to control for this? (normalization by sentence length? random-baseline comparisons?)\n   - Has any study fully solved the problem, or do they all acknowledge the residual risk?\n   - Does Futrell et al. (PNAS 2015) on 37 languages address this confound explicitly?\n\n3. Recent methodological critiques (search: \"dependency length minimization methodology\", \"reappraisal DLM linguistic universal\"):\n   - What methodological review papers exist on DLM? (PMC/arXiv: \"A Reappraisal of Dependency Length Minimization...\")\n   - Do they propose alternatives to pooled-mean comparisons?\n\n**Expected output**: \n- 200–300 words summarizing the confound's mechanism, consequences, and known partial corrections\n- A clear statement of why this confound matters for the survival-analysis reframing (censoring naturally controls for it)\n\n---\n\n### PART 2: Survey Survival-Analysis Precedent in Linguistics\n\n**Objective**: Determine whether survival analysis (Kaplan-Meier, Cox models, frailty terms) has ever been applied to linguistic or behavioral data with position-bounded outcomes, and establish theoretical precedent for the proposed reframing.\n\n**Searches**:\n1. Direct searches for survival analysis + linguistics:\n   - \"survival analysis linguistics\"\n   - \"Kaplan-Meier language\" or \"Cox proportional hazards language\"\n   - \"time-to-event linguistics\" or \"censoring linguistic data\"\n   - Result: Likely none or very few—this may be genuinely novel. Document if zero results.\n\n2. Boundary-condition / position-bounded time-to-event data in other fields (search: \"right-censoring position-bounded\", \"time-to-event covariate maximum\", \"censoring sequential data\"):\n   - Are there examples in psycholinguistics (reading times, eye-tracking)? psychology? behavioral ecology?\n   - How do researchers model outcomes where the maximum possible value depends on a position/sequence parameter?\n\n3. Theoretical justification via biostatistics handbooks:\n   - Search: \"censoring definition survival analysis\", \"right-censoring meaning\", \"time-to-event basics\"\n   - Document what makes an outcome eligibly \"censored\" and why dependency arcs fit that definition\n   - Key insight: A word near a sentence boundary cannot produce a long arc, just as a patient enrolled late in a trial cannot accumulate long follow-up time. Both are censored, not truly event-free.\n\n**Expected output**:\n- 300–400 words on precedent (or lack thereof) for survival analysis in linguistics\n- A focused section (200 words) titled \"Why dependency arcs are valid time-to-event objects\" that explains:\n  - Right-censoring definition and mechanism\n  - Why arc length ≤ min(position, sentence_length − position) is analogous to patient follow-up ≤ enrollment_time + trial_length\n  - Why Kaplan-Meier / Cox assume independence within a cluster (here, no assumptions violated)\n  - Why hazard h(d | arc ≥ d) is a meaningful quantity (it measures instantaneous risk of closure at each distance)\n\n---\n\n### PART 3: Catalog UD Treebanks with Spoken/Written and Typological Metadata\n\n**Objective**: Identify which UD treebanks have paired spoken and written corpora for the same language, and which have accessible typological metadata (word order, morphological richness).\n\n**Searches**:\n1. HuggingFace commul/universal_dependencies dataset:\n   - Document how to access the dataset programmatically\n   - List all treebanks with genre/modality metadata fields\n   - Which treebanks have \"spoken\" or \"speech\" tags? Which have paired written variants?\n\n2. Comprehensive UD treebank catalog (search: \"Universal Dependencies treebanks complete list 2025\", \"UD v2.14 treebank inventory\"):\n   - English-GUM: Has spoken subset. Which splits/sentences?\n   - Slovenian-SST (spoken) and SSJ (written): Paired languages—yes. Same annotation standard?\n   - French: Rhapsodie (spoken) and GSD/ParisStories (written)?—confirm pairing\n   - Cantonese-HK: Spoken (legislative). Is there written Cantonese treebank?\n   - Komi-Zyrian: Has spoken variant?\n   - Polish-LFG: Genre-marked spoken?\n   - German: Mixed-genre? Any spoken?\n   - Compile final list with language, spoken corpus name, written corpus name, sentence/token counts\n\n3. Typological metadata (search: \"WALS word order parameters 2026\", \"Grambank morphological richness\", \"UD morphological features language\"):\n   - Which languages in the catalog have WALS word-order annotation (SVO, SOV, VSO, free-order)?\n   - Which have Grambank data on morphological synthesis?\n   - For languages without these, can you use UD's morphological feature inventory as a proxy? (count unique FEATS values per token)\n\n**Expected output**:\n- A structured table (CSV/JSON-like) with columns:\n  - Language | Spoken_Treebank | Written_Treebank | Paired_Y/N | Spoken_Tokens | Written_Tokens | Word_Order | Morphology_Source\n- At least 6–10 language pairs with confirmed paired spoken/written data\n- A note on data accessibility: Can all be downloaded via HuggingFace or UD homepage?\n- Flagged gaps: Which typologically interesting languages are missing? (e.g., if all are SVO + rich morphology, note lack of free-order languages)\n\n---\n\n### PART 4: Review Recent Speech vs. Writing DLM Studies\n\n**Objective**: Understand how current DLM research characterizes spoken vs. written registers, what pooled-mean approaches find, and what the new survival lens might reveal.\n\n**Key papers to deeply read**:\n1. **Dobrovoljc et al. (2025)** \"Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages\" (arXiv:2505.22774):\n   - Uses English-GUM and Slovenian-SST/SSJ\n   - Finds: spoken has fewer, less diverse syntactic structures; limited overlap between modalities\n   - Is DLM mentioned? If so, how?\n   - Key finding for hypothesis: If speech and writing differ in structure, do they differ in *hazard shape*?\n\n2. **Futrell et al. (PNAS 2015)** \"Large-scale evidence of dependency length minimization in 37 languages\":\n   - Methodology: how do they normalize for sentence length? Do they acknowledge the mixing confound?\n   - Findings on cross-language variation in MDD\n   - Does it include any speech data, or is it all written?\n\n3. **SCiL 2021 cross-linguistic speech vs. writing study** (if identifiable via search: \"dependency length spoken written SCiL 2021\"):\n   - What are the directional effects? (longer spoken? shorter? varies by language?)\n   - Do they use paired treebanks?\n   - How do they normalize for sentence length?\n\n4. **Recent UD-based functional vs. lexical DLM** (2026 work mentioned in hypothesis):\n   - Confirms that dependency *type* (functional vs. lexical) explains variance in DLM\n   - Implication: hazard curves might differ by dependency type as well as register\n\n**Expected output**:\n- 300–400 words summarizing:\n  - What pooled-mean studies report about speech vs. writing DLM (directional findings, language variation)\n  - Limitations of pooled-mean approaches that a hazard-curve lens could overcome\n  - Specific predictions: If spoken is front-loaded (quick closure) vs. written (flat/delayed), what would Kaplan-Meier curves show?\n  - How the survival reframing naturally stratifies by dependency type without extra modeling\n\n---\n\n### PART 5: Establish Technical Feasibility of Survival-Analysis Tools\n\n**Objective**: Confirm that Python survival-analysis libraries (lifelines, scikit-survival) can fit Kaplan-Meier, Cox, and frailty models at UD scale (10k to 1M arcs) and understand their API and limitations.\n\n**Searches**:\n1. **lifelines library** (https://lifelines.readthedocs.io/):\n   - What models does it support? (Kaplan-Meier ✓, Nelson-Aalen ✓, Cox PH ✓, ... frailty?)\n   - Does CoxPHFitter support shared frailty / random effects, or only stratification/penalization?\n   - If not, what workarounds exist? (e.g., fit Cox models per-family separately and compare coefficients?)\n   - Performance: has anyone fit it to 100k+ observations? Any known scaling issues?\n\n2. **scikit-survival library**:\n   - Does it support Cox PH with frailty terms?\n   - Any advantages/disadvantages vs. lifelines for large datasets?\n\n3. **Alternatives** (search: \"Python Cox frailty model\", \"Python shared frailty survival\"):\n   - PyMC3/PyMC for Bayesian frailty models?\n   - statsmodels?\n   - If built-in frailty is unavailable, what is the standard workaround in literature? (manual specification, two-stage fitting?)\n\n**Expected output**:\n- 200–250 words on tools:\n  - Which library to use for Kaplan-Meier / Nelson-Aalen (likely lifelines)\n  - Which library / approach for Cox PH (lifelines; confirm stratification suffices if frailty unavailable)\n  - Frailty term options: built-in vs. workaround (e.g., Bayesian approach or two-stage)\n  - Scaling: Can it handle 1M+ arcs? Any batch-processing considerations?\n- Code snippet outline (pseudocode) showing:\n  - Data format (duration, event, censoring indicator, covariates) for a single arc\n  - How to set up the data from UD treebanks\n  - Pseudocode for Kaplan-Meier fit per language/register\n  - Pseudocode for Cox model with language-family stratification (fallback if frailty unavailable)\n\n---\n\n### PART 6: Synthesize Theoretical Justification\n\n**Objective**: Write a coherent 500-word section that brings together why survival analysis is the right tool for this problem, addressing all assumptions in the hypothesis.\n\n**Content to synthesize**:\n1. **The confound (Part 1)**: Length-mixing distorts pooled-mean comparisons; survival analysis naturally handles this via the censoring mechanism.\n2. **Lack of precedent (Part 2)**: This is novel; no prior linguistics DLM work uses survival tools. Explain why the tool was overlooked and why it fits perfectly.\n3. **Valid reframing (Part 4)**: Explain why arc length is a valid time-to-event outcome:\n   - Event = arc closes (occurs at distance d)\n   - Time = distance in tokens\n   - Censoring = arc would exceed sentence boundary\n   - Conditional hazard h(d | arc ≥ d, position ≤ max_d) = instantaneous risk of closure at d\n4. **Testable assumptions (all assumptions from hypothesis)**:\n   - UD provides well-defined linear positions and head positions ✓ (confirmed in datasets)\n   - Paired spoken/written treebanks exist (Part 3: confirmed)\n   - Arc-length as time-to-event is valid (Part 2: explained)\n   - Survival software can scale to UD (Part 5: confirmed)\n   - Language family is a defensible frailty grouping (cite Glottolog, explain why family matters more than distant genealogy)\n\n**Expected output**:\n- 400–600 words titled \"Theoretical Justification: Why Survival Analysis Fits Dependency-Arc Modeling\"\n- Subsections:\n  - \"The Length-Mixing Confound and Its Solution\" (100 words)\n  - \"Arc Length as a Time-to-Event Outcome\" (150 words)\n  - \"Hazard Functions Capture Shape Information Pooled Means Cannot\" (100 words)\n  - \"Language Family as Frailty Term\" (100 words)\n  - \"Assumptions: Verification and Implications\" (100–150 words)\n\n---\n\n## Deliverables\n\nThe research executor will produce:\n- **research_out.json**: Structured answers to each section above\n- **research_report.md**: A cohesive narrative (1500–2000 words) combining:\n  1. The length-mixing confound (200 words)\n  2. Survival-analysis precedent in linguistics (300 words)\n  3. Catalog of suitable UD treebanks (300 words: table + narrative on coverage)\n  4. Recent speech vs. writing DLM findings (300 words)\n  5. Technical feasibility of tools (200 words)\n  6. Theoretical justification (500–600 words)\n\n## Failure Scenarios and Mitigations\n\n1. **No paired spoken/written treebanks found**: Mitigate by documenting ALL treebanks with genre/modality metadata (even if not perfectly paired), and flag which languages admit no within-language register comparison. Plan may pivot to primarily cross-language typology comparison.\n\n2. **Frailty models unavailable in lifelines**: Mitigate by documenting stratified Cox alternatives (fit per-family, compare coefficients) and Bayesian approaches. Surveyable and defensible, though less elegant than integrated frailty.\n\n3. **Survival analysis truly never applied to linguistics**: Document this as the novelty and justify the transfer from biostatistics. Not a blocker; reframe as a methodological innovation.\n\n4. **Length-mixing confound is already solved in literature**: Mitigate by carefully reviewing proposed solutions (do they fully control variance, or only mean? do they preserve distributional shape information?) and clarifying how survival analysis is *still* an improvement (hazard curves are a richer object than normalized means).\n\n## Success Criteria for This Research Phase\n\n✓ Ferrer-i-Cancho confound explained with mathematical precision (mechanism, examples, partial solutions documented)  \n✓ Survival-analysis precedent surveyed (likely finding: no prior linguistics application; transfer justified)  \n✓ At least 6 language pairs with paired spoken/written treebanks cataloged  \n✓ Typological metadata (word order, morphology) sourced for all languages  \n✓ Kaplan-Meier and Cox PH feasibility confirmed; frailty term approach decided (built-in vs. workaround)  \n✓ Theoretical justification written and coherent across all assumptions  \n✓ Ready to hand off to executor: implementation plan is now concrete, not speculative"
}
```

### [63] TOOL RESULT — Write · 2026-08-13 11:35:43 UTC

```
{"type": "create", "filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-oQQwThF8kM-b-3-invention-loop-iter-1-gen-plan-gen-plan-research-1/d080fb08-09ee-4a4d-8d50-6eb8d7066ffd/scratchpad/research_plan_output.json", "content": "{\n  \"title\": \"Survival Analysis Foundations for Dependency Arc Modeling\",\n  \"summary\": \"Research foundational literature on survival analysis precedent in linguistics, the DLM length-mixing confound, spoken-vs-written register variation in UD treebanks, and theoretical justification for modeling dependency arcs as right-censored time-to-event processes.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"question\": \"Can dependency arcs in UD treebanks be rigorously modeled as censored time-to-event processes using survival-analysis tools, and what is the precedent in linguistics for this approach?\",\n  \"explanation\": \"The hypothesis proposes a novel methodological reframing of dependency-length minimization (DLM) using survival analysis. Current DLM research uses pooled mean dependency distances, which conflate sentence-length effects with genuine linguistic preferences—a documented confound (Ferrer-i-Cancho et al., 2013). Survival analysis (Kaplan-Meier, Cox models with frailty) is the standard biostatistical tool for data whose maximum observable value is bounded by a covariate (here, word position → censoring bound). This research establishes the theoretical and empirical foundation for importing this methodology: (1) confirming the length-mixing confound and its implications, (2) surveying how survival analysis has been applied to behavioral/linguistic data with position-bounded outcomes, (3) cataloging which UD treebanks contain paired spoken/written data and typological metadata, and (4) articulating why modeling arc length as a time-to-event outcome is a valid reframing. This foundation justifies the later implementation step.\",\n  \"research_plan\": \"## Research Plan: Survival-Analysis Foundations for Dependency Arc Modeling\\n\\n### PART 1: Confirm the Methodological Problem (Length-Mixing Confound)\\n\\n**Objective**: Deeply understand and document Ferrer-i-Cancho et al.'s identified length-mixing confound and its specific implications for cross-language/register comparisons.\\n\\n**Searches**:\\n1. Ferrer-i-Cancho & Liu (2013) \\\"The risks of mixing dependency lengths from sequences of different length\\\" (arXiv:1304.3841):\\n   - What exactly is the mathematical/statistical mechanism of the confound? (distortion in mean, variance, shape?)\\n   - What examples do they show (which language pairs, which direction does confound bias?)\\n   - What corrections do they recommend, and why are they partial fixes?\\n   - How does sentence-length distribution differ across languages/registers?\\n\\n2. Follow-up DLM papers citing Ferrer-i-Cancho (search: \\\"dependency length mixing\\\", \\\"sentence length confound DLM\\\"):\\n   - How have subsequent studies tried to control for this? (normalization by sentence length? random-baseline comparisons?)\\n   - Has any study fully solved the problem, or do they all acknowledge the residual risk?\\n   - Does Futrell et al. (PNAS 2015) on 37 languages address this confound explicitly?\\n\\n3. Recent methodological critiques (search: \\\"dependency length minimization methodology\\\", \\\"reappraisal DLM linguistic universal\\\"):\\n   - What methodological review papers exist on DLM? (PMC/arXiv: \\\"A Reappraisal of Dependency Length Minimization...\\\")\\n   - Do they propose alternatives to pooled-mean comparisons?\\n\\n**Expected output**: \\n- 200–300 words summarizing the confound's mechanism, consequences, and known partial corrections\\n- A clear statement of why this confound matters for the survival-analysis reframing (censoring naturally controls for it)\\n\\n---\\n\\n### PART 2: Survey Survival-Analysis Precedent in Linguistics\\n\\n**Objective**: Determine whether survival analysis (Kaplan-Meier, Cox models, frailty terms) has ever been applied to linguistic or behavioral data with position-bounded outcomes, and establish theoretical precedent for the proposed reframing.\\n\\n**Searches**:\\n1. Direct searches for survival analysis + linguistics:\\n   - \\\"survival analysis linguistics\\\"\\n   - \\\"Kaplan-Meier language\\\" or \\\"Cox proportional hazards language\\\"\\n   - \\\"time-to-event linguistics\\\" or \\\"censoring linguistic data\\\"\\n   - Result: Likely none or very few—this may be genuinely novel. Document if zero results.\\n\\n2. Boundary-condition / position-bounded time-to-event data in other fields (search: \\\"right-censoring position-bounded\\\", \\\"time-to-event covariate maximum\\\", \\\"censoring sequential data\\\"):\\n   - Are there examples in psycholinguistics (reading times, eye-tracking)? psychology? behavioral ecology?\\n   - How do researchers model outcomes where the maximum possible value depends on a position/sequence parameter?\\n\\n3. Theoretical justification via biostatistics handbooks:\\n   - Search: \\\"censoring definition survival analysis\\\", \\\"right-censoring meaning\\\", \\\"time-to-event basics\\\"\\n   - Document what makes an outcome eligibly \\\"censored\\\" and why dependency arcs fit that definition\\n   - Key insight: A word near a sentence boundary cannot produce a long arc, just as a patient enrolled late in a trial cannot accumulate long follow-up time. Both are censored, not truly event-free.\\n\\n**Expected output**:\\n- 300–400 words on precedent (or lack thereof) for survival analysis in linguistics\\n- A focused section (200 words) titled \\\"Why dependency arcs are valid time-to-event objects\\\" that explains:\\n  - Right-censoring definition and mechanism\\n  - Why arc length ≤ min(position, sentence_length − position) is analogous to patient follow-up ≤ enrollment_time + trial_length\\n  - Why Kaplan-Meier / Cox assume independence within a cluster (here, no assumptions violated)\\n  - Why hazard h(d | arc ≥ d) is a meaningful quantity (it measures instantaneous risk of closure at each distance)\\n\\n---\\n\\n### PART 3: Catalog UD Treebanks with Spoken/Written and Typological Metadata\\n\\n**Objective**: Identify which UD treebanks have paired spoken and written corpora for the same language, and which have accessible typological metadata (word order, morphological richness).\\n\\n**Searches**:\\n1. HuggingFace commul/universal_dependencies dataset:\\n   - Document how to access the dataset programmatically\\n   - List all treebanks with genre/modality metadata fields\\n   - Which treebanks have \\\"spoken\\\" or \\\"speech\\\" tags? Which have paired written variants?\\n\\n2. Comprehensive UD treebank catalog (search: \\\"Universal Dependencies treebanks complete list 2025\\\", \\\"UD v2.14 treebank inventory\\\"):\\n   - English-GUM: Has spoken subset. Which splits/sentences?\\n   - Slovenian-SST (spoken) and SSJ (written): Paired languages—yes. Same annotation standard?\\n   - French: Rhapsodie (spoken) and GSD/ParisStories (written)?—confirm pairing\\n   - Cantonese-HK: Spoken (legislative). Is there written Cantonese treebank?\\n   - Komi-Zyrian: Has spoken variant?\\n   - Polish-LFG: Genre-marked spoken?\\n   - German: Mixed-genre? Any spoken?\\n   - Compile final list with language, spoken corpus name, written corpus name, sentence/token counts\\n\\n3. Typological metadata (search: \\\"WALS word order parameters 2026\\\", \\\"Grambank morphological richness\\\", \\\"UD morphological features language\\\"):\\n   - Which languages in the catalog have WALS word-order annotation (SVO, SOV, VSO, free-order)?\\n   - Which have Grambank data on morphological synthesis?\\n   - For languages without these, can you use UD's morphological feature inventory as a proxy? (count unique FEATS values per token)\\n\\n**Expected output**:\\n- A structured table (CSV/JSON-like) with columns:\\n  - Language | Spoken_Treebank | Written_Treebank | Paired_Y/N | Spoken_Tokens | Written_Tokens | Word_Order | Morphology_Source\\n- At least 6–10 language pairs with confirmed paired spoken/written data\\n- A note on data accessibility: Can all be downloaded via HuggingFace or UD homepage?\\n- Flagged gaps: Which typologically interesting languages are missing? (e.g., if all are SVO + rich morphology, note lack of free-order languages)\\n\\n---\\n\\n### PART 4: Review Recent Speech vs. Writing DLM Studies\\n\\n**Objective**: Understand how current DLM research characterizes spoken vs. written registers, what pooled-mean approaches find, and what the new survival lens might reveal.\\n\\n**Key papers to deeply read**:\\n1. **Dobrovoljc et al. (2025)** \\\"Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages\\\" (arXiv:2505.22774):\\n   - Uses English-GUM and Slovenian-SST/SSJ\\n   - Finds: spoken has fewer, less diverse syntactic structures; limited overlap between modalities\\n   - Is DLM mentioned? If so, how?\\n   - Key finding for hypothesis: If speech and writing differ in structure, do they differ in *hazard shape*?\\n\\n2. **Futrell et al. (PNAS 2015)** \\\"Large-scale evidence of dependency length minimization in 37 languages\\\":\\n   - Methodology: how do they normalize for sentence length? Do they acknowledge the mixing confound?\\n   - Findings on cross-language variation in MDD\\n   - Does it include any speech data, or is it all written?\\n\\n3. **SCiL 2021 cross-linguistic speech vs. writing study** (if identifiable via search: \\\"dependency length spoken written SCiL 2021\\\"):\\n   - What are the directional effects? (longer spoken? shorter? varies by language?)\\n   - Do they use paired treebanks?\\n   - How do they normalize for sentence length?\\n\\n4. **Recent UD-based functional vs. lexical DLM** (2026 work mentioned in hypothesis):\\n   - Confirms that dependency *type* (functional vs. lexical) explains variance in DLM\\n   - Implication: hazard curves might differ by dependency type as well as register\\n\\n**Expected output**:\\n- 300–400 words summarizing:\\n  - What pooled-mean studies report about speech vs. writing DLM (directional findings, language variation)\\n  - Limitations of pooled-mean approaches that a hazard-curve lens could overcome\\n  - Specific predictions: If spoken is front-loaded (quick closure) vs. written (flat/delayed), what would Kaplan-Meier curves show?\\n  - How the survival reframing naturally stratifies by dependency type without extra modeling\\n\\n---\\n\\n### PART 5: Establish Technical Feasibility of Survival-Analysis Tools\\n\\n**Objective**: Confirm that Python survival-analysis libraries (lifelines, scikit-survival) can fit Kaplan-Meier, Cox, and frailty models at UD scale (10k to 1M arcs) and understand their API and limitations.\\n\\n**Searches**:\\n1. **lifelines library** (https://lifelines.readthedocs.io/):\\n   - What models does it support? (Kaplan-Meier ✓, Nelson-Aalen ✓, Cox PH ✓, ... frailty?)\\n   - Does CoxPHFitter support shared frailty / random effects, or only stratification/penalization?\\n   - If not, what workarounds exist? (e.g., fit Cox models per-family separately and compare coefficients?)\\n   - Performance: has anyone fit it to 100k+ observations? Any known scaling issues?\\n\\n2. **scikit-survival library**:\\n   - Does it support Cox PH with frailty terms?\\n   - Any advantages/disadvantages vs. lifelines for large datasets?\\n\\n3. **Alternatives** (search: \\\"Python Cox frailty model\\\", \\\"Python shared frailty survival\\\"):\\n   - PyMC3/PyMC for Bayesian frailty models?\\n   - statsmodels?\\n   - If built-in frailty is unavailable, what is the standard workaround in literature? (manual specification, two-stage fitting?)\\n\\n**Expected output**:\\n- 200–250 words on tools:\\n  - Which library to use for Kaplan-Meier / Nelson-Aalen (likely lifelines)\\n  - Which library / approach for Cox PH (lifelines; confirm stratification suffices if frailty unavailable)\\n  - Frailty term options: built-in vs. workaround (e.g., Bayesian approach or two-stage)\\n  - Scaling: Can it handle 1M+ arcs? Any batch-processing considerations?\\n- Code snippet outline (pseudocode) showing:\\n  - Data format (duration, event, censoring indicator, covariates) for a single arc\\n  - How to set up the data from UD treebanks\\n  - Pseudocode for Kaplan-Meier fit per language/register\\n  - Pseudocode for Cox model with language-family stratification (fallback if frailty unavailable)\\n\\n---\\n\\n### PART 6: Synthesize Theoretical Justification\\n\\n**Objective**: Write a coherent 500-word section that brings together why survival analysis is the right tool for this problem, addressing all assumptions in the hypothesis.\\n\\n**Content to synthesize**:\\n1. **The confound (Part 1)**: Length-mixing distorts pooled-mean comparisons; survival analysis naturally handles this via the censoring mechanism.\\n2. **Lack of precedent (Part 2)**: This is novel; no prior linguistics DLM work uses survival tools. Explain why the tool was overlooked and why it fits perfectly.\\n3. **Valid reframing (Part 4)**: Explain why arc length is a valid time-to-event outcome:\\n   - Event = arc closes (occurs at distance d)\\n   - Time = distance in tokens\\n   - Censoring = arc would exceed sentence boundary\\n   - Conditional hazard h(d | arc ≥ d, position ≤ max_d) = instantaneous risk of closure at d\\n4. **Testable assumptions (all assumptions from hypothesis)**:\\n   - UD provides well-defined linear positions and head positions ✓ (confirmed in datasets)\\n   - Paired spoken/written treebanks exist (Part 3: confirmed)\\n   - Arc-length as time-to-event is valid (Part 2: explained)\\n   - Survival software can scale to UD (Part 5: confirmed)\\n   - Language family is a defensible frailty grouping (cite Glottolog, explain why family matters more than distant genealogy)\\n\\n**Expected output**:\\n- 400–600 words titled \\\"Theoretical Justification: Why Survival Analysis Fits Dependency-Arc Modeling\\\"\\n- Subsections:\\n  - \\\"The Length-Mixing Confound and Its Solution\\\" (100 words)\\n  - \\\"Arc Length as a Time-to-Event Outcome\\\" (150 words)\\n  - \\\"Hazard Functions Capture Shape Information Pooled Means Cannot\\\" (100 words)\\n  - \\\"Language Family as Frailty Term\\\" (100 words)\\n  - \\\"Assumptions: Verification and Implications\\\" (100–150 words)\\n\\n---\\n\\n## Deliverables\\n\\nThe research executor will produce:\\n- **research_out.json**: Structured answers to each section above\\n- **research_report.md**: A cohesive narrative (1500–2000 words) combining:\\n  1. The length-mixing confound (200 words)\\n  2. Survival-analysis precedent in linguistics (300 words)\\n  3. Catalog of suitable UD treebanks (300 words: table + narrative on coverage)\\n  4. Recent speech vs. writing DLM findings (300 words)\\n  5. Technical feasibility of tools (200 words)\\n  6. Theoretical justification (500–600 words)\\n\\n## Failure Scenarios and Mitigations\\n\\n1. **No paired spoken/written treebanks found**: Mitigate by documenting ALL treebanks with genre/modality metadata (even if not perfectly paired), and flag which languages admit no within-language register comparison. Plan may pivot to primarily cross-language typology comparison.\\n\\n2. **Frailty models unavailable in lifelines**: Mitigate by documenting stratified Cox alternatives (fit per-family, compare coefficients) and Bayesian approaches. Surveyable and defensible, though less elegant than integrated frailty.\\n\\n3. **Survival analysis truly never applied to linguistics**: Document this as the novelty and justify the transfer from biostatistics. Not a blocker; reframe as a methodological innovation.\\n\\n4. **Length-mixing confound is already solved in literature**: Mitigate by carefully reviewing proposed solutions (do they fully control variance, or only mean? do they preserve distributional shape information?) and clarifying how survival analysis is *still* an improvement (hazard curves are a richer object than normalized means).\\n\\n## Success Criteria for This Research Phase\\n\\n✓ Ferrer-i-Cancho confound explained with mathematical precision (mechanism, examples, partial solutions documented)  \\n✓ Survival-analysis precedent surveyed (likely finding: no prior linguistics application; transfer justified)  \\n✓ At least 6 language pairs with paired spoken/written treebanks cataloged  \\n✓ Typological metadata (word order, morphology) sourced for all languages  \\n✓ Kaplan-Meier and Cox PH feasibility confirmed; frailty term approach decided (built-in vs. workaround)  \\n✓ Theoretical justification written and coherent across all assumptions  \\n✓ Ready to hand off to executor: implementation plan is now concrete, not speculative\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [64] ASSISTANT · 2026-08-13 11:35:47 UTC

```
Now let me move the plan to the required output location:
```

### [65] TOOL CALL — Read · 2026-08-13 11:35:47 UTC

```
/tmp/claude-0/-ai-inventor-aii-data-runs-run-oQQwThF8kM-b-3-invention-loop-iter-1-gen-plan-gen-plan-research-1/d080fb08-09ee-4a4d-8d50-6eb8d7066ffd/scratchpad/research_plan_output.json
```

### [66] TOOL RESULT — Read · 2026-08-13 11:35:47 UTC

```
{"type": "text", "file": {"filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-oQQwThF8kM-b-3-invention-loop-iter-1-gen-plan-gen-plan-research-1/d080fb08-09ee-4a4d-8d50-6eb8d7066ffd/scratchpad/research_plan_output.json", "content": "{\n  \"title\": \"Survival Analysis Foundations for Dependency Arc Modeling\",\n  \"summary\": \"Research foundational literature on survival analysis precedent in linguistics, the DLM length-mixing confound, spoken-vs-written register variation in UD treebanks, and theoretical justification for modeling dependency arcs as right-censored time-to-event processes.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"question\": \"Can dependency arcs in UD treebanks be rigorously modeled as censored time-to-event processes using survival-analysis tools, and what is the precedent in linguistics for this approach?\",\n  \"explanation\": \"The hypothesis proposes a novel methodological reframing of dependency-length minimization (DLM) using survival analysis. Current DLM research uses pooled mean dependency distances, which conflate sentence-length effects with genuine linguistic preferences—a documented confound (Ferrer-i-Cancho et al., 2013). Survival analysis (Kaplan-Meier, Cox models with frailty) is the standard biostatistical tool for data whose maximum observable value is bounded by a covariate (here, word position → censoring bound). This research establishes the theoretical and empirical foundation for importing this methodology: (1) confirming the length-mixing confound and its implications, (2) surveying how survival analysis has been applied to behavioral/linguistic data with position-bounded outcomes, (3) cataloging which UD treebanks contain paired spoken/written data and typological metadata, and (4) articulating why modeling arc length as a time-to-event outcome is a valid reframing. This foundation justifies the later implementation step.\",\n  \"research_plan\": \"## Research Plan: Survival-Analysis Foundations for Dependency Arc Modeling\\n\\n### PART 1: Confirm the Methodological Problem (Length-Mixing Confound)\\n\\n**Objective**: Deeply understand and document Ferrer-i-Cancho et al.'s identified length-mixing confound and its specific implications for cross-language/register comparisons.\\n\\n**Searches**:\\n1. Ferrer-i-Cancho & Liu (2013) \\\"The risks of mixing dependency lengths from sequences of different length\\\" (arXiv:1304.3841):\\n   - What exactly is the mathematical/statistical mechanism of the confound? (distortion in mean, variance, shape?)\\n   - What examples do they show (which language pairs, which direction does confound bias?)\\n   - What corrections do they recommend, and why are they partial fixes?\\n   - How does sentence-length distribution differ across languages/registers?\\n\\n2. Follow-up DLM papers citing Ferrer-i-Cancho (search: \\\"dependency length mixing\\\", \\\"sentence length confound DLM\\\"):\\n   - How have subsequent studies tried to control for this? (normalization by sentence length? random-baseline comparisons?)\\n   - Has any study fully solved the problem, or do they all acknowledge the residual risk?\\n   - Does Futrell et al. (PNAS 2015) on 37 languages address this confound explicitly?\\n\\n3. Recent methodological critiques (search: \\\"dependency length minimization methodology\\\", \\\"reappraisal DLM linguistic universal\\\"):\\n   - What methodological review papers exist on DLM? (PMC/arXiv: \\\"A Reappraisal of Dependency Length Minimization...\\\")\\n   - Do they propose alternatives to pooled-mean comparisons?\\n\\n**Expected output**: \\n- 200–300 words summarizing the confound's mechanism, consequences, and known partial corrections\\n- A clear statement of why this confound matters for the survival-analysis reframing (censoring naturally controls for it)\\n\\n---\\n\\n### PART 2: Survey Survival-Analysis Precedent in Linguistics\\n\\n**Objective**: Determine whether survival analysis (Kaplan-Meier, Cox models, frailty terms) has ever been applied to linguistic or behavioral data with position-bounded outcomes, and establish theoretical precedent for the proposed reframing.\\n\\n**Searches**:\\n1. Direct searches for survival analysis + linguistics:\\n   - \\\"survival analysis linguistics\\\"\\n   - \\\"Kaplan-Meier language\\\" or \\\"Cox proportional hazards language\\\"\\n   - \\\"time-to-event linguistics\\\" or \\\"censoring linguistic data\\\"\\n   - Result: Likely none or very few—this may be genuinely novel. Document if zero results.\\n\\n2. Boundary-condition / position-bounded time-to-event data in other fields (search: \\\"right-censoring position-bounded\\\", \\\"time-to-event covariate maximum\\\", \\\"censoring sequential data\\\"):\\n   - Are there examples in psycholinguistics (reading times, eye-tracking)? psychology? behavioral ecology?\\n   - How do researchers model outcomes where the maximum possible value depends on a position/sequence parameter?\\n\\n3. Theoretical justification via biostatistics handbooks:\\n   - Search: \\\"censoring definition survival analysis\\\", \\\"right-censoring meaning\\\", \\\"time-to-event basics\\\"\\n   - Document what makes an outcome eligibly \\\"censored\\\" and why dependency arcs fit that definition\\n   - Key insight: A word near a sentence boundary cannot produce a long arc, just as a patient enrolled late in a trial cannot accumulate long follow-up time. Both are censored, not truly event-free.\\n\\n**Expected output**:\\n- 300–400 words on precedent (or lack thereof) for survival analysis in linguistics\\n- A focused section (200 words) titled \\\"Why dependency arcs are valid time-to-event objects\\\" that explains:\\n  - Right-censoring definition and mechanism\\n  - Why arc length ≤ min(position, sentence_length − position) is analogous to patient follow-up ≤ enrollment_time + trial_length\\n  - Why Kaplan-Meier / Cox assume independence within a cluster (here, no assumptions violated)\\n  - Why hazard h(d | arc ≥ d) is a meaningful quantity (it measures instantaneous risk of closure at each distance)\\n\\n---\\n\\n### PART 3: Catalog UD Treebanks with Spoken/Written and Typological Metadata\\n\\n**Objective**: Identify which UD treebanks have paired spoken and written corpora for the same language, and which have accessible typological metadata (word order, morphological richness).\\n\\n**Searches**:\\n1. HuggingFace commul/universal_dependencies dataset:\\n   - Document how to access the dataset programmatically\\n   - List all treebanks with genre/modality metadata fields\\n   - Which treebanks have \\\"spoken\\\" or \\\"speech\\\" tags? Which have paired written variants?\\n\\n2. Comprehensive UD treebank catalog (search: \\\"Universal Dependencies treebanks complete list 2025\\\", \\\"UD v2.14 treebank inventory\\\"):\\n   - English-GUM: Has spoken subset. Which splits/sentences?\\n   - Slovenian-SST (spoken) and SSJ (written): Paired languages—yes. Same annotation standard?\\n   - French: Rhapsodie (spoken) and GSD/ParisStories (written)?—confirm pairing\\n   - Cantonese-HK: Spoken (legislative). Is there written Cantonese treebank?\\n   - Komi-Zyrian: Has spoken variant?\\n   - Polish-LFG: Genre-marked spoken?\\n   - German: Mixed-genre? Any spoken?\\n   - Compile final list with language, spoken corpus name, written corpus name, sentence/token counts\\n\\n3. Typological metadata (search: \\\"WALS word order parameters 2026\\\", \\\"Grambank morphological richness\\\", \\\"UD morphological features language\\\"):\\n   - Which languages in the catalog have WALS word-order annotation (SVO, SOV, VSO, free-order)?\\n   - Which have Grambank data on morphological synthesis?\\n   - For languages without these, can you use UD's morphological feature inventory as a proxy? (count unique FEATS values per token)\\n\\n**Expected output**:\\n- A structured table (CSV/JSON-like) with columns:\\n  - Language | Spoken_Treebank | Written_Treebank | Paired_Y/N | Spoken_Tokens | Written_Tokens | Word_Order | Morphology_Source\\n- At least 6–10 language pairs with confirmed paired spoken/written data\\n- A note on data accessibility: Can all be downloaded via HuggingFace or UD homepage?\\n- Flagged gaps: Which typologically interesting languages are missing? (e.g., if all are SVO + rich morphology, note lack of free-order languages)\\n\\n---\\n\\n### PART 4: Review Recent Speech vs. Writing DLM Studies\\n\\n**Objective**: Understand how current DLM research characterizes spoken vs. written registers, what pooled-mean approaches find, and what the new survival lens might reveal.\\n\\n**Key papers to deeply read**:\\n1. **Dobrovoljc et al. (2025)** \\\"Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages\\\" (arXiv:2505.22774):\\n   - Uses English-GUM and Slovenian-SST/SSJ\\n   - Finds: spoken has fewer, less diverse syntactic structures; limited overlap between modalities\\n   - Is DLM mentioned? If so, how?\\n   - Key finding for hypothesis: If speech and writing differ in structure, do they differ in *hazard shape*?\\n\\n2. **Futrell et al. (PNAS 2015)** \\\"Large-scale evidence of dependency length minimization in 37 languages\\\":\\n   - Methodology: how do they normalize for sentence length? Do they acknowledge the mixing confound?\\n   - Findings on cross-language variation in MDD\\n   - Does it include any speech data, or is it all written?\\n\\n3. **SCiL 2021 cross-linguistic speech vs. writing study** (if identifiable via search: \\\"dependency length spoken written SCiL 2021\\\"):\\n   - What are the directional effects? (longer spoken? shorter? varies by language?)\\n   - Do they use paired treebanks?\\n   - How do they normalize for sentence length?\\n\\n4. **Recent UD-based functional vs. lexical DLM** (2026 work mentioned in hypothesis):\\n   - Confirms that dependency *type* (functional vs. lexical) explains variance in DLM\\n   - Implication: hazard curves might differ by dependency type as well as register\\n\\n**Expected output**:\\n- 300–400 words summarizing:\\n  - What pooled-mean studies report about speech vs. writing DLM (directional findings, language variation)\\n  - Limitations of pooled-mean approaches that a hazard-curve lens could overcome\\n  - Specific predictions: If spoken is front-loaded (quick closure) vs. written (flat/delayed), what would Kaplan-Meier curves show?\\n  - How the survival reframing naturally stratifies by dependency type without extra modeling\\n\\n---\\n\\n### PART 5: Establish Technical Feasibility of Survival-Analysis Tools\\n\\n**Objective**: Confirm that Python survival-analysis libraries (lifelines, scikit-survival) can fit Kaplan-Meier, Cox, and frailty models at UD scale (10k to 1M arcs) and understand their API and limitations.\\n\\n**Searches**:\\n1. **lifelines library** (https://lifelines.readthedocs.io/):\\n   - What models does it support? (Kaplan-Meier ✓, Nelson-Aalen ✓, Cox PH ✓, ... frailty?)\\n   - Does CoxPHFitter support shared frailty / random effects, or only stratification/penalization?\\n   - If not, what workarounds exist? (e.g., fit Cox models per-family separately and compare coefficients?)\\n   - Performance: has anyone fit it to 100k+ observations? Any known scaling issues?\\n\\n2. **scikit-survival library**:\\n   - Does it support Cox PH with frailty terms?\\n   - Any advantages/disadvantages vs. lifelines for large datasets?\\n\\n3. **Alternatives** (search: \\\"Python Cox frailty model\\\", \\\"Python shared frailty survival\\\"):\\n   - PyMC3/PyMC for Bayesian frailty models?\\n   - statsmodels?\\n   - If built-in frailty is unavailable, what is the standard workaround in literature? (manual specification, two-stage fitting?)\\n\\n**Expected output**:\\n- 200–250 words on tools:\\n  - Which library to use for Kaplan-Meier / Nelson-Aalen (likely lifelines)\\n  - Which library / approach for Cox PH (lifelines; confirm stratification suffices if frailty unavailable)\\n  - Frailty term options: built-in vs. workaround (e.g., Bayesian approach or two-stage)\\n  - Scaling: Can it handle 1M+ arcs? Any batch-processing considerations?\\n- Code snippet outline (pseudocode) showing:\\n  - Data format (duration, event, censoring indicator, covariates) for a single arc\\n  - How to set up the data from UD treebanks\\n  - Pseudocode for Kaplan-Meier fit per language/register\\n  - Pseudocode for Cox model with language-family stratification (fallback if frailty unavailable)\\n\\n---\\n\\n### PART 6: Synthesize Theoretical Justification\\n\\n**Objective**: Write a coherent 500-word section that brings together why survival analysis is the right tool for this problem, addressing all assumptions in the hypothesis.\\n\\n**Content to synthesize**:\\n1. **The confound (Part 1)**: Length-mixing distorts pooled-mean comparisons; survival analysis naturally handles this via the censoring mechanism.\\n2. **Lack of precedent (Part 2)**: This is novel; no prior linguistics DLM work uses survival tools. Explain why the tool was overlooked and why it fits perfectly.\\n3. **Valid reframing (Part 4)**: Explain why arc length is a valid time-to-event outcome:\\n   - Event = arc closes (occurs at distance d)\\n   - Time = distance in tokens\\n   - Censoring = arc would exceed sentence boundary\\n   - Conditional hazard h(d | arc ≥ d, position ≤ max_d) = instantaneous risk of closure at d\\n4. **Testable assumptions (all assumptions from hypothesis)**:\\n   - UD provides well-defined linear positions and head positions ✓ (confirmed in datasets)\\n   - Paired spoken/written treebanks exist (Part 3: confirmed)\\n   - Arc-length as time-to-event is valid (Part 2: explained)\\n   - Survival software can scale to UD (Part 5: confirmed)\\n   - Language family is a defensible frailty grouping (cite Glottolog, explain why family matters more than distant genealogy)\\n\\n**Expected output**:\\n- 400–600 words titled \\\"Theoretical Justification: Why Survival Analysis Fits Dependency-Arc Modeling\\\"\\n- Subsections:\\n  - \\\"The Length-Mixing Confound and Its Solution\\\" (100 words)\\n  - \\\"Arc Length as a Time-to-Event Outcome\\\" (150 words)\\n  - \\\"Hazard Functions Capture Shape Information Pooled Means Cannot\\\" (100 words)\\n  - \\\"Language Family as Frailty Term\\\" (100 words)\\n  - \\\"Assumptions: Verification and Implications\\\" (100–150 words)\\n\\n---\\n\\n## Deliverables\\n\\nThe research executor will produce:\\n- **research_out.json**: Structured answers to each section above\\n- **research_report.md**: A cohesive narrative (1500–2000 words) combining:\\n  1. The length-mixing confound (200 words)\\n  2. Survival-analysis precedent in linguistics (300 words)\\n  3. Catalog of suitable UD treebanks (300 words: table + narrative on coverage)\\n  4. Recent speech vs. writing DLM findings (300 words)\\n  5. Technical feasibility of tools (200 words)\\n  6. Theoretical justification (500–600 words)\\n\\n## Failure Scenarios and Mitigations\\n\\n1. **No paired spoken/written treebanks found**: Mitigate by documenting ALL treebanks with genre/modality metadata (even if not perfectly paired), and flag which languages admit no within-language register comparison. Plan may pivot to primarily cross-language typology comparison.\\n\\n2. **Frailty models unavailable in lifelines**: Mitigate by documenting stratified Cox alternatives (fit per-family, compare coefficients) and Bayesian approaches. Surveyable and defensible, though less elegant than integrated frailty.\\n\\n3. **Survival analysis truly never applied to linguistics**: Document this as the novelty and justify the transfer from biostatistics. Not a blocker; reframe as a methodological innovation.\\n\\n4. **Length-mixing confound is already solved in literature**: Mitigate by carefully reviewing proposed solutions (do they fully control variance, or only mean? do they preserve distributional shape information?) and clarifying how survival analysis is *still* an improvement (hazard curves are a richer object than normalized means).\\n\\n## Success Criteria for This Research Phase\\n\\n✓ Ferrer-i-Cancho confound explained with mathematical precision (mechanism, examples, partial solutions documented)  \\n✓ Survival-analysis precedent surveyed (likely finding: no prior linguistics application; transfer justified)  \\n✓ At least 6 language pairs with paired spoken/written treebanks cataloged  \\n✓ Typological metadata (word order, morphology) sourced for all languages  \\n✓ Kaplan-Meier and Cox PH feasibility confirmed; frailty term approach decided (built-in vs. workaround)  \\n✓ Theoretical justification written and coherent across all assumptions  \\n✓ Ready to hand off to executor: implementation plan is now concrete, not speculative\"\n}\n", "numLines": 9, "startLine": 1, "totalLines": 9}}
```

### [67] ASSISTANT · 2026-08-13 11:36:47 UTC

```
Now I'll write the final output to the required location:
```

### [68] TOOL CALL — Write · 2026-08-13 11:36:47 UTC

```
File: ./.terminal_claude_agent_struct_out.json

{
  "title": "Survival Analysis Foundations for Dependency Arc Modeling",
  "summary": "Research foundational literature on survival analysis precedent in linguistics, the DLM length-mixing confound, spoken-vs-written register variation in UD treebanks, and theoretical justification for modeling dependency arcs as right-censored time-to-event processes.",
  "runpod_compute_profile": "cpu_light",
  "question": "Can dependency arcs in UD treebanks be rigorously modeled as censored time-to-event processes using survival-analysis tools, and what is the precedent in linguistics for this approach?",
  "explanation": "The hypothesis proposes a novel methodological reframing of dependency-length minimization (DLM) using survival analysis. Current DLM research uses pooled mean dependency distances, which conflate sentence-length effects with genuine linguistic preferences—a documented confound (Ferrer-i-Cancho et al., 2013). Survival analysis (Kaplan-Meier, Cox models with frailty) is the standard biostatistical tool for data whose maximum observable value is bounded by a covariate (here, word position → censoring bound). This research establishes the theoretical and empirical foundation for importing this methodology: (1) confirming the length-mixing confound and its implications, (2) surveying how survival analysis has been applied to behavioral/linguistic data with position-bounded outcomes, (3) cataloging which UD treebanks contain paired spoken/written data and typological metadata, and (4) articulating why modeling arc length as a time-to-event outcome is a valid reframing. This foundation justifies the later implementation step.",
  "research_plan": "## Research Plan: Survival-Analysis Foundations for Dependency Arc Modeling\n\n### PART 1: Confirm the Methodological Problem (Length-Mixing Confound)\n\n**Objective**: Deeply understand and document Ferrer-i-Cancho et al.'s identified length-mixing confound and its specific implications for cross-language/register comparisons.\n\n**Searches**:\n1. Ferrer-i-Cancho & Liu (2013) \"The risks of mixing dependency lengths from sequences of different length\" (arXiv:1304.3841):\n   - What exactly is the mathematical/statistical mechanism of the confound? (distortion in mean, variance, shape?)\n   - What examples do they show (which language pairs, which direction does confound bias?)\n   - What corrections do they recommend, and why are they partial fixes?\n   - How does sentence-length distribution differ across languages/registers?\n\n2. Follow-up DLM papers citing Ferrer-i-Cancho (search: \"dependency length mixing\", \"sentence length confound DLM\"):\n   - How have subsequent studies tried to control for this? (normalization by sentence length? random-baseline comparisons?)\n   - Has any study fully solved the problem, or do they all acknowledge the residual risk?\n   - Does Futrell et al. (PNAS 2015) on 37 languages address this confound explicitly?\n\n3. Recent methodological critiques (search: \"dependency length minimization methodology\", \"reappraisal DLM linguistic universal\"):\n   - What methodological review papers exist on DLM? (PMC/arXiv: \"A Reappraisal of Dependency Length Minimization...\")\n   - Do they propose alternatives to pooled-mean comparisons?\n\n**Expected output**: \n- 200–300 words summarizing the confound's mechanism, consequences, and known partial corrections\n- A clear statement of why this confound matters for the survival-analysis reframing (censoring naturally controls for it)\n\n---\n\n### PART 2: Survey Survival-Analysis Precedent in Linguistics\n\n**Objective**: Determine whether survival analysis (Kaplan-Meier, Cox models, frailty terms) has ever been applied to linguistic or behavioral data with position-bounded outcomes, and establish theoretical precedent for the proposed reframing.\n\n**Searches**:\n1. Direct searches for survival analysis + linguistics:\n   - \"survival analysis linguistics\"\n   - \"Kaplan-Meier language\" or \"Cox proportional hazards language\"\n   - \"time-to-event linguistics\" or \"censoring linguistic data\"\n   - Result: Likely none or very few—this may be genuinely novel. Document if zero results.\n\n2. Boundary-condition / position-bounded time-to-event data in other fields (search: \"right-censoring position-bounded\", \"time-to-event covariate maximum\", \"censoring sequential data\"):\n   - Are there examples in psycholinguistics (reading times, eye-tracking)? psychology? behavioral ecology?\n   - How do researchers model outcomes where the maximum possible value depends on a position/sequence parameter?\n\n3. Theoretical justification via biostatistics handbooks:\n   - Search: \"censoring definition survival analysis\", \"right-censoring meaning\", \"time-to-event basics\"\n   - Document what makes an outcome eligibly \"censored\" and why dependency arcs fit that definition\n   - Key insight: A word near a sentence boundary cannot produce a long arc, just as a patient enrolled late in a trial cannot accumulate long follow-up time. Both are censored, not truly event-free.\n\n**Expected output**:\n- 300–400 words on precedent (or lack thereof) for survival analysis in linguistics\n- A focused section (200 words) titled \"Why dependency arcs are valid time-to-event objects\" that explains:\n  - Right-censoring definition and mechanism\n  - Why arc length ≤ min(position, sentence_length − position) is analogous to patient follow-up ≤ enrollment_time + trial_length\n  - Why Kaplan-Meier / Cox assume independence within a cluster (here, no assumptions violated)\n  - Why hazard h(d | arc ≥ d) is a meaningful quantity (it measures instantaneous risk of closure at each distance)\n\n---\n\n### PART 3: Catalog UD Treebanks with Spoken/Written and Typological Metadata\n\n**Objective**: Identify which UD treebanks have paired spoken and written corpora for the same language, and which have accessible typological metadata (word order, morphological richness).\n\n**Searches**:\n1. HuggingFace commul/universal_dependencies dataset:\n   - Document how to access the dataset programmatically\n   - List all treebanks with genre/modality metadata fields\n   - Which treebanks have \"spoken\" or \"speech\" tags? Which have paired written variants?\n\n2. Comprehensive UD treebank catalog (search: \"Universal Dependencies treebanks complete list 2025\", \"UD v2.14 treebank inventory\"):\n   - English-GUM: Has spoken subset. Which splits/sentences?\n   - Slovenian-SST (spoken) and SSJ (written): Paired languages—yes. Same annotation standard?\n   - French: Rhapsodie (spoken) and GSD/ParisStories (written)?—confirm pairing\n   - Cantonese-HK: Spoken (legislative). Is there written Cantonese treebank?\n   - Komi-Zyrian: Has spoken variant?\n   - Polish-LFG: Genre-marked spoken?\n   - German: Mixed-genre? Any spoken?\n   - Compile final list with language, spoken corpus name, written corpus name, sentence/token counts\n\n3. Typological metadata (search: \"WALS word order parameters 2026\", \"Grambank morphological richness\", \"UD morphological features language\"):\n   - Which languages in the catalog have WALS word-order annotation (SVO, SOV, VSO, free-order)?\n   - Which have Grambank data on morphological synthesis?\n   - For languages without these, can you use UD's morphological feature inventory as a proxy? (count unique FEATS values per token)\n\n**Expected output**:\n- A structured table (CSV/JSON-like) with columns:\n  - Language | Spoken_Treebank | Written_Treebank | Paired_Y/N | Spoken_Tokens | Written_Tokens | Word_Order | Morphology_Source\n- At least 6–10 language pairs with confirmed paired spoken/written data\n- A note on data accessibility: Can all be downloaded via HuggingFace or UD homepage?\n- Flagged gaps: Which typologically interesting languages are missing? (e.g., if all are SVO + rich morphology, note lack of free-order languages)\n\n---\n\n### PART 4: Review Recent Speech vs. Writing DLM Studies\n\n**Objective**: Understand how current DLM research characterizes spoken vs. written registers, what pooled-mean approaches find, and what the new survival lens might reveal.\n\n**Key papers to deeply read**:\n1. **Dobrovoljc et al. (2025)** \"Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages\" (arXiv:2505.22774):\n   - Uses English-GUM and Slovenian-SST/SSJ\n   - Finds: spoken has fewer, less diverse syntactic structures; limited overlap between modalities\n   - Is DLM mentioned? If so, how?\n   - Key finding for hypothesis: If speech and writing differ in structure, do they differ in *hazard shape*?\n\n2. **Futrell et al. (PNAS 2015)** \"Large-scale evidence of dependency length minimization in 37 languages\":\n   - Methodology: how do they normalize for sentence length? Do they acknowledge the mixing confound?\n   - Findings on cross-language variation in MDD\n   - Does it include any speech data, or is it all written?\n\n3. **SCiL 2021 cross-linguistic speech vs. writing study** (if identifiable via search: \"dependency length spoken written SCiL 2021\"):\n   - What are the directional effects? (longer spoken? shorter? varies by language?)\n   - Do they use paired treebanks?\n   - How do they normalize for sentence length?\n\n4. **Recent UD-based functional vs. lexical DLM** (2026 work mentioned in hypothesis):\n   - Confirms that dependency *type* (functional vs. lexical) explains variance in DLM\n   - Implication: hazard curves might differ by dependency type as well as register\n\n**Expected output**:\n- 300–400 words summarizing:\n  - What pooled-mean studies report about speech vs. writing DLM (directional findings, language variation)\n  - Limitations of pooled-mean approaches that a hazard-curve lens could overcome\n  - Specific predictions: If spoken is front-loaded (quick closure) vs. written (flat/delayed), what would Kaplan-Meier curves show?\n  - How the survival reframing naturally stratifies by dependency type without extra modeling\n\n---\n\n### PART 5: Establish Technical Feasibility of Survival-Analysis Tools\n\n**Objective**: Confirm that Python survival-analysis libraries (lifelines, scikit-survival) can fit Kaplan-Meier, Cox, and frailty models at UD scale (10k to 1M arcs) and understand their API and limitations.\n\n**Searches**:\n1. **lifelines library** (https://lifelines.readthedocs.io/):\n   - What models does it support? (Kaplan-Meier ✓, Nelson-Aalen ✓, Cox PH ✓, ... frailty?)\n   - Does CoxPHFitter support shared frailty / random effects, or only stratification/penalization?\n   - If not, what workarounds exist? (e.g., fit Cox models per-family separately and compare coefficients?)\n   - Performance: has anyone fit it to 100k+ observations? Any known scaling issues?\n\n2. **scikit-survival library**:\n   - Does it support Cox PH with frailty terms?\n   - Any advantages/disadvantages vs. lifelines for large datasets?\n\n3. **Alternatives** (search: \"Python Cox frailty model\", \"Python shared frailty survival\"):\n   - PyMC3/PyMC for Bayesian frailty models?\n   - statsmodels?\n   - If built-in frailty is unavailable, what is the standard workaround in literature? (manual specification, two-stage fitting?)\n\n**Expected output**:\n- 200–250 words on tools:\n  - Which library to use for Kaplan-Meier / Nelson-Aalen (likely lifelines)\n  - Which library / approach for Cox PH (lifelines; confirm stratification suffices if frailty unavailable)\n  - Frailty term options: built-in vs. workaround (e.g., Bayesian approach or two-stage)\n  - Scaling: Can it handle 1M+ arcs? Any batch-processing considerations?\n- Code snippet outline (pseudocode) showing:\n  - Data format (duration, event, censoring indicator, covariates) for a single arc\n  - How to set up the data from UD treebanks\n  - Pseudocode for Kaplan-Meier fit per language/register\n  - Pseudocode for Cox model with language-family stratification (fallback if frailty unavailable)\n\n---\n\n### PART 6: Synthesize Theoretical Justification\n\n**Objective**: Write a coherent 500-word section that brings together why survival analysis is the right tool for this problem, addressing all assumptions in the hypothesis.\n\n**Content to synthesize**:\n1. **The confound (Part 1)**: Length-mixing distorts pooled-mean comparisons; survival analysis naturally handles this via the censoring mechanism.\n2. **Lack of precedent (Part 2)**: This is novel; no prior linguistics DLM work uses survival tools. Explain why the tool was overlooked and why it fits perfectly.\n3. **Valid reframing (Part 4)**: Explain why arc length is a valid time-to-event outcome:\n   - Event = arc closes (occurs at distance d)\n   - Time = distance in tokens\n   - Censoring = arc would exceed sentence boundary\n   - Conditional hazard h(d | arc ≥ d, position ≤ max_d) = instantaneous risk of closure at d\n4. **Testable assumptions (all assumptions from hypothesis)**:\n   - UD provides well-defined linear positions and head positions ✓ (confirmed in datasets)\n   - Paired spoken/written treebanks exist (Part 3: confirmed)\n   - Arc-length as time-to-event is valid (Part 2: explained)\n   - Survival software can scale to UD (Part 5: confirmed)\n   - Language family is a defensible frailty grouping (cite Glottolog, explain why family matters more than distant genealogy)\n\n**Expected output**:\n- 400–600 words titled \"Theoretical Justification: Why Survival Analysis Fits Dependency-Arc Modeling\"\n- Subsections:\n  - \"The Length-Mixing Confound and Its Solution\" (100 words)\n  - \"Arc Length as a Time-to-Event Outcome\" (150 words)\n  - \"Hazard Functions Capture Shape Information Pooled Means Cannot\" (100 words)\n  - \"Language Family as Frailty Term\" (100 words)\n  - \"Assumptions: Verification and Implications\" (100–150 words)\n\n---\n\n## Deliverables\n\nThe research executor will produce:\n- **research_out.json**: Structured answers to each section above\n- **research_report.md**: A cohesive narrative (1500–2000 words) combining:\n  1. The length-mixing confound (200 words)\n  2. Survival-analysis precedent in linguistics (300 words)\n  3. Catalog of suitable UD treebanks (300 words: table + narrative on coverage)\n  4. Recent speech vs. writing DLM findings (300 words)\n  5. Technical feasibility of tools (200 words)\n  6. Theoretical justification (500–600 words)\n\n## Failure Scenarios and Mitigations\n\n1. **No paired spoken/written treebanks found**: Mitigate by documenting ALL treebanks with genre/modality metadata (even if not perfectly paired), and flag which languages admit no within-language register comparison. Plan may pivot to primarily cross-language typology comparison.\n\n2. **Frailty models unavailable in lifelines**: Mitigate by documenting stratified Cox alternatives (fit per-family, compare coefficients) and Bayesian approaches. Surveyable and defensible, though less elegant than integrated frailty.\n\n3. **Survival analysis truly never applied to linguistics**: Document this as the novelty and justify the transfer from biostatistics. Not a blocker; reframe as a methodological innovation.\n\n4. **Length-mixing confound is already solved in literature**: Mitigate by carefully reviewing proposed solutions (do they fully control variance, or only mean? do they preserve distributional shape information?) and clarifying how survival analysis is *still* an improvement (hazard curves are a richer object than normalized means).\n\n## Success Criteria for This Research Phase\n\n✓ Ferrer-i-Cancho confound explained with mathematical precision (mechanism, examples, partial solutions documented)  \n✓ Survival-analysis precedent surveyed (likely finding: no prior linguistics application; transfer justified)  \n✓ At least 6 language pairs with paired spoken/written treebanks cataloged  \n✓ Typological metadata (word order, morphology) sourced for all languages  \n✓ Kaplan-Meier and Cox PH feasibility confirmed; frailty term approach decided (built-in vs. workaround)  \n✓ Theoretical justification written and coherent across all assumptions  \n✓ Ready to hand off to executor: implementation plan is now concrete, not speculative"
}
```

### [69] TOOL RESULT — Write · 2026-08-13 11:36:47 UTC

```
{"type": "create", "filePath": "./.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Survival Analysis Foundations for Dependency Arc Modeling\",\n  \"summary\": \"Research foundational literature on survival analysis precedent in linguistics, the DLM length-mixing confound, spoken-vs-written register variation in UD treebanks, and theoretical justification for modeling dependency arcs as right-censored time-to-event processes.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"question\": \"Can dependency arcs in UD treebanks be rigorously modeled as censored time-to-event processes using survival-analysis tools, and what is the precedent in linguistics for this approach?\",\n  \"explanation\": \"The hypothesis proposes a novel methodological reframing of dependency-length minimization (DLM) using survival analysis. Current DLM research uses pooled mean dependency distances, which conflate sentence-length effects with genuine linguistic preferences—a documented confound (Ferrer-i-Cancho et al., 2013). Survival analysis (Kaplan-Meier, Cox models with frailty) is the standard biostatistical tool for data whose maximum observable value is bounded by a covariate (here, word position → censoring bound). This research establishes the theoretical and empirical foundation for importing this methodology: (1) confirming the length-mixing confound and its implications, (2) surveying how survival analysis has been applied to behavioral/linguistic data with position-bounded outcomes, (3) cataloging which UD treebanks contain paired spoken/written data and typological metadata, and (4) articulating why modeling arc length as a time-to-event outcome is a valid reframing. This foundation justifies the later implementation step.\",\n  \"research_plan\": \"## Research Plan: Survival-Analysis Foundations for Dependency Arc Modeling\\n\\n### PART 1: Confirm the Methodological Problem (Length-Mixing Confound)\\n\\n**Objective**: Deeply understand and document Ferrer-i-Cancho et al.'s identified length-mixing confound and its specific implications for cross-language/register comparisons.\\n\\n**Searches**:\\n1. Ferrer-i-Cancho & Liu (2013) \\\"The risks of mixing dependency lengths from sequences of different length\\\" (arXiv:1304.3841):\\n   - What exactly is the mathematical/statistical mechanism of the confound? (distortion in mean, variance, shape?)\\n   - What examples do they show (which language pairs, which direction does confound bias?)\\n   - What corrections do they recommend, and why are they partial fixes?\\n   - How does sentence-length distribution differ across languages/registers?\\n\\n2. Follow-up DLM papers citing Ferrer-i-Cancho (search: \\\"dependency length mixing\\\", \\\"sentence length confound DLM\\\"):\\n   - How have subsequent studies tried to control for this? (normalization by sentence length? random-baseline comparisons?)\\n   - Has any study fully solved the problem, or do they all acknowledge the residual risk?\\n   - Does Futrell et al. (PNAS 2015) on 37 languages address this confound explicitly?\\n\\n3. Recent methodological critiques (search: \\\"dependency length minimization methodology\\\", \\\"reappraisal DLM linguistic universal\\\"):\\n   - What methodological review papers exist on DLM? (PMC/arXiv: \\\"A Reappraisal of Dependency Length Minimization...\\\")\\n   - Do they propose alternatives to pooled-mean comparisons?\\n\\n**Expected output**: \\n- 200–300 words summarizing the confound's mechanism, consequences, and known partial corrections\\n- A clear statement of why this confound matters for the survival-analysis reframing (censoring naturally controls for it)\\n\\n---\\n\\n### PART 2: Survey Survival-Analysis Precedent in Linguistics\\n\\n**Objective**: Determine whether survival analysis (Kaplan-Meier, Cox models, frailty terms) has ever been applied to linguistic or behavioral data with position-bounded outcomes, and establish theoretical precedent for the proposed reframing.\\n\\n**Searches**:\\n1. Direct searches for survival analysis + linguistics:\\n   - \\\"survival analysis linguistics\\\"\\n   - \\\"Kaplan-Meier language\\\" or \\\"Cox proportional hazards language\\\"\\n   - \\\"time-to-event linguistics\\\" or \\\"censoring linguistic data\\\"\\n   - Result: Likely none or very few—this may be genuinely novel. Document if zero results.\\n\\n2. Boundary-condition / position-bounded time-to-event data in other fields (search: \\\"right-censoring position-bounded\\\", \\\"time-to-event covariate maximum\\\", \\\"censoring sequential data\\\"):\\n   - Are there examples in psycholinguistics (reading times, eye-tracking)? psychology? behavioral ecology?\\n   - How do researchers model outcomes where the maximum possible value depends on a position/sequence parameter?\\n\\n3. Theoretical justification via biostatistics handbooks:\\n   - Search: \\\"censoring definition survival analysis\\\", \\\"right-censoring meaning\\\", \\\"time-to-event basics\\\"\\n   - Document what makes an outcome eligibly \\\"censored\\\" and why dependency arcs fit that definition\\n   - Key insight: A word near a sentence boundary cannot produce a long arc, just as a patient enrolled late in a trial cannot accumulate long follow-up time. Both are censored, not truly event-free.\\n\\n**Expected output**:\\n- 300–400 words on precedent (or lack thereof) for survival analysis in linguistics\\n- A focused section (200 words) titled \\\"Why dependency arcs are valid time-to-event objects\\\" that explains:\\n  - Right-censoring definition and mechanism\\n  - Why arc length ≤ min(position, sentence_length − position) is analogous to patient follow-up ≤ enrollment_time + trial_length\\n  - Why Kaplan-Meier / Cox assume independence within a cluster (here, no assumptions violated)\\n  - Why hazard h(d | arc ≥ d) is a meaningful quantity (it measures instantaneous risk of closure at each distance)\\n\\n---\\n\\n### PART 3: Catalog UD Treebanks with Spoken/Written and Typological Metadata\\n\\n**Objective**: Identify which UD treebanks have paired spoken and written corpora for the same language, and which have accessible typological metadata (word order, morphological richness).\\n\\n**Searches**:\\n1. HuggingFace commul/universal_dependencies dataset:\\n   - Document how to access the dataset programmatically\\n   - List all treebanks with genre/modality metadata fields\\n   - Which treebanks have \\\"spoken\\\" or \\\"speech\\\" tags? Which have paired written variants?\\n\\n2. Comprehensive UD treebank catalog (search: \\\"Universal Dependencies treebanks complete list 2025\\\", \\\"UD v2.14 treebank inventory\\\"):\\n   - English-GUM: Has spoken subset. Which splits/sentences?\\n   - Slovenian-SST (spoken) and SSJ (written): Paired languages—yes. Same annotation standard?\\n   - French: Rhapsodie (spoken) and GSD/ParisStories (written)?—confirm pairing\\n   - Cantonese-HK: Spoken (legislative). Is there written Cantonese treebank?\\n   - Komi-Zyrian: Has spoken variant?\\n   - Polish-LFG: Genre-marked spoken?\\n   - German: Mixed-genre? Any spoken?\\n   - Compile final list with language, spoken corpus name, written corpus name, sentence/token counts\\n\\n3. Typological metadata (search: \\\"WALS word order parameters 2026\\\", \\\"Grambank morphological richness\\\", \\\"UD morphological features language\\\"):\\n   - Which languages in the catalog have WALS word-order annotation (SVO, SOV, VSO, free-order)?\\n   - Which have Grambank data on morphological synthesis?\\n   - For languages without these, can you use UD's morphological feature inventory as a proxy? (count unique FEATS values per token)\\n\\n**Expected output**:\\n- A structured table (CSV/JSON-like) with columns:\\n  - Language | Spoken_Treebank | Written_Treebank | Paired_Y/N | Spoken_Tokens | Written_Tokens | Word_Order | Morphology_Source\\n- At least 6–10 language pairs with confirmed paired spoken/written data\\n- A note on data accessibility: Can all be downloaded via HuggingFace or UD homepage?\\n- Flagged gaps: Which typologically interesting languages are missing? (e.g., if all are SVO + rich morphology, note lack of free-order languages)\\n\\n---\\n\\n### PART 4: Review Recent Speech vs. Writing DLM Studies\\n\\n**Objective**: Understand how current DLM research characterizes spoken vs. written registers, what pooled-mean approaches find, and what the new survival lens might reveal.\\n\\n**Key papers to deeply read**:\\n1. **Dobrovoljc et al. (2025)** \\\"Counting trees: A treebank-driven exploration of syntactic variation in speech and writing across languages\\\" (arXiv:2505.22774):\\n   - Uses English-GUM and Slovenian-SST/SSJ\\n   - Finds: spoken has fewer, less diverse syntactic structures; limited overlap between modalities\\n   - Is DLM mentioned? If so, how?\\n   - Key finding for hypothesis: If speech and writing differ in structure, do they differ in *hazard shape*?\\n\\n2. **Futrell et al. (PNAS 2015)** \\\"Large-scale evidence of dependency length minimization in 37 languages\\\":\\n   - Methodology: how do they normalize for sentence length? Do they acknowledge the mixing confound?\\n   - Findings on cross-language variation in MDD\\n   - Does it include any speech data, or is it all written?\\n\\n3. **SCiL 2021 cross-linguistic speech vs. writing study** (if identifiable via search: \\\"dependency length spoken written SCiL 2021\\\"):\\n   - What are the directional effects? (longer spoken? shorter? varies by language?)\\n   - Do they use paired treebanks?\\n   - How do they normalize for sentence length?\\n\\n4. **Recent UD-based functional vs. lexical DLM** (2026 work mentioned in hypothesis):\\n   - Confirms that dependency *type* (functional vs. lexical) explains variance in DLM\\n   - Implication: hazard curves might differ by dependency type as well as register\\n\\n**Expected output**:\\n- 300–400 words summarizing:\\n  - What pooled-mean studies report about speech vs. writing DLM (directional findings, language variation)\\n  - Limitations of pooled-mean approaches that a hazard-curve lens could overcome\\n  - Specific predictions: If spoken is front-loaded (quick closure) vs. written (flat/delayed), what would Kaplan-Meier curves show?\\n  - How the survival reframing naturally stratifies by dependency type without extra modeling\\n\\n---\\n\\n### PART 5: Establish Technical Feasibility of Survival-Analysis Tools\\n\\n**Objective**: Confirm that Python survival-analysis libraries (lifelines, scikit-survival) can fit Kaplan-Meier, Cox, and frailty models at UD scale (10k to 1M arcs) and understand their API and limitations.\\n\\n**Searches**:\\n1. **lifelines library** (https://lifelines.readthedocs.io/):\\n   - What models does it support? (Kaplan-Meier ✓, Nelson-Aalen ✓, Cox PH ✓, ... frailty?)\\n   - Does CoxPHFitter support shared frailty / random effects, or only stratification/penalization?\\n   - If not, what workarounds exist? (e.g., fit Cox models per-family separately and compare coefficients?)\\n   - Performance: has anyone fit it to 100k+ observations? Any known scaling issues?\\n\\n2. **scikit-survival library**:\\n   - Does it support Cox PH with frailty terms?\\n   - Any advantages/disadvantages vs. lifelines for large datasets?\\n\\n3. **Alternatives** (search: \\\"Python Cox frailty model\\\", \\\"Python shared frailty survival\\\"):\\n   - PyMC3/PyMC for Bayesian frailty models?\\n   - statsmodels?\\n   - If built-in frailty is unavailable, what is the standard workaround in literature? (manual specification, two-stage fitting?)\\n\\n**Expected output**:\\n- 200–250 words on tools:\\n  - Which library to use for Kaplan-Meier / Nelson-Aalen (likely lifelines)\\n  - Which library / approach for Cox PH (lifelines; confirm stratification suffices if frailty unavailable)\\n  - Frailty term options: built-in vs. workaround (e.g., Bayesian approach or two-stage)\\n  - Scaling: Can it handle 1M+ arcs? Any batch-processing considerations?\\n- Code snippet outline (pseudocode) showing:\\n  - Data format (duration, event, censoring indicator, covariates) for a single arc\\n  - How to set up the data from UD treebanks\\n  - Pseudocode for Kaplan-Meier fit per language/register\\n  - Pseudocode for Cox model with language-family stratification (fallback if frailty unavailable)\\n\\n---\\n\\n### PART 6: Synthesize Theoretical Justification\\n\\n**Objective**: Write a coherent 500-word section that brings together why survival analysis is the right tool for this problem, addressing all assumptions in the hypothesis.\\n\\n**Content to synthesize**:\\n1. **The confound (Part 1)**: Length-mixing distorts pooled-mean comparisons; survival analysis naturally handles this via the censoring mechanism.\\n2. **Lack of precedent (Part 2)**: This is novel; no prior linguistics DLM work uses survival tools. Explain why the tool was overlooked and why it fits perfectly.\\n3. **Valid reframing (Part 4)**: Explain why arc length is a valid time-to-event outcome:\\n   - Event = arc closes (occurs at distance d)\\n   - Time = distance in tokens\\n   - Censoring = arc would exceed sentence boundary\\n   - Conditional hazard h(d | arc ≥ d, position ≤ max_d) = instantaneous risk of closure at d\\n4. **Testable assumptions (all assumptions from hypothesis)**:\\n   - UD provides well-defined linear positions and head positions ✓ (confirmed in datasets)\\n   - Paired spoken/written treebanks exist (Part 3: confirmed)\\n   - Arc-length as time-to-event is valid (Part 2: explained)\\n   - Survival software can scale to UD (Part 5: confirmed)\\n   - Language family is a defensible frailty grouping (cite Glottolog, explain why family matters more than distant genealogy)\\n\\n**Expected output**:\\n- 400–600 words titled \\\"Theoretical Justification: Why Survival Analysis Fits Dependency-Arc Modeling\\\"\\n- Subsections:\\n  - \\\"The Length-Mixing Confound and Its Solution\\\" (100 words)\\n  - \\\"Arc Length as a Time-to-Event Outcome\\\" (150 words)\\n  - \\\"Hazard Functions Capture Shape Information Pooled Means Cannot\\\" (100 words)\\n  - \\\"Language Family as Frailty Term\\\" (100 words)\\n  - \\\"Assumptions: Verification and Implications\\\" (100–150 words)\\n\\n---\\n\\n## Deliverables\\n\\nThe research executor will produce:\\n- **research_out.json**: Structured answers to each section above\\n- **research_report.md**: A cohesive narrative (1500–2000 words) combining:\\n  1. The length-mixing confound (200 words)\\n  2. Survival-analysis precedent in linguistics (300 words)\\n  3. Catalog of suitable UD treebanks (300 words: table + narrative on coverage)\\n  4. Recent speech vs. writing DLM findings (300 words)\\n  5. Technical feasibility of tools (200 words)\\n  6. Theoretical justification (500–600 words)\\n\\n## Failure Scenarios and Mitigations\\n\\n1. **No paired spoken/written treebanks found**: Mitigate by documenting ALL treebanks with genre/modality metadata (even if not perfectly paired), and flag which languages admit no within-language register comparison. Plan may pivot to primarily cross-language typology comparison.\\n\\n2. **Frailty models unavailable in lifelines**: Mitigate by documenting stratified Cox alternatives (fit per-family, compare coefficients) and Bayesian approaches. Surveyable and defensible, though less elegant than integrated frailty.\\n\\n3. **Survival analysis truly never applied to linguistics**: Document this as the novelty and justify the transfer from biostatistics. Not a blocker; reframe as a methodological innovation.\\n\\n4. **Length-mixing confound is already solved in literature**: Mitigate by carefully reviewing proposed solutions (do they fully control variance, or only mean? do they preserve distributional shape information?) and clarifying how survival analysis is *still* an improvement (hazard curves are a richer object than normalized means).\\n\\n## Success Criteria for This Research Phase\\n\\n✓ Ferrer-i-Cancho confound explained with mathematical precision (mechanism, examples, partial solutions documented)  \\n✓ Survival-analysis precedent surveyed (likely finding: no prior linguistics application; transfer justified)  \\n✓ At least 6 language pairs with paired spoken/written treebanks cataloged  \\n✓ Typological metadata (word order, morphology) sourced for all languages  \\n✓ Kaplan-Meier and Cox PH feasibility confirmed; frailty term approach decided (built-in vs. workaround)  \\n✓ Theoretical justification written and coherent across all assumptions  \\n✓ Ready to hand off to executor: implementation plan is now concrete, not speculative\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [70] ASSISTANT · 2026-08-13 11:36:59 UTC

```
Perfect! I've created a detailed, actionable research plan for the artifact. Here's what I've delivered:

## Summary

The plan establishes a comprehensive foundation for the survival-analysis reframing of dependency-length minimization across UD treebanks. It's organized into 6 research parts:

1. **Length-Mixing Confound** – Document Ferrer-i-Cancho et al.'s methodological problem that pooled-mean comparisons conflate sentence length with linguistic preference
2. **Survival-Analysis Precedent** – Survey whether this tool has been applied in linguistics (likely finding: no prior work, justifying novelty)
3. **UD Treebank Catalog** – Identify all languages with paired spoken/written treebanks and typological metadata (word order, morphology)
4. **Recent Speech vs. Writing Studies** – Understand current DLM findings (especially Dobrovoljc's recent work on syntactic modality differences)
5. **Technical Feasibility** – Confirm Python libraries (lifelines) can fit Kaplan-Meier, Cox, and frailty models at UD scale
6. **Theoretical Justification** – Synthesize why dependency arcs are valid time-to-event objects and hazard functions capture shape information pooled means cannot

## Key Features

- **Calibrated for Dobrovoljc**: References her recent "Counting trees" paper on English-GUM and Slovenian treebanks
- **Specific searches**: Each section lists concrete queries, not vague hand-waving
- **Failure scenarios**: Documents what to do if frailty is unavailable, or if no paired treebanks exist
- **Success criteria**: Clear, checkable deliverables (confound mechanism, 6+ language pairs, theoretical write-up)
- **Ready for executor**: The plan is detailed enough that a downstream agent can follow it step-by-step without improvisation

The output file `./.terminal_claude_agent_struct_out.json` is now ready and contains all required fields.

Sources:
- [The risks of mixing dependency lengths from sequences of different length](https://arxiv.org/abs/1304.3841)
- [Large-scale evidence of dependency length minimization in 37 languages](https://www.pnas.org/doi/full/10.1073/pnas.1502134112)
- [Counting trees: A treebank-driven exploration of syntactic variation in speech and writing](https://arxiv.org/abs/2505.22774)
- [Spoken Language Treebanks in Universal Dependencies](https://aclanthology.org/2022.lrec-1.191.pdf)
- [Universal Dependencies](https://universaldependencies.org/)
- [lifelines documentation](https://lifelines.readthedocs.io/)
- [commul/universal_dependencies on HuggingFace](https://huggingface.co/datasets/commul/universal_dependencies)
```
