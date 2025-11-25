# SMMILE (Stanford Multimodal Medical In-context Learning)

## 📊 Benchmark Details

**Name**: SMMILE (Stanford Multimodal Medical In-context Learning)

**Overview**: SMMILE is the first expert-driven multimodal in-context learning benchmark for the medical domain. It includes 111 problems across 6 medical specialties and 13 imaging modalities, designed to evaluate large multimodal language models' (MLLMs) ability to learn from multimodal in-context examples.

**Data Type**: question-image-answer triplets

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://smmile-benchmark.github.io)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SMMILE is to evaluate the ability of multimodal large language models to learn from multimodal in-context examples in medical contexts.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Medical Diagnosis
- Medical Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated by 11 medical experts, composed of multimodal queries and examples.

**Size**: 111 problems, 517 question-image-answer triplets

**Format**: N/A

**Annotation**: Expert-annotated

## 🔬 Methodology

**Methods**:
- Open-ended generation
- Closed-ended generation

**Metrics**:
- Exact Match (EM)
- LLM-as-a-Judge

**Calculation**: Performance evaluated against ground-truth answers

**Interpretation**: Scores reflect the model's ability to generate correct outputs based on provided context.

**Baseline Results**: Average performance of 15 MLLMs demonstrates limitations in learning from multimodal in-context examples.

**Validation**: Models evaluated on both open-ended and closed-ended tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Decision bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Licensed under CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
