# SecLLMHolmes

## 📊 Benchmark Details

**Name**: SecLLMHolmes

**Overview**: SecLLMHolmes is a comprehensive framework designed to evaluate the performance of large language models (LLMs) in identifying and reasoning about software vulnerabilities across eight investigative dimensions using a set of 228 code scenarios.

**Data Type**: code scenarios

**Domains**:
- Computer Science
- Cybersecurity

**Languages**:
- C
- Python

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/ai4cloudops/SecLLMHolmes)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the efficiency and reasoning capabilities of chat-based LLMs for vulnerability detection.

**Target Audience**:
- Researchers
- Security Professionals
- ML Developers

**Tasks**:
- Vulnerability Detection

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from hand-crafted code scenarios, real-world Common Vulnerabilities and Exposures (CVEs), and augmented code scenarios.

**Size**: 228 code scenarios

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated evaluation

**Metrics**:
- Accuracy
- Reasoning Score

**Calculation**: Metrics calculated based on comparison of LLM answers against ground truth labels.

**Interpretation**: Higher scores indicate better performance in detecting security vulnerabilities and providing correct reasoning.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Robustness**: Extraction attack, Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
