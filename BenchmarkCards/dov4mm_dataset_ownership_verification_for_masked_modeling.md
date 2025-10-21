# DOV4MM (Dataset Ownership Verification for Masked Modeling)

## 📊 Benchmark Details

**Name**: DOV4MM (Dataset Ownership Verification for Masked Modeling)

**Overview**: DOV4MM is a methodology designed to verify if a suspicious masked model has been trained on a particular unlabeled dataset, focusing on protecting dataset ownership.

**Data Type**: masked image/model verification

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/xieyc99/DOV4MM)

## 🎯 Purpose and Intended Users

**Goal**: Verify dataset ownership for protected datasets utilized in masked models.

**Target Audience**:
- ML Researchers
- Data Owners
- Security Practitioners

**Tasks**:
- Dataset Ownership Verification

**Limitations**: N/A

## 💾 Data

**Source**: ImageNet-1K, WikiText-103 subsets, Food101, COCO, Places365

**Size**: 10,000 images or selectively sized subsets

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Hypothesis Testing
- Statistical Analysis

**Metrics**:
- p-value
- Sensitivity
- Specificity
- AUROC

**Calculation**: Calculated through one-tailed pairwise t-test based on relative embedding reconstruction difficulty.

**Interpretation**: A p-value less than 0.05 indicates that the suspicious model has likely been pre-trained on the dataset.

**Baseline Results**: DOV4MM outperforms other existing methods in detecting ownership violations.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Security
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
