# BanFakeNews-2.0

## 📊 Benchmark Details

**Name**: BanFakeNews-2.0

**Overview**: BanFakeNews-2.0 is a robust dataset to enhance Bangla fake news detection, comprising 60,000 news items (47,000 authentic and 13,000 fake), manually curated across 13 categories, with an independent test set of 1,000 news articles.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Resources**:
- [GitHub Repository](https://github.com/Shibu4064/IndoNLP)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive resource for improving fake news detection in Bangla.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Classification

**Limitations**: The dataset is imbalanced due to insufficient fake news in some categories.

## 💾 Data

**Source**: Manually collected news articles from credible sources and fact-checking platforms.

**Size**: 60,000 examples

**Format**: N/A

**Annotation**: Manually annotated by three evaluators to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Traditional linguistic features extraction
- SVM classification
- Fine-tuning transformer-based models

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated using standard evaluation metrics on validation and test sets.

**Interpretation**: Higher F1 scores indicate better classification performance for fake versus authentic news.

**Baseline Results**: Traditional SVM methods achieved up to 94% F1 score.

**Validation**: Models were validated using a holdout method with a distribution maintained from prior datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
