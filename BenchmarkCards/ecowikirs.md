# EcoWikiRS

## 📊 Benchmark Details

**Name**: EcoWikiRS

**Overview**: EcoWikiRS is a dataset that connects high-resolution aerial images with species observations and the textual descriptions of their habitats in Wikipedia. It provides a scalable way of supervision for remote sensing vision language models (RS-VLMs) for ecology through weak and noisy supervision.

**Data Type**: triplets (image, GBIF observations, Wikipedia texts)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ZEST

**Resources**:
- [GitHub Repository](https://github.com/eceo-epfl/EcoWikiRS)

## 🎯 Purpose and Intended Users

**Goal**: To learn an ecologically rich embedding space between remote sensing images and texts that describe the local environmental conditions.

**Target Audience**:
- ML Researchers
- Ecologists
- Remote Sensing Practitioners

**Tasks**:
- Ecosystem Mapping
- Zero-Shot Classification

**Limitations**: While fine-tuning pretrained RS-VLMs on the EcoWikiRS dataset leads to performance gains for EUNIS ecosystem recognition, systematic biases are present in species observations and Wikipedia contributions.

## 💾 Data

**Source**: Global Biodiversity Information Facility (GBIF) for species observations, SwissIMAGE for aerial images, Wikipedia for textual descriptions.

**Size**: 91,801 aerial images associated with 2,745 different species

**Format**: N/A

**Annotation**: Data is annotated based on geolocation and text description relevance.

## 🔬 Methodology

**Methods**:
- Fine-tuning VLMs with WINCEL loss
- Zero-shot classification for EUNIS ecosystem recognition

**Metrics**:
- Overall Accuracy (OA)
- Macro F1 Score

**Calculation**: Metrics are calculated based on the model's prediction performance on the validation and test splits of the EcoWikiRS dataset.

**Interpretation**: Higher values of OA and F1 Score indicate better model performance in predicting ecosystem labels.

**Baseline Results**: Fine-tuning results in improved performance over pre-trained models, showcasing the effectiveness of the EcoWikiRS dataset.

**Validation**: Validation is conducted following a spatial block split to avoid spatial autocorrelation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
