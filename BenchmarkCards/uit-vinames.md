# UIT-ViNames

## 📊 Benchmark Details

**Name**: UIT-ViNames

**Overview**: This dataset comprises over 26,850 Vietnamese full names annotated with genders for the purpose of gender prediction based on names.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Vietnamese

**Resources**:
- [Resource](https://sites.google.com/uit.edu.vn/uit-nlp/)

## 🎯 Purpose and Intended Users

**Goal**: To build a dataset for analyzing Vietnamese names for gender prediction using machine learning models.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected from several universities in Vietnam covering a diverse range of names.

**Size**: 26,850 examples

**Format**: N/A

**Annotation**: Annotated with genders: 1 for male and 0 for female.

## 🔬 Methodology

**Methods**:
- Support Vector Machine
- Multinomial Naive Bayes
- Bernoulli Naive Bayes
- Decision Tree
- Random Forest
- Logistic Regression
- Long Short-Term Memory (LSTM)

**Metrics**:
- F1 Score

**Calculation**: Macro average scoring method to calculate F1-score.

**Interpretation**: An F1-score of 96% indicates a high predictive performance on gender detection.

**Validation**: Data was split into training, development, and test sets in a proportion of 70%, 10%, and 20% respectively.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data only contains names and genders, avoiding revealing identities.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
