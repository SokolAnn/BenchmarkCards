# HUMVI (HUManitarian Violent Incidents)

## 📊 Benchmark Details

**Name**: HUMVI (HUManitarian Violent Incidents)

**Overview**: This dataset comprises news articles in three languages (English, French, Arabic) containing instances of different types of violent incidents categorized by the humanitarian sector they impact, such as aid security, education, food security, health, and protection.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Humanitarian Aid

**Languages**:
- English
- French
- Arabic

**Similar Benchmarks**:
- HumSet

**Resources**:
- [GitHub Repository](https://github.com/dataminr-ai/humvi-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive multilingual dataset of violent events, labeled by humanitarian experts for relevancy to multiple key humanitarian aid sectors.

**Target Audience**:
- NLP Researchers
- Humanitarian Organizations

**Tasks**:
- Event Detection
- Categorization

**Limitations**: The dataset comes from a limited set of countries and may not be readily extensible to different parts of the world that are not covered.

## 💾 Data

**Source**: News articles collected using NewsAPI, OSAC, and manually curated by Insecurity Insight.

**Size**: 17,497 articles

**Format**: JSON

**Annotation**: Labels were obtained through expert verification from Insecurity Insight.

## 🔬 Methodology

**Methods**:
- Fine-tuned Models
- Zero-shot Learning

**Metrics**:
- F1 Score

**Calculation**: F1 scores are computed for both relevance and category classification tasks.

**Interpretation**: F1 scores in the range of 0.0 to 1.0, where higher scores indicate better performance.

**Baseline Results**: F1 scores for various models on HUMVI-core indicate that fine-tuned transformers perform best.

**Validation**: Models validated with F1 score metrics against labeled datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes multilingual articles but demographic factors are not analyzed.

**Potential Harm**: Potential for misclassification leading to incorrect interpretations of humanitarian aid threats.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from publicly available news articles does not intentionally include PII.

**Data Licensing**: Not Applicable

**Consent Procedures**: No consent required as data is publicly available.

**Compliance With Regulations**: Not Applicable
