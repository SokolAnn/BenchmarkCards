# AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset

## 📊 Benchmark Details

**Name**: AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset

**Overview**: AfriMed-QA is the first large-scale Pan-African English multi-specialty medical Question-Answering dataset, consisting of 15,000 questions across various medical specialties sourced from over 60 medical schools across 16 African countries. It is designed to evaluate and develop equitable and effective large language models for healthcare in Africa.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- BioASQ

**Resources**:
- [Resource](https://huggingface.co/datasets/intronhealth/afrimedqa_v2)

## 🎯 Purpose and Intended Users

**Goal**: To provide a diverse and representative benchmark dataset for evaluating the performance of large language models in the context of African healthcare.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: While this dataset is comprehensive, it primarily represents questions from West Africa and may not cover the full spectrum of African medical knowledge.

## 💾 Data

**Source**: Sourced from over 60 medical schools across 16 countries in Africa.

**Size**: 15,275 questions

**Format**: JSON

**Annotation**: Expert and crowdsourced annotations, including human ratings and evaluations.

## 🔬 Methodology

**Methods**:
- Quantitative evaluation
- Qualitative human evaluations

**Metrics**:
- Accuracy
- ROUGE-L
- BERTScore

**Calculation**: Accuracy is measured by comparing model answers to reference answers, while qualitative evaluations assess relevance and correctness.

**Interpretation**: Higher accuracy indicates better model performance, and human evaluations provide insights into the quality and local relevance of responses.

**Baseline Results**: Comparison against existing benchmarks such as MedQA.

**Validation**: The dataset was validated through expert review and human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: Dataset includes demographics of contributors to ensure diverse representation.

**Potential Harm**: Potential for harmful misinformation due to inaccuracies in model outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not contain personally identifiable information and requires no deidentification.

**Data Licensing**: Released under a CC-BY-NC-SA 4.0 license.

**Consent Procedures**: All contributors signed informed consent forms and privacy agreements.

**Compliance With Regulations**: Aligned with ethical standards for data handling and participant consent.
