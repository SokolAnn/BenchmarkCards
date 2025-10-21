# UNIAA-Bench

## 📊 Benchmark Details

**Name**: UNIAA-Bench

**Overview**: UNIAA-Bench is a comprehensive benchmark designed to evaluate the aesthetic capabilities of Multi-modal Large Language Models (MLLMs) in Image Aesthetic Assessment (IAA) from three aspects: Aesthetic Perception, Aesthetic Description, and Aesthetic Assessment.

**Data Type**: question-answering pairs, image-description pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2404.09619)

## 🎯 Purpose and Intended Users

**Goal**: To create a unified framework that aligns with human aesthetic processes for evaluating image aesthetics using Multi-modal Large Language Models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Aesthetic Perception
- Aesthetic Description
- Aesthetic Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Five open-source IAA datasets: AVA, AADB, ICAA17K, PARA, PCCD

**Size**: 5,354 question-answer pairs, 501 image-description pairs

**Format**: N/A

**Annotation**: Expert annotations and automated generation for aesthetic quality assessment.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are based on comparison with human judgments and established aesthetic standards.

**Interpretation**: Evaluation metrics reflect the ability of MLLMs to perform aesthetic assessment tasks comparably to human evaluators.

**Baseline Results**: Results indicate UNIAA-LLaVA achieves competitive performance against other MLLMs, approaching human level in some tasks.

**Validation**: Tested extensively through multiple IAA datasets and human validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
