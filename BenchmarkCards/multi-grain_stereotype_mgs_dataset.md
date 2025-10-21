# Multi-Grain Stereotype (MGS) Dataset

## 📊 Benchmark Details

**Name**: Multi-Grain Stereotype (MGS) Dataset

**Overview**: The Multi-Grain Stereotype (MGS) dataset consists of 51,867 instances across gender, race, profession, religion, and other stereotypes, designed to benchmark stereotype detection in Large Language Models (LLMs).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- CrowS-Pairs

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for evaluating and understanding stereotypes in LLMs, enabling effective bias detection and monitoring.

**Target Audience**:
- ML Researchers
- Bias Auditors
- Industry Practitioners

**Tasks**:
- Stereotype Detection

**Limitations**: N/A

## 💾 Data

**Source**: Curated from multiple existing datasets including StereoSet and CrowS-Pairs.

**Size**: 51,867 instances

**Format**: N/A

**Annotation**: Crowdsourced labeling into categories such as stereotype, neutral, and unrelated.

## 🔬 Methodology

**Methods**:
- Fine-tuning of ALBERT-V2 models
- Use of explainable AI (XAI) techniques including SHAP, LIME, and BERTViz

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on model evaluation on training and testing datasets.

**Interpretation**: Higher F1 Scores indicate better classifier performance in detecting stereotypes.

**Baseline Results**: BERT, ALBERT-V2, and other PLM models fine-tuned on the MGS dataset show improved performance over traditional methods.

**Validation**: Models were validated using explainability techniques to ensure alignment with human interpretations of stereotypes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias

**Demographic Analysis**: N/A

**Potential Harm**: The dataset aims to detect and address harmful stereotypes in AI, promoting fairness.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
