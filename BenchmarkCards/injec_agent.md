# INJECAGENT

## 📊 Benchmark Details

**Name**: INJECAGENT

**Overview**: A benchmark designed to assess the vulnerability of tool-integrated LLM agents to indirect prompt injection (IPI) attacks, comprising 1,054 test cases that cover 17 different user tools and 62 attacker tools.

**Data Type**: test cases

**Domains**:
- finance
- smart home devices
- email

**Languages**:
- N/A

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/uiuc-kang-lab/InjecAgent)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and mitigate the risks associated with indirect prompt injection attacks on tool-integrated large language model agents.

**Target Audience**:
- AI researchers
- developers of LLM agents
- security professionals

**Tasks**:
- assess vulnerability of LLM agents
- establish benchmarks for IPI attacks
- increase awareness of IPI risks

**Limitations**: The benchmark only focuses on specific user tools and attacker instructions, and does not cover all possible scenarios.

**Out of Scope Uses**:
- real-time exploitation of vulnerabilities

## 💾 Data

**Source**: INJEC AGENT benchmark dataset

**Size**: 1054 test cases

**Format**: JSON-like structure including user instructions and tool response templates

**Annotation**: Each test case annotates user instructions, expected tool responses, and includes an attacker instruction placeholder.

## 🔬 Methodology

**Methods**:
- Test case generation using GPT-4
- Evaluation of LLM agents using structured test cases

**Metrics**:
- attack success rate (ASR)
- ASR-valid

**Calculation**: ASR is calculated based on the proportion of successful attacks among valid outputs.

**Interpretation**: Higher ASR indicates greater vulnerability to IPI attacks.

**Validation**: The evaluation of LLM agents includes valid output analysis to determine their resilience.

## ⚠️ Targeted Risks

**Risk Categories**:
- Indirect prompt injection
- Data exposure
- Financial loss

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The benchmark exposes potential vulnerabilities but aims to strengthen security against them.

**Data Licensing**: All data used for benchmarking is within ethical and legal bounds.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
