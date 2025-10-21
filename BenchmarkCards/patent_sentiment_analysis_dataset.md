# Patent Sentiment Analysis Dataset

## 📊 Benchmark Details

**Name**: Patent Sentiment Analysis Dataset

**Overview**: A novel dataset to train Machine Learning algorithms to automate the highlighting of semantic information in patent documents, aiding patent practitioners in quickly identifying key arguments in inventions.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Renuk9390/Patent_Sentiment_Analysis)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that assists in the automatic highlighting of important text in patent documents for patent analysis.

**Target Audience**:
- Patent Practitioners
- Machine Learning Researchers

**Tasks**:
- Text Annotation
- Semantic Highlighting

**Limitations**: N/A

## 💾 Data

**Source**: USPTO patents spanning over a decade extracted from XML files

**Size**: 150,000 samples

**Format**: CSV

**Annotation**: Manually labeled and classified into three categories: positive, negative, and neutral

## 🔬 Methodology

**Methods**:
- Machine Learning Classifiers
- Random Forest Classifier
- Logistic Regression
- Support Vector Classifier
- Naive Bayes

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated using standard classification evaluation on test data.

**Interpretation**: Higher precision, recall, and F1 scores indicate better model performance for identifying relevant patent text.

**Baseline Results**: NBSVM model achieved a highest F1 score of 97% for one class.

**Validation**: 5-fold cross-validation used to validate model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
