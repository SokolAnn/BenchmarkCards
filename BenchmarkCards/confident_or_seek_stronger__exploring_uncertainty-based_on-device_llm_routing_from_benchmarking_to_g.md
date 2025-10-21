# Confident or Seek Stronger: Exploring Uncertainty-Based On-device LLM Routing From Benchmarking to Generalization

## 📊 Benchmark Details

**Name**: Confident or Seek Stronger: Exploring Uncertainty-Based On-device LLM Routing From Benchmarking to Generalization

**Overview**: This paper conducts a comprehensive investigation into benchmarking and generalization of uncertainty-driven routing strategies from small language models (SLMs) to large language models (LLMs) over 1500+ settings. It evaluates 8 uncertainty quantification (UQ) methods across 14 datasets to examine their alignment with correctness in routing tasks, proposing a calibration data construction pipeline to enhance routing generalization on new downstream scenarios.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Mathematical Reasoning
- Commonsense Reasoning
- Conversational and Contextual Understanding
- Problem Solving

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- CommonsenseQA
- HellaSwag
- OpenBookQA

**Resources**:
- [Resource](https://huggingface.co/datasets/...)

## 🎯 Purpose and Intended Users

**Goal**: To explore effective routing strategies for SLMs using uncertainty estimation and to enhance deployment on edge devices.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Various datasets including AQuA, GSM8K, MultiArith, TruthfulQA, and others from Hugging Face.

**Size**: 14 datasets

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- ROC AUC
- Accuracy

**Calculation**: Measured the alignment between extracted uncertainty and correctness.

**Interpretation**: Higher ROC AUC scores indicate stronger alignment between confidence and correctness.

**Baseline Results**: N/A

**Validation**: Evaluated across multiple datasets with various SLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
