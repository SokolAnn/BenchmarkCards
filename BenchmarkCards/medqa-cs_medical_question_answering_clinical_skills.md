# MedQA-CS (Medical Question Answering Clinical Skills)

## 📊 Benchmark Details

**Name**: MedQA-CS (Medical Question Answering Clinical Skills)

**Overview**: MedQA-CS is an AI-SCE (AI-Structured Clinical Examination) framework designed to assess large language models' clinical skills through realistic medical scenarios, focusing on instruction-following abilities that reflect actual clinical situations.

**Data Type**: instruction-following tasks

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- MMLU (Massive Multitask Language Understanding)

**Resources**:
- [GitHub Repository](https://github.com/bio-nlp/MedQA-CS)
- [Resource](https://huggingface.co/datasets/bio-nlp-umass/MedQA-CS-Student)
- [Resource](https://huggingface.co/datasets/bio-nlp-umass/MedQA-CS-Exam)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models' clinical skills using a structured examination framework akin to OSCE (Objective Structured Clinical Examinations).

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Information Gathering
- Physical Examination
- Closure
- Differential Diagnosis

**Limitations**: The benchmark relies on data derived from the USMLE Step 2 CS, which may not cover all clinical areas comprehensively; furthermore, the dataset is available only in English and based solely on text inputs.

## 💾 Data

**Source**: Publicly available resources from the USMLE guidelines

**Size**: 1,667 (instruction, input, output) data points

**Format**: JSON

**Annotation**: Expert annotations and evaluations were performed in collaboration with medical professionals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- F1 Score
- UMLS-F1

**Calculation**: Metrics are calculated based on comparing LLM outputs against expert-assigned scores and ground truth definitions.

**Interpretation**: Higher LLM scores indicate better alignment with expert evaluations and better performance in clinical skills assessments, while lower scores point to areas needing improvement.

**Baseline Results**: The average scores reported for various LLMs using MedQA-CS based on expert evaluations range from 62.35 (Claude-3.5-Sonnet) to 48.44 (GPT-3.5).

**Validation**: The reliability of MedQA-CS was validated by experts to ensure high correlation between human assessments and model evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis may highlight disparities in clinical skills assessments across different demographic groups, though specific breakdowns are not provided.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons BY-NC 4.0 License for dataset usage

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
