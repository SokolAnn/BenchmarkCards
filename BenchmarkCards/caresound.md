# CaReSound

## 📊 Benchmark Details

**Name**: CaReSound

**Overview**: CaReSound is a benchmark dataset of annotated medical audio recordings enriched with metadata and paired question-answer examples, designed to drive progress in diagnostic reasoning research.

**Data Type**: audio-question-answer pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- ICBHI
- KAUH
- CirCor
- SPRSound
- ZCHSound

**Resources**:
- [Resource](https://huggingface.co/datasets/tsnngw/CaReSound)
- [Resource](https://huggingface.co/tsnngw/CaReAQA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the CaReSound benchmark is to advance open-ended question-answering in health diagnostics.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Open-ended Question Answering
- Closed-ended Classification

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is built from diverse open-source medical audio recordings, including ICBHI, KAUH, CirCor, SPRSound, and ZCHSound.

**Size**: 16,273 audio samples

**Format**: N/A

**Annotation**: Generated QA pairs based on metadata and annotations via large language models.

## 🔬 Methodology

**Methods**:
- Open-ended Question Answering
- Closed-ended Classification

**Metrics**:
- Accuracy
- BERTScore
- METEOR

**Calculation**: Metrics are calculated based on model predictions against ground truth using semantic and lexical similarity metrics.

**Interpretation**: Higher BERTScore and METEOR values indicate better performance in generating semantically and contextually relevant outputs.

**Baseline Results**: CaReAQA achieves 86.2% accuracy on open-ended diagnostic reasoning tasks.

**Validation**: The benchmark is validated via rigorous testing on multiple unseen datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack, Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
