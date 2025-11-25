# Dental Condition Classification Dataset

## 📊 Benchmark Details

**Name**: Dental Condition Classification Dataset

**Overview**: This paper introduces a semi-supervised learning framework to classify thirteen dental conditions on panoramic radiographs, utilizing a large dataset and incorporating large language models for annotation.

**Data Type**: image

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2406.17915)

## 🎯 Purpose and Intended Users

**Goal**: To classify dental conditions from panoramic radiographs using a semi-supervised learning approach.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Dental Radiologists

**Tasks**:
- Image Classification

**Limitations**: The dataset has limited examples for certain conditions, affecting the model's ability to generalize.

## 💾 Data

**Source**: A dataset of 16,824 panoramic radiographs and 8,029 textual reports from two radiologists.

**Size**: 16,824 images

**Format**: N/A

**Annotation**: Manual annotation with additional auto-labeling using large language models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Statistical analysis

**Metrics**:
- Matthews correlation coefficient (MCC)

**Calculation**: MCC is calculated based on true positives, false positives, false negatives, and true negatives.

**Interpretation**: MCC values range between -1 and 1 with higher values indicating better classification performance.

**Baseline Results**: N/A

**Validation**: Validation was conducted using a substantial dataset of dental conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misdiagnosis due to limited examples of certain dental conditions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data used in the study was ethically sourced with appropriate consent procedures.

**Data Licensing**: Not Applicable

**Consent Procedures**: Research ethics approved by the National Commission for Research Ethics (CONEP).

**Compliance With Regulations**: The study complied with ethical regulations for data usage.
