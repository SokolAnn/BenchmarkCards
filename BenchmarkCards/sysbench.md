# SysBench

## 📊 Benchmark Details

**Name**: SysBench

**Overview**: SysBench is a benchmark that systematically analyzes system message following ability in terms of three limitations of existing LLMs: constraint violation, instruction misjudgment, and multi-turn instability. It includes a high-quality dataset consisting of 500 system messages and corresponding user conversations across various domains.

**Data Type**: multi-turn conversation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/PKU-Baichuan-MLSystemLab/SysBench)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the ability of large language models to follow system messages in interactions.

**Target Audience**:
- Researchers
- Developers
- Practitioners in AI

**Tasks**:
- Instruction Following
- Evaluation of Multi-turn Conversations

**Limitations**: N/A

## 💾 Data

**Source**: Manually constructed evaluation dataset based on six prevalent types of constraints, supplemented by expert annotation.

**Size**: 2,500 turns of conversation across 500 system messages

**Format**: N/A

**Annotation**: Manually annotated by trained evaluators according to guidelines designed by experts.

## 🔬 Methodology

**Methods**:
- Model-based evaluation using advanced LLMs as verifiers
- Manual verification with checklists

**Metrics**:
- Constraint Satisfaction Rate (CSR)
- Instruction Satisfaction Rate (ISR)
- Session Stability Rate (SSR)

**Calculation**: Metrics are calculated based on the number of constraints satisfied over total constraints in conversation turns.

**Interpretation**: Higher rates indicate better performance in following instructions and maintaining stability over multi-turn conversations.

**Validation**: Extensive evaluation across 16 popular LLMs to measure performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark aims to assess and improve LLMs' ability to adhere to instructions and reduce risks in practical applications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
