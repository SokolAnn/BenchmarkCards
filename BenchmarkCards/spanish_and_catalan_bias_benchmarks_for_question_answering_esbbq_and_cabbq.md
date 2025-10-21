# Spanish and Catalan Bias Benchmarks for Question Answering (ESBBQ and CABBQ)

## 📊 Benchmark Details

**Name**: Spanish and Catalan Bias Benchmarks for Question Answering (ESBBQ and CABBQ)

**Overview**: The Spanish and Catalan Bias Benchmarks for Question Answering (ESBBQ and CABBQ) are designed to assess social bias across 10 categories using a multiple-choice QA setting, adapted to the Spanish and Catalan languages and the social context of Spain.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Spanish
- Catalan

**Similar Benchmarks**:
- BBQ (Bias Benchmark for Question Answering)

**Resources**:
- [Resource](https://huggingface.co/datasets/BSC-LT/EsBBQ)
- [Resource](https://huggingface.co/datasets/BSC-LT/CaBBQ)
- [GitHub Repository](https://github.com/langtech-bsc/EsBBQ-CaBBQ)

## 🎯 Purpose and Intended Users

**Goal**: To provide benchmarks for assessing social biases in the Spanish and Catalan context through a Question Answering task.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: Focus on stereotyping social biases; does not encompass all forms of social bias.

## 💾 Data

**Source**: Generated from manually adapted templates based on the original BBQ dataset, validated by a public survey.

**Size**: 27,320 instances

**Format**: JSON

**Annotation**: Manually annotated

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- Bias Score (for assessing reliance on social biases)

**Calculation**: Accuracy calculated based on the proportion of correct answers, while Bias Score determined by comparing prediction frequencies of stereotypical versus anti-stereotypical responses.

**Interpretation**: A higher bias score indicates greater reliance on social bias; ideal models have high accuracy with low bias scores.

**Baseline Results**: Results of various LLMs evaluated on both ambiguous and disambiguated contexts, with observed trends in bias correlation.

**Validation**: Validated through performance measurements on multiple LLMs and analysis of model outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis of stereotypes included in the data based on a public survey reflecting the demographics of the Spanish population.

**Potential Harm**: Evaluating and potentially reinforcing stereotypes affecting marginalized communities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected through a public survey with GDPR compliance; no personal identifiers retained.

**Data Licensing**: Publicly available under an open license.

**Consent Procedures**: Participation in the survey was voluntary; consent was obtained through information provided pre-survey.

**Compliance With Regulations**: Acknowledges handling of sensitive data following legal standards.
