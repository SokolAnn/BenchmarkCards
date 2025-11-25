# RSD-15K (A Large-Scale User-Level Annotated Dataset for Suicide Risk Detection on Social Media)

## 📊 Benchmark Details

**Name**: RSD-15K (A Large-Scale User-Level Annotated Dataset for Suicide Risk Detection on Social Media)

**Overview**: This paper introduces a large-scale dataset containing 15,000 user-level posts for suicide risk detection, aiming to support modeling the dynamic evolution of suicide risk and improve the accuracy of risk assessment through rigorous annotations.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Mental Health

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Suicide-DataSet/RSD-15K)

## 🎯 Purpose and Intended Users

**Goal**: To provide a valuable resource for developing predictive models for mental health detection, focusing on suicide risk detection through social media posts.

**Target Audience**:
- ML Researchers
- Mental Health Professionals
- Data Scientists

**Tasks**:
- Risk Assessment
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Data was extracted from the 'r/SuicideWatch' subreddit on Reddit.

**Size**: 15,000 posts

**Format**: N/A

**Annotation**: Multiple rounds of cross-validation under professional guidance were conducted to ensure reliability and consistency of annotations.

## 🔬 Methodology

**Methods**:
- Traditional Machine Learning
- Deep Learning
- Large Language Models

**Metrics**:
- Accuracy
- Macro F1 Score

**Calculation**: Accuracy and F1 Scores calculated based on predictions made by baseline models on the risk assessment task.

**Interpretation**: Higher accuracy and macro F1 Score indicate better model performance in predicting suicide risk.

**Baseline Results**: XGBoost: 42.5% Accuracy, BiLSTM: 48.6% Accuracy, HiGRU: 52.2% Accuracy, RoBERTa: 71.0% Accuracy, DeBERTa: 76.0% Accuracy.

**Validation**: Data was divided into a training set (80%), validation set (10%), and test set (10%) to ensure proper evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness

**Atlas Risks**:
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: This dataset aims to improve suicide detection systems and support individuals in need.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All personal identifiers were removed to ensure users cannot be re-identified from the data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
