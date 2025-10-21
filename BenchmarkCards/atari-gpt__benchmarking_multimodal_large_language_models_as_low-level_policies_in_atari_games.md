# Atari-GPT: Benchmarking Multimodal Large Language Models as Low-Level Policies in Atari Games

## 📊 Benchmark Details

**Name**: Atari-GPT: Benchmarking Multimodal Large Language Models as Low-Level Policies in Atari Games

**Overview**: This paper introduces a benchmark aimed at testing the emergent capabilities of multimodal LLMs as low-level policies in Atari games.

**Data Type**: game state observations and actions

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://dev1nw.github.io/atari-gpt/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of multimodal LLMs as low-level decision-making agents in Atari games.

**Target Audience**:
- ML Researchers
- Game Developers
- AI Practitioners

**Tasks**:
- Game Playing

**Limitations**: This benchmark does not account for models specifically designed for real-time low-level control tasks.

## 💾 Data

**Source**: Atari game environments from the Arcade Learning Environment (ALE).

**Size**: 7 game environments

**Format**: Game state data

**Annotation**: Automated interaction with game environments based on model-generated actions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Simulation-based evaluation

**Metrics**:
- Game Score
- Visual Understanding Score
- Spatial Reasoning Score
- Strategy Formulation Score

**Calculation**: Metrics are calculated based on the cumulative reward across multiple game episodes.

**Interpretation**: Higher game scores and accuracy in visual and spatial understanding indicate better performance.

**Baseline Results**: Compared LLM performance to human players, random agents, and traditional RL agents.

**Validation**: Performance validation involved assessing model outputs against human-generated evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
