# CEB (Compositional Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: CEB (Compositional Evaluation Benchmark)

**Overview**: CEB is a Compositional Evaluation Benchmark that evaluates biases in large language models (LLMs) across different social groups and tasks, aiming to provide a comprehensive assessment of fairness and bias.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/SongW-SW/CEB)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CEB is to assess biases in large language models from various perspectives through a comprehensive suite of datasets.

**Target Audience**:
- ML Researchers
- Policy Makers
- Model Developers
- Ethics Boards

**Tasks**:
- Bias Evaluation
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Curated datasets designed for bias evaluation of LLMs covering different social groups (age, gender, race, religion) and various tasks.

**Size**: 11,004 samples

**Format**: Various formats including text and tabular forms as specified in tasks.

**Annotation**: Datasets are constructed from existing datasets with additional samples generated using large language models.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-based evaluation

**Metrics**:
- Micro-F1 Score
- Demographic Parity (DP)
- Equalized Odds (EO)
- Unfairness Score

**Calculation**: Metrics are calculated based on the classification results of bias evaluation across different social groups and bias types.

**Interpretation**: Scores indicate the level of bias, with lower scores indicating better performance (less bias).

**Baseline Results**: N/A

**Validation**: Extensive experiments were conducted to validate the performance of LLMs across various tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Four social groups analyzed: age, gender, race, religion.

**Potential Harm**: ['Reinforcement of existing biases', 'Misinterpretation of evaluation results']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Licensed under the CC License to ensure open-source accessibility.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
