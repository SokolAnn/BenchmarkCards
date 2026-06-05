# BGPT REFUTE

## Benchmark Details

**Name**: BGPT REFUTE

**Overview**: A text-only benchmark for evaluating whether language models can critique recent scientific paper summaries with evidence-grounded judgment and calibrated uncertainty rather than persuasive overconfidence.

**Data Type**: Text generation, scientific critique, calibration vignettes

**Domains**:
- Scientific reasoning
- AI for science
- Peer review assistance
- Epistemic calibration
- Hallucination and overclaim detection

**Languages**:
- English

**Similar Benchmarks**:
- ClaimCheck
- PRISM
- TruthfulQA
- HaluEval
- GPQA

**Resources**:
- [Dataset](https://huggingface.co/datasets/BGPT-OFFICIAL/refute)
- [Technical report](https://huggingface.co/datasets/BGPT-OFFICIAL/refute/blob/main/TECHNICAL_REPORT.md)
- [Leaderboard](https://huggingface.co/spaces/BGPT-OFFICIAL/refute-leaderboard)

## Purpose and Intended Users

**Goal**: To evaluate scientific judgment in language models by separating critique skill from epistemic truthfulness, calibration, and flaw discrimination.

**Target Audience**:
- LLM evaluation researchers
- AI-for-science researchers
- Scientific tool builders
- Model developers
- Benchmark maintainers

**Tasks**:
- Falsification
- Limitation detection
- Missing-evidence refusal
- Overclaim correction
- Confidence calibration
- Forced-choice flaw discrimination
- Planted-flaw detection

**Limitations**: Rubric-scored critique tasks use LLM judges; the benchmark is text-only, science-heavy, and small relative to broad multitask suites; soundness vignettes come from a single authoring pipeline; length control mitigates but does not eliminate residual length correlation.

**Out of Scope Uses**:
- General-purpose model capability ranking without axis-level interpretation
- Multimodal scientific claim verification
- Clinical or policy decision-making without human expert review
- Treating composite Truth Score as a substitute for reviewing calibration, skill, and discrimination separately

## Data

**Source**: Structured summaries of recent 2025-2026 science papers, plus objective sound/flawed vignettes for calibration and flaw-detection axes.

**Size**: 120 full benchmark items, 60-item challenge subset, and 74 soundness/calibration vignettes.

**Format**: Hugging Face dataset with three configurations: `refute_120`, `refute_hard_60`, and `refute_soundness`.

**Annotation**: Items include paper cards, reference answer sketches, task-specific rubrics, scoring notes, and objective sound/flawed labels for the soundness split.

## Methodology

**Methods**:
- Length-controlled critique generation
- Rubric-based LLM judge panel for critique skill
- Strictly proper calibration scoring
- Forced-choice sound vs. flawed comparisons
- Cluster-bootstrap confidence intervals and statistical tiers

**Metrics**:
- Critique skill score
- Brier score
- Brier Skill Score
- AUROC
- Expected calibration error
- Forced-choice accuracy
- Composite Truth Score for complete-axis runs

**Calculation**: Model answers are scored on independent evidence channels. Critique answers are judged with strict rubrics; calibration uses Brier loss on probability estimates; forced-choice tasks use accuracy and confidence intervals; the optional Truth Score combines complete axes.

**Interpretation**: Users should interpret REFUTE by axis. High critique skill does not imply calibrated truthfulness, and within-tier model differences should not be overinterpreted.

**Baseline Results**: A June 2026 panel evaluated 19 frontier models. Grok-family models formed the top critique-skill tier, while GLM-5.1 narrowly led composite Truth Score through stronger calibration.

**Validation**: The release reports length-control analysis, judge negative controls, judge-free forced-choice and soundness axes, confidence intervals, and benchmark limitations.

## Targeted Risks

**Risk Categories**:
- Hallucination
- Overconfidence
- Unsupported scientific claims
- Poor model accuracy
- Benchmark overinterpretation

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack, model behavior instability under evidence gaps
- **Transparency**: Lack of explainability or unreliable explanations
- **Governance**: Inadequate system evaluation

**Demographic Analysis**: Not applicable; the benchmark focuses on scientific reasoning and evidence assessment rather than demographic groups.

**Potential Harm**: Misusing fluent model critiques as authoritative scientific review could lead to unsupported conclusions, false confidence, or poor research decisions.

## Ethical and Legal Considerations

**Privacy And Anonymity**: The public release is based on structured scientific paper summaries and benchmark prompts, not private personal data.

**Data Licensing**: Apache-2.0.

**Consent Procedures**: Not applicable for the released benchmark artifact.

**Compliance With Regulations**: Users remain responsible for applying the benchmark in accordance with research, publication, and domain-specific governance requirements.
