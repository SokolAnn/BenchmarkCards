# Evaluating Large Language Models with Grid-Based Game Competitions: An Extensible LLM Benchmark and Leaderboard

## 📊 Benchmark Details

**Name**: Evaluating Large Language Models with Grid-Based Game Competitions: An Extensible LLM Benchmark and Leaderboard

**Overview**: This benchmark introduces a novel and extensible evaluation framework for large language models (LLMs) using grid-based games like Tic-Tac-Toe, Connect Four, and Gomoku, assessing capabilities such as rule comprehension and strategic thinking across diverse prompt types.

**Data Type**: game results and match data in JSON, CSV, TXT, and PNG formats

**Domains**:
- Natural Language Processing
- Game Theory

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- MMLU
- BIG-bench
- TruthfulQA
- HellaSwag

**Resources**:
- [GitHub Repository](https://github.com/research-outcome/LLM-Game-Benchmark/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a framework for evaluating LLMs through dynamic and competitive game scenarios, enhancing understanding of their decision-making and strategic thinking capabilities.

**Target Audience**:
- ML Researchers
- Gaming Enthusiasts
- AI Practitioners

**Tasks**:
- Strategic Decision Making
- Game Playing

**Limitations**: N/A

## 💾 Data

**Source**: Simulated matches among leading LLMs and random players using a web-based game simulation application.

**Size**: 2,310 matches

**Format**: JSON, CSV, TXT, PNG

**Annotation**: Automated recording of match data during simulated games.

## 🔬 Methodology

**Methods**:
- Game simulations
- Leaderboards

**Metrics**:
- Win rates
- Draw rates
- Disqualification rates
- Missed opportunities

**Calculation**: Percentage of wins, draws, and disqualifications computed post-simulation to gauge model performance.

**Interpretation**: Higher win rates and lower disqualification rates indicate better strategic and rule comprehension by LLMs.

**Baseline Results**: Performance of LLMs compared against a random play generator.

**Validation**: Results from multiple matches were aggregated to form a leaderboard.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-source under appropriate licenses, detailed in GitHub repository.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
