# Decoding News Bias: Multi Bias Detection in News Articles

## 📊 Benchmark Details

**Name**: Decoding News Bias: Multi Bias Detection in News Articles

**Overview**: This study proposes a new approach to bias detection in news articles by identifying various types of biases using a dataset curated through Large Language Models (LLMs). It addresses gaps in existing bias detection methods by classifying articles into seven distinct bias categories.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://aylien.com/)

## 🎯 Purpose and Intended Users

**Goal**: To extend the framework for detecting biases in news articles and improve the integrity and impartiality of media reporting through comprehensive bias identification.

**Target Audience**:
- ML Researchers
- Media Analysts
- Ethics Researchers

**Tasks**:
- Bias Detection

**Limitations**: The reliability of annotations provided by LLMs requires further exploration to minimize inconsistencies.

## 💾 Data

**Source**: News articles collected from Aylein API covering multiple domains.

**Size**: 4,886 samples

**Format**: N/A

**Annotation**: Dataset labeled using Large Language Models (LLMs) with a focus on various bias categories.

## 🔬 Methodology

**Methods**:
- Transformer-based model evaluation
- LLM-based dataset annotation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated using standard evaluation methods for multilabel classification.

**Interpretation**: Higher scores indicate better performance in detecting various biases.

**Baseline Results**: BERT achieved the highest F1-score of 0.89 in detecting Political Bias.

**Validation**: Multilabel Stratified KFold used to maintain label distributions across splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
