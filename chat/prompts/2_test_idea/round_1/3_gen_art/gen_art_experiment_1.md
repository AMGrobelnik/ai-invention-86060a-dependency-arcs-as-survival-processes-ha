# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_oQQwThF8kM-b` — Dependency Arcs as Survival Processes: Hazard-Based Characterization of Syntactic Dependency Lengths Across Universal Dependencies
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-08-13 11:38:15 UTC

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

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

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
Your workspace: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx3
type: experiment
title: Survival Analysis on UD Dependency Lengths
summary: >-
  Reframe dependency arcs as censored time-to-event objects using survival analysis (Kaplan-Meier, Nelson-Aalen, Cox proportional
  hazards with language-family shared frailty) to investigate dependency-length minimization patterns across UD treebanks,
  test whether spoken registers show front-loaded hazard curves relative to written, and identify families whose residual
  hazard deviates from typological predictions. Validate robustness to sentence-length-mixing confound via resampling.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "# SURVIVAL ANALYSIS IMPLEMENTATION: DEPENDENCY-LENGTH HAZARD ESTIMATION\n\n## PHASE 1: DATA LOADING\
  \ & ARC-LENGTH COMPUTATION\n# Input: commul/universal_dependencies from HuggingFace\n# Output: arc_length_table.csv with\
  \ columns [arc_length, censoring_bound, treebank, register, language, family, word_order_class, morphological_richness]\n\
  \nload_ud_dataset():\n  - Use datasets.load_dataset('commul/universal_dependencies')\n  - For each treebank split (train/validation/test):\n\
  \    - Iterate over sentences and their dependency trees\n    - Extract machine-parseable genre/modality tag (e.g., 'spoken'\
  \ vs 'written' from treebank metadata)\n    - If tag missing, infer from treebank name patterns (e.g., Rhapsodie='spoken',\
  \ GSD='written')\n    - Yield: (head_idx, dependent_idx, sentence_length, treebank_name, register, language)\n\ncompute_arc_lengths_and_censoring():\n\
  \  for each arc (head, dependent, sent_len, treebank, register, language):\n    - arc_length = |head_idx - dependent_idx|\
  \  # Distance in tokens\n    - distance_to_left_boundary = dependent_idx\n    - distance_to_right_boundary = sent_len -\
  \ 1 - dependent_idx\n    - censoring_bound = max(distance_to_left_boundary, distance_to_right_boundary)\n      # A word\
  \ at position i cannot form an arc longer than min(i, sent_len-1-i)\n      # Right-censoring: observed arc_length ≤ censoring_bound;\
  \ if arc_length == censoring_bound, it's (potentially) censored\n    - Append (arc_length, censoring_bound, treebank, register,\
  \ language, event=1 if arc_length < censoring_bound else 0)\n\nenrich_with_metadata():\n  - Map treebank → language\n  -\
  \ Fetch language_family from Glottolog API / JSON dump\n  - Fetch word_order_class from WALS (OV/VO) or UD morphological-feature\
  \ density as proxy\n  - Compute morphological_richness = count_unique_morphological_features / token_count (per treebank)\n\
  \  - Join back to arc_length_table\n\n## PHASE 2: NON-PARAMETRIC HAZARD ESTIMATION (Per-Treebank & Per-Register)\n# Output:\
  \ km_curves.json (Kaplan-Meier), na_curves.json (Nelson-Aalen), survival_stats.csv\n\nkaplan_meier_per_register():\n  #\
  \ Using lifelines.KaplanMeierFitter\n  for each (language, register) pair where both spoken & written exist:\n    - Fit\
  \ KM to arcs where register == 'spoken' with arc_length as duration, event indicator\n    - Fit KM to arcs where register\
  \ == 'written'\n    - Plot both curves on same axes; compute confidence bands at 0.025/0.975 quantiles\n    - Store: KM_curves[language][register]\
  \ = {durations, survival_func, conf_int_lower, conf_int_upper}\n    - Log: median arc_length, IQR, % censored\n\nnelson_aalen_per_treebank():\n\
  \  # Using lifelines.NelsonAalenFitter\n  for each treebank:\n    - Fit NA estimator to all arcs; yields cumulative hazard\
  \ H(d)\n    - Compute instantaneous hazard h(d) from Kaplain-Meier via h(d) ≈ -dS(d)/d(d) / S(d)\n    - Store: NA_curves[treebank]\
  \ = {durations, cumulative_hazard, instantaneous_hazard}\n\n## PHASE 3: COX PROPORTIONAL-HAZARDS MODEL WITH SHARED FRAILTY\n\
  # Output: cox_model.pkl, cox_summary.csv (coefficients, CIs, p-values), frailty_terms.json\n# Using PyMC (Bayesian hierarchical\
  \ Cox) + lifelines baseline hazard\n\nprepare_cox_data():\n  - Aggregate arc_length_table: columns = [duration, event, register,\
  \ word_order, morph_richness, language_family]\n  - Exclude treebanks with <50 arcs or no register label (data quality gate)\n\
  \  - Encode categorical: register (0/1), word_order (OV/VO/free → dummy)\n  - Standardize continuous: word_order_scale =\
  \ (word_order - mean) / sd, morph_richness_scale\n  - Create grouping: language_family → integer cluster ID (0..N_families-1)\n\
  \  - Final table: N rows × (duration, event, register, word_order_scale, morph_richness_scale, family_id)\n\nfit_pymc_cox_frailty_model():\n\
  \  # Bayesian hierarchical Cox model via Poisson likelihood trick\n  # λ_i(t) = z_{f(i)} × exp(β_register × register_i +\
  \ β_order × order_i + β_morph × morph_i) × λ_0(t)\n  # where z_f ~ Gamma(α, β) is the frailty for family f\n  \n  model\
  \ = PyMC():\n    # Priors on fixed effects (weakly informative)\n    β_register ~ Normal(0, 1)       # Effect of spoken\
  \ vs written\n    β_order ~ Normal(0, 1)          # Effect of word order (negative = flatter hazard)\n    β_morph ~ Normal(0,\
  \ 1)          # Effect of morphological richness\n    \n    # Frailty: gamma-distributed random effects per language family\n\
  \    # Gamma(α, β) with α ~ HalfNormal(2), β ~ HalfNormal(2)\n    α_frailty ~ HalfNormal(2)\n    β_frailty ~ HalfNormal(2)\n\
  \    z_frailty ~ Gamma(α_frailty, β_frailty, shape=(N_families,))  # One per family\n    \n    # Likelihood via Poisson\
  \ \"trick\": break each observation into time intervals,\n    # model count of events as Poisson with log-link\n    # (requires\
  \ time-discretization; lifelines handles this)\n    # log(μ_ij) = log(y_ij) + log(z_{f(i)}) + β_register × register_i +\
  \ ...\n    # where y_ij = duration of interval j for observation i\n    \n    likelihood ~ Poisson(μ, observed=events_per_interval)\n\
  \    \n    # Sample posterior\n    trace = pm.sample(draws=2000, tune=1000, cores=4, return_inferencedata=True)\n  \n  #\
  \ Extract posterior summaries\n  summary_table = az.summary(trace)\n  cox_coefficients = summary_table[['mean', 'hdi_2.5%',\
  \ 'hdi_97.5%']] for [β_register, β_order, β_morph]\n  frailty_posterior = trace.posterior['z_frailty'].values  # shape (chains,\
  \ draws, N_families)\n  \n  # Ranking families by frailty deviation from cluster baseline\n  frailty_families = az.summary(trace.posterior['z_frailty'])\n\
  \  frailty_families['family_id'] = range(N_families)\n  frailty_families = merge(frailty_families, family_metadata, on='family_id')\n\
  \  frailty_families['typological_cluster'] = assign_cluster(family_typology)  # OV/VO/free\n  frailty_families['cluster_baseline']\
  \ = frailty_families.groupby('typological_cluster')['mean'].transform('mean')\n  frailty_families['residual_frailty'] =\
  \ frailty_families['mean'] - frailty_families['cluster_baseline']\n  frailty_families = sort_by('residual_frailty', descending=True)\
  \  # Families with largest deviations first\n  \n  # Store top deviating families (e.g., top 5 / bottom 5)\n  top_outlier_families\
  \ = frailty_families[['family_name', 'mean', 'hdi_2.5%', 'hdi_97.5%', 'residual_frailty']].head(10)\n  \n  return cox_coefficients,\
  \ frailty_families, top_outlier_families, trace\n\n## PHASE 4: ROBUSTNESS CHECK — SENTENCE-LENGTH RESAMPLING\n# Validate:\
  \ hazard-based estimates are robust to sentence-length composition; pooled-MDD estimates are not.\n# Output: robustness_comparison.json,\
  \ robustness_plot.pdf\n\nsentence_length_resampling_validation():\n  # Problem: Dependency-length distribution is mechanically\
  \ confounded by sentence length.\n  # If language A has many long sentences, its mean arc length will be higher even if\
  \ proportionally it minimizes more.\n  # Solution: Resample arcs to balance sentence-length distributions across register/language\
  \ pairs.\n  \n  for each (language, register) pair:\n    observed_data = arc_lengths where (language==lang AND register==reg)\n\
  \    \n    # Compute empirical CDF of sentence lengths per register\n    cdf_spoken = ECDF(sentence_lengths where register=='spoken')\n\
  \    cdf_written = ECDF(sentence_lengths where register=='written')\n    \n    # Resample approach 1: Uniform sentence-length\
  \ distribution\n    # Randomly drop long-sentence arcs until spoken & written have same sentence-length distribution\n \
  \   unif_sent_lengths_min = min(min(sentence_lengths[spoken]), min(sentence_lengths[written]))\n    unif_sent_lengths_max\
  \ = max(max(sentence_lengths[spoken]), max(sentence_lengths[written]))\n    \n    arcs_resampled_spoken = subsample(arcs[spoken],\
  \ keep only sent_len in [min, max], preserve arc_length distribution)\n    arcs_resampled_written = subsample(arcs[written],\
  \ keep only sent_len in [min, max], preserve arc_length distribution)\n    \n    # Fit Cox model on resampled data\n   \
  \ cox_resampled = fit_pymc_cox_frailty_model(arcs_resampled_spoken + arcs_resampled_written)\n    \n    # Compare: do β_register,\
  \ frailty terms remain stable?\n    coef_diff_register = cox_resampled.β_register.mean - cox_original.β_register.mean\n\
  \    coef_diff_order = cox_resampled.β_order.mean - cox_original.β_order.mean\n    coef_diff_morph = cox_resampled.β_morph.mean\
  \ - cox_original.β_morph.mean\n    \n    frailty_correlation = spearman(cox_original.frailty_families['mean'], \n      \
  \                              cox_resampled.frailty_families['mean'])\n    \n    # Parallel comparison: pooled MDD statistics\
  \ (from prior literature)\n    mean_arc_original_spoken = mean(arc_lengths[spoken])\n    mean_arc_original_written = mean(arc_lengths[written])\n\
  \    mdd_ratio_original = mean_arc_original_spoken / mean_arc_original_written\n    \n    mean_arc_resampled_spoken = mean(arcs_resampled_spoken.arc_length)\n\
  \    mean_arc_resampled_written = mean(arcs_resampled_written.arc_length)\n    mdd_ratio_resampled = mean_arc_resampled_spoken\
  \ / mean_arc_resampled_written\n    \n    # Result: Hazard-based Cox estimates should be stable (correlation > 0.8); MDD\
  \ ratios should shift\n    log(f\"Language {lang}: Cox coef_register stable? {abs(coef_diff_register) < 0.1}; \"\n     \
  \   f\"MDD ratio stable? {abs(mdd_ratio_original - mdd_ratio_resampled) < 0.05}\")\n    \n    robustness_summary[lang] =\
  \ {\n      'cox_coef_register_delta': coef_diff_register,\n      'frailty_correlation': frailty_correlation,\n      'mdd_ratio_shift':\
  \ abs(mdd_ratio_original - mdd_ratio_resampled),\n      'verdict': 'COX_STABLE' if abs(coef_diff_register) < 0.1 else 'COX_UNSTABLE'\n\
  \    }\n\n## PHASE 5: CROSS-CHECK AGAINST PRIOR LITERATURE\n# Validate: hazard-based results align with known DLM patterns\
  \ from pooled-MDD studies.\n# Output: cross_check_results.md, directional_effects_table.csv\n\ncross_check_prior_findings():\n\
  \  # Known findings from Futrell et al. (2015), SCiL 2021, \"Grammar Does the Work\" 2026:\n  # - Spoken often shows shorter\
  \ mean dependency distance (or similar to written)\n  # - Word-order/morphology strongly correlates with DLM magnitude\n\
  \  # - Functional deps minimize more than lexical deps\n  \n  # This study's expectations (if hypothesis is correct):\n\
  \  # - Spoken: front-loaded hazard (high h(d) at small d, steep decay) → negative β_register coefficient\n  # - Free-word-order:\
  \ flatter hazard → negative β_order coefficient (looser commitment to short arcs)\n  # - High morphological richness: flatter\
  \ hazard → negative β_morph coefficient\n  \n  # Cross-check 1: Direction of β_register across languages\n  spoken_advantage_langs\
  \ = [lang for lang in cox_summary if cox_summary[lang]['β_register']['mean'] < 0]\n  log(f\"Languages where spoken shows\
  \ front-loaded hazard (β_register < 0): {len(spoken_advantage_langs)} / {N_langs}\")\n  log(f\"Detailed: {spoken_advantage_langs}\"\
  )\n  \n  # Cross-check 2: Order/morphology effects\n  log(f\"Word-order effect (β_order): mean = {cox_summary['β_order']['mean']:.3f},\
  \ \"\n      f\"95% CI [{cox_summary['β_order']['hdi_2.5%']:.3f}, {cox_summary['β_order']['hdi_97.5%']:.3f}]\")\n  log(f\"\
  Interpretation: {('consistent with free-order→flatter' if cox_summary['β_order']['mean'] < 0 else 'opposite to prediction')}\"\
  )\n  \n  # Cross-check 3: Comparison to specific papers\n  #   - SCiL 2021 found inconsistent spoken-vs-written direction;\
  \ this study should clarify via hazard shape\n  #   - \"Grammar Does the Work\" 2026 found functional deps minimize more;\
  \ check if frailty captures it\n  \n  # Cross-check 4: Hazard-curve shape recovery\n  # Manually inspect KM curves for 3-5\
  \ representative language pairs (e.g., French, English, Slovenian)\n  # Visually confirm: spoken curves drop faster at small\
  \ d, then plateau → matches front-loaded hypothesis\n  \n  cross_check_table = {\n    'hypothesis_direction': 'spoken_front_loaded\
  \ + free_order_flatter + high_morph_flatter',\n    'β_register_direction': 'negative' if cox_summary['β_register']['mean']\
  \ < 0 else 'positive',\n    'β_order_direction': 'negative' if cox_summary['β_order']['mean'] < 0 else 'positive',\n   \
  \ 'β_morph_direction': 'negative' if cox_summary['β_morph']['mean'] < 0 else 'positive',\n    'n_langs_spoken_advantage':\
  \ len(spoken_advantage_langs),\n    'frailty_outliers_recovered': len(top_outlier_families[top_outlier_families['residual_frailty'].abs()\
  \ > threshold])\n  }\n\n## PHASE 6: OUTPUT & REPORTING\n# Output files: method_out.json with all results\n\ngenerate_outputs():\n\
  \  results = {\n    'metadata': {\n      'n_treebanks': len(unique(arc_length_table['treebank'])),\n      'n_languages':\
  \ len(unique(arc_length_table['language'])),\n      'n_families': len(unique(arc_length_table['family'])),\n      'n_arcs_total':\
  \ len(arc_length_table),\n      'n_arcs_censored': sum(arc_length_table['event'] == 0),\n      'pct_censored': 100 * sum(arc_length_table['event']\
  \ == 0) / len(arc_length_table),\n      'n_spoken_written_pairs': len([(l, r) for l, r in unique(arc_length_table[['language',\
  \ 'register']])])\n    },\n    'kaplan_meier': {\n      'per_language_pair': km_curves,  # {language: {register: {durations,\
  \ survival, conf_int}}}\n      'median_arcs': {lang: {reg: median(arc_lengths[lang][reg])} for lang, reg in km_curves.keys()}\n\
  \    },\n    'nelson_aalen': {\n      'per_treebank': na_curves  # {treebank: {durations, cumulative_hazard, instantaneous_hazard}}\n\
  \    },\n    'cox_model': {\n      'fixed_effects': {\n        'β_register': {'mean': ..., 'hdi_2.5%': ..., 'hdi_97.5%':\
  \ ...},\n        'β_order': {...},\n        'β_morph': {...}\n      },\n      'frailty': {\n        'top_outliers': top_outlier_families.to_dict(),\n\
  \        'family_posterior_samples': frailty_posterior.shape  # (chains, draws, N_families)\n      },\n      'fit_diagnostics':\
  \ {\n        'n_divergences': trace.sample_stats['diverging'].sum(),\n        'rhat_summary': {var: mean(rhat_values) for\
  \ var in fixed_effects.keys()}\n      }\n    },\n    'robustness': {\n      'per_language': robustness_summary,\n      'summary':\
  \ {\n        'cox_stable_langs': sum(1 for lang in robustness_summary if robustness_summary[lang]['verdict'] == 'COX_STABLE'),\n\
  \        'mdd_unstable_langs': sum(1 for lang in robustness_summary if robustness_summary[lang]['mdd_ratio_shift'] > 0.05)\n\
  \      }\n    },\n    'cross_check': cross_check_table,\n    'hypothesis_verdict': {\n      'spoken_front_loaded': 'CONFIRMED'\
  \ if n_langs_spoken_advantage > N_langs * 0.6 else 'NOT_CONFIRMED',\n      'word_order_effect': 'CONFIRMED' if abs(cox_summary['β_order']['mean'])\
  \ > 0.1 and ci_excludes_zero else 'UNCERTAIN',\n      'family_deviance_exists': 'CONFIRMED' if len(top_outliers) > 0 else\
  \ 'NOT_CONFIRMED',\n      'robustness_to_sent_length': 'CONFIRMED' if (cox_stable_langs > N_langs * 0.5 and mdd_unstable_langs\
  \ > N_langs * 0.5) else 'UNCERTAIN'\n    }\n  }\n  \n  write_json('method_out.json', results)\n"
