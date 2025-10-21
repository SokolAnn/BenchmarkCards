# REDDIT ESS (Effective Social Support Interaction Dataset)

## 📊 Benchmark Details

**Name**: REDDIT ESS (Effective Social Support Interaction Dataset)

**Overview**: REDDIT ESS is a novel dataset derived from Reddit posts, including supportive comments and original posters’ follow-up responses, aimed at evaluating multiple dimensions of effective social support in mental health contexts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Emotion Support Conversation (ESConv)

**Resources**:
- [Resource](https://anonymous.4open.science/r/RedditESS-3577)

## 🎯 Purpose and Intended Users

**Goal**: To understand effective social support to refine AI-driven support tools, with an emphasis on analyzing various dimensions of support beyond mere empathy.

**Target Audience**:
- ML Researchers
- Mental Health Professionals
- AI Developers

**Tasks**:
- Support Classification
- Response Generation

**Limitations**: The dataset primarily focuses on edited posts, which may limit its comprehensiveness.

## 💾 Data

**Source**: Reddit posts and comments

**Size**: 59,666 comments linked to 1,689 unique posts

**Format**: JSON

**Annotation**: Annotated by human evaluators using majority consensus for effectiveness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on the proportion of effective social support comments.

**Interpretation**: Comment effectiveness determined by community validation and original poster feedback.

**Baseline Results**: Human annotators agreed with the effective social support label in 94.68% of supportive cases.

**Validation**: Reliability assessed through qualitative evaluations and cross-annotator comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Output bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: Dataset includes diverse user interactions across various mental health-related subreddits.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All personally identifiable information (PII) has been anonymized, and data was collected from publicly available sources.

**Data Licensing**: Not Applicable

**Consent Procedures**: Obtained from publicly available Reddit posts and comments.

**Compliance With Regulations**: Complies with Reddit's data usage policy.
