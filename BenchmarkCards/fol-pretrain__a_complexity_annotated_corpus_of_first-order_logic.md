# FOL-Pretrain: A complexity annotated corpus of first-order logic

## 📊 Benchmark Details

**Name**: FOL-Pretrain: A complexity annotated corpus of first-order logic

**Overview**: FOL-Pretrain is a large-scale, fully open, complexity-annotated dataset of first-order logic reasoning traces, designed to analyze algorithmic reasoning in large language models (LLMs). The dataset consists of 3.5 billion tokens, including 8.8 million human-annotated examples and 7.5 million synthetically generated examples.

**Data Type**: first-order logic expressions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LogicBench
- FOLIO

**Resources**:
- [Resource](https://arxiv.org/abs/2505.14932)

## 🎯 Purpose and Intended Users

**Goal**: To provide a scalable, interpretable artifact for studying how large language models learn and generalize symbolic reasoning processes.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Logical Reasoning

**Limitations**: The dataset focuses on first-order logic, which may not capture the full range of reasoning phenomena found in real-world tasks.

## 💾 Data

**Source**: Generated from human-annotated logical forms, symbolic rule generation, and LLM prompting.

**Size**: 3.5 billion tokens

**Format**: N/A

**Annotation**: Includes human curation and algorithmically verified components.

## 🔬 Methodology

**Methods**:
- Evaluation of algorithmic reasoning via logical expressions.
- Token-level evaluation and representation-level probing.

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the model's prediction correctness against ground truth.

**Interpretation**: Results are interpreted based on the accuracy of logical reasoning tasks.

**Baseline Results**: A GPT-2 small model pretrained on the FOL-Pretrain corpus achieved significant performance in logical reasoning tasks.

**Validation**: Results were validated through standard evaluation metrics such as accuracy, and correlated with representational analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: While the dataset is designed to enhance reasoning systems, potential misuse includes generating misleading information.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International License (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
