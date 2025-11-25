# Stereotypes in Language Models

## 📊 Benchmark Details

**Name**: Stereotypes in Language Models

**Overview**: This paper presents the first dataset comprising stereotypical attributes of a range of social groups and proposes a method to elicit stereotypes encoded by pretrained language models in an unsupervised manner.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/RochelleChoenni/stereotypes_in_lms)

## 🎯 Purpose and Intended Users

**Goal**: To expose varying implicit stereotypes that different models incorporate and to bring awareness to how quickly attitudes towards groups change based on contextual differences in training data.

**Target Audience**:
- ML Researchers
- Social Psychologists

**Tasks**:
- Bias Detection
- Emotion Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Autocomplete suggestions from search engines

**Size**: Approximately 2,000 stereotypical attributes about 274 social groups

**Format**: N/A

**Annotation**: Automatically retrieved using a search engine's autocomplete feature

## 🔬 Methodology

**Methods**:
- Stereotype elicitation method
- Recall@k evaluation

**Metrics**:
- Recall

**Calculation**: Recall@k is computed as the proportion of retrieved stereotypical attributes that match the attributes in the dataset.

**Interpretation**: Higher recall indicates better performance in retrieving stereotypes encoded by the models.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis of demographic factors and stereotypes associated with specific social groups.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected is publicly available and completely anonymous.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
