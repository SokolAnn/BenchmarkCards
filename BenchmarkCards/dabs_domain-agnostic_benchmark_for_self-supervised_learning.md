# DABS (Domain-Agnostic Benchmark for Self-Supervised Learning)

## 📊 Benchmark Details

**Name**: DABS (Domain-Agnostic Benchmark for Self-Supervised Learning)

**Overview**: DABS measures how well a single SSL algorithm works on many different domains, comprising seven domains representing different kinds of data: natural images, English text, speech, chest x-rays, multichannel sensor data, multilingual text, and images with text descriptions.

**Data Type**: unlabeled datasets for pretraining and labeled datasets for evaluation

**Domains**:
- Natural Language Processing
- Computer Vision
- Healthcare

**Languages**:
- English
- Spanish
- French
- German
- Chinese
- Korean
- Japanese

**Resources**:
- [GitHub Repository](https://github.com/alextamkin/dabs)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized way to evaluate the performance of domain-agnostic methods.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Self-Supervised Learning

**Limitations**: DABS is a 'living benchmark' and does not capture how well domain-agnostic methods can be combined with domain-specific methods.

## 💾 Data

**Source**: The benchmark consists of datasets across seven domains: natural images (ImageNet), speech (LibriSpeech), English text (WikiText-103), multilingual text (mC4), chest x-rays (CheXpert, ChestX-ray8), multi-channel sensor data (PAMAP2), and images with text descriptions (MS COCO).

**Size**: 1,281,167 images for ImageNet, 145,265 examples for LibriSpeech, 1,165,029 tokens for WikiText-103, 26TB+ for mC4, 223,414 images for CheXpert, 50,000 examples for PAMAP2, 117,266 images for MS COCO.

**Format**: Various formats including images and text datasets.

**Annotation**: Data is unlabeled for pretraining tasks and labeled for evaluation tasks.

## 🔬 Methodology

**Methods**:
- Linear classification
- Contrastive learning

**Metrics**:
- Accuracy
- Average Area Under ROC (AUC)

**Calculation**: Models are assessed by their average transfer learning performance on downstream tasks across domains.

**Interpretation**: The performance is interpreted based on accuracy percentages across various transfer tasks.

**Validation**: Standardized processing and evaluation protocols were established for fair comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: For PAMAP2, participants consented to data use for scientific purposes.

**Compliance With Regulations**: Not Applicable
