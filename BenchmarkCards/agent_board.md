# AGENT BOARD

## 📊 Benchmark Details

**Name**: AGENT BOARD

**Overview**: AGENT BOARD offers a pioneering comprehensive benchmark and open-source evaluation framework tailored to analytical evaluation of LLM agents. It provides a fine-grained progress rate metric and a comprehensive evaluation toolkit for assessing agents in multi-round interactions within partially-observable environments.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hkust-nlp/AgentBoard)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language model agents across diverse scenarios in a unified framework.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Embodied AI
- Game
- Web
- Tool

**Limitations**: N/A

## 💾 Data

**Source**: 1013 exemplary environments across 9 unique tasks designed for multi-turn interaction.

**Size**: 1013 environments

**Format**: JSON

**Annotation**: Manually annotated subgoals verified through multiple stages by human annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Progress Rate
- Success Rate

**Calculation**: Metrics are calculated based on the performance tracking of agents interacting over multiple rounds in diverse environments.

**Interpretation**: Higher progress rates indicate better incremental performance in task completion, while success rates indicate overall task completion.

**Baseline Results**: N/A

**Validation**: Multiple rounds of human verification for annotating subgoals and progress rates.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal information is leaked during evaluation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
