# Temporal Wiki and Unified Clark

## 📊 Benchmark Details

**Name**: Temporal Wiki and Unified Clark

**Overview**: This paper introduces two benchmarks, Temporal Wiki and Unified Clark, designed to evaluate the ability of LLMs to handle temporally evolving knowledge in question answering tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Templama
- Clark

**Resources**:
- [GitHub Repository](https://github.com/atahanoezer/TQA)

## 🎯 Purpose and Intended Users

**Goal**: To assess model robustness in settings where factual information accumulates, shifts, or conflicts over time.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Historical Wikipedia snapshots and timestamped news articles.

**Size**: N/A

**Format**: JSON

**Annotation**: Manual curation and verification for document quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on model output compared to human-annotated gold answers.

**Interpretation**: Higher F1 Score and Accuracy indicate better model performance in understanding and integrating temporal information.

**Baseline Results**: N/A

**Validation**: Experiments conducted with multiple LLM architectures to validate the performance across benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
