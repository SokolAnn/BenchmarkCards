# EAHawk (Email Agent Hijacking Evaluation Framework)

## 📊 Benchmark Details

**Name**: EAHawk (Email Agent Hijacking Evaluation Framework)

**Overview**: EAHawk is an automated pipeline designed to evaluate the Email Agent Hijacking (EAH) attack on LLM email agents, allowing for large-scale assessment of security vulnerabilities in email-based LLM agents.

**Data Type**: email agent instances

**Domains**:
- Natural Language Processing
- Cybersecurity

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/deepset-ai/EAHawk)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation of the security risks associated with LLM email agents through automated testing.

**Target Audience**:
- Cybersecurity Researchers
- Software Developers
- AI Researchers

**Tasks**:
- Email Security Evaluation
- Vulnerability Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Evaluation generated through automated testing on email agent instances derived from LLM frameworks and applications.

**Size**: 1,404 instances

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated testing
- Static analysis
- Dynamic analysis

**Metrics**:
- Attack Success Rate

**Calculation**: Percentage of successful hijacking attempts out of total attempts.

**Interpretation**: Higher success rates indicate greater vulnerability in email agents to hijacking attacks.

**Baseline Results**: 66.20% overall attack success rate across 1,404 instances.

**Validation**: Empirical testing against real-world agent configurations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security
- Privacy

**Atlas Risks**:
- **Privacy**: Data privacy rights alignment
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Data leakage of private user information', 'Compromise of user accounts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Evaluation conducted using controlled accounts without interference with real user data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
