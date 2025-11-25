# ManyHarm

## 📊 Benchmark Details

**Name**: ManyHarm

**Overview**: ManyHarm is a dataset of 2,400 malicious demonstrations spanning 12 types of harmful behaviors, designed to facilitate research on adversarial techniques in language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AdvBench
- HarmBench

**Resources**:
- [GitHub Repository](https://github.com/averyma/pandas)

## 🎯 Purpose and Intended Users

**Goal**: To improve the understanding and method of jailbreaking language models and to develop a dataset that aids in this process.

**Target Audience**:
- ML Researchers
- Ethicists
- AI Safety Researchers

**Tasks**:
- Adversarial Attacks
- Safety Research

**Limitations**: N/A

## 💾 Data

**Source**: The ManyHarm dataset was created through automated generation and manual curation, designed to encompass unsafe prompts and harmful question-answer pairs.

**Size**: 2,400 examples

**Format**: N/A

**Annotation**: Automated generation followed by manual curation to ensure malicious content.

## 🔬 Methodology

**Methods**:
- Evaluation of attack success rate (ASR) using LLM-based and rule-based methods.

**Metrics**:
- Attack Success Rate (ASR-L)
- Rule-based Attack Success Rate (ASR-R)

**Calculation**: The attack is successful if the response does not include any phrases from a predefined list of refusal phrases.

**Interpretation**: Higher ASR indicates better performance in bypassing model defenses.

**Validation**: Evaluations across various models and datasets to determine robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Spreading disinformation, Improper usage

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data will be released upon request, subject to eligibility review for research purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