fallback_plan: |-
  **Fallback 1: Marginal Cox model (no frailty).** If PyMC Bayesian fitting is too slow or fails to converge, use lifelines.CoxPHFitter (frequentist) with fixed effects only (register, word_order, morphology). Fit one model per language (not pooled) to preserve language structure, then manually rank families by median residual hazard. Loss: no principled random-effect quantification, but still recovers the main spoken-vs-written and typology effects.

  **Fallback 2: Non-parametric comparison only.** If Cox fitting fails entirely, fall back to stratified Kaplan-Meier curves per register/language pair + Mann-Whitney/logrank tests for significance. Report hazard shapes qualitatively (front-loaded vs flat) without parametric coefficients. Loss: no frailty ranking of families, but still validates hypothesis directionally on hazard shapes.

  **Fallback 3: Simplified frailty via clustering. ** If PyMC is slow, implement a lightweight empirical-Bayes frailty via within-family pooling: for each family, estimate family-level baseline hazard as pooled-across-treebanks Nelson-Aalen, then compute residual hazard per family. Not fully Bayesian, but fast and interpretable.

  **Fallback 4: Reduced dataset scope.** If full UD is too large or OOM, subset to: (a) 10 largest treebanks with strongest register labels; (b) only Indo-European languages (largest sample, best metadata); (c) subsample arcs uniformly to 50k total. Refit on subset, report sample-size caveat.

  **Time-savers if execution is tight:** (1) Skip Bayesian inference; use frequentist Cox + permutation tests for uncertainty. (2) Omit detailed frailty posterior inspection; report only point estimates. (3) Skip robustness resampling; validate robustness via bootstrapped Cox estimates instead. (4) Skip manual cross-check literature review; report only coefficient directions.
