# MEDFRAME QA

## 📊 Benchmark Details

**Name**: MEDFRAME QA

**Overview**: MEDFRAME QA is the first benchmark explicitly designed to evaluate multi-image reasoning in medical visual question answering (VQA), consisting of 2,851 VQA pairs from medical videos.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- VQA-RAD
- VQA-Med-2019
- VQA-Med-2021
- SLAKE
- MedXpertQA

**Resources**:
- [Resource](https://huggingface.co/datasets/SuhaoYu1020/MedFrameQA)
- [Resource](https://ucsc-vlaa.github.io/MedFrameQA/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate multi-image reasoning capabilities of MLLMs in clinical scenarios similar to real-world diagnostic situations.

**Target Audience**:
- ML Researchers
- Medical Professionals
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Extracted from 3,420 medical videos available on YouTube.

**Size**: 2,851 question-answering pairs

**Format**: N/A

**Annotation**: Automatically generated via an automated pipeline using GPT-4 for image filtering, caption alignment, and question generation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the percentage of correctly answered questions by models.

**Interpretation**: Higher accuracy indicates better performance of models in multi-image reasoning tasks.

**Baseline Results**: Most models performed with accuracies below 50%.

**Validation**: Validation through automated and manual quality checks ensuring question complexity and relevance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
