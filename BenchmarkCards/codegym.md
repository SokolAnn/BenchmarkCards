# CodeGym

## 📊 Benchmark Details

**Name**: CodeGym

**Overview**: CodeGym is a scalable framework that synthesizes diverse, verifiable, and controllable multi-turn tool-use environments for agent reinforcement learning, enabling LLM agents to explore and master various workflows actively.

**Data Type**: interactive environments for tool-use tasks

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- tau-bench
- ALFWorld
- MMLU-Pro

**Resources**:
- [GitHub Repository](https://github.com/StigLidu/CodeGym)

## 🎯 Purpose and Intended Users

**Goal**: To provide a general-purpose reinforcement learning environment for training tool-augmented large language model agents and to improve their generalization capabilities.

**Target Audience**:
- ML Researchers
- Artificial Intelligence Practitioners

**Tasks**:
- Multi-Turn Tool Use
- Reinforcement Learning

**Limitations**: N/A

## 💾 Data

**Source**: KodCode dataset

**Size**: 80,000 examples

**Format**: N/A

**Annotation**: Automatically generated from coding problems

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Evaluation on benchmark tasks

**Metrics**:
- Accuracy
- Average Reward

**Calculation**: Metrics are calculated based on the completion of tasks and the correctness of the answers submitted by the agents.

**Interpretation**: Higher accuracy and greater population of task completion indicate stronger performance and generalizability of model agents.

**Baseline Results**: The baseline results are demonstrated through improvements in out-of-distribution accuracy for trained models.

**Validation**: Models are validated on held-out OOD benchmarks and in-domain performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack, Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
