# Catalonia Independence Corpus (CIC)

## 📊 Benchmark Details

**Name**: Catalonia Independence Corpus (CIC)

**Overview**: This paper presents a method to obtain multilingual datasets for stance detection in Twitter. The Catalonia Independence Corpus (CIC) includes semi-automatically annotated tweets in Catalan and Spanish, aimed at facilitating multilingual and crosslingual research on stance detection.

**Data Type**: annotated tweets

**Domains**:
- Natural Language Processing

**Languages**:
- Catalan
- Spanish

**Resources**:
- [GitHub Repository](https://github.com/ZotovaElena/Multilingual-Stance-Detection)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large, balanced, and multilingual annotated corpus for stance detection in Twitter, allowing for comparative analyses in multilingual settings.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Stance Detection

**Limitations**: N/A

## 💾 Data

**Source**: Collected tweets from Twitter API focusing on the topic of Catalonia's independence

**Size**: 10,000 annotated tweets per language (Catalan and Spanish)

**Format**: JSON

**Annotation**: Semi-automatically annotated using user-based information and manual categorization of user accounts.

## 🔬 Methodology

**Methods**:
- User-based annotation
- Topic modelling
- LDA for tweet selection

**Metrics**:
- F1 Score

**Calculation**: F1 average score is calculated based on the classification results of the stance labels: FAVOR, AGAINST, NONE.

**Interpretation**: Higher F1 scores indicate better classification performance on stance detection tasks.

**Baseline Results**: Previous benchmarks include SemEval 2016 and TW-1O datasets.

**Validation**: Evaluated using multiple language models including mBERT and XLM-R.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-NC-ND 4.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
