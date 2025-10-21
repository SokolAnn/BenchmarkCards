# Greatest Good Benchmark (GGB)

## 📊 Benchmark Details

**Name**: Greatest Good Benchmark (GGB)

**Overview**: The GGB is a novel framework designed to evaluate the moral judgments of Large Language Models (LLMs) by adapting the Oxford Utilitarianism Scale (OUS) and incorporates an extended dataset that is ten times larger than the original. It allows for direct comparison between the moral preferences of LLMs and humans.

**Data Type**: utilitarian moral dilemmas

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/noehsueh/greatest-good-benchmarkevaluation)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' moral judgments using utilitarian dilemmas and provide insights into their alignment with human moral values.

**Target Audience**:
- ML Researchers
- Model Developers
- Ethics Researchers

**Tasks**:
- Moral Reasoning Evaluation

**Limitations**: The benchmark primarily uses English and may not be representative of all languages or populations.

## 💾 Data

**Source**: Synthetic dataset derived from the Oxford Utilitarianism Scale (OUS), expanded with expert involvement.

**Size**: 5940 prompts generated across multiple variations and statements

**Format**: JSON

**Annotation**: Expert evaluation and synthetic creation of moral dilemma statements.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated modeling tests

**Metrics**:
- Statistical significance tests
- Effect sizes

**Calculation**: Responses averaged across multiple variations of moral dilemma prompts to gauge consistency.

**Interpretation**: Responses are interpreted based on mean values in comparison to human lay population standards.

**Validation**: Models were evaluated based on consistency of moral preferences across multiple prompts and iterations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Future research could include analysis across different demographics and languages.

**Potential Harm**: Potentially biased moral judgments reflected in model training data.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal data from individuals were used; scenarios analyzed are fictional.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
