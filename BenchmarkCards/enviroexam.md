# EnviroExam

## 📊 Benchmark Details

**Name**: EnviroExam

**Overview**: EnviroExam is a comprehensive evaluation method designed to assess the knowledge of large language models in the field of environmental science, covering undergraduate, master’s, and doctoral courses with 936 questions across 42 core courses.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- Ceval
- Lawbench
- Medbench

**Resources**:
- [Resource](https://enviroexam.enviroscientist.cn)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and rank the performance of large language models in environmental science.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The evaluation method is susceptible to test data leakage due to reliance on existing large language models for question generation.

## 💾 Data

**Source**: Questions derived from the curricula of top international universities.

**Size**: 936 questions

**Format**: N/A

**Annotation**: Manually refined and proofread by researchers.

## 🔬 Methodology

**Methods**:
- 0-shot testing
- 5-shot testing
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The total score is calculated as the arithmetic mean of model scores, adjusted by the coefficient of variation.

**Interpretation**: A score above 60 is considered passing; models are evaluated based on their ability to answer questions correctly.

**Baseline Results**: In the 5-shot tests, 61.3% of models passed; 48.39% passed the 0-shot tests.

**Validation**: Evaluated against 31 open-source large language models, providing comparative results.

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
