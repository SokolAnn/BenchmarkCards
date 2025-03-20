# Unmasking Contextual Stereotypes: Measuring and Mitigating BERT’s Gender Bias

## 📊 Benchmark Details

**Name**: Unmasking Contextual Stereotypes: Measuring and Mitigating BERT’s Gender Bias

**Overview**: This paper focuses on measuring and mitigating gender bias in BERT by examining associations between gender-denoting target words and names of professions in English and German. The study presents a new Bias Evaluation Corpus with Professions (BEC-Pro) and demonstrates methodologies for assessing and reducing biases.

**Data Type**: corpus

**Domains**:
- Natural Language Processing
- Gender Bias

**Languages**:
- English
- German

**Similar Benchmarks**:
- Equity Evaluation Corpus
- GAP corpus

**Resources**:
- [GitHub Repository](https://github.com/marionbartl/gender-bias-BERT)

## 🎯 Purpose and Intended Users

**Goal**: To measure and mitigate gender bias in BERT and promote fairness in NLP systems.

**Target Audience**:
- Researchers in NLP
- Gender bias scholars
- AI ethics practitioners

**Tasks**:
- Measuring gender bias
- Mitigating gender bias
- Creating bias evaluation datasets

**Limitations**: Focus on gender bias only; binary gender perspective used.

**Out of Scope Uses**:
- Non-gender-related biases
- Bias in other embedding models

## 💾 Data

**Source**: U.S. Bureau of Labor Statistics

**Size**: 5,400 sentences

**Format**: template-based corpus

**Annotation**: Sentences constructed from templates; contains gender-denoting phrases and professional terms.

## 🔬 Methodology

**Methods**:
- Counterfactual Data Substitution (CDS)
- Masked Language Model (MLM) querying

**Metrics**:
- Association scores
- Wilcoxon signed-rank test

**Calculation**: Logarithm of the ratio of target probabilities to prior probabilities.

**Interpretation**: Positive associations reveal bias favoring gender-specific professions.

**Baseline Results**: N/A

**Validation**: Comparison with real-world U.S. workforce statistics

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on Jobs

**Demographic Analysis**: Bias analysis based on gender-specific associations in professions.

**Potential Harm**: ['Reinforcement of stereotypes', 'Inequitable treatment in hiring processes']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data used from publicly available sources, ensuring no personal data breach.

**Data Licensing**: Creative Commons for the dataset.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
