# LUMA (Learning from Uncertain and Multimodal Data)

## 📊 Benchmark Details

**Name**: LUMA (Learning from Uncertain and Multimodal Data)

**Overview**: LUMA is a unique multimodal dataset featuring audio, image, and textual data from 50 classes, specifically designed for learning from uncertain data. The dataset allows the controlled injection of varying types and degrees of uncertainty to achieve and tailor specific experiments and benchmarking initiatives.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/bezirganyan/LUMA)
- [Resource](https://huggingface.co/datasets/bezirganyan/LUMA)

## 🎯 Purpose and Intended Users

**Goal**: To promote and support the development, evaluation, and benchmarking of trustworthy and robust multimodal deep learning approaches.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Multimodal Classification
- Uncertainty Quantification

**Limitations**: N/A

## 💾 Data

**Source**: Images from CIFAR-10/100 dataset, audio from three audio corpora, and text generated using the Gemma-7B Large Language Model.

**Size**: 3GB

**Format**: N/A

**Annotation**: Automatically validated and manually validated audio samples.

## 🔬 Methodology

**Methods**:
- Monte-Carlo Dropout
- Deep Ensemble
- Reliable Conflictive Multi-View Learning

**Metrics**:
- Accuracy
- AUC

**Calculation**: Metrics are calculated based on model predictions on varying datasets.

**Interpretation**: Higher uncertainty values should ideally indicate a model's recognition of noise or out-of-distribution samples.

**Baseline Results**: N/A

**Validation**: Evaluation on clean, reduced diversity, increased label noise, and increased sample noise datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Dataset includes a bias analysis.

**Potential Harm**: Potential for bias in generated texts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
