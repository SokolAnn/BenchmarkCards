# OphthBench

## 📊 Benchmark Details

**Name**: OphthBench

**Overview**: OphthBench is a specialized benchmark designed to assess LLM performance within the context of Chinese ophthalmic practices, systematically dividing a typical ophthalmic clinical workflow into five key scenarios: Education, Triage, Diagnosis, Treatment, and Prognosis, comprising 9 tasks and 591 questions.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- CMExam
- CMB
- MedMCQA
- MedBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized and systematic evaluation framework to assess the capabilities and practical utility of large language models in ophthalmology.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Ophthalmologists

**Tasks**:
- Education
- Triage
- Diagnosis
- Treatment
- Prognosis

**Limitations**: Does not include all LLMs, especially ophthalmology-specific models.

## 💾 Data

**Source**: Developed using representative exercises from the Chinese Medical Licensing Exam, authoritative Chinese ophthalmology textbooks, and real-world clinical cases.

**Size**: 591 questions

**Format**: N/A

**Annotation**: Questions reviewed and refined by ophthalmologists to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Task performance is calculated using a scoring method that normalizes scores across tasks.

**Interpretation**: Higher scores indicate better performance in assessing LLM capabilities.

**Baseline Results**: Results from 39 widely used LLMs are analyzed.

**Validation**: Tasks were designed to minimize bias from prompt sensitivity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential for misdiagnosis or treatment errors, particularly due to misinformation or hallucinations from the models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
