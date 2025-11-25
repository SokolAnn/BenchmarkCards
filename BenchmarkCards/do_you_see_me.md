# Do You See Me

## 📊 Benchmark Details

**Name**: Do You See Me

**Overview**: Do You See Me is a scalable benchmark designed to systematically evaluate Multimodal Large Language Models (MLLMs) on their core visual perception skills. It consists of 1,758 images and 2,612 questions across seven human-psychology inspired subtasks in both 2D and 3D.

**Data Type**: image-question pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMVP
- CV-Bench
- MVP-Bench

**Resources**:
- [GitHub Repository](https://github.com/microsoft/Do-You-See-Me)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured framework for evaluating the visual perception capabilities of MLLMs, highlighting areas of weakness and providing insights into improving model performance.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Visual Discrimination
- Joint Shape-Color Discrimination
- Letter Discrimination
- Visual Form Constancy
- Visual Figure-Ground
- Visual Closure
- Visual Spatial

**Limitations**: The dataset may have a relatively small size for a comprehensive evaluation.

## 💾 Data

**Source**: Programmatically generated synthetic dataset

**Size**: 1,758 images and 2,612 questions

**Format**: N/A

**Annotation**: Programmatically generated

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: The evaluation uses the accuracy of MLLMs in answering visual questions correctly compared to the ground truth.

**Interpretation**: Performance is evaluated based on the accuracy of visual perception tasks, with context provided for understanding visual reasoning.

**Validation**: Models were evaluated against human performance benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Transparency

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Transparency**: Lack of training data transparency
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark aims to detect and address foundational visual perception inaccuracies in MLLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
