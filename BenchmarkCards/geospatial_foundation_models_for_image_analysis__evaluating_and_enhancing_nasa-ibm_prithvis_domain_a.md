# Geospatial foundation models for image analysis: evaluating and enhancing NASA-IBM Prithvi’s domain adaptability

## 📊 Benchmark Details

**Name**: Geospatial foundation models for image analysis: evaluating and enhancing NASA-IBM Prithvi’s domain adaptability

**Overview**: This paper evaluates the effectiveness of NASA-IBM's foundation model Prithvi in its ability for multiple downstream tasks for remote sensing image analysis. Four benchmark datasets containing environmental and land use features and covering diverse geographical regions are selected in the analysis.

**Data Type**: image

**Domains**:
- Geospatial Analysis
- Remote Sensing

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.48550/arXiv.2310.18660)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of NASA-IBM's foundation model Prithvi and its applicability in remote sensing image analysis tasks.

**Target Audience**:
- Geospatial Researchers
- AI Practitioners
- Remote Sensing Analysts

**Tasks**:
- Object Detection
- Instance Segmentation

**Limitations**: N/A

## 💾 Data

**Source**: Four benchmark datasets including Mars crater, Earth’s natural features, Ice-wedge polygons, and EuroCrops.

**Size**: 10,000 images

**Format**: N/A

**Annotation**: Annotated by domain experts with instance-level bounding boxes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Average Precision (mAP)

**Calculation**: Computed mAP scores for model performance across multiple IoU thresholds.

**Interpretation**: Higher mAP scores indicate better model performance in object detection and segmentation tasks.

**Validation**: Evaluated using four distinct remote sensing datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
