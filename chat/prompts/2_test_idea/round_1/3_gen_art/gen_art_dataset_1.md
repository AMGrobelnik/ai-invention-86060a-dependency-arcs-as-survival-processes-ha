# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_oQQwThF8kM-b` — Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-13 11:38:04 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Find, evaluate, and prepare high-quality datasets for the research experiment.
Adapt your search strategy based on the hypothesis and domain requirements.
</task>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. MUST check for and avoid each one.

**1. Picking Obscure or Unusable Datasets**
Do NOT select datasets just because they match a keyword. Red flags: very few downloads (<100), no documentation (dataset card, paper, or GitHub page). Prefer well-used datasets (not necessarily popular or widely known) with clear documentation.
CHECK: >100 downloads? Has documentation? If any "no" → find a better dataset.

**2. Fabricating Dataset Provenance**
Do NOT invent justifications for why a dataset is relevant. If a dataset name contains a number (e.g., "797"), do NOT assume it refers to a specific benchmark suite, OpenML ID, or paper without verification. In past runs, an agent assumed "797" referred to "OpenML benchmark suite 797" with zero evidence, then fabricated a rationale. This was completely false.
CHECK: Can you cite a specific, verifiable source (paper, benchmark page, dataset card) confirming this dataset is what you claim? If not, do not make provenance claims.

**3. Not Verifying Dataset Usefulness**
Always sanity-check that a dataset is actually suitable for the task before committing. Download a sample, inspect the features, and run a quick baseline appropriate for the domain. If the dataset lacks signal or structure for the hypothesis being tested, the entire experiment is wasted.

**4. Settling for the Only Search Result**
If your search returns only 1-2 results, your search terms are too narrow. Broaden your queries, try different keyword combinations, or search for well-known benchmark datasets in the domain. A single obscure result from a narrow query should never be your final choice.
CHECK: Fewer than 5 candidate datasets? Run additional searches with broader or different terms before making a selection.
</common_mistakes_to_avoid>

<critical_requirements>
- Keep final response under 300 characters
</critical_requirements>

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
Your workspace: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: UD Dependency Arcs with Survival-Analysis Features
summary: >-
  Assemble all dependency arcs from 296+ Universal Dependencies treebanks (168+ languages) with computed arc lengths, position-bounded
  censoring bounds, register/modality labels, typological covariates, and language-family groupings for survival-analysis
  investigation of dependency-length minimization.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  Complete extraction of every dependency arc from all accessible UD treebanks (v2.18, 296+ treebanks) with arc-level features:
  observed arc length d, position-bounded maximum arc length (censoring bound based on token distance to sentence boundary),
  register/modality label (spoken vs. written vs. other), language code and language family (via Glottolog), and typological
  covariates (word-order class, morphological richness proxy from WALS/Grambank or UD morphology feature count). Schema must
  explicitly document censoring bounds and their sentence-position basis. Target: 1-5 million individual arc records, split
  into full (all arcs), mini (50k random sample for testing), and preview (500-1k examples) variants. All data validated against
  source treebanks and cross-referenced with Glottolog for family labels and WALS/Grambank for typological features where
  available.
dataset_search_plan: |-
  1. PRIMARY SOURCE: Download commul/universal_dependencies from HuggingFace (296+ treebanks as of v2.18, May 2026). This includes all CoNLL-U formatted treebanks with metadata.

  2. METADATA & REGISTER LABELING: For each treebank, extract register/modality labels from (a) treebank README.md machine-readable metadata (YAML), (b) 18 genre categories documented in UD (spoken, written, academic, news, fiction, web, etc.), and (c) special UD features like # speaker/addressee tokens which mark spoken interaction. Priority sources: English-GUM (12 genres including spoken/written), French-Rhapsodie (spoken) + French-GSD (written), Slovenian (paired data per recent paper), English-CHILDES (child-adult interaction), Estonian-EWT. For treebanks with only one register, label accordingly but include them (fallback: treat unspecified as 'unspecified' rather than drop).

  3. ARC EXTRACTION & CENSORING BOUNDS: For each token in each sentence: (a) extract its head token ID and compute arc length d = |token_id - head_id|, (b) compute censoring bound = max(token_id, sentence_length - token_id) [the distance to the NEARER sentence boundary, which structurally prevents any arc longer than this], (c) flag if d > censoring_bound (data quality check; should be zero). Output: one row per arc with fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound, register, language_code, language_name, family_id, word_order_type, morph_richness_proxy.

  4. TYPOLOGICAL FEATURES: (a) WALS lookup by language code: retrieve word-order features (SVO/SOV/VSO class if available) and nominal-morphology features (case marking yes/no). (b) Grambank lookup: binary features for word-order patterns (SVO/SOV/VSO/VOS/OVS/OSV presence) and morphological richness indicators. (c) FALLBACK: If WALS/Grambank has no entry for a language, compute morphological-richness proxy = count of distinct UD morphological features (POS, Gender, Number, Case, Tense, Mood, etc.) in that treebank's tokens, normalized by token count, as a scalar between 0-1. Include a 'data_source' field for each typological feature (WALS/Grambank/UD_proxy) so quality is transparent.

  5. LANGUAGE FAMILIES (Glottolog): (a) Download Glottolog CLDF dataset (from GitHub glottolog/glottolog or glottolog/glottolog-cldf or ZENODO). (b) Use pyglottolog Python API to look up each language by ISO code and extract its classification path (family, subfamily if available). (c) Use the top-level family node as the 'family_id' for frailty grouping; also include full classification path as 'family_path' for reference. (d) Fallback: if a language is not in Glottolog, mark family_id as 'unknown' but do NOT drop the treebank.

  6. SCHEMA DESIGN & VALIDATION: Design JSON schema (one row per arc) with required fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound [CRITICAL: document that censoring_bound = max(token_id, sent_len - token_id) in schema description], register (enum: spoken, written, academic, news, fiction, web, other, unspecified), language_code, language_name, family_id, family_path, word_order_type (optional, nullable), morph_richness_proxy (float 0-1), morph_richness_data_source (WALS/Grambank/UD_proxy). Use aii-json skill to validate a sample of rows before final output.

  7. QUALITY CHECKS & SPOT-VALIDATION: (a) For a random sample of 100-200 arcs, verify that arc_length <= censoring_bound (should be 100% true; flag any violations). (b) Cross-check register labels: spot-read treebank metadata to confirm 'spoken' arcs come from marked spoken subcorpora. (c) Verify language codes are ISO 639-3 and consistent across UD and Glottolog. (d) For 10-20 languages with matched WALS and Grambank entries, confirm word-order classification consistency between sources (should be close to identical). (e) Inspect morphological-richness proxies for outliers (plot distribution, should be unimodal and clustered around 0.1-0.6 for most languages).

  8. SPLITS & EXPORT: (a) FULL: All extracted arcs, deduplicated, ordered by language, treebank, sentence. (b) MINI: 50k random arcs stratified by register and language family (for quick iteration in executor testing). (c) PREVIEW: 500-1000 arcs from diverse languages/registers for documentation. All three as data_out.json with one JSON object per line (JSONL) or as a single JSON array, depending on size; use aii-file-size-limit skill if >300MB to advise on splits. Include a schema document and a summary statistics table (arcs per language, arcs per register, arc-length distribution quartiles by register).

  9. FALLBACK & ROBUSTNESS: If HuggingFace API fails, fetch UD treebanks directly from UniversalDependencies GitHub (UD_<language>-<treebank> repos). If Glottolog unavailable, use cached/static Glottolog export (available on ZENODO as versioned snapshot). If WALS/Grambank incomplete, ensure UD_proxy is computed for all languages. If a treebank has parsing errors or malformed CoNLL-U, log the issue and skip that treebank but continue; do NOT fail the entire run.

  10. DOCUMENTATION: Generate a README.md with data dictionary, sample rows, source citations (commul/universal_dependencies, Glottolog, WALS, Grambank), notes on censoring-bound computation (with a concrete example sentence), register labeling methodology, known limitations (e.g., % of languages with paired spoken/written data, % coverage by WALS/Grambank vs UD_proxy), and reproduction instructions (language/versions of pyglottolog, UD dataset commit, etc.).
