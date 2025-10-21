# CALM (Comprehensive Assessment of Language Models)

## 📊 Benchmark Details

**Name**: CALM (Comprehensive Assessment of Language Models)

**Overview**: CALM is introduced for robust measurement of social biases in language models by utilizing a diverse set of templates generated from existing datasets, covering three NLP tasks: Question Answering, Sentiment Analysis, and Natural Language Inference.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/vipulgupta1011/CALM)

## 🎯 Purpose and Intended Users

**Goal**: To quantify language model bias in a consistent and rigorous manner, focusing on gender and race biases.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Sentiment Analysis
- Natural Language Inference

**Limitations**: The dataset’s target word list is limited to seven social groups in the US and the templates are in English, which may restrict broader bias assessment.

## 💾 Data

**Source**: Derived from sixteen datasets for question-answering, sentiment analysis, and natural language inference.

**Size**: 78,400 prompts

**Format**: N/A

**Annotation**: Templates manually verified and created by replacing names with corresponding tags.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Bias score

**Calculation**: The bias score is calculated as the percentage difference from the baseline performance for each social group.

**Interpretation**: Lower scores indicate less bias; a model with a bias score of 0% is considered unbiased.

**Validation**: Sensitivity analysis conducted to assess the reliability and robustness of the CALM dataset through various perturbations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
