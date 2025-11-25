# CausalGraph2LLM

## 📊 Benchmark Details

**Name**: CausalGraph2LLM

**Overview**: CausalGraph2LLM is a comprehensive benchmark comprising over 700k queries across diverse causal graph settings to evaluate the causal reasoning capabilities of LLMs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/ivaxi0s/CausalGraph2LLM)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the ability of LLMs to encode causal graphs and their effectiveness in assisting with causal reasoning tasks.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Causal Reasoning
- Graph-Level Queries
- Node-Level Queries

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic and real-world datasets(Such as Insurance and Alarm causal graphs)

**Size**: 747,754 queries

**Format**: JSON, Adjacency, GraphML, GraphViz, Multi node, Single node

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the correctness of LLM's responses to causal queries.

**Interpretation**: Higher scores indicate better understanding and reasoning capabilities of causal graphs.

**Baseline Results**: N/A

**Validation**: Extensive experiments on various models and encoding strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential biases introduced based on contextual knowledge.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
