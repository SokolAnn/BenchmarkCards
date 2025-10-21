# Moderating Harm: Benchmarking Large Language Models for Cyberbullying Detection in YouTube

## 📊 Benchmark Details

**Name**: Moderating Harm: Benchmarking Large Language Models for Cyberbullying Detection in YouTube

**Overview**: This study benchmarks three state-of-the-art large language models on a corpus of 5,080 YouTube comments drawn from high-abuse videos in various domains, to detect cyberbullying and harassment.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Arabic
- Indonesian

**Similar Benchmarks**:
- OLID
- HateCheck

**Resources**:
- [GitHub Repository](https://github.com/Ammce/papers/tree/main/llm-cyberbullying-moderation)

## 🎯 Purpose and Intended Users

**Goal**: To compare the performance of advanced large language models in detecting cyberbullying within real YouTube comments.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Content Moderation Developers

**Tasks**:
- Cyberbullying Detection

**Limitations**: N/A

## 💾 Data

**Source**: YouTube Data API

**Size**: 5,080 comments

**Format**: N/A

**Annotation**: Manually annotated by reviewers using a binary rubric for harmful and non-harmful comments.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on true positives, true negatives, false positives, and false negatives of model predictions compared to ground truth.

**Interpretation**: Precision and recall provide insights into the model's effectiveness in detecting harmful comments, with an F1 Score balancing the two.

**Baseline Results**: Benchmarks include macro-F1 scores from previous models like BERT-base fine-tuned on HateXplain.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Cyberbullying', 'Hate speech']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All user identifiers and personally identifiable details were removed or replaced with placeholders to mitigate re-identification risk.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
