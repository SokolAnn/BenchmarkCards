# EvoCodeBench

## 📊 Benchmark Details

**Name**: EvoCodeBench

**Overview**: EvoCodeBench is a new benchmark for evaluating Large Language Models in code generation, aligning with real-world code repositories and offering comprehensive annotations across multiple dimensions.

**Data Type**: code samples

**Domains**:
- Software Engineering

**Languages**:
- English
- Python

**Similar Benchmarks**:
- HumanEval
- CoNaLa
- MBPP
- APPS
- CoderEval

**Resources**:
- [GitHub Repository](https://github.com/seketeam/EvoCodeBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark that reflects the real-world capabilities of LLMs in code generation tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: EvoCodeBench is currently a monolingual benchmark that primarily focuses on English and Python.

## 💾 Data

**Source**: Collected from 25 real-world open-source repositories on GitHub

**Size**: 275 samples

**Format**: N/A

**Annotation**: Comprehensive annotations including requirements, reference code, and dependencies

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Pass@k
- Recall@k

**Calculation**: Metrics are calculated based on test cases to evaluate functional correctness and dependency invocation.

**Interpretation**: Higher Pass@k and Recall@k values indicate better code generation performance of LLMs.

**Baseline Results**: N/A

**Validation**: Results are validated against real-world code generation tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack, Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All samples have been manually checked to ensure no private information or offensive content is included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
