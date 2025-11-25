# CLOTHO

## 📊 Benchmark Details

**Name**: CLOTHO

**Overview**: CLOTHO is a task-specific, pre-generation adequacy measure that estimates input difficulty directly from hidden LLM states, aiming to improve testing efficiency by prioritizing which inputs to run and label first.

**Data Type**: text

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://anonymous.4open.science/r/clotho-artifact-DE31)

## 🎯 Purpose and Intended Users

**Goal**: Improve task-specific LLM testing by prioritizing inputs for human labeling to expose failures earlier and reduce testing costs.

**Target Audience**:
- ML Researchers
- Software Engineers
- Industry Practitioners

**Tasks**:
- Input Adequacy Measurement
- Failure Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Empirical evaluation across various LLM tasks and datasets created for measuring input adequacy.

**Size**: Between 5,000 to 20,000 inputs per task

**Format**: N/A

**Annotation**: Human-labeled inputs based on model performance assessments.

## 🔬 Methodology

**Methods**:
- Gaussian Mixture Model Sampling
- Active Learning Strategy

**Metrics**:
- ROC-AUC

**Calculation**: Calculated likelihood of passing inputs through GMM based on hidden states.

**Interpretation**: Higher ROC-AUC indicates better prediction of input adequacy and failure rates.

**Baseline Results**: Achieved a ROC-AUC of 0.716 in predicting correctness with limited labeling.

**Validation**: Cross-validation on reference input sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
