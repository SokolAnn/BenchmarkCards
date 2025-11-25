# Chichewa SMS Fraud Detection Dataset

## 📊 Benchmark Details

**Name**: Chichewa SMS Fraud Detection Dataset

**Overview**: This paper introduces a dataset for SMS fraud detection in Chichewa, including experiments with machine learning algorithms to classify SMS messages as fraud or non-fraud.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chichewa

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.14607454)

## 🎯 Purpose and Intended Users

**Goal**: To construct a dataset of SMSs in Chichewa for understanding SMS-enabled fraud and to build and test classification algorithms.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected through crowdsourcing from the Malawi University of Business and Applied Sciences and local telecommunication companies.

**Size**: 676 SMS messages

**Format**: CSV

**Annotation**: Labels provided by contributors indicating whether SMS is fraudulent or normal.

## 🔬 Methodology

**Methods**:
- Logistic Regression
- Random Forest
- Support Vector Machine
- Naive Bayes

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- AUC-ROC

**Calculation**: Metrics calculated using predictions from classification algorithms on the datasets.

**Interpretation**: Accuracy reflects the correct classification of SMS messages, while precision and recall indicate the rates of false positives and false negatives.

**Baseline Results**: Best model (Random Forest) achieved 98% accuracy on the Chichewa dataset.

**Validation**: Models validated through a 80:20 training-test split.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided non-personal, non-sensitive SMS messages.

**Compliance With Regulations**: Not Applicable