testing_plan: |-
  **Stage 1: Data loading test (5 min).** Load commul/universal_dependencies on HuggingFace; confirm: (a) ≥90 treebanks load; (b) ≥40 languages; (c) ≥5 language/register pairs with both spoken & written data; (d) each treebank has valid dependency trees and sentence lengths. Fail signal: KeyError on treebank name or dependency structure, <5 language pairs with paired modality.

  **Stage 2: Arc-length computation test (5 min).** Compute arc_length and censoring_bound on toy dataset (1 language, 100 sentences); manually inspect 20 rows to confirm: (a) arc_length is always ≤ censoring_bound (no logical error); (b) censoring_bound is correctly computed as max(distance_to_left, distance_to_right); (c) event indicator (censored vs observed) is sensible (censored iff arc_length == censoring_bound). Fail signal: negative values, arc_length > bound, or obvious spatial errors.

  **Stage 3: Metadata enrichment test (5 min).** Fetch language families from Glottolog; map 10 random treebanks → language → family. Confirm: (a) all languages resolve to valid families; (b) no missing values; (c) word_order and morphological_richness compute without NaN. Fail signal: <90% family coverage or missing covariates.

  **Stage 4: Non-parametric hazard test (10 min).** Fit Kaplan-Meier on one language pair (e.g., French spoken vs written, n_arcs~5k each). Confirm: (a) KM curves fit without error; (b) survival function is monotone decreasing (mathematical requirement); (c) confidence intervals are non-empty; (d) spoken KM curve drops faster at small arc_length (visual sanity check). Fail signal: KM curve non-monotone, CI widths > 1.0, or reversed spoken/written order.

  **Stage 5: Cox model setup test (10 min).** Prepare data for Cox: standardize covariates, create family_id column, set up Poisson-trick time intervals (e.g., 1-token intervals). Fit full Cox model on 50k subsampled arcs, monitor: (a) no NaN in likelihood; (b) MCMC sampling starts (≥100 draws without divergence); (c) posterior summary computes (β, HDE CI). Fail signal: likelihood error, all divergences, or summary NaN.

  **Stage 6: Frailty extraction test (5 min).** Extract frailty posterior for 5 largest language families; compute mean, HDI, residual vs. cluster baseline. Confirm: (a) frailty values > 0 (property of gamma/lognormal); (b) HDI is narrower than posterior SD (credible intervals < posterior range); (c) families rank by residual without NA. Fail signal: negative frailty, inverted HDI, or unsorted output.

  **Stage 7: Robustness validation test (15 min).** Resample arcs for one language pair (French) to balance sentence lengths; refit Cox; compare β_register before/after. Confirm: (a) coefficient change < 0.2 (stability threshold); (b) MDD ratio changes >0.05 (sensitivity validation); (c) frailty family ranking Spearman corr > 0.7. Fail signal: large coefficient shifts, identical MDD ratios (confound not present), or frailty rank reversals.

  **Stage 8: Integration test (60-90 min).** Run full pipeline on all data: load UD, compute arc lengths, fit KM/NA per language pair (50+ pairs), fit Cox on pooled data, extract/rank frailties, validate robustness on 3+ languages. Monitor: (a) total runtime <6h; (b) no OOM errors; (c) ≥10 language pairs with usable curves; (d) ≥50% families with non-trivial frailty posterior. Output final method_out.json and spot-check 3 plots (KM curves, Cox summary forest plot, frailty by family).

  **Confirmation signals (any one is success):** (1) Cox coefficient directions align with hypothesis (β_register < 0 for spoken front-load, β_order < 0 for free-word-order); (2) ≥60% of language pairs show spoken KM curve steeper at d=1-5, flatter at d>10 vs written (visual); (3) ≥5 language families identified as outliers (|residual_frailty| > 2× median). (4) Robustness check shows Cox stable & MDD unstable for ≥3 languages.
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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

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
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-08-13 11:38:15 UTC

