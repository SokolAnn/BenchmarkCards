# SuperCLUE-Safety (SC-Safety)

## 📊 Benchmark Details

**Name**: SuperCLUE-Safety (SC-Safety)

**Overview**: SC-Safety is a multi-round adversarial benchmark designed to systematically assess the safety of large language models (LLMs) in Chinese, featuring 4912 open-ended questions across more than 20 safety sub-dimensions. It aims to enhance the testing of models by incorporating multi-round discussions and adversarial interactions, going beyond conventional single-round assessments.

**Data Type**: Questionnaire

**Domains**:
- Natural Language Processing
- Artificial Intelligence

**Languages**:
- Chinese

**Similar Benchmarks**:
- C-Eval
- CLUE
- SafetyBench

**Resources**:
- [Resource](https://www.CLUEbenchmarks.com)

## 🎯 Purpose and Intended Users

**Goal**: To promote collaborative efforts to create safer and more trustworthy large language models (LLMs).

**Target Audience**:
- Researchers
- Developers
- Data Scientists

**Tasks**:
- Assess safety in language models
- Benchmark safety performance

**Limitations**: Performance metrics are limited to the models assessed in the study.

**Out of Scope Uses**:
- Deployment in production without rigorous safety checks

## 💾 Data

**Source**: SC-Safety database

**Size**: 4912 questions

**Format**: Open-ended questions

**Annotation**: Adversarial human-model interactions and multi-turn queries.

## 🔬 Methodology

**Methods**:
- Adversarial Questioning
- Multi-turn Interaction
- Open-ended Evaluation

**Metrics**:
- Safety Score (0-2)
- Comparative performance assessment

**Calculation**: Average safety scores across questions and models.

**Interpretation**: Scores reflect the safety levels of LLM responses under adversarial conditions.

**Baseline Results**: N/A

**Validation**: Empirical evaluation through comparative analysis of model outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Contamination
- Privacy Risks
- Ethical Risks
- Legal Compliance Risks

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Accuracy**: Data contamination, Poor model accuracy
- **Fairness**: Data bias
- **Legal Compliance**: Model usage rights restrictions

**Demographic Analysis**: N/A

**Potential Harm**: Potential harm in generating unsafe or unethical content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy and anonymity of data subjects must be preserved during testing.

**Data Licensing**: Data used in the benchmark is subject to licensing agreements.

**Consent Procedures**: Explicit consent must be obtained from individuals represented in data, if applicable.

**Compliance With Regulations**: Compliance with local regulations regarding data collection and usage.
