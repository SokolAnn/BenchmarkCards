# PharmaSimText

## 📊 Benchmark Details

**Name**: PharmaSimText

**Overview**: PharmaSimText is a novel benchmark derived from the PharmaSim virtual pharmacy environment designed for practicing diagnostic conversations with over 500 scenario variations that can be used for developing and evaluating learner agents.

**Data Type**: scenario variations for diagnostic conversations

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/epfl-ml4ed/PharmaSimText-LLM-RL)

## 🎯 Purpose and Intended Users

**Goal**: To develop a benchmark for evaluating agents in text-based learning tasks and enhancing their generalization capabilities through the integration of Reinforcement Learning and Large Language Models.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Educators

**Tasks**:
- Dialogue Management
- Diagnostic Conversation

**Limitations**: N/A

## 💾 Data

**Source**: Derived from PharmaSim, adapted for text-based interactions and enhanced with generative capabilities of LLMs alongside expert insights.

**Size**: 500+ scenario variations

**Format**: N/A

**Annotation**: Scenario variations were generated using LLMs and reviewed by human experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Post-test Performance Score
- Trajectory Quality Score
- Combined Score

**Calculation**: Metrics are calculated based on agent performance in scenario completion and conversation quality.

**Interpretation**: Higher scores indicate better diagnostic accuracy and quality of interactions.

**Baseline Results**: N/A

**Validation**: Evaluated across diverse patient profiles and scenario variations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack, Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
