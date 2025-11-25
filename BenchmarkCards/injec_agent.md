# INJEC AGENT

## 📊 Benchmark Details

**Name**: INJEC AGENT

**Overview**: INJEC AGENT is a benchmark designed to assess the vulnerability of tool-integrated LLM agents to indirect prompt injection attacks. It comprises 1,054 test cases covering 17 different user tools and 62 attacker tools.

**Data Type**: test cases

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/uiuc-kang-lab/InjecAgent)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of INJEC AGENT is to evaluate the vulnerability of LLM agents against indirect prompt injection attacks in tool-integrated scenarios.

**Target Audience**:
- ML Researchers
- Security Analysts

**Tasks**:
- Security Assessment
- Vulnerability Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Generated test cases simulating indirect prompt injection scenarios using various tools.

**Size**: 1,054 test cases

**Format**: JSON

**Annotation**: Test cases generated with the assistance of GPT-4 and manually refined for realism and diversity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Attack Success Rate (ASR)
- ASR-valid

**Calculation**: Attack success is calculated based on the proportion of successful manipulations across valid outputs.

**Interpretation**: Higher ASR values indicate greater vulnerability of the LLM agents to indirect prompt injection attacks.

**Baseline Results**: Initial evaluation of various LLM agents showed significant vulnerability to attacks, with the prompted GPT-4 showing a 24% success rate.

**Validation**: The benchmark has been validated through testing various LLM agents across multiple scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The benchmark involves careful handling of personal data during testing to prevent misuse.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