target_num_datasets: 1
</artifact_plan>



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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 8 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 4 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 2 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
```

### [2] HUMAN-USER prompt · 2026-08-13 11:38:04 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-python · 2026-08-13 11:38:08 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-08-13 11:38:08 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-json · 2026-08-13 11:38:08 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-file-size-limit · 2026-08-13 11:38:08 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [7] SKILL-INPUT — aii-use-hardware · 2026-08-13 11:38:08 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [8] SKILL-INPUT — aii-parallel-computing · 2026-08-13 11:38:08 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [9] SKILL-INPUT — aii-hf-datasets · 2026-08-13 11:38:08 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: Searches, previews, and downloads datasets from HuggingFace Hub. Use when user needs machine learning datasets, training data, HuggingFace datasets, dataset discovery, or .parquet/.json exports.
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [10] SKILL-INPUT — aii-handbook-auto-computational-linguistics · 2026-08-13 11:38:08 UTC

The agent loaded the **aii-handbook-auto-computational-linguistics** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-handbook-auto-computational-linguistics
description: "Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering). ALWAYS read before ANY computational-linguistics research work — ideation/novelty assessment, study planning, experiment/eval design, write-up, or review; do NOT do any of these from priors alone (the field's measurement norms were overturned through 2025-2026 and several obvious-looking directions are saturated). Triggers: computational linguistics, ACL/EMNLP/NAACL/EACL/TACL/CoNLL/ARR, linguistic structure in language models, grammaticality, minimal pairs, BLiMP, syntax/morphology/semantics of LMs, psycholinguistics, surprisal, reading times, annotation and annotator disagreement, human label variation, corpora, low-resource and multilingual NLP, dialects and language varieties, benchmark validity, LLM-as-judge, transformer expressivity. NOT for: building or fine-tuning models, prompt engineering, retrieval/agent architecture, speech signal processing, or information retrieval with no linguistic question."
---

<!-- GENERATED by amg-handbook-forge — DRAFT for expert review. v2 (second-pass draft;
     v1 superseded — search-first directive promoted to Overview, density 247->229). generated: 2026-07-27 · next_check:
     2026-10-27 (volatile.md half-life ≈ 3 months). ✓x=exec · [Sn]=cited · ⚠️=candidate.
     Row fails → `STALE: <what>` in place. -->

# Computational linguistics — field handbook

## Overview

Scope: computational linguistics as a SCIENCE of language — what models reveal about language and
about human language processing, and how such claims are measured. NLP engineering (training,
prompting, retrieval, agents) is out of scope. The star is the SUBSTRATE below: a dated,
source-anchored map with an explicit do-not-redo list. The only IDEATION lens is open questions;
a thin execution floor follows it.

**How to use this map.** It is a STARTING POINT, not a substitute for looking. Its crowded
list is necessarily incomplete and its frontier is dated; map-silence means *not-yet-checked*,
never *open*. Before committing to any direction, run your own fresh, dated saturation search
on that specific direction and confirm it is actually unoccupied. Treat the sections below as
material to reason against — the questions especially — rather than as conclusions to accept.

## Organizing principles (how the field reasons)

- **The measurement instrument is itself under audit.** A 445-benchmark, 29-reviewer systematic review found "patterns
  related to the measured phenomena, tasks, and scoring metrics which undermine the validity of the
  resulting claims" [S2] — a capability claim is judged on its construct, not just its number.
- **Output is not competence.** "LLMs' metalinguistic judgments are inferior to quantities directly
  derived from representations" [S3]; grammaticality separates in hidden states where string
  probability does not [S12].
- **A negative result about a model is a claim about your probe:** "negative results relying on
  metalinguistic prompts cannot be taken as conclusive evidence that an LLM lacks a particular
  linguistic generalization" [S3].
- **Disagreement is data.** Human label variation "reflects the diversity of human perspectives
  rather than mere error"; collapsing it manufactures "artificial consensus" [S7].
- **Explanatory status is graded, and the grades are named.** LLMs supply "how-possibly
  explanations (HPEs)" about acquisition and competence, while "current LLMs do not yet satisfy"
  the requirements for how-actually explanations [S4].
- **Theory bounds the empirics** — expressivity results explain "why current transformer
  architectures struggle to implement exact discrete algorithms" [S24] — but they are
  assumption-relative by construction [S11].

## Frontier (recency-weighted)

**Measurement & construct validity** *(weight-capped — the loudest thread)*

- A systematic review of 445 LLM benchmarks by 29 expert reviewers found validity-undermining
  patterns across measured phenomena, tasks and scoring metrics [S2] (NeurIPS 2025).
- The JUDGe 2026 workshop frames judge validity as a systems property: "Evaluation validity is not a property of
  a judge in isolation" [S25] (2026). Peer-reviewed baseline beneath it: reliability varies by
  property, judge expertise, and whether text is human- or model-generated [S21] (ACL 2025).
- Contamination has its own position paper, which sets out to "highlight the wide prevalence of
  benchmark dataset contamination and outline the properties of contamination-resistant datasets"
  [S14] (ICML 2026 Position Track).

**What LMs represent vs what they output**

- A grammaticality probe "outperforms LM probability-based grammaticality judgments" — yet
  on semantic plausibility "the probe however performs worse than string probability" [S12] (2026-05).
- ACL 2026's Best Paper found a directional semantic failure: a "pervasive Teleological Bias" where
  models "hallucinate completion for goal-oriented events, even overriding explicit textual
  cancellation"; prompting interventions "partially reduce this bias but trigger a calibration
  crisis" [S8] (2026).

**Cognitive modelling and the scale paradox**

- Surprisal's fit to reading times peaks near two billion training tokens, after which perplexity
  gains produce "poorer fits to human reading times" [S16] (Findings of EMNLP 2023).
- Not an artifact of latency measures — the inverse relation "still obtains" on two fMRI datasets
  across 17 LMs [S17] (EACL 2026).
- The predictor is unstable: early-layer representations beat surprisal on early-pass eye movements,
  and "the best-performing predictor varies strongly depending on the language and eye-tracking
  measure" [S23] (ACL 2026).

**The resource map and language varieties**

- Catalogue counts mislead: 59% of the surveyed languages score zero catalogued-dataset density, yet literature mining shows active dataset production for many [S5] (2026-05).
- The dominant multilingual benchmark is criticized at protocol level — many translations "fall below
  the claimed 90% quality standard", and "copying named entities, can yield non-trivial BLEU
  scores" [S13] (EMNLP 2025).

**Annotation, disagreement, pluralism**

- The perspectivist turn has its own survey, mapping "a shift from consensus learning toward
  explicitly modeling disagreement, and toward capturing structured relationships among
  annotators" [S6] (2026-01).

**Meta-science of the field**

- Submission volume outran reviewing capacity — 17,087 submissions against 1,424 area chairs,
  with the community weighing "options for limiting submissions for the first time in ACL's
  history" [S1] (2026-05) — yet measured review quality shows "no consistent decline in median
  review quality across venues and years" [S22] (2026-01). ACL 2026's special theme was model
  explainability [S10].

## Recent (~1–2 yr, compressed) · Durable core

- Durable and still load-bearing: surprisal theory as the LM-to-processing-cost bridge [S16];
  minimal-pair evaluation as the standard syntactic instrument [S12]; direct probability
  measurement as the stronger read-out of linguistic knowledge [S3]; the child-learning data
  bound — "less than 100 million words" — with curriculum learning, heavily attempted,
  "largely unsuccessful" [S18].
- The three standing stances on LLMs and linguistic theory [S4]: **insulationism** (LLMs are
  irrelevant to human language), **eliminativism** (they can replace traditional linguistic
  theories), **conciliationism** (they are useful tools for linguistic research).

## ⛔ Already crowded — go ELSEWHERE (do-not-redo)

The blank space is NOT in these lanes; each is saturated through H1-2026:

- **Creating another multilingual / low-resource benchmark.** Dense and institutionalized: the
  FLORES+ family plus its published protocol critique [S13], variety-level suites [S19], and
  and a 232-paper survey of the multilingual/edge pipeline [S20].
- **Benchmark-contamination detection.** Saturated; the prevalence of contamination and the
  properties of resistant datasets are already laid out in a peer-reviewed position paper [S14].
- **LLM-as-judge meta-evaluation and bias catalogues.** A 20-dataset / 11-model peer-reviewed study
  [S21] plus a dedicated 2026 workshop [S25] own this.
- **Minimal-pair grammaticality evaluation and its representation-level follow-up.** Models already
  "discriminate well between grammatical and ungrammatical sentences in tightly controlled minimal
  pairs", and the probe-vs-probability comparison is published [S12].
- **Human label variation / perspectivist modelling.** Mapped end-to-end by its own survey [S6] and
  already escalated into post-training [S7].
- **Computational morphology and low-resource dependency parsing.** Both have their own survey and
  a 2026 cross-architecture evaluation [S29] [S30].
- **Computational sociolinguistics / dialect NLP.** Mapped by its own survey [S27], with a
  variety-level benchmark already published [S19].
- **Sign-language processing tooling and reproducibility.** The ad-hoc-code problem and a framework
  answer to it are published [S28].
- **Language-documentation annotation tooling.** 98 tools already surveyed against documentary
  requirements [S26].
- **Coreference and discourse resolution.** A shared-task series in its fifth edition, with a 2026
  benchmark wave alongside it [S31].
- **Diachronic / lexical semantic change.** Mature enough that its canonical benchmark is itself
  under published critique, with a dedicated workshop series [S32].
- **Surprisal-vs-reading-time psychometrics.** The inverse-scaling result, its tipping point, its
  fMRI generalization, and its layerwise refinement are all published [S16] [S17] [S23].

> **Standing directive — this list is necessarily INCOMPLETE.** Map-silence means *not-yet-checked*,
> NOT *open*. Before committing to any direction this map does not explicitly flag as crowded, run a
> fresh, dated saturation search and confirm the space is actually unoccupied. (Measured in this forge's own
> A/B runs: a live-searching baseline beats a static handbook precisely on the crowded lanes a map omits.)

## Open questions the field hasn't answered

*(the whole lens — the reader answers in their own way)*

1. Prompted output underestimates linguistic knowledge [S3], and grammaticality separates in hidden
   states where string probability does not [S12]. **Is the observable this field treats as its
   measurement — model output, or string probability — even the right object for a claim about
   linguistic competence?** Instruments changed without this being settled.
2. If a review of 445 benchmarks finds validity-undermining patterns [S2] while judge validity is a
   property of a whole pipeline rather than a judge [S25], what would a capability claim here have
   to report before it should be believed?
3. LLMs supply how-possibly but not how-actually explanations of language [S4]. What evidence would
   move a computational result across that line, and does any current design even address it?
4. The best cognitive predictor is a deliberately undertrained model [S16] [S17], while the strongest
   predictor varies by layer, language, and measure [S23]. What is being modelled when psychometric
   fit and language-modelling quality pull in opposite directions?
5. Catalogue counts and literature evidence disagree about which languages are resourced [S5], and
   the dominant benchmark is protocol-flawed for exactly those languages [S13]. Is "low-resource" a
   property of languages, of documentation infrastructure, or of evaluation design?
6. Submission volume outran reviewing capacity to the point of considering caps [S1], yet measured
   review quality has not declined [S22]. If the bottleneck is not quality, what is the constraint
   actually selecting for in what gets published?

## What counts as DEEP here (taste)

| Naive move | Expert judgment/move | Why (failure prevented) | tier | src |
|---|---|---|---|---|
| Add a benchmark, a language, or a model to an existing evaluation and report the numbers. | *Computational Linguistics* prints the bar for a **squib**: "unexpectedness, as for example a demonstration that a commonly accepted idea or method is flawed", or "genuine novelty, as for example thus-far unnoticed language data that challenges current methods". Not "more coverage". | problematizes-nothing — coverage counts only if it breaks something | A | [S9] |
| Probe an LLM on a linguistic phenomenon and report accuracy. | The ACL 2026 **Best Paper** derived a diagnostic from linguistic theory, found a *systematic directional* failure — models "systematically hallucinate completion for goal-oriented events" — and showed prompting fixes "partially reduce this bias but trigger a calibration crisis". Theory-derived contrast plus a failure with a shape. | problematizes-nothing — an accuracy number on a new phenomenon is coverage | L | [S8] |
| Conclude from failed metalinguistic prompts that a model lacks a linguistic generalization. | **Buried (EMNLP 2023):** metalinguistic judgments are inferior to direct probability read-outs, and "consistency gets worse as the prompt query diverges from direct measurements of next-word probabilities". Reopening condition: the same negative result reproduced against direct probability measurement. | wrong-result — you measured the probe, not the model | L | [S3] |

> **Science-vs-application, as this field draws it:** the journal asks for a "substantive
> contribution to the computational processing of language" and clear unexpectedness, genuine
> novelty, or broad relevance [S9]. A working system with a headline number and no overturned
> assumption is application-tier — hence the separate resource, demo, and social-impact award
> tracks rather than one axis [S15].

## Critical rules (execution · eval · validity)

| Naive move | Expert judgment/move | Why (failure prevented) | tier | src |
|---|---|---|---|---|
| Test linguistic knowledge by prompting the model to judge. | Designing the probe: read probabilities directly where possible; report prompting as a second, weaker measurement — never as sole evidence for absence. | wrong-result — negative results are unsound from prompts alone | L | [S3] |
| Report benchmark accuracy as a capability claim. | Writing the claim: define the construct, say how items operationalize it, and report uncertainty. | wrong-result — the score does not measure the named phenomenon | L | [S2] |
| Use FLORES+ as ground truth for low-resource MT quality. | Choosing the eval set: check quality and domain fit for your languages and add a naturalistic set — models strong on one can look weak on the other. | wrong-result — the benchmark's own quality bound caps your conclusion | L | [S13] |
| Aggregate annotations to a majority label by default. | Handling annotation: decide explicitly whether disagreement is error or signal for THIS task; preserve the distribution when it is signal. | wrong-result — artificial consensus erases the phenomenon | L | [S7] [S6] |
| Reach for a pretrained transformer parser on a low-resource language. | Choosing the architecture: below the data crossover a Biaffine LSTM beats transformers, and morphological complexity widens that disadvantage. | wasted-cost — the bigger model is the weaker one in that regime | L | [S30] |
| Call a language low-resource from catalogue counts. | Scoping resources: check literature-level dataset circulation, not just registered catalogues, before claiming a data gap. | wrong-result — the gap may be documentation, not data | L | [S5] |
| Argue cognitive plausibility from a bigger, better LM. | Making a processing claim: treat training data and model scale as deliberate variables and report layer and measure — the best predictor changes with both. | wrong-result — the inverse relation holds on latency and fMRI alike [S17]; fit peaks near 2B training tokens [S16] | L | [S16] [S17] [S23] |

## Decision guide

- **Competence vs performance:** for "does the model know X", read probabilities or probe
  representations [S3] [S12]; for "does it use X when generating", behavioral output is right —
  do not swap them.
- **Cognitive-modelling target:** latency and fMRI now agree on inverse scaling [S16] [S17]; early-
  vs late-pass measures disagree on the best predictor [S23] — name the measure before the model.
- **Aggregating annotations:** aggregate when the task has a defensible single answer; preserve the
  distribution when variation is interpretive [S6] [S7].
- **Placing yourself in the theory debate:** the field names three positions — insulationist,
  eliminativist, conciliationist [S4]; a paper implies one whether or not it says so.

## Ground rules (known-lane — terse)

- Surprisal = negative log probability of a word in context; the standard LM-to-processing-cost link [S16].
- Minimal pairs = near-identical sentences differing in acceptability; BLiMP-style suites are the
  canonical syntactic instrument [S12].
- Human label variation (HLV) = legitimate annotator disagreement, distinct from annotation error [S7].
- Construct validity = whether a measure represents the phenomenon it names; now a routine reviewer
  question in this field [S2].

## Reference documentation

- **[volatile.md](volatile.md)** — dated frontier numbers, lane-occupancy flags, and per-source
  review status. Re-check this FIRST before any novelty verdict or write-up.

## Candidate lane  ⚠️ (expert to resolve — NOT verified)

- ⚠️ **No peer-reviewed 2026 synthesis of "what computational linguistics is now" was recoverable
  this pass.** A Philosophy Compass survey of the philosophy of language models exists but was
  paywalled; the field-identity framing rests on one preprint [S4] plus venue artifacts [S9] [S10].
  Confirm before asserting a field-wide consensus in a write-up.
- ⚠️ **The ACL 2026 award slate could not be read with committee rationale** — the page lists titles
  only, so the taste row rests on the paper's own abstract [S8] plus the journal's printed criteria
  [S9], not a meta-review. Confirm/refute: an award rationale or area-chair commentary for ACL 2026.
```