```
Direction: Computational Linguistics — Dependency Distance Minimization Across UD Treebanks. Something genuinely novel and groundbreaking that measures dependency-distance distributions across UD treebanks, investigates whether spoken language minimizes more than written, characterizes how typology interacts with the pattern, and identifies families that deviate. MUST use commul/universal_dependencies on HuggingFace.

Ambition: level 3 of 5 — phenomenological science: surface and rigorously characterize a new empirical regularity or anomaly in the data, even before a full theoretical explanation exists.

Reviewer: I am Kaja Dobrovoljc (JSI / University of Ljubljana). Calibrate from my existing papers. Cross-domain methods (information theory, mixed-effects models, sequence models) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for ACL, EMNLP, or the Computational Linguistics journal. Audience: computational linguists and quantitative typologists. Tone: empirically rigorous, careful with linguistic detail, reproducible on public UD.
```

### [3] SKILL-INPUT — aii-python · 2026-08-13 11:38:21 UTC

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

### [4] SKILL-INPUT — aii-use-hardware · 2026-08-13 11:38:21 UTC

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

### [5] SKILL-INPUT — aii-long-running-tasks · 2026-08-13 11:38:21 UTC

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

### [6] SKILL-INPUT — aii-json · 2026-08-13 11:38:21 UTC

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

