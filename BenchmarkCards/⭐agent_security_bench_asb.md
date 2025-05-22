# Agent Security Bench (ASB)

## 📊 Benchmark Details

**Name**: Agent Security Bench (ASB)

**Overview**: A comprehensive framework designed to formalize, benchmark, and evaluate the attacks and defenses of LLM-based agents, including diverse attack scenarios and evaluation metrics.

**Data Type**: Mixed (Tools and Tasks)

**Domains**:
- e-commerce
- autonomous driving
- finance
- IT management
- medical care
- education
- psychology
- legal advice
- research
- aerospace

**Similar Benchmarks**:
- InjecAgent
- AgentDojo

**Resources**:
- [GitHub Repository](https://github.com/agiresearch/ASB)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the security vulnerabilities of LLM-based agents and benchmark various adversarial attacks and defenses.

**Target Audience**:
- Researchers
- AI practitioners
- Security analysts

**Tasks**:
- Evaluate agent security vulnerabilities
- Benchmark attacks and defenses
- Analyze agent performance in various scenarios

**Limitations**: Focuses primarily on LLM-based agents and their security vulnerabilities, may not encompass all agent types or attacks.

**Out of Scope Uses**:
- Non-LLM agent vulnerabilities
- General AI system assessments

## 💾 Data

**Source**: Agent Security Bench (ASB)

**Size**: Varies based on task and agents used

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Benchmarking of 27 different attack types and defenses on ASB across 13 LLM backbones
- Evaluation through 7 metrics including ASR, RR, PNA, and NRP

**Metrics**:
- Attack success rate (ASR)
- Refusal rate (RR)
- Performance under no attack (PNA)
- Benign performance (BP)
- False negative rate (FNR)
- False positive rate (FPR)
- Net resilient performance (NRP)

**Calculation**: Metrics calculated based on the performance and success of various attacks against LLM agents under controlled conditions.

**Interpretation**: Higher ASR indicates more successful attacks. A lower RR indicates better defenses. NRP assesses usability relative to adversarial success rates.

**Baseline Results**: N/A

**Validation**: Results validated through systematic benchmarking against predefined metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data privacy
- System security vulnerabilities
- Model reliability
- User trust

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy
- **Privacy**: Personal information in data, Data privacy rights alignment, Reidentification
- **Fairness**: Data bias, Output bias, Decision bias
- **Value Alignment**: Improper retraining, Improper data curation, Incomplete advice
- **Robustness**: Prompt injection attack, Evasion attack, Data poisoning
- **Misuse**: Improper usage, Spreading disinformation
- **Governance**: Lack of system transparency, Incomplete usage definition
- **Explainability**: Unexplainable output, Untraceable attribution
- **Societal Impact**: Impact on Jobs, Impact on education: plagiarism

**Demographic Analysis**: N/A

**Potential Harm**: Risk of compromising user data and agent reliability.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data used in benchmarking adheres to privacy and ethical standards.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