### [11] SYSTEM-USER prompt · 2026-08-13 11:44:01 UTC

```
<task-notification>
<task-id>b6fi00099</task-id>
<tool-use-id>toolu_016neGokSPzwMf4852hbU65x</tool-use-id>
<output-file>/tmp/claude-0/-ai-inventor-aii-data-runs-run-oQQwThF8kM-b-3-invention-loop-iter-1-gen-art-gen-art-dataset-1/d6e9efb7-9a2a-49b0-91b3-aebecd89bcc0/tasks/b6fi00099.output</output-file>
<status>completed</status>
<summary>Background command "mkdir -p temp/datasets/ud_sample /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/temp/datasets
cat &gt; /tmp/dl_ud.py &lt;&lt; 'EOF'
import json, sys
from pathlib import Path
from huggingface_hub import hf_hub_download, HfApi
from loguru import logger
import pandas as pd

logger.remove(); logger.add(sys.stdout, level="INFO")

TREEBANKS = [
 "en_gum","en_ewt","en_childes","fr_rhapsodie","fr_gsd","sl_ssj","sl_sst",
 "et_ewt","ar_padt","ja_gsd","ko_gsd","fi_tdt","tr_imst","zh_gsd","hi_hdtb",
 "ru_syntagrus","eu_bdt","wo_wtb","ta_ttb","pcm_nsc","de_gsd","pt_gsd",
 "id_gsd","sv_talbanken","la_ittb","bxr_bdt","sah_yktdt","swl_sslc",
]

api = HfApi()
info = api.dataset_info("commul/universal_dependencies")
all_files = [s.rfilename for s in info.siblings if s.rfilename.endswith(".parquet")]

out_dir = Path("temp/datasets/ud_sample")
out_dir.mkdir(parents=True, exist_ok=True)
rows_total = 0
manifest = []
for tb in TREEBANKS:
    files = [f for f in all_files if f.startswith(f"parquet/{tb}/")]
    if not files:
        logger.warning(f"NO FILES for {tb}")
        continue
    for f in files:
        local = hf_hub_download(repo_id="commul/universal_dependencies", filename=f, repo_type="dataset")
        df = pd.read_parquet(local)
        split = f.split("/")[-1].replace(".parquet","")
        dest = out_dir / f"{tb}__{split}.parquet"
        df.to_parquet(dest)
        rows_total += len(df)
        manifest.append({"treebank": tb, "split": split, "n_sentences": len(df), "file": str(dest.relative_to("temp/datasets"))})
        logger.info(f"{tb}/{split}: {len(df)} sentences -&gt; {dest}")

Path("temp/datasets/ud_sample_manifest.json").write_text(json.dumps(manifest, indent=2))
logger.info(f"TOTAL sentences downloaded: {rows_total}")
EOF
source .venv/bin/activate &amp;&amp; python3 /tmp/dl_ud.py 2&gt;&amp;1 | tail -100" completed (exit code 0)</summary>
</task-notification>
```

