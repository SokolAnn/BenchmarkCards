# TempAnswerQA

## 📊 Benchmark Details

**Name**: TempAnswerQA

**Overview**: TempAnswerQA is a benchmark distilled from Test of Time and TempTabQA, focusing on numerical temporal question answering to evaluate models beyond exact match (EM) metrics.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Test of Time
- TempTabQA

**Resources**:
- [GitHub Repository](https://github.com/aauss/temporal-answer-qa)

## 🎯 Purpose and Intended Users

**Goal**: To provide a specialized evaluation procedure for temporal QA tasks that captures continuous error metrics.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from existing temporal QA benchmarks including Test of Time and TempTabQA.

**Size**: 3,434 QA pairs

**Format**: JSON

**Annotation**: Questions classified as requiring temporal answers and annotated for expected answer formats.

## 🔬 Methodology

**Methods**:
- Regression-based evaluation metrics
- Empirical model evaluation

**Metrics**:
- symmetric mean absolute percentage error (sMAPE)
- mean absolute scaled error (MASE)

**Calculation**: Metrics calculated based on the absolute differences between expected and predicted temporal answers.

**Interpretation**: Smaller values in sMAPE and MASE indicate better model performance, emphasizing the importance of error magnitude.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
