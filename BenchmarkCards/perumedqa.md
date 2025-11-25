# PeruMedQA

## 📊 Benchmark Details

**Name**: PeruMedQA

**Overview**: PeruMedQA is a multiple-choice question-answering (MCQA) dataset of medical examination questions for Peruvian physicians seeking specialty training, containing 8,380 questions across 12 medical domains.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Spanish

**Similar Benchmarks**:
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/google-health/medgemma/blob/main/notebooks/fine_tune_with_hugging_face.ipynb)
- [Resource](https://www.conareme.org.pe/web/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models (LLMs) on medical examination questions in Spanish from Peru and to provide a benchmark dataset for future research.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Medical Educators

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Questions from medical examinations published by the Consejo Nacional de Residentado Médico (CONAREME) in Peru.

**Size**: 8,380 questions

**Format**: CSV

**Annotation**: Manual verification of extracted answers from original PDFs.

## 🔬 Methodology

**Methods**:
- Zero-shot task-specific prompting
- Fine-tuning with PEFT and LoRA

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the number of correct answers divided by the total number of valid answers.

**Interpretation**: Higher accuracy indicates better performance of LLMs in answering medical exam questions.

**Baseline Results**: medgemma-27b-text-it achieved scores >90% in several instances.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset covers questions relevant to the Peruvian medical context.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was sourced from publicly available exam questions, ensuring no private data is involved.

**Data Licensing**: Apache 2.0 license for the dataset allowing commercial and non-commercial use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