### [12] SYSTEM-USER prompt · 2026-08-13 11:46:11 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: UD Dependency Arcs with Survival-Analysis Features
summary: >-
  Assemble all dependency arcs from 296+ Universal Dependencies treebanks (168+ languages) with computed arc lengths, position-bounded
  censoring bounds, register/modality labels, typological covariates, and language-family groupings for survival-analysis
  investigation of dependency-length minimization.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  Complete extraction of every dependency arc from all accessible UD treebanks (v2.18, 296+ treebanks) with arc-level features:
  observed arc length d, position-bounded maximum arc length (censoring bound based on token distance to sentence boundary),
  register/modality label (spoken vs. written vs. other), language code and language family (via Glottolog), and typological
  covariates (word-order class, morphological richness proxy from WALS/Grambank or UD morphology feature count). Schema must
  explicitly document censoring bounds and their sentence-position basis. Target: 1-5 million individual arc records, split
  into full (all arcs), mini (50k random sample for testing), and preview (500-1k examples) variants. All data validated against
  source treebanks and cross-referenced with Glottolog for family labels and WALS/Grambank for typological features where
  available.
dataset_search_plan: |-
  1. PRIMARY SOURCE: Download commul/universal_dependencies from HuggingFace (296+ treebanks as of v2.18, May 2026). This includes all CoNLL-U formatted treebanks with metadata.

  2. METADATA & REGISTER LABELING: For each treebank, extract register/modality labels from (a) treebank README.md machine-readable metadata (YAML), (b) 18 genre categories documented in UD (spoken, written, academic, news, fiction, web, etc.), and (c) special UD features like # speaker/addressee tokens which mark spoken interaction. Priority sources: English-GUM (12 genres including spoken/written), French-Rhapsodie (spoken) + French-GSD (written), Slovenian (paired data per recent paper), English-CHILDES (child-adult interaction), Estonian-EWT. For treebanks with only one register, label accordingly but include them (fallback: treat unspecified as 'unspecified' rather than drop).

  3. ARC EXTRACTION & CENSORING BOUNDS: For each token in each sentence: (a) extract its head token ID and compute arc length d = |token_id - head_id|, (b) compute censoring bound = max(token_id, sentence_length - token_id) [the distance to the NEARER sentence boundary, which structurally prevents any arc longer than this], (c) flag if d > censoring_bound (data quality check; should be zero). Output: one row per arc with fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound, register, language_code, language_name, family_id, word_order_type, morph_richness_proxy.

  4. TYPOLOGICAL FEATURES: (a) WALS lookup by language code: retrieve word-order features (SVO/SOV/VSO class if available) and nominal-morphology features (case marking yes/no). (b) Grambank lookup: binary features for word-order patterns (SVO/SOV/VSO/VOS/OVS/OSV presence) and morphological richness indicators. (c) FALLBACK: If WALS/Grambank has no entry for a language, compute morphological-richness proxy = count of distinct UD morphological features (POS, Gender, Number, Case, Tense, Mood, etc.) in that treebank's tokens, normalized by token count, as a scalar between 0-1. Include a 'data_source' field for each typological feature (WALS/Grambank/UD_proxy) so quality is transparent.

  5. LANGUAGE FAMILIES (Glottolog): (a) Download Glottolog CLDF dataset (from GitHub glottolog/glottolog or glottolog/glottolog-cldf or ZENODO). (b) Use pyglottolog Python API to look up each language by ISO code and extract its classification path (family, subfamily if available). (c) Use the top-level family node as the 'family_id' for frailty grouping; also include full classification path as 'family_path' for reference. (d) Fallback: if a language is not in Glottolog, mark family_id as 'unknown' but do NOT drop the treebank.

  6. SCHEMA DESIGN & VALIDATION: Design JSON schema (one row per arc) with required fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound [CRITICAL: document that censoring_bound = max(token_id, sent_len - token_id) in schema description], register (enum: spoken, written, academic, news, fiction, web, other, unspecified), language_code, language_name, family_id, family_path, word_order_type (optional, nullable), morph_richness_proxy (float 0-1), morph_richness_data_source (WALS/Grambank/UD_proxy). Use aii-json skill to validate a sample of rows before final output.

  7. QUALITY CHECKS & SPOT-VALIDATION: (a) For a random sample of 100-200 arcs, verify that arc_length <= censoring_bound (should be 100% true; flag any violations). (b) Cross-check register labels: spot-read treebank metadata to confirm 'spoken' arcs come from marked spoken subcorpora. (c) Verify language codes are ISO 639-3 and consistent across UD and Glottolog. (d) For 10-20 languages with matched WALS and Grambank entries, confirm word-order classification consistency between sources (should be close to identical). (e) Inspect morphological-richness proxies for outliers (plot distribution, should be unimodal and clustered around 0.1-0.6 for most languages).

  8. SPLITS & EXPORT: (a) FULL: All extracted arcs, deduplicated, ordered by language, treebank, sentence. (b) MINI: 50k random arcs stratified by register and language family (for quick iteration in executor testing). (c) PREVIEW: 500-1000 arcs from diverse languages/registers for documentation. All three as data_out.json with one JSON object per line (JSONL) or as a single JSON array, depending on size; use aii-file-size-limit skill if >300MB to advise on splits. Include a schema document and a summary statistics table (arcs per language, arcs per register, arc-length distribution quartiles by register).

  9. FALLBACK & ROBUSTNESS: If HuggingFace API fails, fetch UD treebanks directly from UniversalDependencies GitHub (UD_<language>-<treebank> repos). If Glottolog unavailable, use cached/static Glottolog export (available on ZENODO as versioned snapshot). If WALS/Grambank incomplete, ensure UD_proxy is computed for all languages. If a treebank has parsing errors or malformed CoNLL-U, log the issue and skip that treebank but continue; do NOT fail the entire run.

  10. DOCUMENTATION: Generate a README.md with data dictionary, sample rows, source citations (commul/universal_dependencies, Glottolog, WALS, Grambank), notes on censoring-bound computation (with a concrete example sentence), register labeling methodology, known limitations (e.g., % of languages with paired spoken/written data, % coverage by WALS/Grambank vs UD_proxy), and reproduction instructions (language/versions of pyglottolog, UD dataset commit, etc.).
target_num_datasets: 1
</artifact_plan>



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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Update data.py to only include the chosen 1 dataset and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
TODO 2. Verify full_data_out.json, preview_data_out.json, and mini_data_out.json exist in your workspace (see <workspace>) and contain correct data.
TODO 3. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to full_data_out.json.
TODO 4. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DatasetExpectedFiles": {
      "description": "All expected output files from dataset artifact.",
      "properties": {
        "script": {
          "description": "Path to data.py script. Example: 'data.py'",
          "title": "Script",
          "type": "string"
        },
        "datasets": {
          "description": "Dataset file groups \u2014 one per dataset, each with full/mini/preview variants",
          "items": {
            "$ref": "#/$defs/DatasetFileSet"
          },
          "title": "Datasets",
          "type": "array"
        }
      },
      "required": [
        "script",
        "datasets"
      ],
      "title": "DatasetExpectedFiles",
      "type": "object"
    },
    "DatasetFileSet": {
      "description": "One dataset's three required output variants.",
      "properties": {
        "full": {
          "description": "Full dataset JSON file(s). Single file or split files. Example: ['full_data_out.json'] or ['full_data_out/full_data_out_1.json', 'full_data_out/full_data_out_2.json']",
          "items": {
            "type": "string"
          },
          "title": "Full",
          "type": "array"
        },
        "mini": {
          "description": "Mini dataset JSON file path (3 examples). Example: 'mini_data_out.json'",
          "title": "Mini",
          "type": "string"
        },
        "preview": {
          "description": "Preview dataset JSON file path (10 examples). Example: 'preview_data_out.json'",
          "title": "Preview",
          "type": "string"
        }
      },
      "required": [
        "full",
        "mini",
        "preview"
      ],
      "title": "DatasetFileSet",
      "type": "object"
    }
  },
  "description": "Dataset artifact \u2014 structured output + file metadata.\n\nFinds, evaluates, and prepares datasets for research experiments.\nProduces data.py and full_data_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/DatasetExpectedFiles",
      "description": "All output files you created. Must include data.py script plus dataset file groups (full/mini/preview variants)."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "DatasetArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [13] SYSTEM-USER prompt · 2026-08-13 11:47:07 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [14] SYSTEM-USER prompt · 2026-08-13 11:47:19 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [15] SYSTEM-USER prompt · 2026-08-13 11:47:29 UTC

