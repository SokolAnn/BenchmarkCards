# BanditBench

## 📊 Benchmark Details

**Name**: BanditBench

**Overview**: BanditBench is a comprehensive suite designed for evaluating the decision-making capabilities of large language models (LLMs) in both multi-armed bandit (MAB) and contextual bandit (CB) settings, assessing their in-context exploration abilities and performance across varied tasks with differing complexities.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/allenanie/EVOLvE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the in-context exploration capabilities of large language models through structured bandit environments.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Decision Making
- Reinforcement Learning

**Limitations**: N/A

## 💾 Data

**Source**: Comprehensive suite of multi-armed bandit (MAB) and contextual bandit (CB) environments

**Size**: Variable based on task configurations

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- A/B testing

**Metrics**:
- Win-rate
- Cumulative reward

**Calculation**: Performance measured based on the win-rate of various LLMs across 16 configurations for MAB and 2 configurations for CB, comparing metrics such as cumulative rewards obtained over multiple trials.

**Interpretation**: Models are compared based on their cumulative reward performance across different tasks and configurations.

**Validation**: 30 independent runs for statistical significance on each experimental setup.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
