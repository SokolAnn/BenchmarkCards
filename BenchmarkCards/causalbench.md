# CausalBench

## 📊 Benchmark Details

**Name**: CausalBench

**Overview**: CausalBench is developed to evaluate causal learning capabilities of large language models (LLMs) using various tasks and structures derived from the causal research community.

**Data Type**: causal relationships

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://www.bnlearn.com/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing LLMs’ capabilities in causal learning.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Causal Identification
- Causal Skeleton Identification
- Correlation Identification

**Limitations**: N/A

## 💾 Data

**Source**: Causal learning data sourced from the Bnlearn community.

**Size**: 15 datasets

**Format**: Tabular

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy
- Structural Hamming Distance (SHD)
- Structural Intervention Distance (SID)

**Calculation**: Performance calculated using metrics comparing LLM outputs to ground truth causal graphs.

**Interpretation**: Higher F1 scores and accuracies indicate better causal detection abilities.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