### [7] SKILL-INPUT — aii-file-size-limit · 2026-08-13 11:38:21 UTC

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

### [8] SKILL-INPUT — aii-parallel-computing · 2026-08-13 11:38:21 UTC

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

### [9] SKILL-INPUT — aii-hf-datasets · 2026-08-13 11:38:39 UTC

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

### [10] SKILL-INPUT — aii-handbook-auto-computational-linguistics · 2026-08-13 11:38:39 UTC

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

### [11] SYSTEM-USER prompt · 2026-08-13 11:52:48 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_oQQwThF8kM-b/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx3
type: experiment
title: Survival Analysis on UD Dependency Lengths
summary: >-
  Reframe dependency arcs as censored time-to-event objects using survival analysis (Kaplan-Meier, Nelson-Aalen, Cox proportional
  hazards with language-family shared frailty) to investigate dependency-length minimization patterns across UD treebanks,
  test whether spoken registers show front-loaded hazard curves relative to written, and identify families whose residual
  hazard deviates from typological predictions. Validate robustness to sentence-length-mixing confound via resampling.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "# SURVIVAL ANALYSIS IMPLEMENTATION: DEPENDENCY-LENGTH HAZARD ESTIMATION\n\n## PHASE 1: DATA LOADING\
  \ & ARC-LENGTH COMPUTATION\n# Input: commul/universal_dependencies from HuggingFace\n# Output: arc_length_table.csv with\
  \ columns [arc_length, censoring_bound, treebank, register, language, family, word_order_class, morphological_richness]\n\
  \nload_ud_dataset():\n  - Use datasets.load_dataset('commul/universal_dependencies')\n  - For each treebank split (train/validation/test):\n\
  \    - Iterate over sentences and their dependency trees\n    - Extract machine-parseable genre/modality tag (e.g., 'spoken'\
  \ vs 'written' from treebank metadata)\n    - If tag missing, infer from treebank name patterns (e.g., Rhapsodie='spoken',\
  \ GSD='written')\n    - Yield: (head_idx, dependent_idx, sentence_length, treebank_name, register, language)\n\ncompute_arc_lengths_and_censoring():\n\
  \  for each arc (head, dependent, sent_len, treebank, register, language):\n    - arc_length = |head_idx - dependent_idx|\
  \  # Distance in tokens\n    - distance_to_left_boundary = dependent_idx\n    - distance_to_right_boundary = sent_len -\
  \ 1 - dependent_idx\n    - censoring_bound = max(distance_to_left_boundary, distance_to_right_boundary)\n      # A word\
  \ at position i cannot form an arc longer than min(i, sent_len-1-i)\n      # Right-censoring: observed arc_length ≤ censoring_bound;\
  \ if arc_length == censoring_bound, it's (potentially) censored\n    - Append (arc_length, censoring_bound, treebank, register,\
  \ language, event=1 if arc_length < censoring_bound else 0)\n\nenrich_with_metadata():\n  - Map treebank → language\n  -\
  \ Fetch language_family from Glottolog API / JSON dump\n  - Fetch word_order_class from WALS (OV/VO) or UD morphological-feature\
  \ density as proxy\n  - Compute morphological_richness = count_unique_morphological_features / token_count (per treebank)\n\
  \  - Join back to arc_length_table\n\n## PHASE 2: NON-PARAMETRIC HAZARD ESTIMATION (Per-Treebank & Per-Register)\n# Output:\
  \ km_curves.json (Kaplan-Meier), na_curves.json (Nelson-Aalen), survival_stats.csv\n\nkaplan_meier_per_register():\n  #\
  \ Using lifelines.KaplanMeierFitter\n  for each (language, register) pair where both spoken & written exist:\n    - Fit\
  \ KM to arcs where register == 'spoken' with arc_length as duration, event indicator\n    - Fit KM to arcs where register\
  \ == 'written'\n    - Plot both curves on same axes; compute confidence bands at 0.025/0.975 quantiles\n    - Store: KM_curves[language][register]\
  \ = {durations, survival_func, conf_int_lower, conf_int_upper}\n    - Log: median arc_length, IQR, % censored\n\nnelson_aalen_per_treebank():\n\
  \  # Using lifelines.NelsonAalenFitter\n  for each treebank:\n    - Fit NA estimator to all arcs; yields cumulative hazard\
  \ H(d)\n    - Compute instantaneous hazard h(d) from Kaplain-Meier via h(d) ≈ -dS(d)/d(d) / S(d)\n    - Store: NA_curves[treebank]\
  \ = {durations, cumulative_hazard, instantaneous_hazard}\n\n## PHASE 3: COX PROPORTIONAL-HAZARDS MODEL WITH SHARED FRAILTY\n\
  # Output: cox_model.pkl, cox_summary.csv (coefficients, CIs, p-values), frailty_terms.json\n# Using PyMC (Bayesian hierarchical\
  \ Cox) + lifelines baseline hazard\n\nprepare_cox_data():\n  - Aggregate arc_length_table: columns = [duration, event, register,\
  \ word_order, morph_richness, language_family]\n  - Exclude treebanks with <50 arcs or no register label (data quality gate)\n\
  \  - Encode categorical: register (0/1), word_order (OV/VO/free → dummy)\n  - Standardize continuous: word_order_scale =\
  \ (word_order - mean) / sd, morph_richness_scale\n  - Create grouping: language_family → integer cluster ID (0..N_families-1)\n\
  \  - Final table: N rows × (duration, event, register, word_order_scale, morph_richness_scale, family_id)\n\nfit_pymc_cox_frailty_model():\n\
  \  # Bayesian hierarchical Cox model via Poisson likelihood trick\n  # λ_i(t) = z_{f(i)} × exp(β_register × register_i +\
  \ β_order × order_i + β_morph × morph_i) × λ_0(t)\n  # where z_f ~ Gamma(α, β) is the frailty for family f\n  \n  model\
  \ = PyMC():\n    # Priors on fixed effects (weakly informative)\n    β_register ~ Normal(0, 1)       # Effect of spoken\
  \ vs written\n    β_order ~ Normal(0, 1)          # Effect of word order (negative = flatter hazard)\n    β_morph ~ Normal(0,\
  \ 1)          # Effect of morphological richness\n    \n    # Frailty: gamma-distributed random effects per language family\n\
  \    # Gamma(α, β) with α ~ HalfNormal(2), β ~ HalfNormal(2)\n    α_frailty ~ HalfNormal(2)\n    β_frailty ~ HalfNormal(2)\n\
  \    z_frailty ~ Gamma(α_frailty, β_frailty, shape=(N_families,))  # One per family\n    \n    # Likelihood via Poisson\
  \ \"trick\": break each observation into time intervals,\n    # model count of events as Poisson with log-link\n    # (requires\
  \ time-discretization; lifelines handles this)\n    # log(μ_ij) = log(y_ij) + log(z_{f(i)}) + β_register × register_i +\
  \ ...\n    # where y_ij = duration of interval j for observation i\n    \n    likelihood ~ Poisson(μ, observed=events_per_interval)\n\
  \    \n    # Sample posterior\n    trace = pm.sample(draws=2000, tune=1000, cores=4, return_inferencedata=True)\n  \n  #\
  \ Extract posterior summaries\n  summary_table = az.summary(trace)\n  cox_coefficients = summary_table[['mean', 'hdi_2.5%',\
  \ 'hdi_97.5%']] for [β_register, β_order, β_morph]\n  frailty_posterior = trace.posterior['z_frailty'].values  # shape (chains,\
  \ draws, N_families)\n  \n  # Ranking families by frailty deviation from cluster baseline\n  frailty_families = az.summary(trace.posterior['z_frailty'])\n\
  \  frailty_families['family_id'] = range(N_families)\n  frailty_families = merge(frailty_families, family_metadata, on='family_id')\n\
  \  frailty_families['typological_cluster'] = assign_cluster(family_typology)  # OV/VO/free\n  frailty_families['cluster_baseline']\
  \ = frailty_families.groupby('typological_cluster')['mean'].transform('mean')\n  frailty_families['residual_frailty'] =\
  \ frailty_families['mean'] - frailty_families['cluster_baseline']\n  frailty_families = sort_by('residual_frailty', descending=True)\
  \  # Families with largest deviations first\n  \n  # Store top deviating families (e.g., top 5 / bottom 5)\n  top_outlier_families\
  \ = frailty_families[['family_name', 'mean', 'hdi_2.5%', 'hdi_97.5%', 'residual_frailty']].head(10)\n  \n  return cox_coefficients,\
  \ frailty_families, top_outlier_families, trace\n\n## PHASE 4: ROBUSTNESS CHECK — SENTENCE-LENGTH RESAMPLING\n# Validate:\
  \ hazard-based estimates are robust to sentence-length composition; pooled-MDD estimates are not.\n# Output: robustness_comparison.json,\
  \ robustness_plot.pdf\n\nsentence_length_resampling_validation():\n  # Problem: Dependency-length distribution is mechanically\
  \ confounded by sentence length.\n  # If language A has many long sentences, its mean arc length will be higher even if\
  \ proportionally it minimizes more.\n  # Solution: Resample arcs to balance sentence-length distributions across register/language\
  \ pairs.\n  \n  for each (language, register) pair:\n    observed_data = arc_lengths where (language==lang AND register==reg)\n\
  \    \n    # Compute empirical CDF of sentence lengths per register\n    cdf_spoken = ECDF(sentence_lengths where register=='spoken')\n\
  \    cdf_written = ECDF(sentence_lengths where register=='written')\n    \n    # Resample approach 1: Uniform sentence-length\
  \ distribution\n    # Randomly drop long-sentence arcs until spoken & written have same sentence-length distribution\n \
  \   unif_sent_lengths_min = min(min(sentence_lengths[spoken]), min(sentence_lengths[written]))\n    unif_sent_lengths_max\
  \ = max(max(sentence_lengths[spoken]), max(sentence_lengths[written]))\n    \n    arcs_resampled_spoken = subsample(arcs[spoken],\
  \ keep only sent_len in [min, max], preserve arc_length distribution)\n    arcs_resampled_written = subsample(arcs[written],\
  \ keep only sent_len in [min, max], preserve arc_length distribution)\n    \n    # Fit Cox model on resampled data\n   \
  \ cox_resampled = fit_pymc_cox_frailty_model(arcs_resampled_spoken + arcs_resampled_written)\n    \n    # Compare: do β_register,\
  \ frailty terms remain stable?\n    coef_diff_register = cox_resampled.β_register.mean - cox_original.β_register.mean\n\
  \    coef_diff_order = cox_resampled.β_order.mean - cox_original.β_order.mean\n    coef_diff_morph = cox_resampled.β_morph.mean\
  \ - cox_original.β_morph.mean\n    \n    frailty_correlation = spearman(cox_original.frailty_families['mean'], \n      \
  \                              cox_resampled.frailty_families['mean'])\n    \n    # Parallel comparison: pooled MDD statistics\
  \ (from prior literature)\n    mean_arc_original_spoken = mean(arc_lengths[spoken])\n    mean_arc_original_written = mean(arc_lengths[written])\n\
  \    mdd_ratio_original = mean_arc_original_spoken / mean_arc_original_written\n    \n    mean_arc_resampled_spoken = mean(arcs_resampled_spoken.arc_length)\n\
  \    mean_arc_resampled_written = mean(arcs_resampled_written.arc_length)\n    mdd_ratio_resampled = mean_arc_resampled_spoken\
  \ / mean_arc_resampled_written\n    \n    # Result: Hazard-based Cox estimates should be stable (correlation > 0.8); MDD\
  \ ratios should shift\n    log(f\"Language {lang}: Cox coef_register stable? {abs(coef_diff_register) < 0.1}; \"\n     \
  \   f\"MDD ratio stable? {abs(mdd_ratio_original - mdd_ratio_resampled) < 0.05}\")\n    \n    robustness_summary[lang] =\
  \ {\n      'cox_coef_register_delta': coef_diff_register,\n      'frailty_correlation': frailty_correlation,\n      'mdd_ratio_shift':\
  \ abs(mdd_ratio_original - mdd_ratio_resampled),\n      'verdict': 'COX_STABLE' if abs(coef_diff_register) < 0.1 else 'COX_UNSTABLE'\n\
  \    }\n\n## PHASE 5: CROSS-CHECK AGAINST PRIOR LITERATURE\n# Validate: hazard-based results align with known DLM patterns\
  \ from pooled-MDD studies.\n# Output: cross_check_results.md, directional_effects_table.csv\n\ncross_check_prior_findings():\n\
  \  # Known findings from Futrell et al. (2015), SCiL 2021, \"Grammar Does the Work\" 2026:\n  # - Spoken often shows shorter\
  \ mean dependency distance (or similar to written)\n  # - Word-order/morphology strongly correlates with DLM magnitude\n\
  \  # - Functional deps minimize more than lexical deps\n  \n  # This study's expectations (if hypothesis is correct):\n\
  \  # - Spoken: front-loaded hazard (high h(d) at small d, steep decay) → negative β_register coefficient\n  # - Free-word-order:\
  \ flatter hazard → negative β_order coefficient (looser commitment to short arcs)\n  # - High morphological richness: flatter\
  \ hazard → negative β_morph coefficient\n  \n  # Cross-check 1: Direction of β_register across languages\n  spoken_advantage_langs\
  \ = [lang for lang in cox_summary if cox_summary[lang]['β_register']['mean'] < 0]\n  log(f\"Languages where spoken shows\
  \ front-loaded hazard (β_register < 0): {len(spoken_advantage_langs)} / {N_langs}\")\n  log(f\"Detailed: {spoken_advantage_langs}\"\
  )\n  \n  # Cross-check 2: Order/morphology effects\n  log(f\"Word-order effect (β_order): mean = {cox_summary['β_order']['mean']:.3f},\
  \ \"\n      f\"95% CI [{cox_summary['β_order']['hdi_2.5%']:.3f}, {cox_summary['β_order']['hdi_97.5%']:.3f}]\")\n  log(f\"\
  Interpretation: {('consistent with free-order→flatter' if cox_summary['β_order']['mean'] < 0 else 'opposite to prediction')}\"\
  )\n  \n  # Cross-check 3: Comparison to specific papers\n  #   - SCiL 2021 found inconsistent spoken-vs-written direction;\
  \ this study should clarify via hazard shape\n  #   - \"Grammar Does the Work\" 2026 found functional deps minimize more;\
  \ check if frailty captures it\n  \n  # Cross-check 4: Hazard-curve shape recovery\n  # Manually inspect KM curves for 3-5\
  \ representative language pairs (e.g., French, English, Slovenian)\n  # Visually confirm: spoken curves drop faster at small\
  \ d, then plateau → matches front-loaded hypothesis\n  \n  cross_check_table = {\n    'hypothesis_direction': 'spoken_front_loaded\
  \ + free_order_flatter + high_morph_flatter',\n    'β_register_direction': 'negative' if cox_summary['β_register']['mean']\
  \ < 0 else 'positive',\n    'β_order_direction': 'negative' if cox_summary['β_order']['mean'] < 0 else 'positive',\n   \
  \ 'β_morph_direction': 'negative' if cox_summary['β_morph']['mean'] < 0 else 'positive',\n    'n_langs_spoken_advantage':\
  \ len(spoken_advantage_langs),\n    'frailty_outliers_recovered': len(top_outlier_families[top_outlier_families['residual_frailty'].abs()\
  \ > threshold])\n  }\n\n## PHASE 6: OUTPUT & REPORTING\n# Output files: method_out.json with all results\n\ngenerate_outputs():\n\
  \  results = {\n    'metadata': {\n      'n_treebanks': len(unique(arc_length_table['treebank'])),\n      'n_languages':\
  \ len(unique(arc_length_table['language'])),\n      'n_families': len(unique(arc_length_table['family'])),\n      'n_arcs_total':\
  \ len(arc_length_table),\n      'n_arcs_censored': sum(arc_length_table['event'] == 0),\n      'pct_censored': 100 * sum(arc_length_table['event']\
  \ == 0) / len(arc_length_table),\n      'n_spoken_written_pairs': len([(l, r) for l, r in unique(arc_length_table[['language',\
  \ 'register']])])\n    },\n    'kaplan_meier': {\n      'per_language_pair': km_curves,  # {language: {register: {durations,\
  \ survival, conf_int}}}\n      'median_arcs': {lang: {reg: median(arc_lengths[lang][reg])} for lang, reg in km_curves.keys()}\n\
  \    },\n    'nelson_aalen': {\n      'per_treebank': na_curves  # {treebank: {durations, cumulative_hazard, instantaneous_hazard}}\n\
  \    },\n    'cox_model': {\n      'fixed_effects': {\n        'β_register': {'mean': ..., 'hdi_2.5%': ..., 'hdi_97.5%':\
  \ ...},\n        'β_order': {...},\n        'β_morph': {...}\n      },\n      'frailty': {\n        'top_outliers': top_outlier_families.to_dict(),\n\
  \        'family_posterior_samples': frailty_posterior.shape  # (chains, draws, N_families)\n      },\n      'fit_diagnostics':\
  \ {\n        'n_divergences': trace.sample_stats['diverging'].sum(),\n        'rhat_summary': {var: mean(rhat_values) for\
  \ var in fixed_effects.keys()}\n      }\n    },\n    'robustness': {\n      'per_language': robustness_summary,\n      'summary':\
  \ {\n        'cox_stable_langs': sum(1 for lang in robustness_summary if robustness_summary[lang]['verdict'] == 'COX_STABLE'),\n\
  \        'mdd_unstable_langs': sum(1 for lang in robustness_summary if robustness_summary[lang]['mdd_ratio_shift'] > 0.05)\n\
  \      }\n    },\n    'cross_check': cross_check_table,\n    'hypothesis_verdict': {\n      'spoken_front_loaded': 'CONFIRMED'\
  \ if n_langs_spoken_advantage > N_langs * 0.6 else 'NOT_CONFIRMED',\n      'word_order_effect': 'CONFIRMED' if abs(cox_summary['β_order']['mean'])\
  \ > 0.1 and ci_excludes_zero else 'UNCERTAIN',\n      'family_deviance_exists': 'CONFIRMED' if len(top_outliers) > 0 else\
  \ 'NOT_CONFIRMED',\n      'robustness_to_sent_length': 'CONFIRMED' if (cox_stable_langs > N_langs * 0.5 and mdd_unstable_langs\
  \ > N_langs * 0.5) else 'UNCERTAIN'\n    }\n  }\n  \n  write_json('method_out.json', results)\n"
