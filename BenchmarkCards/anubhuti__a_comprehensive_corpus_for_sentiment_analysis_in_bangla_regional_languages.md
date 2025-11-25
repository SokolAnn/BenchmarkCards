# ANUBHUTI: A Comprehensive Corpus for Sentiment Analysis in Bangla Regional Languages

## 📊 Benchmark Details

**Name**: ANUBHUTI: A Comprehensive Corpus for Sentiment Analysis in Bangla Regional Languages

**Overview**: ANUBHUTI is a pioneering corpus developed for sentiment analysis in Bangla regional dialects, addressing a critical gap in low-resource NLP research for languages such as Sylhet, Chittagong, Noakhali, and Mymensingh.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bangla

**Similar Benchmarks**:
- Vashantor

**Resources**:
- [Resource](https://data.mendeley.com/datasets/gbkszkt8z3/2)

## 🎯 Purpose and Intended Users

**Goal**: To advance dialect-aware sentiment analysis by leveraging modern transformer architectures, domain adaptation, and interpretability techniques.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Sentiment Analysis

**Limitations**: Limited domain coverage primarily focuses on political and religious texts.

## 💾 Data

**Source**: Collected from a publicly available Bangla Sentiment Analysis corpus and manually translated into four major regional dialects.

**Size**: 2,000 sentences

**Format**: CSV

**Annotation**: Annotated using dual annotation scheme: multiclass thematic labeling (Political, Religious, Neutral) and multilabel emotion annotation (Anger, Contempt, Disgust, Enjoyment, Fear, Sadness, Surprise).

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Cohen’s Kappa

**Calculation**: Cohen’s Kappa was used to evaluate inter-annotator agreement.

**Interpretation**: A higher Kappa score indicates stronger agreement between annotators.

**Validation**: Quality assurance performed via systematic checks for missing data, anomalies, and inconsistencies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The dataset captures various dialects, contributing to linguistic diversity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not contain sensitive or private information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
