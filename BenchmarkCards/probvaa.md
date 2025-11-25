# ProbVAA

## 📊 Benchmark Details

**Name**: ProbVAA

**Overview**: ProbVAA is a dataset with statements on policy measures from seven EU countries, designed to assess the reliability and consistency of LLMs' stances on political statements.

**Data Type**: statement pairs with policy annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Polish
- Hungarian
- German
- Dutch
- Italian
- Spanish

**Resources**:
- [GitHub Repository](https://github.com/tceron/eval_political_worldviews)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the political biases of large language models (LLMs) and assess their reliability in answering political statements based on a robust testing methodology.

**Target Audience**:
- ML Researchers
- Political Scientists
- NLP Practitioners

**Tasks**:
- Bias Evaluation
- Political Stance Detection

**Limitations**: The dataset is limited to statements from European countries and translated to English, which may not represent global political perspectives.

## 💾 Data

**Source**: Political voting advice applications (VAAs) from seven EU countries.

**Size**: 1434 statements

**Format**: CSV

**Annotation**: Statements were annotated for policy issues with high inter-annotator agreement.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Response sampling
- Psychometric testing

**Metrics**:
- Confidence intervals
- Cohen's kappa

**Calculation**: Metrics are calculated based on variances in model outputs across different prompt variations and response tests.

**Interpretation**: A reliable model should yield consistent answers across variants of the same statement.

**Baseline Results**: Baseline established using responses from models with increasing parameter counts showing reliability improvements.

**Validation**: The dataset and methodology underwent rigorous testing for reliability across differing statement formats.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Prompt injection attack, Evasion attack

**Demographic Analysis**: The dataset includes political statement responses from multiple demographic backgrounds across seven countries.

**Potential Harm**: The dataset poses risks of reinforcing political biases, potentially skewing perceptions of political stances.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
