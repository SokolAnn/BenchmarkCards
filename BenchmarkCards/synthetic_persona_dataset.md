# Synthetic Persona Dataset

## 📊 Benchmark Details

**Name**: Synthetic Persona Dataset

**Overview**: The Synthetic Persona Dataset is introduced to systematically investigate cross-modal factual memorization in vision-language models by creating diverse synthetic personas, complete with visual representations and textual descriptions, aimed at quantifying knowledge transfer between modalities.

**Data Type**: image-description pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2506.05198)

## 🎯 Purpose and Intended Users

**Goal**: To quantify cross-modal memorization in vision-language models by analyzing how knowledge is transferred between modalities, specifically from images to text and vice versa.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Cross-Modal Knowledge Transfer
- Multi-hop Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic persona dataset generated using text-to-image models and narrative description models.

**Size**: 100 unique personas with multiple image and description variants

**Format**: Image and text files

**Annotation**: Automatically generated descriptions conditioned on visual attributes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Measured performance based on model's ability to recall names and attributes from images and descriptions.

**Interpretation**: Higher accuracy indicates better cross-modal memorization and knowledge transfer.

**Validation**: Controlled experiments using synthetic data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Synthetic data is used to mitigate privacy risks inherent in real data collection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
