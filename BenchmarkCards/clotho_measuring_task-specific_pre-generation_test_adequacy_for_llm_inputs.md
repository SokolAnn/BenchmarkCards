# CLOTHO (Measuring Task-Specific Pre-Generation Test Adequacy for LLM Inputs)

## 📊 Benchmark Details

**Name**: CLOTHO (Measuring Task-Specific Pre-Generation Test Adequacy for LLM Inputs)

**Overview**: CLOTHO is a task-specific, pre-generation adequacy measure that estimates input difficulty directly from hidden LLM states and ranks inputs by their likelihood of failure to improve task-specific LLM testing.

**Data Type**: input-output pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://anonymous.4open.science/r/clotho-artifact-DE31)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CLOTHO is to improve task-specific LLM testing by prioritizing which inputs to run and label first, ideally exposing failures earlier and with less effort.

**Target Audience**:
- ML Researchers
- Software Test Engineers

**Tasks**:
- Error Detection
- Input Classification

**Limitations**: N/A

## 💾 Data

**Source**: Aggregated datasets across multiple tasks with specific prompts and input requirements.

**Size**: N/A

**Format**: N/A

**Annotation**: Labelling is performed by human annotators based on model outcomes.

## 🔬 Methodology

**Methods**:
- Error Rate Prediction
- Sample Prioritization

**Metrics**:
- ROC-AUC
- Spearman Rank Correlation

**Calculation**: Metrics are calculated based on the likelihood of passing inputs in relation to the reference distribution derived from hidden states.

**Interpretation**: A higher ROC-AUC score indicates better performance in failure prediction and test input prioritization.

**Baseline Results**: Tests were compared against existing pre-generation and post-generation metrics.

**Validation**: Validation of CLOTHO was performed across eight benchmark tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
