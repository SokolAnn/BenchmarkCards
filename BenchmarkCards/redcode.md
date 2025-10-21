# RedCode

## 📊 Benchmark Details

**Name**: RedCode

**Overview**: RedCode is a benchmark for evaluating the safety of code agents in risky code execution and generation, focusing on comprehensive assessments of handling unsafe code.

**Data Type**: code execution prompts, malicious code generation prompts

**Domains**:
- Computer Security

**Languages**:
- Python
- Bash

**Similar Benchmarks**:
- AgentMonitor
- R-judge
- ToolEmu

**Resources**:
- [GitHub Repository](https://github.com/AI-secure/RedCode)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation platform for the safety of code agents, revealing their vulnerabilities in unsafe code execution and generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Security Experts

**Tasks**:
- Malware Generation Evaluation
- Code Execution Safety Evaluation

**Limitations**: Limited to Python and Bash programming languages.

## 💾 Data

**Source**: Constructed from risky scenarios derived from Common Weakness Enumeration (CWE) and previous safety benchmarks.

**Size**: 4,050 testing instances for RedCode-Exec, 160 for RedCode-Gen

**Format**: Python scripts, Bash scripts, natural language text

**Annotation**: Manually curated and semi-automatically generated using LLMs

## 🔬 Methodology

**Methods**:
- Automated metrics
- Custom evaluation scripts

**Metrics**:
- Attack Success Rate
- Rejection Rate
- Execution Failure Rate

**Calculation**: Metrics calculated based on agent responses and the outcomes of executed code.

**Interpretation**: A high rejection rate suggests strong safety awareness, while a high attack success rate indicates vulnerabilities.

**Baseline Results**: Existing code agents evaluated against a set of designed risky scenarios.

**Validation**: Utilized Docker container environments for controlled execution and result analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Security

**Atlas Risks**:
- **Fairness**
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
