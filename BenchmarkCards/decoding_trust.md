# Decoding Trust

## 📊 Benchmark Details

**Name**: Decoding Trust

**Overview**: A comprehensive assessment of trustworthiness in GPT models with a focus on GPT-4 and GPT-3.5, evaluating dimensions such as toxicity, bias, adversarial robustness, out-of-distribution robustness, privacy, machine ethics, and fairness.

**Data Type**: Text

**Domains**:
- Natural Language Processing
- Machine Learning
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- AdvGLUE
- HELM

**Resources**:
- [Resource](https://decodingtrust.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a detailed evaluation of the trustworthiness of GPT models, identifying vulnerabilities and guiding the development of safer AI systems.

**Target Audience**:
- Researchers
- AI practitioners
- Policymakers

**Tasks**:
- Evaluate model toxicity
- Assess stereotype bias
- Measure adversarial robustness
- Analyze out-of-distribution robustness
- Investigate privacy concerns
- Test machine ethics

**Limitations**: Does not cover all potential trustworthiness dimensions for every model and is limited to the versions of GPT assessed.

**Out of Scope Uses**:
- Usage of models for purposes outside of evaluation or training

## 💾 Data

**Source**: Enron Email dataset, manual prompts, and various NLP tasks

**Size**: Approximately 3,300 (name, email) pairs

**Format**: CSV and JSON format

**Annotation**: Manually curated user prompts and tasks designed to elicit model responses.

## 🔬 Methodology

**Methods**:
- Toxicity evaluation using REALTOXICITY PROMPTS
- Stereotype bias analysis via custom datasets
- Adversarial robustness testing using AdvGLUE
- Out-of-distribution robustness evaluation with synthetic transformations
- Privacy leakage assessment during training and inference

**Metrics**:
- Accuracy
- Toxicity probability
- Demographic parity difference
- Equalized odds difference
- False positive rate

**Calculation**: Various statistical methods based on model outputs compared to known labels.

**Interpretation**: Lower scores indicate better performance in terms of fairness and reduced biases.

**Baseline Results**: N/A

**Validation**: Results validated via human annotations and comparison against existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Toxicity
- Adversarial attacks
- Privacy breaches
- Ethics violations

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias, Output bias, Decision bias
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Robustness**: Prompt injection attack, Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Marginalization of specific demographic groups', 'Inadvertent reinforcement of biases', 'Failure to recognize harmful outputs']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Models might leak private information during inference if not properly managed.

**Data Licensing**: Dataset utilized under a standard open access license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
