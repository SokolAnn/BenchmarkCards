# Camouflaged Jailbreak Prompts

## 📊 Benchmark Details

**Name**: Camouflaged Jailbreak Prompts

**Overview**: This paper introduces the Camouflaged Jailbreak Prompts dataset, containing 500 curated examples (400 harmful and 100 benign prompts) designed to rigorously stress-test LLM safety protocols against sophisticated jailbreaking attempts that conceal malicious intent within seemingly benign language.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AdvBench
- JailbreakBench
- HarmBench
- SafetyBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To assess extreme jailbreak vulnerabilities in large language models and improve LLM safety protocols.

**Target Audience**:
- Researchers
- AI Safety Developers

**Tasks**:
- Threat Assessment
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Curated dataset of prompts specifically designed to assess LLM vulnerabilities in technical domains.

**Size**: 500 examples

**Format**: N/A

**Annotation**: Curated and annotated by researchers for harmfulness and benignness.

## 🔬 Methodology

**Methods**:
- Evaluation against Benchmarks
- Metrics Evaluation using Judge LLM

**Metrics**:
- Safety Awareness
- Technical Feasibility
- Implementation Safeguards
- Harmful Potential
- Educational Value
- Content Quality
- Compliance Score

**Calculation**: Scores are calculated on a scale of 0-20 across each dimension, indicating the safety performance of LLMs against the prompts.

**Interpretation**: Higher scores indicate better model adherence to safety protocols and ethical considerations.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Security Vulnerabilities
- Robustness
- Ethics

**Atlas Risks**:
- **Robustness**: Prompt injection attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
