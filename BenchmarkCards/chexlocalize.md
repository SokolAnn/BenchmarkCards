# CheXlocalize

## 📊 Benchmark Details

**Name**: CheXlocalize

**Overview**: CheXlocalize is a dataset designed to evaluate the ability of models to localize pathologies on chest radiographs by providing annotations through pixel-wise segmentation maps for 10 distinct findings.

**Data Type**: image

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2509.18015)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the ability of multi-modal large language models (MLLMs) to localize pathologies on chest radiographs.

**Target Audience**:
- Healthcare Researchers
- Medical Imaging Practitioners

**Tasks**:
- Object Detection

**Limitations**: Some pathologies in the CheXlocalize dataset have a small image count, leading to large error bars for those results.

## 💾 Data

**Source**: Images collected from Stanford Hospital with expert radiologist annotations for localization of pathological findings.

**Size**: 234 validation images, 668 test images

**Format**: Images with pixel-level segmentation maps

**Annotation**: Expert annotations provided by radiologists

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Hit Rate

**Calculation**: A prediction is considered a hit if at least 50% of the grid cell overlaps with the ground truth segmentation.

**Interpretation**: Higher hit rates indicate better localization capabilities of the models.

**Baseline Results**: CNN baseline showed an average hit rate of 59.9%, while humans achieved 80.1% accuracy.

**Validation**: Comparison against human benchmarks and CNN performance using predefined metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
