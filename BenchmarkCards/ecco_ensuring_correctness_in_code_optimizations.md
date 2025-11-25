# ECCO (Ensuring Correctness in Code Optimizations)

## 📊 Benchmark Details

**Name**: ECCO (Ensuring Correctness in Code Optimizations)

**Overview**: ECCO is a reproducible benchmark for evaluating program efficiency via two paradigms: natural language-based code generation and history-based code editing. It supports evaluations in terms of execution correctness, runtime efficiency, and memory efficiency.

**Data Type**: Python code pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Python

**Resources**:
- [GitHub Repository](https://github.com/CodeEff/ECCO)

## 🎯 Purpose and Intended Users

**Goal**: To provide a solid testbed for program optimization and facilitate research in LLM-based generation of efficient code.

**Target Audience**:
- ML Researchers
- Software Developers
- Industry Practitioners

**Tasks**:
- Code Optimization
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from the IBM CodeNet dataset containing competitive programming problems.

**Size**: 50,000 Python solution pairs across 1,380 competitive programming problems

**Format**: Pairs of Python code solutions

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Execution feedback
- Natural Language feedback

**Metrics**:
- Pass@1
- Runtime Efficiency
- Memory Efficiency

**Calculation**: Performance metrics are calculated based on execution results from an isolated environment ensuring reproducibility.

**Interpretation**: Higher pass@1 indicates better functional correctness, while runtime and memory efficiency metrics indicate performance improvements.

**Baseline Results**: N/A

**Validation**: Results validated through execution over a cloud-hosted code execution platform.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Prompt injection attack, Evasion attack
- **Fairness**: Data bias, Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
