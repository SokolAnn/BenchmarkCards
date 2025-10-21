# BharatBBQ

## 📊 Benchmark Details

**Name**: BharatBBQ

**Overview**: BharatBBQ is a multilingual benchmark designed to systematically evaluate social biases in language models within the Indian context, utilizing a question-answering framework across various social categories.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Hindi
- English
- Marathi
- Bengali
- Tamil
- Telugu
- Odia
- Assamese

**Similar Benchmarks**:
- BBQ

**Resources**:
- [Resource](https://arxiv.org/abs/2508.07090)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of BharatBBQ is to evaluate the presence of biases in multilingual language models, specifically in the Indian context, and to make these evaluations culturally relevant.

**Target Audience**:
- ML Researchers
- AI Developers
- Sociologists

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset has been constructed from culturally adapted templates based on the original Bias Benchmark for Question Answering (BBQ) with additional data collected from community inputs on biases.

**Size**: 392,864 examples

**Format**: N/A

**Annotation**: Templates created through manual verification and adaptation for cultural relevance; translated into multiple languages.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Bias Score (BS)
- Stereotypical Bias Score (SBS)
- Accuracy

**Calculation**: Bias scores and accuracy are computed based on the responses provided by language models to ambiguous and disambiguated contexts in the dataset.

**Interpretation**: Higher bias scores indicate a stronger preference for stereotyped responses, while accuracy reflects the model's capability to handle questions that require contextual understanding.

**Validation**: Templates validated through independent annotator reviews using Cohen’s Kappa score for reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The benchmark captures various demographic biases, reflecting intersectional identities within Indian society.

**Potential Harm**: BharatBBQ aims to identify and mitigate biases in AI systems, promoting fairness without reinforcing harmful stereotypes.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
