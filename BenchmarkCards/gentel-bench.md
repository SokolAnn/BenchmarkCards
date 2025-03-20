# GenTel-Bench

## 📊 Benchmark Details

**Name**: GenTel-Bench

**Overview**: A comprehensive evaluation benchmark designed to assess safeguarding techniques for detecting prompt injection attacks in large language models.

**Data Type**: text

**Domains**:
- chatbot
- content generation and curation
- language translation
- code generation
- sentiment analysis and market insights
- detecting and preventing cyber attacks
- education
- storytelling
- sales automation
- HR recruitment and candidate screening

**Languages**:
- English
- Chinese
- Japanese
- French
- Spanish
- German

**Similar Benchmarks**:
- ToxicChat
- Adversarial Prompt Shield
- Jailbreak-LLM
- Deita

**Resources**:
- [Resource](https://gentellab.github.io/gentel-safe.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified framework for defending against prompt injection attacks and comprehensive evaluation benchmarks.

**Target Audience**:
- Researchers
- AI developers
- Security practitioners

**Tasks**:
- Evaluate attack detection methods
- Develop robust safeguards
- Benchmark performance against prompt injection attacks

**Limitations**: N/A

**Out of Scope Uses**:
- Personal use not aligned with research
- Commercial exploitation of the tool without authorization

## 💾 Data

**Source**: Combined from public platforms and established datasets for LLM applications.

**Size**: Over 170,000 data points comprising benign samples and 84,812 prompt injection attacks.

**Format**: text

**Annotation**: Data has been labeled as harmful injection attack samples and benign samples by domain experts.

## 🔬 Methodology

**Methods**:
- Data augmentation
- Binary classification
- Model training using multilingual E5 text embedding models

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 score

**Calculation**: Standard classification metrics calculated to evaluate the model's performance.

**Interpretation**: Performance metrics indicate the effectiveness of prompt injection detection against various attack types.

**Baseline Results**: N/A

**Validation**: Empirical testing against various existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Prompt Injection Attacks
- Data Privacy Breaches
- Misuse of AI Technology

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Extraction attack, Evasion attack, Prompt leaking, Data poisoning, Hallucination
- **Societal Impact**: Impact on cultural diversity, Impact on education: plagiarism, Impact on Jobs, Impact on affected communities, Impact on education: bypassing learning, Impact on the environment, Human exploitation, Impact on human agency
- **Privacy**: Personal information in data, Data privacy rights alignment, Reidentification, Membership inference attack, Attribute inference attack, Personal information in prompt, Exposing personal information
- **Fairness**: Data bias, Output bias, Decision bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Reputational damage due to harmful outputs', 'Legal implications from misuse', 'Ethical concerns surrounding technology deployment']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Prompt injection attacks may expose sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
