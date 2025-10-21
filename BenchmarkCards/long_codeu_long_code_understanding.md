# LONG CODEU (Long Code Understanding)

## 📊 Benchmark Details

**Name**: LONG CODEU (Long Code Understanding)

**Overview**: LONG CODEU is a benchmark designed to evaluate long context language models' (LCLMs) understanding ability of long codes in software engineering. It comprises four aspects: code unit perception, intra-code unit understanding, inter-code unit relation understanding, and long code documentation understanding, along with eight specific tasks.

**Data Type**: code

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RepoQA
- L-Eval
- Long Bench
- SWE-bench
- DevEval

**Resources**:
- [GitHub Repository](https://github.com/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation framework for assessing the long code understanding capabilities of long-context language models.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Code Unit Perception
- Intra-Code Unit Understanding
- Inter-Code Unit Relation Understanding
- Long Documentation Understanding

**Limitations**: The benchmark is currently monolingual and focuses solely on Python code.

## 💾 Data

**Source**: Collected from real-world code repositories on GitHub, created after June 2024.

**Size**: 500 examples per task

**Format**: Code files

**Annotation**: Manually labeled by developers

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Recall
- Precision
- CodeBLEU

**Calculation**: Metrics are calculated based on exact matches and consistency with retrieved outputs.

**Interpretation**: Higher precision and recall indicates better long code understanding capabilities.

**Validation**: Metrics correlate well with human evaluations, demonstrating reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
