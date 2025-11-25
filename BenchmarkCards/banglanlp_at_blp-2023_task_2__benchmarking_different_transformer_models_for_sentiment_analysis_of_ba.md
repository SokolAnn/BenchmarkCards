# BanglaNLP at BLP-2023 Task 2: Benchmarking different Transformer Models for Sentiment Analysis of Bangla Social Media Posts

## 📊 Benchmark Details

**Name**: BanglaNLP at BLP-2023 Task 2: Benchmarking different Transformer Models for Sentiment Analysis of Bangla Social Media Posts

**Overview**: This paper presents a benchmark for sentiment analysis of Bangla social media posts, using various Transformer-based architectures to quantify model performance in this low-resource language scenario.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Similar Benchmarks**:
- SentNoB
- BanglaBERT
- XLM-Roberta

**Resources**:
- [GitHub Repository](https://github.com/Saumajit/BanglaNLP/tree/main/Task_2)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark different transformer models for sentiment analysis of Bangla social media posts and evaluate their effectiveness in a low-resource language.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Sentiment Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Datasets from two distinct sources: MUBASE (manually annotated Tweets and Facebook posts) and SentNob (public comments from social media).

**Size**: 33,000 sentences (train and dev combined)

**Format**: N/A

**Annotation**: Manually annotated for sentiment polarity.

## 🔬 Methodology

**Methods**:
- Finetuning
- P-Tuning

**Metrics**:
- Micro F1

**Calculation**: Micro F1 is calculated by counting true positives, false negatives, and false positives globally.

**Interpretation**: Micro F1 indicates how well the model predicts the correct sentiment class.

**Baseline Results**: Micro-F1 of 67.02% on the test set.

**Validation**: Model performance validated on a dedicated test set after prior training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

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
