# Authorship Validation Datasets

## 📊 Benchmark Details

**Name**: Authorship Validation Datasets

**Overview**: This paper presents a collection of new datasets for authorship validation tasks based on the Enron email corpus. These datasets simulate inauthentic messages using both human-written and large language model-generated emails.

**Data Type**: email pairs

**Domains**:
- Natural Language Processing
- Cybersecurity

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/r-dube/bec)

## 🎯 Purpose and Intended Users

**Goal**: To enable real-time detection of impersonation in employment emails by verifying the authorship of email messages.

**Target Audience**:
- ML Researchers
- Cybersecurity Practitioners
- Email Security System Developers

**Tasks**:
- Authorship Validation

**Limitations**: N/A

## 💾 Data

**Source**: Enron email corpus

**Size**: 2,200 emails

**Format**: CSV

**Annotation**: Manually labeled as authentic or inauthentic based on writing style.

## 🔬 Methodology

**Methods**:
- Naive Bayes
- Char-CNN

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Performance metrics calculated based on true positives, false positives, true negatives, and false negatives across different datasets.

**Interpretation**: Accuracy measures the total number of correct predictions while the F1 Score represents the balance between precision and recall.

**Baseline Results**: Naive Bayes achieved a maximum accuracy of 94.59% and an F1 score of 95.13%. Char-CNN achieved a maximum accuracy of 98.92% and an F1 score of 98.59%.

**Validation**: Classifiers were validated using a split of 80:20 for training and testing across the constructed datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
