# EMBODIED AGENT INTERFACE

## 📊 Benchmark Details

**Name**: EMBODIED AGENT INTERFACE

**Overview**: The EMBODIED AGENT INTERFACE benchmarks Large Language Models (LLMs) for embodied decision making, addressing limitations in existing evaluations through standardized goal specifications, modular ability interfaces, and comprehensive fine-grained evaluation metrics that break down performance into various error types.

**Data Type**: task trajectories and action sequences

**Domains**:
- Natural Language Processing
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- BEHA VIOR
- VirtualHome

**Resources**:
- [Resource](https://embodied-agent-interface.github.io)
- [GitHub Repository](https://github.com/embodied-agent-interface/embodied-agent-interface)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of LLMs in achieving embodied decision-making tasks through systematic benchmarking.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Robotics Developers

**Tasks**:
- Goal Interpretation
- Action Sequencing
- Subgoal Decomposition
- Transition Modeling

**Limitations**: N/A

## 💾 Data

**Source**: Annotated tasks and trajectories collected from BEHA VIOR and VirtualHome environments.

**Size**: 438 tasks across environments with varying action lengths, including human demonstration videos.

**Format**: JSON

**Annotation**: Annotations were manually curated and verified using simulator evaluations.

## 🔬 Methodology

**Methods**:
- Goal Interpretation
- Action Sequencing
- Subgoal Decomposition
- Transition Modeling

**Metrics**:
- Precision
- Recall
- F1 Score
- Task Success Rate
- Execution Success Rate

**Calculation**: Metrics are calculated based on the accuracy of LLM outputs against ground truth task definitions using supervised learning methods.

**Interpretation**: Higher precision and recall indicate better performance in interpreting and executing tasks.

**Baseline Results**: The highest task success rates observed for EAI on BEHA VIOR tasks using various LLMs.

**Validation**: Comparative evaluation against human performance to validate effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information is included; data is sourced from open-access environments.

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
