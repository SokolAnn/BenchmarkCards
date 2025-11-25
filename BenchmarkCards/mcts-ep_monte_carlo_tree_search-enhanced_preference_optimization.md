# MCTS-EP (Monte Carlo Tree Search-Enhanced Preference Optimization)

## 📊 Benchmark Details

**Name**: MCTS-EP (Monte Carlo Tree Search-Enhanced Preference Optimization)

**Overview**: MCTS-EP is an online learning framework that integrates large language models with Monte Carlo Tree Search for training embodied agents, emphasizing efficient preference data collection and multi-modal reasoning.

**Data Type**: preference pairs and success trajectories

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ALFWorld
- WebShop

**Resources**:
- [GitHub Repository](https://github.com/xuhang-2/Embodied-Agent-Planning)

## 🎯 Purpose and Intended Users

**Goal**: To provide an online framework that generates preference data and trains embodied agents efficiently in interactive environments.

**Target Audience**:
- ML Researchers
- Robotics Researchers

**Tasks**:
- Embodied Planning
- Multi-Modal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: ALFWorld and WebShop environments for benchmark testing.

**Size**: N/A

**Format**: N/A

**Annotation**: Preference data collected from Monte Carlo Tree Search.

## 🔬 Methodology

**Methods**:
- Monte Carlo Tree Search
- Preference Optimization
- Imitation Learning

**Metrics**:
- Success Rate
- Average Reward
- Average Interaction Steps

**Calculation**: Success rate is calculated as the percentage of tasks completed successfully.

**Interpretation**: A higher success rate and lower average interaction steps indicate better performance.

**Baseline Results**: MCTS-EP achieved 92% success rate in ALFWorld and 0.81 average reward in WebShop.

**Validation**: MCTS-EP evaluated against several state-of-the-art methods across different benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
