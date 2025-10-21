# RephQA

## 📊 Benchmark Details

**Name**: RephQA

**Overview**: RephQA is a benchmark for evaluating the readability of LLMs in public health question answering (QA). It contains 533 expert-reviewed QA pairs from 27 sources across 13 topics, and includes a proxy multiple-choice task to assess informativeness, along with two readability metrics: Flesch-Kincaid grade level and professional score.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- MedMCQA
- MMLU
- PubMedQA
- LiveQA
- MedicationQA
- JAMA & Medbullets

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To conduct a comprehensive investigation into the readability of LLMs in public health question-answering tasks.

**Target Audience**:
- Lay Users
- Patients
- Healthcare Professionals

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 533 expert-reviewed QA pairs curated from 27 authoritative online public health resources.

**Size**: 533 examples

**Format**: N/A

**Annotation**: Expert-reviewed by professionals in nursing, public health, and clinical communication.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Flesch-Kincaid grade level
- Professional score

**Calculation**: Calculating readability scores and accuracy through proxy multiple-choice QA.

**Interpretation**: Readability scores indicate the clarity of language used; lower grade levels and professional scores suggest more accessible language.

**Baseline Results**: Most LLMs fail to meet the desired readability standards.

**Validation**: Evaluation of 25 LLMs on RephQA.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
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
