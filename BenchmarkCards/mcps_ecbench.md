# MCPS ECBENCH

## 📊 Benchmark Details

**Name**: MCPS ECBENCH

**Overview**: MCPS ECBENCH is a comprehensive security benchmark and playground that integrates prompt datasets, MCP servers, MCP clients, and attack scripts to evaluate security risks across the Model Context Protocol (MCP) ecosystem.

**Data Type**: prompt datasets, security attack scripts

**Domains**:
- Computer Security

**Languages**:
- English

**Similar Benchmarks**:
- MCIP-Bench
- SafeMCP

**Resources**:
- [GitHub Repository](https://github.com/AIS2Lab/MCPSecBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic and extensible evaluation framework for testing security vulnerabilities in MCP-powered agent systems.

**Target Audience**:
- Security Researchers
- AI Practitioners

**Tasks**:
- Security Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Integrated prompt datasets and security attack scenarios

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Systematic evaluation
- Experimental testing of attack scenarios

**Metrics**:
- Attack Success Rate (ASR)
- Refusal Rate (RR)

**Calculation**: Metrics are calculated as the proportion of successful attempts in the testing of attack scenarios.

**Interpretation**: Higher ASR indicates more successful exploitation of vulnerabilities, while lower RR indicates effective defenses against malicious inputs.

**Baseline Results**: Results show over 85% of identified attacks compromise at least one platform, with core vulnerabilities affecting all tested systems.

**Validation**: Systematic statistical testing performed to assess attack vectors across major MCP hosts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security Risks

**Atlas Risks**:
- **Robustness**: Prompt injection attack
- **Misuse**: Spreading disinformation
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Data leakage', 'Compromised user actions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
