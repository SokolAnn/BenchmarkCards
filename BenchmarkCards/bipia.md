# BIPIA

## 📊 Benchmark Details

**Name**: BIPIA

**Overview**: The first benchmark for indirect prompt injection attacks to assess the risk of such vulnerabilities in LLMs.

**Data Type**: Text

**Domains**:
- Email QA
- Web QA
- Table QA
- Summarization
- Code QA

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/microsoft/BIPIA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the vulnerabilities of LLMs to indirect prompt injection attacks and develop effective defenses.

**Target Audience**:
- Researchers
- Developers
- Practitioners in AI safety

**Tasks**:
- Evaluate LLMs against indirect prompt injection attacks
- Test defense mechanisms

**Limitations**: Focus on indirect prompt injection attacks; does not cover direct attacks.

## 💾 Data

**Source**: BIPIA dataset

**Size**: 626,250 training prompts, 86,250 test prompts

**Format**: Structured text prompts

**Annotation**: Malicious instructions embedded in external content

## 🔬 Methodology

**Methods**:
- Rule-based evaluation
- LLM-as-judge evaluation
- Adversarial training
- In-context learning

**Metrics**:
- Attack Success Rate (ASR)
- ROUGE-1

**Calculation**: ASR computed based on the ratio of successful attacks to total attacks.

**Interpretation**: Lower ASR indicates better defense against prompt injection attacks.

**Validation**: Tested defenses against original model performance and evaluated through multiple task prompts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Indirect prompt injection attack risks

**Atlas Risks**:
- **Robustness**: Prompt injection attack
- **Accuracy**: Poor model accuracy
- **Governance**: Lack of model transparency

**Potential Harm**: Potential for malicious outputs based on exploited vulnerabilities in LLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Manually reviewed to exclude harmful attacks on personal property and health.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
