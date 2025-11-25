# CrossEval

## 📊 Benchmark Details

**Name**: CrossEval

**Overview**: CrossEval is a benchmark comprising 1,400 human-annotated prompts, with each prompt designed to evaluate both individual and cross capabilities of large language models (LLMs). It systematically explores the intersection of multiple abilities that are often required for real-world tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- MMLU (Massive Multitask Language Understanding)

**Resources**:
- [Resource](https://www.llm-cross-capabilities.org)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate large language models on both individual and cross-capabilities, revealing insights on their strengths and weaknesses in handling complex, real-world tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Text Classification
- Question Answering
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Human-annotated prompts following a detailed taxonomy covering individual and cross capabilities of LLMs.

**Size**: 1,400 prompts

**Format**: JSONL

**Annotation**: Manual annotation by expert human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance of LLMs in responding to the benchmark prompts, aggregated over various models.

**Interpretation**: Score interpretation defines performance thresholds based on agreement with expert human ratings.

**Baseline Results**: N/A

**Validation**: Ensured through rigorous human annotation and subsequent evaluation rounds to achieve high inter-rater agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
