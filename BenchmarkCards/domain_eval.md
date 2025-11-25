# DOMAIN EVAL

## 📊 Benchmark Details

**Name**: DOMAIN EVAL

**Overview**: DOMAIN EVAL is a multi-domain code generation benchmark designed to evaluate LLMs' coding capabilities thoroughly across six domains, providing insights into their strengths and weaknesses.

**Data Type**: code generation subjects

**Domains**:
- Computer Science

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- MBPP

**Resources**:
- [Resource](https://domaineval.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for comparing and assessing the code generation abilities of LLMs in various coding domains.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from GitHub repositories focusing on various coding domains

**Size**: 2,454 subjects and 5,892 test cases

**Format**: N/A

**Annotation**: Automated generation of test cases and subjects from code repositories

## 🔬 Methodology

**Methods**:
- Automated metric evaluation
- Test-guided construction

**Metrics**:
- Pass@1
- Pass@5

**Calculation**: The metrics are calculated based on the accuracy of generated code against test cases.

**Interpretation**: Higher Pass@k scores indicate better code generation capabilities of the LLMs.

**Baseline Results**: N/A

**Validation**: Evaluated against 12 representative LLMs

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
