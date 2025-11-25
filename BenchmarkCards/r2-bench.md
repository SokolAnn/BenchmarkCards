# R2-Bench

## 📊 Benchmark Details

**Name**: R2-Bench

**Overview**: R2-Bench is a benchmark framework to evaluate the robustness of referring perception models against various perturbations across five key tasks.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2403.04924)

## 🎯 Purpose and Intended Users

**Goal**: To systematically assess the resilience of referring perception models against perturbations under realistic conditions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Referring Image Segmentation
- Video Object Segmentation
- Referring Video Object Segmentation
- Audiovisual Segmentation
- Queryable 3D Mapping

**Limitations**: N/A

## 💾 Data

**Source**: Custom synthesized data augmented with various perturbations.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Intersection over Union (mIoU)
- Region Similarity (J)
- Contour Accuracy (F)

**Calculation**: Metrics are calculated based on performance change compared to clean data.

**Interpretation**: Higher scores indicate better robustness of models under perturbations.

**Baseline Results**: Various baseline models tested, specific performance results vary.

**Validation**: N/A

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
