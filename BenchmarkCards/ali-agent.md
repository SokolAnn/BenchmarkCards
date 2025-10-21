# ALI-Agent

## 📊 Benchmark Details

**Name**: ALI-Agent

**Overview**: ALI-Agent is an evaluation framework that leverages LLM-powered agents to conduct in-depth and adaptive alignment assessments, automating the generation of test scenarios to probe long-tail risks in large language models (LLMs).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CrowS-Pairs
- ETHICS
- DecodingTrust
- Social Chemistry 101

**Resources**:
- [GitHub Repository](https://github.com/SophieZheng998/ALI-Agent.git)

## 🎯 Purpose and Intended Users

**Goal**: To provide a scalable and adaptable framework for evaluating the alignment of LLMs with human values, focusing on detecting long-tail risks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Bias Detection
- Ethical Evaluation

**Limitations**: Reliance on the capabilities of the core large language model used, which may affect evaluation outcomes.

## 💾 Data

**Source**: Automated generation from existing datasets and user queries, incorporating performance data across multiple LLMs.

**Size**: 11,243 test scenarios

**Format**: N/A

**Annotation**: Test scenarios developed and refined through automated processes, evaluated by human annotators for quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Evaluation through human feedback
- A/B testing

**Metrics**:
- Model agreeability
- Attack success rate (ASR)

**Calculation**: Metrics are computed based on the agreement of the models with test scenarios and their responses to prompts.

**Interpretation**: Higher values in model agreeability indicate greater instances of misalignment.

**Baseline Results**: Performance comparison against existing benchmarks like CrowS-Pairs and ETHICS showed higher misalignment rates with ALI-Agent.

**Validation**: Evaluated through iterative refinements to improve scenario quality and robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: Evaluations conducted included demographic considerations in evaluating biases on scenarios.

**Potential Harm**: The framework aims to identify exposure to misalignments that could perpetuate harmful stereotypes or beliefs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
