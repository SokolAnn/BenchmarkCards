# CivSim (Civilization Simulator)

## 📊 Benchmark Details

**Name**: CivSim (Civilization Simulator)

**Overview**: CivSim is a testbed developed for evaluating LLM-based human-like agents in an interactive environment based on the strategy game 'Unciv'. It focuses on enabling researchers to study digital players through simulation of complex decision-making and interactions with human players.

**Data Type**: game state data

**Domains**:
- Artificial Intelligence
- Gaming
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CivRealm

**Resources**:
- [GitHub Repository](https://github.com/fuxiAIlab/CivAgent)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust benchmarking environment for developing and evaluating large language models (LLMs) as human-like agents in the context of strategy gaming.

**Target Audience**:
- AI Researchers
- Game Developers
- Model Developers

**Tasks**:
- Diplomatic Negotiation
- Deception Detection
- Game Strategy Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The data is derived from gameplay in Unciv, including player interactions and decisions made during the game.

**Size**: N/A

**Format**: JSON

**Annotation**: Data is annotated based on gameplay events and outcomes recorded during player interactions.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Player participation evaluation

**Metrics**:
- Score based on civilization performance
- Diplomatic success rates
- Negotiation success rates

**Calculation**: Scores are calculated based on a combination of resources, diplomatic relations, military power, and overall civilization progress as defined in 'Unciv'.

**Interpretation**: Higher scores indicate better performance and strategic planning capabilities of agents within the game framework.

**Baseline Results**: Comparison of CivAgent variants against established performance metrics in the CivSim environment.

**Validation**: The validity of the CivSim benchmark is tested through player trials and detailed evaluation of agent interactions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The project follows MPL-2.0 open-source license.

**Consent Procedures**: Legal consent forms required for user data collection are discussed in the paper.

**Compliance With Regulations**: Not Applicable
