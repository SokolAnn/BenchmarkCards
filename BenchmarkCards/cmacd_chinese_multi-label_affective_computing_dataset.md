# CMACD (Chinese Multi-label Affective Computing Dataset)

## 📊 Benchmark Details

**Name**: CMACD (Chinese Multi-label Affective Computing Dataset)

**Overview**: The CMACD dataset integrates personality traits with multi-level quantifications of emotion intensity, designed to advance machine recognition of complex human emotions based on data collected from social media users. It is the first dataset to unify personality and emotion within a single framework, specifically for Chinese users.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/yeaso/Chinese-Affective-Computing-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: The primary goal of CMACD is to facilitate research in affective computing by providing a comprehensive dataset that captures the relationship between personality traits (MBTI) and emotions, annotated with intensity levels.

**Target Audience**:
- ML Researchers
- Psychologists
- Domain Experts

**Tasks**:
- Emotion Recognition
- Personality Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from the Weibo platform, integrating users' posts and their self-identified MBTI personality traits.

**Size**: 566,900 posts

**Format**: CSV

**Annotation**: Emotion labels were annotated using the Extended Quantification Network (EQN) framework, capturing multiple emotions and their intensity levels.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Machine learning classification
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Mean accuracy calculated over validation/testing set of models trained on the dataset.

**Interpretation**: An accuracy score closer to 100% indicates better performance, with the BERT model reported achieving significant effectiveness on classification tasks in the evaluation.

**Baseline Results**: BERT achieved an accuracy of 0.9284 in emotion classification and demonstrated competitive performance in personality prediction tasks, with other models varying in effectiveness.

**Validation**: The dataset has been validated using various models including SVM, FastText, and BERT, demonstrating strong utility across multiple classifications.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset has been compiled in strict compliance with user privacy protections, but it still involves research on human personality and emotions.

**Data Licensing**: The data is made available free of charge to researchers with a legitimate need, with an application process through email.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
