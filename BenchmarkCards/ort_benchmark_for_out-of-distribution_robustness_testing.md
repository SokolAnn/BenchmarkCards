# ORT (Benchmark for Out-of-Distribution Robustness Testing)

## 📊 Benchmark Details

**Name**: ORT (Benchmark for Out-of-Distribution Robustness Testing)

**Overview**: ORT is designed to evaluate the robustness of unlearning methods against variations in knowledge expression, systematically investigating Form-Dependent Bias across various downstream tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2506.07795)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate unlearning effectiveness and understand the Form-Dependent Bias in unlearning methods.

**Target Audience**:
- ML Researchers
- Model Developers
- Ethical AI Practitioners

**Tasks**:
- Question Answering
- Knowledge Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: 200 real-world prominent individuals as unlearning targets, with multi-format evaluation tasks for each target.

**Size**: 12,294 evaluation entries on Forget Set, 22,758 evaluation entries on Retain Set

**Format**: JSON

**Annotation**: Annotation conducted through natural language prompts and LLM outputs.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Probability Reduction

**Calculation**: Evaluation of knowledge retention and forgetting through probability-based metrics for different task formats.

**Interpretation**: Lower probability indicates successful unlearning of the target knowledge.

**Validation**: Comprehensive tests across different unlearning methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
