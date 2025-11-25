# FAIRGAMER

## 📊 Benchmark Details

**Name**: FAIRGAMER

**Overview**: FAIRGAMER is the first bias evaluation benchmark for LLMs in video game scenarios, designed to evaluate social/cultural biases exhibited by LLMs and their impact on game balance through six specific tasks and a novel evaluation metric, Decision Log Standard Deviation (Dlstd).

**Data Type**: numerical

**Domains**:
- Computer Games

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/Anonymous999-xxx/FairGamer)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and quantify the social/cultural biases of LLMs and their direct effects on game balance within video game contexts.

**Target Audience**:
- ML Researchers
- Game Developers

**Tasks**:
- Social Bias Detection
- Game Balance Evaluation

**Limitations**: FAIRGAMER Benchmark provides valuable insights into LLM biases but has limitations including limited data coverage focusing on a small number of representative games.

## 💾 Data

**Source**: Data collected from 58 Steam games encompassing both real-world and fully fictional game content.

**Size**: 89,980 test cases

**Format**: JSON

**Annotation**: Data structured around six tasks to evaluate biases in LLMs interactions in games.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Decision Log Standard Deviation (Dlstd)

**Calculation**: The Dlstd metric is calculated based on the variance of decision distributions in LLM outputs to quantify bias.

**Interpretation**: A higher Dlstd indicates greater bias among different entities, resulting in poorer game balance or unreasonable difficulty levels.

**Baseline Results**: Experiments evaluated eight state-of-the-art models, revealing various degrees of bias across tasks.

**Validation**: Extensive testing across multiple models and scenarios to ensure reliable measurement of LLM biases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes demographic analysis across different race and career categories with varying discount offerings.

**Potential Harm**: Potential impacts of LLM biases may lead to unfair advantages or disadvantages in competitive gaming scenarios.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
