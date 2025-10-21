# Cholera X Emotion Classification Dataset

## 📊 Benchmark Details

**Name**: Cholera X Emotion Classification Dataset

**Overview**: The study aims to classify emotions expressed in social media posts about Cholera based on a dataset of 23,000 tweets, utilizing machine learning models for emotion classification.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To classify emotions in social media posts related to Cholera outbreaks.

**Target Audience**:
- Public Health Researchers
- Data Scientists
- Machine Learning Practitioners

**Tasks**:
- Emotion Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected tweets from the Twitter API using related hashtags.

**Size**: 23,000 tweets

**Format**: CSV

**Annotation**: Emotion labeling using the pysentimiento library based on Ekman's basic wheel of emotions.

## 🔬 Methodology

**Methods**:
- Long Short-Term Memory (LSTM)
- Logistic Regression
- Decision Tree
- BERT

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated using standard definitions for classification problems.

**Interpretation**: High accuracy, precision, recall, and F1 Score indicate effective emotion classification.

**Baseline Results**: LSTM achieved an accuracy of 76%, Logistic Regression achieved 60%, Decision Tree achieved 56%, and BERT achieved 66%.

**Validation**: The dataset was split into 80% training and 20% testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Public sentiment misrepresentation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
