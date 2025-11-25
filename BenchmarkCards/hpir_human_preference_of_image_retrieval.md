# HPIR (Human Preference of Image Retrieval)

## 📊 Benchmark Details

**Name**: HPIR (Human Preference of Image Retrieval)

**Overview**: HPIR is a test set designed for evaluating the alignment of image retrieval systems with human aesthetic preferences. It leverages 150 pseudo queries generated to reflect user interests in aesthetics, where human evaluators compare groupings of image results for accuracy and aesthetic appeal.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2406.09397)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the alignment of human aesthetics in image retrieval systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Human-labeled dataset constructed from pseudo queries.

**Size**: 150 queries

**Format**: N/A

**Annotation**: Human labelers evaluate groups of images for aesthetic quality, with evaluations repeated to ensure reliability.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Reinforcement learning

**Metrics**:
- Accuracy
- Aesthetic quality

**Calculation**: Calculated as average accuracy and aesthetic ratings from human labels.

**Interpretation**: Higher scores indicate better alignment with human aesthetic preferences.

**Validation**: Validated through multiple rounds of human comparisons for robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
