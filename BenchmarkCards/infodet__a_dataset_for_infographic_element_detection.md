# InfoDet: A Dataset for Infographic Element Detection

## 📊 Benchmark Details

**Name**: InfoDet: A Dataset for Infographic Element Detection

**Overview**: InfoDet is a dataset designed to support the development of accurate object detection models for charts and human-recognizable objects (HROs) in infographics. It contains 11,264 real and 90,000 synthetic infographics, with over 14 million bounding box annotations.

**Data Type**: infographic images with bounding box annotations

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/InfoDet2025/InfoDet)
- [Resource](https://huggingface.co/datasets/InfoDet/InfoDet)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to enhance the chart understanding capabilities of vision-language models and support object detection models for infographic elements.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Object Detection
- Chart Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Real infographics collected from chart-rich online platforms and synthetic infographics created programmatically from design templates.

**Size**: 101,264 infographics (11,264 real and 90,000 synthetic)

**Format**: N/A

**Annotation**: Bounding box annotations created through a combination of model-in-the-loop and programmatic methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Average Precision (mAP)
- Average Recall (AR)

**Calculation**: Metrics are calculated based on the true positive, false positive, and false negative detections from the object detection models evaluated on the InfoDet test set.

**Interpretation**: Higher mAP and AR indicate better performance in accurately detecting infographic elements.

**Baseline Results**: The best-performing models achieve an mAP of up to 88.2% for chart and HRO categories.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
