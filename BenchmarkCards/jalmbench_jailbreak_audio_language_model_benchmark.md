# JALMBench (Jailbreak Audio Language Model Benchmark)

## 📊 Benchmark Details

**Name**: JALMBench (Jailbreak Audio Language Model Benchmark)

**Overview**: JALMBench is the first comprehensive benchmark to assess the safety of Audio Language Models (ALMs) against jailbreak attacks, including a dataset of 2,200 text samples and 51,381 audio samples totaling over 268 hours, along with support for multiple attack and defense methods.

**Data Type**: text and audio samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AdvBench

**Resources**:
- [Resource](https://huggingface.co/datasets/AnonymousUser000/JALMBench)
- [GitHub Repository](https://github.com/sfofgalaxy/JALMBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized evaluation framework for assessing the safety of Audio Language Models (ALMs) against jailbreak attacks.

**Target Audience**:
- Researchers
- Developers
- Safety Evaluators

**Tasks**:
- Jailbreak Attack Assessment
- Safety Evaluation of ALMs

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from various harmful query methods and generated audio samples.

**Size**: 51,381 audio samples and 2,200 text samples, totaling over 268 hours

**Format**: N/A

**Annotation**: Generated through automated processes and manual selections.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: The ASR is calculated based on the model's response to harmful queries evaluated on a 5-point safety scale.

**Interpretation**: A higher ASR indicates greater vulnerability to jailbreak attacks.

**Baseline Results**: N/A

**Validation**: Evaluated across 12 mainstream ALMs with detailed attack and defense analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Extraction attack, Evasion attack
- **Societal Impact**: Impact on education: bypassing learning, Impact on the environment

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
