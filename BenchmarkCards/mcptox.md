# MCPTox

## 📊 Benchmark Details

**Name**: MCPTox

**Overview**: MCPTox is the first benchmark designed to systematically evaluate Tool Poisoning Attacks within the real-world Model Context Protocol ecosystem. It enables a standardized and realistic evaluation of agent robustness against Tool Poisoning attacks, featuring 1312 malicious test cases generated from 353 authentic tools across 45 live MCP servers.

**Data Type**: test cases with malicious instruction descriptions

**Domains**:
- Computer Security

**Languages**:
- English

**Similar Benchmarks**:
- InjecAgent
- AgentDojo

**Resources**:
- [Resource](https://anonymous.4open.science/r/AAAI26-7C02)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LLM agents' vulnerabilities to Tool Poisoning attacks and to promote the development of safer AI agents.

**Target Audience**:
- ML Researchers
- Security Analysts
- Model Developers

**Tasks**:
- Security Evaluation

**Limitations**: Single-turn interaction; does not model long-term, conversational interactions.

## 💾 Data

**Source**: Data consists of malicious test cases generated using state-of-the-art language models based on tool descriptions from real-world MCP servers.

**Size**: 1,312 test cases

**Format**: N/A

**Annotation**: Generated using semi-automated processes assisted by human verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation in validation

**Metrics**:
- Attack Success Rate (ASR)
- Refused Ratio

**Calculation**: Attack Success Rate is calculated as the number of successful attacks divided by the total number of valid outputs.

**Interpretation**: An ASR approaching 100% indicates a high vulnerability to Tool Poisoning; lower values suggest better resilience.

**Baseline Results**: Highest attack success rate observed was 72.8% for specific LLM models.

**Validation**: Validated against real-world MCP servers ensuring realistic evaluation conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential exfiltration of sensitive information and manipulation of legitimate tool actions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
