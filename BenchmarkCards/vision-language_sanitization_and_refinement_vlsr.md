# Vision-Language Sanitization and Refinement (VLSR)

## 📊 Benchmark Details

**Name**: Vision-Language Sanitization and Refinement (VLSR)

**Overview**: The VLSR framework illustrates a method for label sanitization and refinement in multi-label manufacturing image datasets, improving dataset quality by addressing label noise and inconsistencies.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.13332887)

## 🎯 Purpose and Intended Users

**Goal**: To improve label quality in industrial datasets by sanitizing labels through a vision-language framework.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Multi-label Classification

**Limitations**: N/A

## 💾 Data

**Source**: Factorynet dataset, a manufacturing industrial dataset containing noisy labels from human annotations and web-scraped sources.

**Size**: 10,160 images, 6,426 distinct labels

**Format**: CSV

**Annotation**: Labels were generated from both crowdsourced and web-scraped sources.

## 🔬 Methodology

**Methods**:
- Cosine similarity analysis
- Clustering with DBSCAN

**Metrics**:
- Accuracy

**Calculation**: Cosine similarity is used to assess the semantic alignment between image and label embeddings to identify suitable labels.

**Interpretation**: High cosine similarity values indicate effective matches between images and labels.

**Baseline Results**: N/A

**Validation**: The dataset was validated through comparison of image-label pairs and clustering evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Privacy**: Data privacy rights alignment
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
