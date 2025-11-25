# SimuHome

## 📊 Benchmark Details

**Name**: SimuHome

**Overview**: SimuHome is a benchmark designed to evaluate smart home large language model agents in a time-accelerated environment that simulates smart devices, supporting various user query types and requirements, assessing agent performance in handling latent intents, temporal dependencies, and device constraints.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HomeBench

**Resources**:
- [Resource](https://arxiv.org/abs/2509.24282)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reproducible evaluation framework for smart home agents that interact with dynamically changing environments and to assess their capabilities in handling complex user queries.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Device Control
- Environmental Variable Querying
- Implicit Intent Inference
- Temporal Coordination

**Limitations**: Current models struggle with latent intent inference, live-state verification, and temporal scheduling; GPT-4.1 achieves an overall success rate of 54% across all query types.

## 💾 Data

**Source**: Simulated smart home environment utilizing Matter protocol with various device interactions and environmental variables.

**Size**: 600 episodes

**Format**: JSON

**Annotation**: Manually validated benchmark episodes with feasible and infeasible scenarios.

## 🔬 Methodology

**Methods**:
- Simulator-based evaluation
- LLM-judge-based evaluation

**Metrics**:
- Success Rate

**Calculation**: Evaluation based on comparing final states in the simulator for feasible tasks and logical checks against LLM judges for infeasible tasks.

**Interpretation**: Success rates are derived from comparing the final output states of agents with the desired goals, with respect to time constraints and device conditions.

**Baseline Results**: GPT-4.1 achieved a 54% success rate across all query types.

**Validation**: The benchmark is designed to be fully reproducible and allows stress-testing of agents under various scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Benchmark aims to detect and prevent issues related to latent intent inference and actual state verification during interactions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
