# MLL Benchmark (Model Label Learning Benchmark)

## 📊 Benchmark Details

**Name**: MLL Benchmark (Model Label Learning Benchmark)

**Overview**: The benchmark consists of 49 pre-trained Vision-Language Models (VLMs) and 17 target task datasets for evaluating VLM selection and reuse methods.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/LAMDASZ-ML/MLL)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate evaluation of VLM selection and reuse methods across multiple tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Classification
- Geo-localization
- Object Distance Estimation
- Facial Expression Classification
- Optical Character Recognition
- Action Recognition

**Limitations**: The current implementation focuses solely on VLMs and visual classification tasks.

## 💾 Data

**Source**: 49 pre-trained VLMs, 17 target datasets including diverse domains and tasks.

**Size**: 49 VLMs, 17 target tasks

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Model selection
- Model reuse

**Metrics**:
- Accuracy

**Calculation**: Evaluation methodology based on zero-shot performance on target tasks.

**Interpretation**: Higher accuracy indicates better selection and reuse methods for VLMs.

**Baseline Results**: N/A

**Validation**: Effects of using different counts of reused models were analysed.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
