# This is Not a Dataset

## 📊 Benchmark Details

**Name**: This is Not a Dataset

**Overview**: The largest negation probing dataset, which includes affirmative and negative sentences with and without distractors, incorporating multiple types of relations and negations to improve understanding of negation by large language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hitz-zentroa/This-is-not-a-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: To investigate and improve the understanding of negation in large language models by providing a comprehensive dataset for evaluation.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Negation Understanding

**Limitations**: The dataset contains a limited number of low-quality sentences.

## 💾 Data

**Source**: Generated from WordNet relations.

**Size**: 381,300 sentences

**Format**: N/A

**Annotation**: Semi-automatically generated with human quality assessment.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Coherence

**Calculation**: Accuracy is calculated as (TP + TN) / (TP + TN + FP + FN). Coherence is determined based on the relationship between affirmative and negative sentence labels.

**Interpretation**: A higher accuracy indicates a model's proficiency in understanding the truth values of sentences. Coherence reflects the model's consistency in labeling affirmative and negative pairs correctly.

**Validation**: The dataset's linguistic quality is validated through human evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
