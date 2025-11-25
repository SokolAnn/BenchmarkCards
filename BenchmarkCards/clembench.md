# clembench

## 📊 Benchmark Details

**Name**: clembench

**Overview**: clembench constitutes a valuable tool for the community for testing chat-optimised LLMs and as an instrument for detailed studies of specific aspects of LLM behaviour.

**Data Type**: game episodes

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- Italian
- Brazilian Portuguese
- Japanese
- Turkish
- Telugu
- Simplified Chinese

**Similar Benchmarks**:
- HELM
- Chatbot arena

**Resources**:
- [GitHub Repository](https://github.com/clembench/)
- [Resource](https://clembench.github.io/leaderboard.html)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate chat-optimised LLMs and provide a framework for investigating multilingual capabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dialogue Games
- Evaluation of Language Models

**Limitations**: N/A

## 💾 Data

**Source**: Generated instances of games from the clemgame framework.

**Size**: 53 models tracked

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Game-specific scoring rules

**Metrics**:
- Quality score ranging from 0 to 100
- Percentage of games played to end

**Calculation**: Overall score is computed by averaging the main metric for each game, then averaging over games.

**Interpretation**: A higher score indicates better performance by the models in the game scenarios.

**Baseline Results**: Rank correlation of 0.71 between previous and current evaluation runs.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