```
<validation-feedback>
Attempt 3 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [16] SYSTEM-USER prompt · 2026-08-13 11:49:41 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Find, evaluate, and prepare high-quality datasets for the research experiment.
Adapt your search strategy based on the hypothesis and domain requirements.
</task>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. MUST check for and avoid each one.

**1. Picking Obscure or Unusable Datasets**
Do NOT select datasets just because they match a keyword. Red flags: very few downloads (<100), no documentation (dataset card, paper, or GitHub page). Prefer well-used datasets (not necessarily popular or widely known) with clear documentation.
CHECK: >100 downloads? Has documentation? If any "no" → find a better dataset.

**2. Fabricating Dataset Provenance**
Do NOT invent justifications for why a dataset is relevant. If a dataset name contains a number (e.g., "797"), do NOT assume it refers to a specific benchmark suite, OpenML ID, or paper without verification. In past runs, an agent assumed "797" referred to "OpenML benchmark suite 797" with zero evidence, then fabricated a rationale. This was completely false.
CHECK: Can you cite a specific, verifiable source (paper, benchmark page, dataset card) confirming this dataset is what you claim? If not, do not make provenance claims.

**3. Not Verifying Dataset Usefulness**
Always sanity-check that a dataset is actually suitable for the task before committing. Download a sample, inspect the features, and run a quick baseline appropriate for the domain. If the dataset lacks signal or structure for the hypothesis being tested, the entire experiment is wasted.

**4. Settling for the Only Search Result**
If your search returns only 1-2 results, your search terms are too narrow. Broaden your queries, try different keyword combinations, or search for well-known benchmark datasets in the domain. A single obscure result from a narrow query should never be your final choice.
CHECK: Fewer than 5 candidate datasets? Run additional searches with broader or different terms before making a selection.
</common_mistakes_to_avoid>

<critical_requirements>
- Keep final response under 300 characters
</critical_requirements>

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

<CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>
YOUR PREVIOUS EXECUTION ATTEMPT CATASTROPHICALLY FAILED.
The entire worker container crashed after 704s.
Error: output_format validation failed after 3 retries: The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Last messages before the crash:
  - [agent_tool_call: Bash] Tool: Bash
cat /ai-inventor/.claude/skills/aii-json/scripts/aii_json_format_mini_preview.py 2>/dev/null | head -100
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "#!/usr/bin/env python\n\"\"\"\nJSON Formatter - Generate full, mini, and preview versions\n\nCreates three versions of a JSON file:\n- full: Identical to original\n- mini: Only first 3 items from primary array\n- preview: Mini version with all strings truncated to 200 chars\n\nSupports both bare arrays and dict-wrapped arrays (e.g. {\"examples\": [...]}).\nUse --format to specify which schema format to use (determines the array key).\n\nUsage:\n    python aii_json_format_mini_preview.py --input data.json\n    python aii_json_format_mini_preview.py --format exp_sel_data_out --input data.json\n    python aii_json_format_mini_preview.py --format exp_sel_data_out --input data.json --output-dir ./output\n\"\"\"\n\nimport argparse\nimport sys\nfrom pathlib import Path\n\ntry:\n    from aii_lib.abilities.aii_ability import aii_ability\nexcept ImportError:  # standalone use: aii_lib / ability server not installed\n\n    def aii_ability(*_args, **_kwargs):\n        \"\"\"No-op decorator fallback (the real one only attaches server metadata).\"\"\"\n\n        def _decorator(func):\n            return func\n\n        return _decorator\n\n\nSERVER_NAME = \"aii_json__format\"\nDEFAULT_TIMEOUT = 60.0\n\n# Configuration\nMAX_ARRAY_ITEMS = 3\nMAX_STRING_LENGTH = 200\nTRUNCATE_MARKER = \"...\"\n\n# Format → primary array key mapping (must match schemas in ../schemas/)\n# For datasets-grouped schemas, the top-level key is \"datasets\" and each\n# entry contains an \"examples\" array that also needs slicing.\nFORMAT_ARRAY_KEY: dict[str, str] = {\n    \"exp_sel_data_out\": \"datasets\",\n    \"exp_gen_sol_out\": \"datasets\",\n    \"exp_eval_sol_out\": \"datasets\",\n    \"exp_proof_out\": \"lemmas\",\n}\n\n# Schemas that use datasets-grouped structure (need nested example slicing)\nDATASETS_GROUPED_FORMATS = {\"exp_sel_data_out\", \"exp_gen_sol_out\", \"exp_eval_sol_out\"}\n\n\n# =============================================================================\n# Core Logic (used by server handler)\n# =============================================================================\n\n\ndef init_json_format():\n    \"\"\"Initialize JSON format environment with warmup.\"\"\"\n    import json\n\n    # Warmup: parse/serialize a small JSON to warm up the module\n    json.loads(json.dumps({\"warmup\": True}))\n\n\n@aii_ability(\n    name=\"aii_json__format\",\n    description=\"Generate full, mini, and preview versions of a JSON file.\",\n    venv=\"../../.ability_client_venv\",\n    requirements=\"server_requirements.txt\",\n    worker_init=\"init_json_format\",\n)\ndef core_json_format(\n    input_file: str = \"\", output_dir: str | None = None, format_type: str | None = None\n) -> dict:\n    \"\"\"\n    Generate full, mini, and preview versions of JSON file.\n\n    Args:\n        input_file: Path to input JSON file\n        output_dir: Optional output directory (defaults to same as input)\n        format_type: Optional schema format (e.g. \"exp_
  - [agent_tool_call: Bash] Tool: Bash
rm -f /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json
df -h /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1 | tail -1
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "mfs#euro-2.runpod.net:9421  2.1P  1.4P  742T  66% /ai-inventor/aii_data", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_response] Now updating data.py to write pre-split shards directly (avoiding a 5GB monolithic file) plus mini/preview.
  - [agent_tool_call: Edit] Tool: Edit
File: /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data.py
OLD: def main():
    manifest = json.loads((DATA_DIR / "ud_sample_manifest.json").read_text())

    # FINAL CHOICE: ud_arcs_curated. Registers come from each treebank's own documented
    # provenance (spoken vs. written subcorpora, e.g. sl_sst/sl_ssj, fr_rhapsodie/fr_gsd,
    # en_childes/en_ewt), not from commul/ud_genre's bootstrapped classifier, whose own
    # dataset card states its labels "are not authoritative gold annotations."
    ds1 = build_ud_arcs_curated(manifest, None)

    out = {
        "metadata": {
            "source": "commul/universal_dependencies (HF), Grambank CLDF (GitHub grambank/grambank), Glottolog CLDF (GitHub glottolog/glottolog-cldf)",
            "description": "Dependency-arc-level records with survival-analysis censoring bounds, register, family, and typology covariates, from a 28-treebank curated sample of commul/universal_dependencies spanning spoken/written register-matched pairs (sl_sst/sl_ssj, fr_rhapsodie/fr_gsd, en_childes/en_ewt/en_gum) and 20+ language families.",
        },
        "datasets": [
            {"dataset": "ud_arcs_curated", "examples": ds1},
        ],
    }
    out_path = BASE / "full_data_out.json"
    out_path.write_text(json.dumps(out))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size / 1e6:.1f} MB)")
NEW: METADATA = {
    "source": "commul/universal_dependencies (HF), Grambank CLDF (GitHub grambank/grambank), Glottolog CLDF (GitHub glottolog/glottolog-cldf)",
    "description": "Dependency-arc-level records with survival-analysis censoring bounds, register, family, and typology covariates, from a 28-treebank curated sample of commul/universal_dependencies spanning spoken/written register-matched pairs (sl_sst/sl_ssj, fr_rhapsodie/fr_gsd, en_childes/en_ewt/en_gum) and 20+ language families.",
}
DATASET_NAME = "ud_arcs_curated"
SHARD_SIZE = 100_000  # ~874 bytes/example observed -> ~85MB/shard, under the 100MB limit


def truncate_strings(obj, max_len=200):
    if isinstance(obj, str):
        return obj[:max_len] + "..." if len(obj) > max_len else obj
    if isinstance(obj, list):
        return [truncate_strings(x, max_len) for x in obj[:3]]
    if isinstance(obj, dict):
        return {k: truncate_strings(v, max_len) for k, v in obj.items()}
    return obj


def main():
    manifest = json.loads((DATA_DIR / "ud_sample_manifest.json").read_text())

    # FINAL CHOICE: ud_arcs_curated. Registers come from each treebank's own documented
    # provenance (spoken vs. written subcorpora, e.g. sl_sst/sl_ssj, fr_rhapsodie/fr_gsd,
    # en_childes/en_ewt), not from commul/ud_genre's bootstrapped classifier, whose own
    # dataset card states its labels "are not authoritative gold annotations."
    examples = build_ud_arcs_curated(manifest, None)
    n = len(examples)

    out_dir = BASE / "full_data_out"
    out_dir.mkdir(exist_ok=True)
    n_shards = (n + SHARD
  - [agent_tool_result: Edit] Tool: Edit
Result:
{"filePath": "/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/data.py", "oldString": "def main():\n    manifest = json.loads((DATA_DIR / \"ud_sample_manifest.json\").read_text())\n\n    # FINAL CHOICE: ud_arcs_curated. Registers come from each treebank's own documented\n    # provenance (spoken vs. written subcorpora, e.g. sl_sst/sl_ssj, fr_rhapsodie/fr_gsd,\n    # en_childes/en_ewt), not from commul/ud_genre's bootstrapped classifier, whose own\n    # dataset card states its labels \"are not authoritative gold annotations.\"\n    ds1 = build_ud_arcs_curated(manifest, None)\n\n    out = {\n        \"metadata\": {\n            \"source\": \"commul/universal_dependencies (HF), Grambank CLDF (GitHub grambank/grambank), Glottolog CLDF (GitHub glottolog/glottolog-cldf)\",\n            \"description\": \"Dependency-arc-level records with survival-analysis censoring bounds, register, family, and typology covariates, from a 28-treebank curated sample of commul/universal_dependencies spanning spoken/written register-matched pairs (sl_sst/sl_ssj, fr_rhapsodie/fr_gsd, en_childes/en_ewt/en_gum) and 20+ language families.\",\n        },\n        \"datasets\": [\n            {\"dataset\": \"ud_arcs_curated\", \"examples\": ds1},\n        ],\n    }\n    out_path = BASE / \"full_data_out.json\"\n    out_path.write_text(json.dumps(out))\n    logger.info(f\"Wrote {out_path} ({out_path.stat().st_size / 1e6:.1f} MB)\")", "newString": "METADATA = {\n    \"source\": \"commul/universal_dependencies (HF), Grambank CLDF (GitHub grambank/grambank), Glottolog CLDF (GitHub glottolog/glottolog-cldf)\",\n    \"description\": \"Dependency-arc-level records with survival-analysis censoring bounds, register, family, and typology covariates, from a 28-treebank curated sample of commul/universal_dependencies spanning spoken/written register-matched pairs (sl_sst/sl_ssj, fr_rhapsodie/fr_gsd, en_childes/en_ewt/en_gum) and 20+ language families.\",\n}\nDATASET_NAME = \"ud_arcs_curated\"\nSHARD_SIZE = 100_000  # ~874 bytes/example observed -> ~85MB/shard, under the 100MB limit\n\n\ndef truncate_strings(obj, max_len=200):\n    if isinstance(obj, str):\n        return obj[:max_len] + \"...\" if len(obj) > max_len else obj\n    if isinstance(obj, list):\n        return [truncate_strings(x, max_len) for x in obj[:3]]\n    if isinstance(obj, dict):\n        return {k: truncate_strings(v, max_len) for k, v in obj.items()}\n    return obj\n\n\ndef main():\n    manifest = json.loads((DATA_DIR / \"ud_sample_manifest.json\").read_text())\n\n    # FINAL CHOICE: ud_arcs_curated. Registers come from each treebank's own documented\n    # provenance (spoken vs. written subcorpora, e.g. sl_sst/sl_ssj, fr_rhapsodie/fr_gsd,\n    # en_childes/en_ewt), not from commul/ud_genre's bootstrapped classifier, whose own\n    # dataset card states its labels \"are not authoritative gold annotations.\"\n    examples = build_ud_arcs_curated(manifest,
  - [agent_tool_call: Bash] Tool: Bash
cd /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
source .venv/bin/activate
nohup python3 data.py > logs/data_run3.log 2>&1 &
echo "PID: $!"
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "PID: 1795", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_tool_call: Monitor] Tool: Monitor
{'command': 'while kill -0 1795 2>/dev/null; do sleep 5; done; echo "process 1795 ended"; tail -15 /ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/logs/data_run3.log', 'description': 'wait for shard-writing data.py run to finish', 'timeout_ms': 600000, 'persistent': False}
  - [agent_tool_result: Monitor] Tool: Monitor
Result:
{"taskId": "bw2ps5p7d", "timeoutMs": 600000, "persistent": false}
  - [agent_response] Waiting for the sharded write to complete.
  - [agent_tool_call: Bash] Tool: Bash
echo ok
  - [agent_tool_result: Bash] Tool: Bash
Result:
{"stdout": "ok", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
  - [agent_response] Waiting on the background shard-writing run to finish.

This was NOT a normal code error — the entire container died. Study the error
and last messages above carefully. Identify what caused the crash and be
EXTREMELY careful to avoid repeating it. Do NOT use the same approach.
</CRITICAL_WARNING__PREVIOUS_ATTEMPT_CRASHED>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: UD Dependency Arcs with Survival-Analysis Features
summary: >-
  Assemble all dependency arcs from 296+ Universal Dependencies treebanks (168+ languages) with computed arc lengths, position-bounded
  censoring bounds, register/modality labels, typological covariates, and language-family groupings for survival-analysis
  investigation of dependency-length minimization.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  Complete extraction of every dependency arc from all accessible UD treebanks (v2.18, 296+ treebanks) with arc-level features:
  observed arc length d, position-bounded maximum arc length (censoring bound based on token distance to sentence boundary),
  register/modality label (spoken vs. written vs. other), language code and language family (via Glottolog), and typological
  covariates (word-order class, morphological richness proxy from WALS/Grambank or UD morphology feature count). Schema must
  explicitly document censoring bounds and their sentence-position basis. Target: 1-5 million individual arc records, split
  into full (all arcs), mini (50k random sample for testing), and preview (500-1k examples) variants. All data validated against
  source treebanks and cross-referenced with Glottolog for family labels and WALS/Grambank for typological features where
  available.
dataset_search_plan: |-
  1. PRIMARY SOURCE: Download commul/universal_dependencies from HuggingFace (296+ treebanks as of v2.18, May 2026). This includes all CoNLL-U formatted treebanks with metadata.

  2. METADATA & REGISTER LABELING: For each treebank, extract register/modality labels from (a) treebank README.md machine-readable metadata (YAML), (b) 18 genre categories documented in UD (spoken, written, academic, news, fiction, web, etc.), and (c) special UD features like # speaker/addressee tokens which mark spoken interaction. Priority sources: English-GUM (12 genres including spoken/written), French-Rhapsodie (spoken) + French-GSD (written), Slovenian (paired data per recent paper), English-CHILDES (child-adult interaction), Estonian-EWT. For treebanks with only one register, label accordingly but include them (fallback: treat unspecified as 'unspecified' rather than drop).

  3. ARC EXTRACTION & CENSORING BOUNDS: For each token in each sentence: (a) extract its head token ID and compute arc length d = |token_id - head_id|, (b) compute censoring bound = max(token_id, sentence_length - token_id) [the distance to the NEARER sentence boundary, which structurally prevents any arc longer than this], (c) flag if d > censoring_bound (data quality check; should be zero). Output: one row per arc with fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound, register, language_code, language_name, family_id, word_order_type, morph_richness_proxy.

  4. TYPOLOGICAL FEATURES: (a) WALS lookup by language code: retrieve word-order features (SVO/SOV/VSO class if available) and nominal-morphology features (case marking yes/no). (b) Grambank lookup: binary features for word-order patterns (SVO/SOV/VSO/VOS/OVS/OSV presence) and morphological richness indicators. (c) FALLBACK: If WALS/Grambank has no entry for a language, compute morphological-richness proxy = count of distinct UD morphological features (POS, Gender, Number, Case, Tense, Mood, etc.) in that treebank's tokens, normalized by token count, as a scalar between 0-1. Include a 'data_source' field for each typological feature (WALS/Grambank/UD_proxy) so quality is transparent.

  5. LANGUAGE FAMILIES (Glottolog): (a) Download Glottolog CLDF dataset (from GitHub glottolog/glottolog or glottolog/glottolog-cldf or ZENODO). (b) Use pyglottolog Python API to look up each language by ISO code and extract its classification path (family, subfamily if available). (c) Use the top-level family node as the 'family_id' for frailty grouping; also include full classification path as 'family_path' for reference. (d) Fallback: if a language is not in Glottolog, mark family_id as 'unknown' but do NOT drop the treebank.

  6. SCHEMA DESIGN & VALIDATION: Design JSON schema (one row per arc) with required fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound [CRITICAL: document that censoring_bound = max(token_id, sent_len - token_id) in schema description], register (enum: spoken, written, academic, news, fiction, web, other, unspecified), language_code, language_name, family_id, family_path, word_order_type (optional, nullable), morph_richness_proxy (float 0-1), morph_richness_data_source (WALS/Grambank/UD_proxy). Use aii-json skill to validate a sample of rows before final output.

  7. QUALITY CHECKS & SPOT-VALIDATION: (a) For a random sample of 100-200 arcs, verify that arc_length <= censoring_bound (should be 100% true; flag any violations). (b) Cross-check register labels: spot-read treebank metadata to confirm 'spoken' arcs come from marked spoken subcorpora. (c) Verify language codes are ISO 639-3 and consistent across UD and Glottolog. (d) For 10-20 languages with matched WALS and Grambank entries, confirm word-order classification consistency between sources (should be close to identical). (e) Inspect morphological-richness proxies for outliers (plot distribution, should be unimodal and clustered around 0.1-0.6 for most languages).

  8. SPLITS & EXPORT: (a) FULL: All extracted arcs, deduplicated, ordered by language, treebank, sentence. (b) MINI: 50k random arcs stratified by register and language family (for quick iteration in executor testing). (c) PREVIEW: 500-1000 arcs from diverse languages/registers for documentation. All three as data_out.json with one JSON object per line (JSONL) or as a single JSON array, depending on size; use aii-file-size-limit skill if >300MB to advise on splits. Include a schema document and a summary statistics table (arcs per language, arcs per register, arc-length distribution quartiles by register).

  9. FALLBACK & ROBUSTNESS: If HuggingFace API fails, fetch UD treebanks directly from UniversalDependencies GitHub (UD_<language>-<treebank> repos). If Glottolog unavailable, use cached/static Glottolog export (available on ZENODO as versioned snapshot). If WALS/Grambank incomplete, ensure UD_proxy is computed for all languages. If a treebank has parsing errors or malformed CoNLL-U, log the issue and skip that treebank but continue; do NOT fail the entire run.

  10. DOCUMENTATION: Generate a README.md with data dictionary, sample rows, source citations (commul/universal_dependencies, Glottolog, WALS, Grambank), notes on censoring-bound computation (with a concrete example sentence), register labeling methodology, known limitations (e.g., % of languages with paired spoken/written data, % coverage by WALS/Grambank vs UD_proxy), and reproduction instructions (language/versions of pyglottolog, UD dataset commit, etc.).
target_num_datasets: 1
</artifact_plan>



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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 8 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 4 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 2 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
```

