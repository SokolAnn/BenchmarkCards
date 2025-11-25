# TempAnswerQA

## 📊 Benchmark Details

**Name**: TempAnswerQA

**Overview**: TempAnswerQA is a benchmark distilled from Test of Time and TempTabQA, consisting of questions requiring numerical, temporal answers to evaluate models beyond exact match.

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

**Goal**: To provide a benchmark for evaluating temporal reasoning in LLMs using specialized regression-based metrics.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Questions sampled from existing temporal QA benchmarks (Test of Time and TempTabQA).

**Size**: 3,434 QA pairs

**Format**: JSON

**Annotation**: Manually annotated expected answer formats and temporal units.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Regression-based evaluation

**Metrics**:
- symmetric mean absolute percentage error (sMAPE)
- mean absolute scaled error (MASE)

**Calculation**: Mean absolute errors calculated and scaled by mean absolute deviation of the dataset.

**Interpretation**: Lower values of sMAPE and MASE indicate better model performance.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
