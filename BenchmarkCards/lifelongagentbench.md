# LifelongAgentBench

## 📊 Benchmark Details

**Name**: LifelongAgentBench

**Overview**: LifelongAgentBench is the first unified benchmark designed to systemically assess the lifelong learning ability of LLM agents across diverse interactive environments. The benchmark evaluates agents' abilities to acquire atomic skills, transfer them across tasks, and maintain performance over long sequences of tasks with interdependencies.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AgentBench
- WebArena
- VisualWebArena

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of LifelongAgentBench is to evaluate the lifelong learning capabilities of LLM-based agents, facilitating understanding of their ability to adapt over time in complex environments.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Task Execution
- Skill Transfer Evaluation
- Knowledge Retention Assessment

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark dataset consists of dynamically created tasks in three environments—Database (DB), Operating System (OS), and Knowledge Graph (KG)—designed to simulate complex, evolving scenarios requiring continuous learning.

**Size**: 1,396 tasks

**Format**: CSV

**Annotation**: Automatically verified using SQL query validation, OS state hashing, and SPARQL output verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Task Success Rate

**Calculation**: Measures performance based on the percentage of correctly completed tasks across different environments and configurations.

**Interpretation**: Higher task success rates indicate superior lifelong learning abilities and operational adaptability of LLM agents.

**Baseline Results**: Evaluated across various model backbones including Llama, Qwen, and DeepSeek.

**Validation**: Cross-verified results through extensive experimental trials under controlled conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety
- Privacy
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Diminished model performance due to experience replay complexities and context limitations.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
