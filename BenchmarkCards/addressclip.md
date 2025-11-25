# AddressCLIP

## 📊 Benchmark Details

**Name**: AddressCLIP

**Overview**: This study introduces the problem of Image Address Localization (IAL) and proposes the AddressCLIP framework along with three datasets to study the task of predicting readable textual addresses from images.

**Data Type**: image-address pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Pitts-250K
- SF-XL

**Resources**:
- [GitHub Repository](https://github.com/xsx1001/AddressCLIP)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the study of image address localization using the proposed AddressCLIP framework and the introduced datasets.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image Address Localization

**Limitations**: N/A

## 💾 Data

**Source**: Three datasets were built from the Pitts-250K and SF-XL datasets specifically for the Image Address Localization problem, including addresses derived from Google Maps reverse geocoding.

**Size**: 234K images (Pitts-IAL), 184K images (SF-IAL-Base), 1.96M images (SF-IAL-Large)

**Format**: N/A

**Annotation**: Addresses were annotated through reverse geocoding, manual verification, and semantic address partitioning.

## 🔬 Methodology

**Methods**:
- Image-Text Contrastive Learning
- Image-Geography Matching

**Metrics**:
- Top-1 Accuracy
- Top-5 Accuracy
- Street-level Accuracy (SA)
- Sub-Street-level Accuracy (SSA)

**Calculation**: Metrics are computed based on the correctness of predicted addresses against ground truth across the introduced datasets.

**Interpretation**: Higher accuracy percentages indicate better performance in predicting human-readable addresses from images.

**Baseline Results**: AddressCLIP achieves over 80% Top-1 accuracy across three datasets with notable improvements over existing benchmarks.

**Validation**: Performed through comparisons with zero-shot models and existing retrieval-based approaches.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

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
