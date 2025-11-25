# CASTLE (CWE Automated Security Testing and Low-Level Evaluation)

## 📊 Benchmark Details

**Name**: CASTLE (CWE Automated Security Testing and Low-Level Evaluation)

**Overview**: CASTLE is a benchmarking dataset for evaluating the vulnerability detection capabilities of different methods, assessing 13 static analysis tools, 10 LLMs, and 2 formal verification tools using a hand-crafted dataset of 250 micro-benchmark programs covering 25 common CWEs.

**Data Type**: source code programs

**Domains**:
- Computer Security

**Languages**:
- C

**Similar Benchmarks**:
- SARD
- Big-Vul
- DiverseVul

**Resources**:
- [GitHub Repository](https://github.com/CASTLE-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To enable direct comparisons among current and future vulnerability scanning tools, including traditional static analyzers, formal verification techniques, and LLM-based approaches.

**Target Audience**:
- ML Researchers
- Security Practitioners
- Software Engineers

**Tasks**:
- Vulnerability Detection

**Limitations**: N/A

## 💾 Data

**Source**: Curated collection of compilable C micro-benchmarks, created by cybersecurity experts.

**Size**: 250 programs

**Format**: C source files

**Annotation**: Manually crafted and validated by human experts.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- CASTLE Score

**Calculation**: The CASTLE Score integrates true and false positive rates, awarding bonus points for detecting high-impact vulnerabilities.

**Interpretation**: The score reflects a tool's overall reliability rather than a simple pass/fail assessment.

**Validation**: The dataset was verified through expert validation for accuracy and reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Security

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
