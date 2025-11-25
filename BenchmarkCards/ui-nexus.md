# UI-NEXUS

## 📊 Benchmark Details

**Name**: UI-NEXUS

**Overview**: UI-NEXUS is a comprehensive benchmark designed to evaluate mobile agents on three categories of compositional operations: Simple Concatenation, Context Transition, and Deep Dive. It supports interactive evaluation in 20 fully controllable local utility app environments and 30 online Chinese and English service apps.

**Data Type**: interactive task templates

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- AndroidWorld
- Mind2Web

**Resources**:
- [Resource](https://ui-nexus.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate the performance of mobile agents on compositional operation tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Compositional Task Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: 20 local utility apps and 30 online service apps with 100 interactive task templates.

**Size**: 100 task templates

**Format**: N/A

**Annotation**: Task templates are generated through a combination of large language models and human refinement.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Task Success Rate
- Termination Reason
- Inference Cost
- Inference Latency

**Calculation**: Metrics are calculated based on agent performance and task execution outcomes during evaluation.

**Interpretation**: Higher task success rates indicate better performance of the mobile agents.

**Validation**: The benchmark supports both offline evaluations and interactive evaluation environments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