### [17] HUMAN-USER prompt · 2026-08-13 11:49:41 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [18] SYSTEM-USER prompt · 2026-08-13 11:53:07 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: UD Dependency Arcs with Survival-Analysis Features
summary: >-
  Assemble all dependency arcs from 296+ Universal Dependencies treebanks (168+ languages) with computed arc lengths, position-bounded
  censoring bounds, register/modality labels, typological covariates, and language-family groupings for survival-analysis
  investigation of dependency-length minimization.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  Complete extraction of every dependency arc from all accessible UD treebanks (v2.18, 296+ treebanks) with arc-level features:
  observed arc length d, position-bounded maximum arc length (censoring bound based on token distance to sentence boundary),
  register/modality label (spoken vs. written vs. other), language code and language family (via Glottolog), and typological
  covariates (word-order class, morphological richness proxy from WALS/Grambank or UD morphology feature count). Schema must
  explicitly document censoring bounds and their sentence-position basis. Target: 1-5 million individual arc records, split
  into full (all arcs), mini (50k random sample for testing), and preview (500-1k examples) variants. All data validated against
  source treebanks and cross-referenced with Glottolog for family labels and WALS/Grambank for typological features where
  available.
dataset_search_plan: |-
  1. PRIMARY SOURCE: Download commul/universal_dependencies from HuggingFace (296+ treebanks as of v2.18, May 2026). This includes all CoNLL-U formatted treebanks with metadata.

  2. METADATA & REGISTER LABELING: For each treebank, extract register/modality labels from (a) treebank README.md machine-readable metadata (YAML), (b) 18 genre categories documented in UD (spoken, written, academic, news, fiction, web, etc.), and (c) special UD features like # speaker/addressee tokens which mark spoken interaction. Priority sources: English-GUM (12 genres including spoken/written), French-Rhapsodie (spoken) + French-GSD (written), Slovenian (paired data per recent paper), English-CHILDES (child-adult interaction), Estonian-EWT. For treebanks with only one register, label accordingly but include them (fallback: treat unspecified as 'unspecified' rather than drop).

  3. ARC EXTRACTION & CENSORING BOUNDS: For each token in each sentence: (a) extract its head token ID and compute arc length d = |token_id - head_id|, (b) compute censoring bound = max(token_id, sentence_length - token_id) [the distance to the NEARER sentence boundary, which structurally prevents any arc longer than this], (c) flag if d > censoring_bound (data quality check; should be zero). Output: one row per arc with fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound, register, language_code, language_name, family_id, word_order_type, morph_richness_proxy.

  4. TYPOLOGICAL FEATURES: (a) WALS lookup by language code: retrieve word-order features (SVO/SOV/VSO class if available) and nominal-morphology features (case marking yes/no). (b) Grambank lookup: binary features for word-order patterns (SVO/SOV/VSO/VOS/OVS/OSV presence) and morphological richness indicators. (c) FALLBACK: If WALS/Grambank has no entry for a language, compute morphological-richness proxy = count of distinct UD morphological features (POS, Gender, Number, Case, Tense, Mood, etc.) in that treebank's tokens, normalized by token count, as a scalar between 0-1. Include a 'data_source' field for each typological feature (WALS/Grambank/UD_proxy) so quality is transparent.

  5. LANGUAGE FAMILIES (Glottolog): (a) Download Glottolog CLDF dataset (from GitHub glottolog/glottolog or glottolog/glottolog-cldf or ZENODO). (b) Use pyglottolog Python API to look up each language by ISO code and extract its classification path (family, subfamily if available). (c) Use the top-level family node as the 'family_id' for frailty grouping; also include full classification path as 'family_path' for reference. (d) Fallback: if a language is not in Glottolog, mark family_id as 'unknown' but do NOT drop the treebank.

  6. SCHEMA DESIGN & VALIDATION: Design JSON schema (one row per arc) with required fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound [CRITICAL: document that censoring_bound = max(token_id, sent_len - token_id) in schema description], register (enum: spoken, written, academic, news, fiction, web, other, unspecified), language_code, language_name, family_id, family_path, word_order_type (optional, nullable), morph_richness_proxy (float 0-1), morph_richness_data_source (WALS/Grambank/UD_proxy). Use aii-json skill to validate a sample of rows before final output.

  7. QUALITY CHECKS & SPOT-VALIDATION: (a) For a random sample of 100-200 arcs, verify that arc_length <= censoring_bound (should be 100% true; flag any violations). (b) Cross-check register labels: spot-read treebank metadata to confirm 'spoken' arcs come from marked spoken subcorpora. (c) Verify language codes are ISO 639-3 and consistent across UD and Glottolog. (d) For 10-20 languages with matched WALS and Grambank entries, confirm word-order classification consistency between sources (should be close to identical). (e) Inspect morphological-richness proxies for outliers (plot distribution, should be unimodal and clustered around 0.1-0.6 for most languages).

  8. SPLITS & EXPORT: (a) FULL: All extracted arcs, deduplicated, ordered by language, treebank, sentence. (b) MINI: 50k random arcs stratified by register and language family (for quick iteration in executor testing). (c) PREVIEW: 500-1000 arcs from diverse languages/registers for documentation. All three as data_out.json with one JSON object per line (JSONL) or as a single JSON array, depending on size; use aii-file-size-limit skill if >300MB to advise on splits. Include a schema document and a summary statistics table (arcs per language, arcs per register, arc-length distribution quartiles by register).

  9. FALLBACK & ROBUSTNESS: If HuggingFace API fails, fetch UD treebanks directly from UniversalDependencies GitHub (UD_<language>-<treebank> repos). If Glottolog unavailable, use cached/static Glottolog export (available on ZENODO as versioned snapshot). If WALS/Grambank incomplete, ensure UD_proxy is computed for all languages. If a treebank has parsing errors or malformed CoNLL-U, log the issue and skip that treebank but continue; do NOT fail the entire run.

  10. DOCUMENTATION: Generate a README.md with data dictionary, sample rows, source citations (commul/universal_dependencies, Glottolog, WALS, Grambank), notes on censoring-bound computation (with a concrete example sentence), register labeling methodology, known limitations (e.g., % of languages with paired spoken/written data, % coverage by WALS/Grambank vs UD_proxy), and reproduction instructions (language/versions of pyglottolog, UD dataset commit, etc.).
