# Entropy-Memorization Law

## 📊 Benchmark Details

**Name**: Entropy-Memorization Law

**Overview**: This paper presents the Entropy-Memorization Law, which characterizes the relationship between data entropy and memorization difficulty in LLMs, offering a method to distinguish between training and testing datasets, enabling dataset inference.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LiveBench
- MIMIR

**Resources**:
- [Resource](https://arxiv.org/abs/2507.06056)

## 🎯 Purpose and Intended Users

**Goal**: To explore how to characterize memorization difficulty of training data in LLMs and to develop a method for distinguishing training from testing data.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Data Scientists

**Tasks**:
- Dataset Inference

**Limitations**: N/A

## 💾 Data

**Source**: OLMo family of open models and their associated datasets.

**Size**: 240,000 examples and 300,000 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Linear regression analysis
- Entropy estimation
- Dataset Inference (DI)

**Metrics**:
- Pearson correlation
- Levenshtein Distance (edit distance)

**Calculation**: Levenshtein distance measures the differences between responses and answers at the token level.

**Interpretation**: Higher memorization scores indicate lower similarity between generated responses and reference answers.

**Baseline Results**: Pearson r values reached up to 0.972 in testing.

**Validation**: Algorithm validated through regression on experimental data from the OLMo models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential privacy leakage and risks of proprietary data exposure.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All datasets used are licensed under Open Data Commons Attribution License (ODC-By).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
