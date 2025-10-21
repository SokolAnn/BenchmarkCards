# Zéroe

## 📊 Benchmark Details

**Name**: Zéroe

**Overview**: Zéroe is the first large-scale catalogue and benchmark of low-level adversarial attacks in NLP, encompassing nine different attack modes designed to test the robustness of NLP models against realistic attacks.

**Data Type**: adversarial text examples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/yannikbenz/zeroe)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for testing the robustness of NLP models against low-level adversarial attacks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Adversarial attacks published in the Zéroe benchmark.

**Size**: N/A

**Format**: N/A

**Annotation**: Automatically generated through various attack methodologies.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- AUCROC

**Calculation**: Metrics are computed by comparing the performance of models on clean data versus attacked data.

**Interpretation**: Decreases in accuracy and AUCROC indicate vulnerabilities to adversarial attacks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