fallback_plan: |-
  **Fallback 1: Marginal Cox model (no frailty).** If PyMC Bayesian fitting is too slow or fails to converge, use lifelines.CoxPHFitter (frequentist) with fixed effects only (register, word_order, morphology). Fit one model per language (not pooled) to preserve language structure, then manually rank families by median residual hazard. Loss: no principled random-effect quantification, but still recovers the main spoken-vs-written and typology effects.

  **Fallback 2: Non-parametric comparison only.** If Cox fitting fails entirely, fall back to stratified Kaplan-Meier curves per register/language pair + Mann-Whitney/logrank tests for significance. Report hazard shapes qualitatively (front-loaded vs flat) without parametric coefficients. Loss: no frailty ranking of families, but still validates hypothesis directionally on hazard shapes.

  **Fallback 3: Simplified frailty via clustering. ** If PyMC is slow, implement a lightweight empirical-Bayes frailty via within-family pooling: for each family, estimate family-level baseline hazard as pooled-across-treebanks Nelson-Aalen, then compute residual hazard per family. Not fully Bayesian, but fast and interpretable.

  **Fallback 4: Reduced dataset scope.** If full UD is too large or OOM, subset to: (a) 10 largest treebanks with strongest register labels; (b) only Indo-European languages (largest sample, best metadata); (c) subsample arcs uniformly to 50k total. Refit on subset, report sample-size caveat.

  **Time-savers if execution is tight:** (1) Skip Bayesian inference; use frequentist Cox + permutation tests for uncertainty. (2) Omit detailed frailty posterior inspection; report only point estimates. (3) Skip robustness resampling; validate robustness via bootstrapped Cox estimates instead. (4) Skip manual cross-check literature review; report only coefficient directions.