target_num_datasets: 1
</artifact_plan>



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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. For the top 2 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

Each data ROW must be a separate example — do NOT create one example per dataset or per fold. Each data point (row, sample, instance) = one example. 500 rows → 500 examples. The output is GROUPED BY DATASET:
```json
{
  "datasets": [
    {
      "dataset": "iris",
      "examples": [
        {"input": "...", "output": "...", "metadata_fold": 2, "metadata_feature_names": [...]},
        ...
      ]
    },
    {
      "dataset": "adult_census",
      "examples": [...]
    }
  ]
}
```
Per-example required fields:
- `input`: input features/text (tabular: JSON string of feature values)
- `output`: target/label (as string)
Per-example optional metadata via `metadata_<name>` fields (flat, not nested object):
- `metadata_fold`: fold assignment (int), `metadata_feature_names`: feature name list, `metadata_task_type`: "classification"/"regression", `metadata_n_classes`: number of classes, `metadata_row_index`: original row index, etc.
Do NOT use `split`, `dataset`, or `context` as per-example fields. Dataset name goes at the group level, metadata goes in `metadata_*` fields.
TODO 2. Run 'uv run data.py' and fix errors. Validate full_data_out.json against exp_sel_data_out.json schema (aii-json skill) — fix errors. Generate preview, mini, full versions with aii-json skill's format script.
TODO 3. Read preview to inspect examples. Choose THE BEST 1 DATASET based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [19] SYSTEM-USER prompt · 2026-08-13 12:04:03 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx2
type: dataset
title: UD Dependency Arcs with Survival-Analysis Features
summary: >-
  Assemble all dependency arcs from 296+ Universal Dependencies treebanks (168+ languages) with computed arc lengths, position-bounded
  censoring bounds, register/modality labels, typological covariates, and language-family groupings for survival-analysis
  investigation of dependency-length minimization.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: >-
  Complete extraction of every dependency arc from all accessible UD treebanks (v2.18, 296+ treebanks) with arc-level features:
  observed arc length d, position-bounded maximum arc length (censoring bound based on token distance to sentence boundary),
  register/modality label (spoken vs. written vs. other), language code and language family (via Glottolog), and typological
  covariates (word-order class, morphological richness proxy from WALS/Grambank or UD morphology feature count). Schema must
  explicitly document censoring bounds and their sentence-position basis. Target: 1-5 million individual arc records, split
  into full (all arcs), mini (50k random sample for testing), and preview (500-1k examples) variants. All data validated against
  source treebanks and cross-referenced with Glottolog for family labels and WALS/Grambank for typological features where
  available.
