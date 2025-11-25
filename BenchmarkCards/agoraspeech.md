# AgoraSpeech

## 📊 Benchmark Details

**Name**: AgoraSpeech

**Overview**: AgoraSpeech is a meticulously curated, high-quality dataset of 171 political speeches from six parties during the Greek national elections in 2023, encompassing annotations for multiple NLP tasks and designed for political discourse analysis.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Greek
- English

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.13957176)
- [GitHub Repository](https://github.com/Datalab-AUTH/AgoraSpeech-EDA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive, high-quality annotated dataset of political discourse, supporting various analyses and applications in political science and NLP.

**Target Audience**:
- Political Scientists
- Data Scientists
- Journalists

**Tasks**:
- Text Classification
- Topic Identification
- Sentiment Analysis
- Named Entity Recognition
- Polarization Detection
- Populism Detection

**Limitations**: N/A

## 💾 Data

**Source**: Political speeches from the Greek national elections sourced from political parties' press offices and public communications.

**Size**: 171 speeches, 5,279 paragraphs, 31,674 annotations

**Format**: CSV

**Annotation**: Hybrid: Initial ChatGPT-generated annotations validated by human experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Calculated as the fraction of paragraphs where ChatGPT’s annotation remains unchanged by human reviewers relative to the total number of paragraphs for each NLP task.

**Interpretation**: A high accuracy indicates strong alignment between ChatGPT and human annotations.

**Baseline Results**: Text classification accuracy: 89%, Sentiment analysis accuracy: 93%, Polarization detection accuracy: 88%, Topic classification accuracy: 61%.

**Validation**: Utilizing a human-in-the-loop methodology for validating and refining ChatGPT annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Transparency

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
