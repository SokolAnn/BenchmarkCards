# Orak

## 📊 Benchmark Details

**Name**: Orak

**Overview**: Orak is a foundational benchmark for training and evaluating LLM agents across diverse video games, focusing on 12 popular titles from various genres.

**Data Type**: gameplay trajectories

**Domains**:
- Gaming

**Languages**:
- English

**Similar Benchmarks**:
- GAMA-bench
- GameBench
- GameArena
- SmartPlay
- Balrog
- DSGBench
- LMGame-Bench

**Resources**:
- [GitHub Repository](https://github.com/krafton-ai/Orak)

## 🎯 Purpose and Intended Users

**Goal**: Establish a foundation for building gaming agents and evaluate LLMs on realistic decision-making tasks.

**Target Audience**:
- ML Researchers
- Game Developers
- AI Practitioners

**Tasks**:
- Game Interaction
- Agent Evaluation
- Performance Benchmarking

**Limitations**: N/A

## 💾 Data

**Source**: Expert LLM gameplay trajectories across 12 popular video games

**Size**: 11,000 examples

**Format**: JSON

**Annotation**: Automatically generated from gameplay experiences

## 🔬 Methodology

**Methods**:
- Automated metrics
- Game score evaluations
- Agent performance analysis

**Metrics**:
- Game Leaderboards
- Win Rates
- Performance Scores

**Calculation**: Scores are calculated based on gameplay metrics and interactions with the game environment.

**Interpretation**: Higher scores indicate better agent performance and more effective gameplay strategies.

**Baseline Results**: N/A

**Validation**: Extensive experiments conducted across diverse games with various LLMs to validate effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: The benchmark includes various demographics through the selection of diverse games, ensuring a wide representation of gameplay experiences.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Users must purchase commercial games for evaluation and must not redistribute any game assets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
