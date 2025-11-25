# JailTrickBench

## 📊 Benchmark Details

**Name**: JailTrickBench

**Overview**: JailTrickBench evaluates the impact of various attack settings on LLM performance and provides a baseline for jailbreak attacks, encouraging the adoption of a standardized evaluation framework. It includes comprehensive experiments with numerous jailbreak attack methods against several defense strategies.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- JailbreakBench
- JailBreakV-28K

**Resources**:
- [GitHub Repository](https://github.com/usail-hkust/JailTrickBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized evaluation framework for benchmarking jailbreak attacks on large language models (LLMs).

**Target Audience**:
- ML Researchers
- Security Analysts

**Tasks**:
- Security Evaluation
- Benchmarking

**Limitations**: N/A

## 💾 Data

**Source**: Two widely recognized datasets: AdvBench and MaliciousInstruct, with approximately 520 and 100 examples respectively.

**Size**: 520 examples

**Format**: N/A

**Annotation**: Manual selection and creation of adversarial examples.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Comparative analysis

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: ASR is calculated as the percentage of instructions that are not rejected and are responded to appropriately.

**Interpretation**: Higher ASR indicates more successful jailbreak attacks.

**Baseline Results**: Various baselines established with multiple models under different configurations.

**Validation**: Empirical validation through extensive experimentation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: Standardizes evaluation to prevent safety and security risks in LLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset contains examples representing harmful intents; consent procedures for example generation using GPT-4 mentioned.

**Data Licensing**: Not Applicable

**Consent Procedures**: Observed during the collection of adversarial prompts and responses.

**Compliance With Regulations**: Not Applicable
