# GAME BENCH

## 📊 Benchmark Details

**Name**: GAME BENCH

**Overview**: GAME BENCH is a cross-domain benchmark for evaluating strategic reasoning abilities of LLM agents across various games, focusing on the strengths of reasoning skills identified in strategy games.

**Data Type**: game states and actions

**Domains**:
- Artificial Intelligence
- Game Theory
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Joshuaclymer/GameBench)

## 🎯 Purpose and Intended Users

**Goal**: To measure the strategic reasoning abilities of LLM agents in diverse game environments.

**Target Audience**:
- ML Researchers
- Game Developers
- AI Practitioners

**Tasks**:
- Strategic Reasoning in Games
- Multi-Agent Interaction

**Limitations**: N/A

## 💾 Data

**Source**: Games played between LLM agents and human agents as described in the benchmark.

**Size**: N/A

**Format**: JSON

**Annotation**: Game interactions and match results annotated by agent performances.

## 🔬 Methodology

**Methods**:
- Automated metrics via agent ratings
- Human evaluation

**Metrics**:
- Ratings based on the exponential Bradley-Terry model
- Win probabilities

**Calculation**: Weights among matches are calculated inversely to the number of matches per game, applying a bootstrapped sampling method for pairwise comparisons.

**Interpretation**: Higher ratings indicate better strategic reasoning ability.

**Baseline Results**: Human performance serves as the upper baseline, with models compared against each other and random action baseline.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential for advances in strategic reasoning capability leading to misuse or harmful AI applications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data available under CC-BY 4.0 License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
