# HRScene

## 📊 Benchmark Details

**Name**: HRScene

**Overview**: HRScene is a unified benchmark for high-resolution image (HRI) understanding, incorporating diverse real-world scenes and synthetic datasets for evaluating Vision Large Language Models (VLMs). It aims to assess performance across various applications like medical diagnosis, urban planning, and more.

**Data Type**: high-resolution images

**Domains**:
- Natural Language Processing
- Computer Vision
- Healthcare
- Urban Planning

**Languages**:
- N/A

**Similar Benchmarks**:
- MMMU
- VQAv2
- AI2D

**Resources**:
- [Resource](https://yszh8.github.io/hrscene/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for high-resolution image understanding, enabling evaluation and improvement of Vision Large Language Models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Classification
- Visual Question Answering
- Document Analysis
- Object Detection

**Limitations**: N/A

## 💾 Data

**Source**: HRScene incorporates 25 real-world datasets and 2 synthetic diagnostic datasets collected from diverse domains.

**Size**: 7,068 images

**Format**: varied (including various resolutions and types)

**Annotation**: Re-annotated by 10 graduate-level annotators and constructed to maintain high quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on exact match for multiple-choice questions and average performance across validation and test sets.

**Interpretation**: Higher scores indicate better performance of VLMs on the tasks evaluated.

**Baseline Results**: Average accuracy of existing VLMs around 50% across the benchmark tasks.

**Validation**: Extensive experiments involving 28 VLMs to evaluate their performance on HRScene.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
