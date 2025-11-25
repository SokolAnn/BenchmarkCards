# Synthetic Time-Aligned Fungal Growth Dataset

## 📊 Benchmark Details

**Name**: Synthetic Time-Aligned Fungal Growth Dataset

**Overview**: This dataset is designed to facilitate training and evaluation for the CLIPTime model, annotating images of fungal growth with aligned timestamps and categorical stage labels.

**Data Type**: image and text with timestamps

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/PetarDurdevic/Funghi)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the Synthetic Time-Aligned Fungal Growth Dataset is to provide a basis for modeling biological progression and temporal dynamics in fungal growth.

**Target Audience**:
- ML Researchers
- Biological Researchers

**Tasks**:
- Classification
- Regression

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic dataset generated for assessing fungal growth stages and timestamps.

**Size**: Not explicitly stated

**Format**: Not explicitly stated

**Annotation**: Images are accompanied by categorical labels and timestamps for each growth stage.

## 🔬 Methodology

**Methods**:
- Multi-task learning
- Transformer-based regression

**Metrics**:
- Classification Accuracy
- Temporal Accuracy
- Mean Squared Error

**Calculation**: Metrics are calculated using standard approaches for cross-entropy loss for classification and MSE for regression.

**Interpretation**: Higher accuracy indicates effective classification of fungal stages, while lower MSE indicates better timestamp prediction.

**Baseline Results**: Not explicitly stated

**Validation**: Model evaluation is conducted against the synthetic dataset across multiple training epochs to assess performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
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
