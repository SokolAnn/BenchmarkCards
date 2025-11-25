# SafeRAG (Security in Retrieval-Augmented Generation)

## 📊 Benchmark Details

**Name**: SafeRAG (Security in Retrieval-Augmented Generation)

**Overview**: The SafeRAG benchmark evaluates the security vulnerabilities of retrieval-augmented generation (RAG) components against various data injection attacks, including noise, inter-context conflict, toxicity, and denial-of-service (DoS) attacks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/IAAR-Shanghai/SafeRAG)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation of the security of RAG systems against data injection attacks, identifying vulnerabilities and assessing the effectiveness of existing safety mechanisms.

**Target Audience**:
- ML Researchers
- Security Analysts
- Model Developers

**Tasks**:
- Security Evaluation
- Adversarial Testing

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from news articles and expert annotations

**Size**: 100 unique question-context pairs

**Format**: JSON

**Annotation**: Manually annotated by experts with LLM assistance

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Attack Success Rate (ASR)
- F1 Score
- Retrieval Accuracy (RA)

**Calculation**: Metrics are computed based on the performance of RAG systems in responding to attack-injected contexts compared to golden contexts.

**Interpretation**: Higher ASR indicates vulnerabilities while higher F1 scores reflect better defensive capabilities against attacks.

**Validation**: Experiments conducted using 14 representative RAG components against various injection attack scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security
- Safety
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack, Data poisoning
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not collect or use personally identifiable information (PII).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
