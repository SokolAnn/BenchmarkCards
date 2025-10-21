# CodeAssistBench (CAB)

## 📊 Benchmark Details

**Name**: CodeAssistBench (CAB)

**Overview**: CodeAssistBench (CAB) is a benchmark framework for evaluating multi-turn programming assistance in realistic settings, using real-world questions derived from GitHub issues to test the capabilities of large language models in programming tasks.

**Data Type**: multi-turn conversation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- InfiBench
- StackEval

**Resources**:
- [Resource](https://anonymous.4open.science/r/CAB-CBA3/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of large language models in providing multi-turn programming assistance based on real-world scenarios.

**Target Audience**:
- ML Researchers
- Model Developers
- Software Engineers

**Tasks**:
- Programming Assistance

**Limitations**: A limited number of programming languages are covered, and it does not currently assess proprietary codebases.

## 💾 Data

**Source**: GitHub issues derived from public repositories.

**Size**: 3,286 multi-turn conversations

**Format**: N/A

**Annotation**: Automatically generated through filtering and structured data extraction methods.

## 🔬 Methodology

**Methods**:
- Automated Dataset Generation
- Simulated User-Agent Interactions
- Multi-Agent Evaluation Framework

**Metrics**:
- Correctness
- Verbosity

**Calculation**: Metrics are calculated based on correctness and appropriateness of responses provided by models.

**Interpretation**: Responses are assessed for correctness in technical answers and overall user satisfaction during interactions.

**Validation**: Evaluation triggered when a user expresses satisfaction or the conversation reaches a maximum of 10 turns.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential risks include reliance on AI suggestions leading to bugs or security issues.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