testing_plan: |-
  **Stage 1: Data loading test (5 min).** Load commul/universal_dependencies on HuggingFace; confirm: (a) ≥90 treebanks load; (b) ≥40 languages; (c) ≥5 language/register pairs with both spoken & written data; (d) each treebank has valid dependency trees and sentence lengths. Fail signal: KeyError on treebank name or dependency structure, <5 language pairs with paired modality.

  **Stage 2: Arc-length computation test (5 min).** Compute arc_length and censoring_bound on toy dataset (1 language, 100 sentences); manually inspect 20 rows to confirm: (a) arc_length is always ≤ censoring_bound (no logical error); (b) censoring_bound is correctly computed as max(distance_to_left, distance_to_right); (c) event indicator (censored vs observed) is sensible (censored iff arc_length == censoring_bound). Fail signal: negative values, arc_length > bound, or obvious spatial errors.

  **Stage 3: Metadata enrichment test (5 min).** Fetch language families from Glottolog; map 10 random treebanks → language → family. Confirm: (a) all languages resolve to valid families; (b) no missing values; (c) word_order and morphological_richness compute without NaN. Fail signal: <90% family coverage or missing covariates.

  **Stage 4: Non-parametric hazard test (10 min).** Fit Kaplan-Meier on one language pair (e.g., French spoken vs written, n_arcs~5k each). Confirm: (a) KM curves fit without error; (b) survival function is monotone decreasing (mathematical requirement); (c) confidence intervals are non-empty; (d) spoken KM curve drops faster at small arc_length (visual sanity check). Fail signal: KM curve non-monotone, CI widths > 1.0, or reversed spoken/written order.

  **Stage 5: Cox model setup test (10 min).** Prepare data for Cox: standardize covariates, create family_id column, set up Poisson-trick time intervals (e.g., 1-token intervals). Fit full Cox model on 50k subsampled arcs, monitor: (a) no NaN in likelihood; (b) MCMC sampling starts (≥100 draws without divergence); (c) posterior summary computes (β, HDE CI). Fail signal: likelihood error, all divergences, or summary NaN.

  **Stage 6: Frailty extraction test (5 min).** Extract frailty posterior for 5 largest language families; compute mean, HDI, residual vs. cluster baseline. Confirm: (a) frailty values > 0 (property of gamma/lognormal); (b) HDI is narrower than posterior SD (credible intervals < posterior range); (c) families rank by residual without NA. Fail signal: negative frailty, inverted HDI, or unsorted output.

  **Stage 7: Robustness validation test (15 min).** Resample arcs for one language pair (French) to balance sentence lengths; refit Cox; compare β_register before/after. Confirm: (a) coefficient change < 0.2 (stability threshold); (b) MDD ratio changes >0.05 (sensitivity validation); (c) frailty family ranking Spearman corr > 0.7. Fail signal: large coefficient shifts, identical MDD ratios (confound not present), or frailty rank reversals.

  **Stage 8: Integration test (60-90 min).** Run full pipeline on all data: load UD, compute arc lengths, fit KM/NA per language pair (50+ pairs), fit Cox on pooled data, extract/rank frailties, validate robustness on 3+ languages. Monitor: (a) total runtime <6h; (b) no OOM errors; (c) ≥10 language pairs with usable curves; (d) ≥50% families with non-trivial frailty posterior. Output final method_out.json and spot-check 3 plots (KM curves, Cox summary forest plot, frailty by family).

  **Confirmation signals (any one is success):** (1) Cox coefficient directions align with hypothesis (β_register < 0 for spoken front-load, β_order < 0 for free-word-order); (2) ≥60% of language pairs show spoken KM curve steeper at d=1-5, flatter at d>10 vs written (visual); (3) ≥5 language families identified as outliers (|residual_frailty| > 2× median). (4) Robustness check shows Cox stable & MDD unstable for ≥3 languages.
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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

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
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
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
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
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
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `./.terminal_claude_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [12] SYSTEM-USER prompt · 2026-08-13 11:53:30 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [13] SYSTEM-USER prompt · 2026-08-13 11:53:56 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The output file `.terminal_claude_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [14] SYSTEM-USER prompt · 2026-08-13 11:55:00 UTC

```
<validation-feedback>
Attempt 3 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: "We treat how far apart grammatically linked words sit in a sentence as a 'lifetime' that can be cut short by sentence edges, then use medical-style survival statistics across 350 language corpora to see if spoken language keeps words closer together than writing." is too long (at most 250 characters, got 263)
Every required field must be present and every field type must match the schema.

Produce `.terminal_claude_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
