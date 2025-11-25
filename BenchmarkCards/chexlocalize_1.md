# CheXlocalize

## 📊 Benchmark Details

**Name**: CheXlocalize

**Overview**: The CheXlocalize dataset evaluates the ability of models to localize pathologies on chest radiographs, providing expert radiologist annotations for the localization of distinct findings.

**Data Type**: image

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2509.18015)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the ability of multimodal large language models to localize pathological findings in chest radiographs.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Radiologists

**Tasks**:
- Image Localization

**Limitations**: The analysis focused on one dataset, potentially leading to variability in results across different pathologies and limits generalizability.

## 💾 Data

**Source**: CheXlocalize dataset, consisting of chest radiograph images with expert radiologist annotations.

**Size**: 200 validation radiographs, 500 test radiographs

**Format**: N/A

**Annotation**: Expert radiologist annotations for localization provided in the form of pixel-wise segmentation maps.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Hit Rate

**Calculation**: A prediction is a hit if at least 50% of the grid cell overlaps with the ground truth segmentation.

**Interpretation**: Performance is compared to a human benchmark and a CNN baseline, where hit rates indicate accuracy in localizing pathologies.

**Baseline Results**: CNN baseline achieved an average hit rate of 59.9%, human benchmark showed 80.1%.

**Validation**: Validation was performed using the validation split of the CheXlocalize dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
