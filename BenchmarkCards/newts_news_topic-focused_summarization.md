# NEWTS (News Topic-Focused Summarization)

## 📊 Benchmark Details

**Name**: NEWTS (News Topic-Focused Summarization)

**Overview**: NEWTS is a specialized dataset designed for topic-focused abstractive summarization, containing 2400 training and 600 test samples from news articles, with each article accompanied by two human-written reference summaries focused on different topics.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate adaptive free-form summarization models and assess the effectiveness of steering vectors in controlling text properties.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Summarization

**Limitations**: High steering strengths can degrade text quality significantly.

## 💾 Data

**Source**: NEWTS dataset based on the CNN/DailyMail dataset

**Size**: 3,000 samples (2,400 training and 600 test)

**Format**: N/A

**Annotation**: Manually annotated summaries

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE Score
- BERTScore
- Perplexity

**Calculation**: Metrics calculated by comparing generated summaries to reference summaries and evaluating linguistic quality.

**Interpretation**: Higher metrics indicate better alignment with human-written references and overall quality.

**Validation**: Evaluation done using both intrinsic quality metrics and extrinsic comparison against reference summaries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
