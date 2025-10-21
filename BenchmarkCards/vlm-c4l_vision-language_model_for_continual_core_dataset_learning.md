# VLM-C4L (Vision-Language Model for Continual Core Dataset Learning)

## 📊 Benchmark Details

**Name**: VLM-C4L (Vision-Language Model for Continual Core Dataset Learning)

**Overview**: VLM-C4L introduces a continual learning framework that optimizes corner case datasets for autonomous driving using Vision-Language Models, enabling models to learn from diverse corner cases while preserving performance on previously learned scenarios.

**Data Type**: images

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- CODA

**Resources**:
- [Resource](http://www.vlmc4l.site/)

## 🎯 Purpose and Intended Users

**Goal**: To enhance autonomous driving systems' ability to handle corner cases through a continual learning framework and optimized dataset.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Object Detection

**Limitations**: N/A

## 💾 Data

**Source**: Waymo dataset and CODA dataset

**Size**: 8,000 images

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Average Precision (AP)
- Average Recall (AR)

**Calculation**: Metrics are calculated based on the true positive detections compared to ground truth in the datasets.

**Interpretation**: Higher AP and AR scores indicate better performance in detecting objects in challenging conditions.

**Baseline Results**: Sparse R-CNN and Cascade-DETR are used as baseline models.

**Validation**: The framework is validated through comprehensive experiments on large-scale, real-world datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
