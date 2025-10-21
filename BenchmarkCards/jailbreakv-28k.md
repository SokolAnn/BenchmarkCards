# JailBreakV-28K

## 📊 Benchmark Details

**Name**: JailBreakV-28K

**Overview**: JailBreakV-28K is a comprehensive benchmark designed to evaluate the transferability of LLM jailbreak attacks to MLLMs and assess the robustness and safety of MLLMs against diverse jailbreak attacks.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SafeBench
- MM-SafetyBench

**Resources**:
- [Resource](https://eddyluo1232.github.io/JailBreakV28K/)
- [Resource](https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k)

## 🎯 Purpose and Intended Users

**Goal**: To investigate whether techniques that successfully jailbreak Large Language Models (LLMs) can effectively jailbreak Multimodal Large Language Models (MLLMs) and evaluate their robustness against various jailbreak attacks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Robustness Assessment
- Vulnerability Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Generated from a combination of pre-existing datasets and newly curated malicious queries.

**Size**: 28,000 examples

**Format**: N/A

**Annotation**: Manual annotation and synthesis of malicious queries.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: ASR is defined as the number of successful jailbreak attempts divided by the total number of attempts.

**Interpretation**: Higher ASR indicates a greater vulnerability of the MLLMs to jailbreak attacks.

**Baseline Results**: The average ASR of jailbreak prompts across various models revealed significant vulnerabilities.

**Validation**: Evaluation of the ASR across 10 different MLLMs against the JailBreakV-28K dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Safety

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
