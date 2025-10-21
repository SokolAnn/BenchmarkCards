# LMRL-Gym: Benchmarks for Multi-Turn Reinforcement Learning

## 📊 Benchmark Details

**Name**: LMRL-Gym: Benchmarks for Multi-Turn Reinforcement Learning

**Overview**: Our paper introduces the LMRL-Gym benchmark for evaluating multi-turn RL for LLMs, consisting of 8 different language tasks that cover a range of tasks in open-ended dialogue and text games and require multiple rounds of language interaction.

**Data Type**: language tasks with multiple turns of interaction

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Dialogue-based RL benchmarks
- Text-based game benchmarks

**Resources**:
- [Resource](https://lmrl-gym.github.io/)
- [GitHub Repository](https://github.com/abdulhaim/LMRL-Gym)

## 🎯 Purpose and Intended Users

**Goal**: To enable RL algorithm researchers to benchmark and iterate on developing better RL methods for multi-turn language-based interaction tasks.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Reinforcement Learning Developers

**Tasks**:
- Multi-Turn Dialogue
- Strategic Decision Making
- Information Gathering
- Negotiation

**Limitations**: The benchmark primarily uses smaller GPT-based LLMs to generate datasets, making it less applicable for larger-scale applications.

## 💾 Data

**Source**: Synthetic datasets generated using LLMs through simulations of conversational interactions and text-based games.

**Size**: 800,000 interactions across 8 different tasks

**Format**: JSON

**Annotation**: Automatically generated from LLM interactions and datasets.

## 🔬 Methodology

**Methods**:
- Online Reinforcement Learning
- Offline Reinforcement Learning
- Behavioral Cloning

**Metrics**:
- Normalized Reward
- Success Rate

**Calculation**: Rewards are calculated based on the performance of agents in completing tasks within defined constraints.

**Interpretation**: Higher rewards indicate better performance in achieving task objectives.

**Baseline Results**: Online PPO consistently outperformed offline value-based methods across various tasks, indicating significant gaps in performance.

**Validation**: Benchmarks validated through systematic tests against multiple RL algorithms.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: Benchmarks incorporate a variety of objects and tasks to ensure a diverse range of interactions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Datasets generated do not contain personally identifiable information as they are fully synthetic.

**Data Licensing**: Open-source with the MIT license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The research follows best practices in data handling and ethical standards.
