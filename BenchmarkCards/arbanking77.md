# ArBanking77

## 📊 Benchmark Details

**Name**: ArBanking77

**Overview**: ArBanking77 is a large Arabic dataset for intent detection in the banking domain, consisting of 31,404 queries in Modern Standard Arabic and Palestinian dialect, classified into 77 intents.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Resources**:
- [Resource](https://sina.birzeit.edu/arbanking77)

## 🎯 Purpose and Intended Users

**Goal**: To provide an Arabic intent dataset to aid in the development and evaluation of intent detection models in the banking domain.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Intent Detection

**Limitations**: Our dataset is limited to MSA and Palestinian dialect and covers only 77 intents.

## 💾 Data

**Source**: The dataset was arabized and localized from the original Banking77 dataset.

**Size**: 31,404 queries

**Format**: JSON

**Annotation**: The data was annotated by 26 annotators through multiple phases and reviewed for quality.

## 🔬 Methodology

**Methods**:
- Fine-tuning a BERT-based model

**Metrics**:
- F1 Score

**Calculation**: The F1 Score was calculated based on precision and recall from the predictions made by the model.

**Interpretation**: An F1 Score closer to 1 indicates better model performance in correctly identifying intents.

**Validation**: The dataset was split into training (90%) and validation (10%) sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
