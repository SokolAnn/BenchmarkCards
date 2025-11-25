# BPQA (Blood Pressure Question Answering)

## 📊 Benchmark Details

**Name**: BPQA (Blood Pressure Question Answering)

**Overview**: BPQA is a newly developed dataset containing 100 medical question-answer pairs verified by medical students, designed to evaluate how well language models can leverage blood pressure measurements to answer relevant medical questions.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/Kekelilii/BPQA100)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate language models on their ability to interpret and use blood pressure measurements in medical question-answering tasks.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners

**Tasks**:
- Question Answering

**Limitations**: The dataset may not fully capture the diversity of clinical scenarios as it focuses solely on blood pressure measurements.

## 💾 Data

**Source**: Dataset created by the authors, verified by medical students.

**Size**: 100 medical QA pairs

**Format**: N/A

**Annotation**: Verified by medical students

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation

**Metrics**:
- Accuracy

**Calculation**: Evaluated based on the ability to answer yes or no questions related to blood pressure.

**Interpretation**: Higher accuracy indicates better performance in leveraging blood pressure data for medical questions.

**Validation**: Evaluation compared various language models across multiple dataset variants.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes context-specific considerations for minority patient demographics.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
