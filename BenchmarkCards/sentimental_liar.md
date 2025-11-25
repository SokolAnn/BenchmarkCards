# Sentimental LIAR

## 📊 Benchmark Details

**Name**: Sentimental LIAR

**Overview**: Sentimental LIAR extends the LIAR dataset by adding features based on sentiment and emotion analysis of claims. It aims to automate the detection of false short-text claims on social media using advanced deep learning architectures.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LIAR

**Resources**:
- [GitHub Repository](https://github.com/UNHSAILLab/SentimentalLIAR)

## 🎯 Purpose and Intended Users

**Goal**: To enhance automated detection of fake claims on social media by providing a new benchmark dataset with additional features that improve classification accuracy.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Fake Claim Detection

**Limitations**: N/A

## 💾 Data

**Source**: Extended from the LIAR dataset, augmented with sentiment and emotion attributes through existing NLP APIs.

**Size**: 12,836 statements

**Format**: N/A

**Annotation**: Annotated with binary labels for true or false claims derived from original LIAR multi-class labels.

## 🔬 Methodology

**Methods**:
- Deep Learning
- Neural Networks

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on model predictions compared to ground truth labels in the dataset.

**Interpretation**: Higher accuracy and F1 scores indicate better performance in detecting fake claims.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
