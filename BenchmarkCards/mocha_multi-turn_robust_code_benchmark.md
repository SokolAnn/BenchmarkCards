# MOCHA (Multi-turn Robust Code Benchmark)

## 📊 Benchmark Details

**Name**: MOCHA (Multi-turn Robust Code Benchmark)

**Overview**: MOCHA is a comprehensive benchmark for evaluating the robustness of code LLMs against multi-turn malicious coding prompts, focusing on vulnerabilities of models when faced with sophisticated adversarial attacks that decompose malicious tasks into seemingly benign subtasks.

**Data Type**: malicious coding prompts

**Domains**:
- Computer Security

**Languages**:
- English

**Similar Benchmarks**:
- ADVBENCH
- HARMBENCH
- REDCODE

**Resources**:
- [GitHub Repository](https://github.com/purpcode-uiuc/mocha)
- [Resource](https://huggingface.co/purpcode)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation benchmark for the robustness of code language models against adversarial and malicious prompts, particularly focusing on multi-turn interactions.

**Target Audience**:
- Cybersecurity Researchers
- Machine Learning Practitioners
- LLM Developers

**Tasks**:
- Code Generation
- Malicious Prompt Detection

**Limitations**: N/A

## 💾 Data

**Source**: Generated through a combination of language models and synthesized prompt engineering techniques.

**Size**: 10,084 training samples, 200 validation prompts, 200 test samples

**Format**: JSON

**Annotation**: Manually verified for malicious intent and categorized based on threat types.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Adversarial evaluation

**Metrics**:
- Rejection Rate (RR)
- Pass@1

**Calculation**: Metrics are calculated based on the performance of models against adversarial prompts during evaluation.

**Interpretation**: Higher rejection rates indicate better robustness to malicious prompts.

**Validation**: Dataset validated through manual review of sample prompts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Security

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Research-Only License (CC BY-NC 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
