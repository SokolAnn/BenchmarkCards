# Dataset, Evaluation, and Benchmark for Deception Reasoning

## 📊 Benchmark Details

**Name**: Dataset, Evaluation, and Benchmark for Deception Reasoning

**Overview**: We extend deception detection to deception reasoning, further providing objective evidence to support subjective judgment. Specifically, we provide potential lies and basic facts and then analyze why this sentence may be a lie by combining factual inconsistencies and intent behind them. To facilitate subsequent research, we construct a dataset and define evaluation metrics. This task can serve as a benchmark for evaluating the complex reasoning capability of large language models (LLMs).

**Data Type**: text (multi-turn interrogation dialogues with annotated potential lies and reasoning explanations)

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- Chinese

**Similar Benchmarks**:
- CAIL2018
- IEMOCAP

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Extend deception detection to deception reasoning by providing potential lies and basic facts and analyzing why a sentence may be a lie (considering factual inconsistencies and intent); provide a dataset and evaluation metrics to serve as a benchmark for evaluating complex reasoning capability of LLMs.

**Target Audience**:
- ML Researchers
- Model Developers
- Legal practitioners

**Tasks**:
- Deception Reasoning
- Open-ended Question Answering
- Reasoning (commonsense/logical)

**Limitations**: The dataset relies on GPT-4 for synthesis so only a subset of legal instruments from CAIL2018 was used; evaluation covers many but not all LLMs; the work focuses on the reasonableness of reasoning rather than the authenticity of deceptive behaviors and primarily uses synthetic dialogues; future work will consider real interrogation dialogues and multimodal data.

## 💾 Data

**Source**: Legal instruments sampled from CAIL2018; dialogues synthesized using GPT-4 and GPT-3.5 based on selected legal instruments; potential lies manually selected and analyzed.

**Size**: 191 dialogues

**Format**: N/A

**Annotation**: Manual selection of potential lies and manual reasoning annotations by authors/annotators; post-filtering to remove unnatural dialogues; automatic generation steps (GPT-4/GPT-3.5) used in synthesis.

## 🔬 Methodology

**Methods**:
- Automatic evaluation (GPT-4 as evaluator)
- Manual evaluation by human annotators (8 annotators)
- Automatic generation of dialogues using GPT-4 and GPT-3.5
- Two-stage target content and action extraction (GPT-4/GPT-3.5)

**Metrics**:
- Accuracy
- Completeness
- Logic
- Depth

**Calculation**: Each metric is scored on a 0-10 scale with detailed scoring rubrics provided in Tables 6–9 of the paper. Automatic evaluation uses GPT-4 as the evaluator with the provided prompts; manual evaluation is performed by human annotators. Scores are reported per metric and can be summed.

**Interpretation**: Higher scores indicate better alignment with facts (Accuracy), more comprehensive coverage (Completeness), stronger logical coherence (Logic), and deeper analysis (Depth). Detailed meanings for score ranges are provided in Tables 6–9.

**Baseline Results**: Table 3 reports automatic and manual evaluation results for multiple LLMs (ChatGLM2-6B, WizardLM-13B, Baichuan2-13B, ERINE3.5, Qwen-14B, Claude3-Haiku, GPT-3.5, ERINE4.0, GLM-4-9B, Gemini-1.5-Pro, Qwen2-7B). Example manual results: GLM-4-9B manual Acc.7.56 Com.7.54 Log.7.59 Dep.7.55 Sum 30.24; Qwen2-7B manual Acc.7.41 Com.7.49 Log.7.48 Dep.7.41 Sum 29.79. (Full per-model scores are listed in Table 3.)

**Validation**: Validation includes manual evaluation by 8 annotators and comparison with the automatic GPT-4 evaluator via Pearson correlation coefficients (PCCs). Reported PCC scores between automatic and manual evaluations are: 0.81, 0.87, 0.80, 0.89, 0.86 (for Accuracy, Completeness, Logic, Depth, Sum respectively). Dialogue naturalness was evaluated by comparing 10 real dialogues from IEMOCAP and 10 synthetic dialogues: automatic average scores: real 4.00, synthetic 3.88; manual average synthetic score 3.70. Ablation study shows two-stage + GPT-4 achieves target accuracy 98 and action complexity 0 on a sampled evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Societal Impact

**Atlas Risks**:
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Legal instruments used for dataset construction may provide guidance to criminals.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
