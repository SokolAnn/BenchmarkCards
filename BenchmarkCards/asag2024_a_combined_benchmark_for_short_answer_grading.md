# ASAG2024 (A Combined Benchmark for Short Answer Grading)

## 📊 Benchmark Details

**Name**: ASAG2024 (A Combined Benchmark for Short Answer Grading)

**Overview**: The ASAG2024 benchmark facilitates the comparison of automated grading systems and combines seven commonly used short-answer grading datasets in a common structure and grading scale.

**Data Type**: question-answer-grade triplets

**Domains**:
- Education

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/Mey erger/ASAG2024)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for the assessment of automated short-answer grading systems.

**Target Audience**:
- ML Researchers
- Education Practitioners
- Model Developers

**Tasks**:
- Short Answer Grading

**Limitations**: N/A

## 💾 Data

**Source**: Combined from seven commonly used short-answer grading datasets.

**Size**: 19,000 question-answer-grade triplets

**Format**: N/A

**Annotation**: Each dataset must contain reference answers, provided answers by humans, and grades.

## 🔬 Methodology

**Methods**:
- Automated grading methods
- Mean baseline prediction

**Metrics**:
- Root Mean Square Error (RMSE)
- Weighted RMSE (wRMSE)

**Calculation**: wRMSE is calculated by weighting the grades according to how often similar grades appear in the data source.

**Interpretation**: Lower RMSE values indicate better accuracy in grading predictions.

**Baseline Results**: Mean error of GPT-3.5-turbo is 0.30 and GPT-4o is 0.27.

**Validation**: Initial evaluations of existing automated grading solutions are presented.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
