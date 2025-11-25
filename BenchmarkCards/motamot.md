# Motamot

## 📊 Benchmark Details

**Name**: Motamot

**Overview**: The 'Motamot' dataset, comprising 7,058 instances annotated with positive and negative sentiments, is developed specifically for political sentiment analysis in the Bengali language, sourced from diverse online newspapers.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Resources**:
- [GitHub Repository](https://github.com/Mukaffi28/Bengali-Political-Sentiment-Analysis)
- [Resource](https://doi.org/10.17632/hdhnrrwdz2.1)

## 🎯 Purpose and Intended Users

**Goal**: To investigate public sentiments about politics in Bangladeshi online newspapers during elections and provide insights for political parties and voters.

**Target Audience**:
- ML Researchers
- Political Analysts
- Domain Experts

**Tasks**:
- Sentiment Analysis

**Limitations**: The dataset is limited to positive and negative sentiment labels, potentially restricting granularity in sentiment analysis.

## 💾 Data

**Source**: Compiled from various online newspapers focusing on political events during Bangladeshi elections.

**Size**: 7,058 instances

**Format**: CSV

**Annotation**: Manually annotated by a team of six student annotators with guidelines ensuring uniformity in sentiment labeling.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on model performance on held-out test sets.

**Interpretation**: Higher accuracy, precision, recall, and F1 Score indicate better performance in capturing political sentiments.

**Validation**: Utilized Fleiss Kappa to measure inter-rater reliability, achieving a kappa score of 0.87.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
