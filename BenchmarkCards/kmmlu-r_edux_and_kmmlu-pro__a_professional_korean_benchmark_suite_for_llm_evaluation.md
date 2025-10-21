# KMMLU-R EDUX and KMMLU-PRO: A Professional Korean Benchmark Suite for LLM Evaluation

## 📊 Benchmark Details

**Name**: KMMLU-R EDUX and KMMLU-PRO: A Professional Korean Benchmark Suite for LLM Evaluation

**Overview**: The paper introduces KMMLU-R EDUX and KMMLU-PRO, two benchmarks designed to evaluate Korean expert-level knowledge and professional licensure exams, respectively, focusing on real-world applicability of large language models in various professional domains.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Korean

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)

**Resources**:
- [Resource](https://huggingface.co/datasets/LGAI-EXAONE/KMMLU-Redux)
- [Resource](https://huggingface.co/datasets/LGAI-EXAONE/KMMLU-Pro)

## 🎯 Purpose and Intended Users

**Goal**: To provide rigorous benchmarks addressing professional knowledge in Korea and evaluate the performance of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmarks are limited to text-only and multiple-choice questions, restricting the evaluation of real-world licensure exams that may include non-textual modalities.

## 💾 Data

**Source**: Korean National Technical Qualification exams and Korean National Professional Licensure exams

**Size**: 2,587 examples for KMMLU-R EDUX, 2,822 examples for KMMLU-PRO

**Format**: JSON

**Annotation**: Annotated by human experts to ensure quality and reduce contamination.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy
- Pass Rate in Licensure Exams

**Calculation**: Metrics were calculated based on model performance against the benchmarks with specific passing criteria set for licensure exams.

**Interpretation**: A model must score at least 40% in each subject and achieve an overall average of 60% to pass the exams.

**Validation**: Models were validated against real-world professional exams to ensure alignment with human standards.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used in the benchmarks are publicly available or collected from official licensing materials released by government or professional institutions.

**Data Licensing**: CC-BY-NC-ND 4.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