dataset_search_plan: |-
  1. PRIMARY SOURCE: Download commul/universal_dependencies from HuggingFace (296+ treebanks as of v2.18, May 2026). This includes all CoNLL-U formatted treebanks with metadata.

  2. METADATA & REGISTER LABELING: For each treebank, extract register/modality labels from (a) treebank README.md machine-readable metadata (YAML), (b) 18 genre categories documented in UD (spoken, written, academic, news, fiction, web, etc.), and (c) special UD features like # speaker/addressee tokens which mark spoken interaction. Priority sources: English-GUM (12 genres including spoken/written), French-Rhapsodie (spoken) + French-GSD (written), Slovenian (paired data per recent paper), English-CHILDES (child-adult interaction), Estonian-EWT. For treebanks with only one register, label accordingly but include them (fallback: treat unspecified as 'unspecified' rather than drop).

  3. ARC EXTRACTION & CENSORING BOUNDS: For each token in each sentence: (a) extract its head token ID and compute arc length d = |token_id - head_id|, (b) compute censoring bound = max(token_id, sentence_length - token_id) [the distance to the NEARER sentence boundary, which structurally prevents any arc longer than this], (c) flag if d > censoring_bound (data quality check; should be zero). Output: one row per arc with fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound, register, language_code, language_name, family_id, word_order_type, morph_richness_proxy.

  4. TYPOLOGICAL FEATURES: (a) WALS lookup by language code: retrieve word-order features (SVO/SOV/VSO class if available) and nominal-morphology features (case marking yes/no). (b) Grambank lookup: binary features for word-order patterns (SVO/SOV/VSO/VOS/OVS/OSV presence) and morphological richness indicators. (c) FALLBACK: If WALS/Grambank has no entry for a language, compute morphological-richness proxy = count of distinct UD morphological features (POS, Gender, Number, Case, Tense, Mood, etc.) in that treebank's tokens, normalized by token count, as a scalar between 0-1. Include a 'data_source' field for each typological feature (WALS/Grambank/UD_proxy) so quality is transparent.

  5. LANGUAGE FAMILIES (Glottolog): (a) Download Glottolog CLDF dataset (from GitHub glottolog/glottolog or glottolog/glottolog-cldf or ZENODO). (b) Use pyglottolog Python API to look up each language by ISO code and extract its classification path (family, subfamily if available). (c) Use the top-level family node as the 'family_id' for frailty grouping; also include full classification path as 'family_path' for reference. (d) Fallback: if a language is not in Glottolog, mark family_id as 'unknown' but do NOT drop the treebank.

  6. SCHEMA DESIGN & VALIDATION: Design JSON schema (one row per arc) with required fields: treebank_id, sentence_id, token_id, head_id, deprel, arc_length, censoring_bound [CRITICAL: document that censoring_bound = max(token_id, sent_len - token_id) in schema description], register (enum: spoken, written, academic, news, fiction, web, other, unspecified), language_code, language_name, family_id, family_path, word_order_type (optional, nullable), morph_richness_proxy (float 0-1), morph_richness_data_source (WALS/Grambank/UD_proxy). Use aii-json skill to validate a sample of rows before final output.

  7. QUALITY CHECKS & SPOT-VALIDATION: (a) For a random sample of 100-200 arcs, verify that arc_length <= censoring_bound (should be 100% true; flag any violations). (b) Cross-check register labels: spot-read treebank metadata to confirm 'spoken' arcs come from marked spoken subcorpora. (c) Verify language codes are ISO 639-3 and consistent across UD and Glottolog. (d) For 10-20 languages with matched WALS and Grambank entries, confirm word-order classification consistency between sources (should be close to identical). (e) Inspect morphological-richness proxies for outliers (plot distribution, should be unimodal and clustered around 0.1-0.6 for most languages).

  8. SPLITS & EXPORT: (a) FULL: All extracted arcs, deduplicated, ordered by language, treebank, sentence. (b) MINI: 50k random arcs stratified by register and language family (for quick iteration in executor testing). (c) PREVIEW: 500-1000 arcs from diverse languages/registers for documentation. All three as data_out.json with one JSON object per line (JSONL) or as a single JSON array, depending on size; use aii-file-size-limit skill if >300MB to advise on splits. Include a schema document and a summary statistics table (arcs per language, arcs per register, arc-length distribution quartiles by register).

  9. FALLBACK & ROBUSTNESS: If HuggingFace API fails, fetch UD treebanks directly from UniversalDependencies GitHub (UD_<language>-<treebank> repos). If Glottolog unavailable, use cached/static Glottolog export (available on ZENODO as versioned snapshot). If WALS/Grambank incomplete, ensure UD_proxy is computed for all languages. If a treebank has parsing errors or malformed CoNLL-U, log the issue and skip that treebank but continue; do NOT fail the entire run.

  10. DOCUMENTATION: Generate a README.md with data dictionary, sample rows, source citations (commul/universal_dependencies, Glottolog, WALS, Grambank), notes on censoring-bound computation (with a concrete example sentence), register labeling methodology, known limitations (e.g., % of languages with paired spoken/written data, % coverage by WALS/Grambank vs UD_proxy), and reproduction instructions (language/versions of pyglottolog, UD dataset commit, etc.).
target_num_datasets: 1
</artifact_plan>



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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Update data.py to only include the chosen 1 dataset and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
TODO 2. Verify full_data_out.json, preview_data_out.json, and mini_data_out.json exist in your workspace (see <workspace>) and contain correct data.
TODO 3. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to full_data_out.json.
TODO 4. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DatasetExpectedFiles": {
      "description": "All expected output files from dataset artifact.",
      "properties": {
        "script": {
          "description": "Path to data.py script. Example: 'data.py'",
          "title": "Script",
          "type": "string"
        },
        "datasets": {
          "description": "Dataset file groups \u2014 one per dataset, each with full/mini/preview variants",
          "items": {
            "$ref": "#/$defs/DatasetFileSet"
          },
          "title": "Datasets",
          "type": "array"
        }
      },
      "required": [
        "script",
        "datasets"
      ],
      "title": "DatasetExpectedFiles",
      "type": "object"
    },
    "DatasetFileSet": {
      "description": "One dataset's three required output variants.",
      "properties": {
        "full": {
          "description": "Full dataset JSON file(s). Single file or split files. Example: ['full_data_out.json'] or ['full_data_out/full_data_out_1.json', 'full_data_out/full_data_out_2.json']",
          "items": {
            "type": "string"
          },
          "title": "Full",
          "type": "array"
        },
        "mini": {
          "description": "Mini dataset JSON file path (3 examples). Example: 'mini_data_out.json'",
          "title": "Mini",
          "type": "string"
        },
        "preview": {
          "description": "Preview dataset JSON file path (10 examples). Example: 'preview_data_out.json'",
          "title": "Preview",
          "type": "string"
        }
      },
      "required": [
        "full",
        "mini",
        "preview"
      ],
      "title": "DatasetFileSet",
      "type": "object"
    }
  },
  "description": "Dataset artifact \u2014 structured output + file metadata.\n\nFinds, evaluates, and prepares datasets for research experiments.\nProduces data.py and full_data_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/DatasetExpectedFiles",
      "description": "All output files you created. Must include data.py script plus dataset file groups (full/mini/preview variants)."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "DatasetArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [20] SYSTEM-USER prompt · 2026-08-13 12:07:36 UTC

```
<verification_failed>
Your dataset output failed verification (attempt 1/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: ud_arcs_curated

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Use 'ls' to check what files exist, then create the missing ones.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files (data.py, full_data_out.json, preview_data_out.json, mini_data_out.json)

After making changes, verify:
- 'ls -la' shows all required files
- JSON files are valid (use aii-json skill validation)
- full_data_out.json has at least 50 examples
</task>
```
