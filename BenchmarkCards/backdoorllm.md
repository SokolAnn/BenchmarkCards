# BackdoorLLM

## 📊 Benchmark Details

**Name**: BackdoorLLM

**Overview**: BackdoorLLM is the first comprehensive benchmark for studying backdoor attacks on Large Language Models (LLMs). It features a repository of backdoor benchmarks with a standardized training pipeline, diverse attack strategies, extensive evaluations, and insights into the effectiveness and limitations of backdoors in LLMs.

**Data Type**: N/A

**Domains**:
- Natural Language Processing
- Machine Learning

**Languages**:
- English

**Similar Benchmarks**:
- BadChain
- BackdoorBench

**Resources**:
- [GitHub Repository](https://github.com/bboylyg/BackdoorLLM)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized framework to study backdoor attacks on LLMs and raise awareness of related security threats.

**Target Audience**:
- Researchers
- AI practitioners
- Safety analysts

**Tasks**:
- Evaluate backdoor attack efficacy
- Develop defense mechanisms against backdoor threats

**Limitations**: N/A

**Out of Scope Uses**:
- N/A

## 💾 Data

**Source**: Stanford Alpaca, AdvBench, math reasoning data, SST-2, AGNews

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Data Poisoning Attacks
- Weight Poisoning Attacks
- Hidden State Attacks
- Chain-of-Thought Attacks

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: ASR is measured for both clean prompts and backdoored prompts.

**Interpretation**: Higher ASR indicates a more effective backdoor attack.

**Validation**: Extensive experiments across 8 backdoor attacks on 7 scenarios and 6 model architectures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data poisoning
- Weight poisoning
- Hidden state manipulation
- Chain-of-thought

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data
- **Misuse**: Spreading disinformation, Dangerous use

**Demographic Analysis**: N/A

**Potential Harm**: Potential for generating harmful outputs based on backdoor triggers.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
