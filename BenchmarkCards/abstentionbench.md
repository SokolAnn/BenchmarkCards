# AbstentionBench

## 📊 Benchmark Details

**Name**: AbstentionBench

**Overview**: AbstentionBench is a large-scale benchmark for holistically evaluating abstention capabilities of LLMs across diverse scenarios, incorporating 20 datasets covering questions with unknown answers, underspecified input, and false premises.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Mathematics
- Science
- Philosophy
- Medicine

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- GSM8K
- GPQA
- SQuAD
- BIG-Bench

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/AbstentionBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of large language models (LLMs) to abstain from answering questions when appropriate.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Abstention Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Various public datasets, including modifications of existing benchmarks (GSM8K, GPQA, MMLU). Also includes newly created underspecified variants.

**Size**: 35,000+ questions

**Format**: JSON

**Annotation**: Manual annotation to identify appropriate abstention responses and labeling of datasets.

## 🔬 Methodology

**Methods**:
- Automatic metrics
- Human evaluation via LLM judgment

**Metrics**:
- Recall
- Precision
- F1 Score

**Calculation**: Recall is computed as the proportion of correct abstention responses among all instances where abstention is appropriate.

**Interpretation**: Higher recall indicates better performance in correctly abstaining from answering when necessary.

**Baseline Results**: Not explicitly stated.

**Validation**: Extensive validation with human annotators for model responses and LLM judge accuracies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
