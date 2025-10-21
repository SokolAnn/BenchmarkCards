# MIRAGE (MetaInductive ReAsonin G Evaluation)

## 📊 Benchmark Details

**Name**: MIRAGE (MetaInductive ReAsonin G Evaluation)

**Overview**: MIRAGE is a synthetic dataset aimed at evaluating and explaining the inductive reasoning process in large language models (LLMs). It provides both inductive and deductive evaluation tasks, tailored for flexible test data with various forms, distributions, and difficulty levels.

**Data Type**: inductive and deductive evaluation tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ARC
- MiniSCAN
- ListFunctions
- MiniARC
- 1D-ARC
- Case2Code

**Resources**:
- [GitHub Repository](https://github.com/BugMakerzzz/mirage)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate and analyze the inductive reasoning capabilities of large language models (LLMs) through flexible and varied testing scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Rule Induction
- Example Inference

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated based on various vector operations and rules.

**Size**: N/A

**Format**: N/A

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on model performance in the inductive and deductive tasks using synthetic data.

**Interpretation**: A high accuracy rate indicates effective inductive reasoning capabilities, while discrepancies between rule induction and example inference suggest reliance on neighbor-based reasoning.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
