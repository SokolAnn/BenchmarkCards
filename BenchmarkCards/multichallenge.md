# MultiChallenge

## 📊 Benchmark Details

**Name**: MultiChallenge

**Overview**: MultiChallenge is a pioneering benchmark evaluating large language models (LLMs) on conducting multi-turn conversations with human users, focusing on realistic challenges in human-LLM interactions.

**Data Type**: multi-turn conversation history with user instructions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MT-Bench
- MT-Eval

**Resources**:
- [GitHub Repository](https://github.com/ekwinox117/multi-challenge)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multi-turn conversational capabilities of large language models and to identify their challenges in engaging with human users.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multi-turn Conversation Evaluation
- Question Answering
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated through a multi-agent system and human-reviewed.

**Size**: 273 test examples

**Format**: CSV

**Annotation**: Manual annotation by human experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM as judge with instance-level rubrics

**Metrics**:
- Average Accuracy

**Calculation**: Metrics are calculated based on the responses of LLMs to user prompts across various challenge categories within the benchmark.

**Interpretation**: Higher accuracy indicates better performance in respect to multi-turn conversation challenges.

**Baseline Results**: Claude 3.5 Sonnet achieved an average accuracy of 41.4% on MultiChallenge.

**Validation**: Evaluation methods are validated through comparison with human-rated outcomes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Difficulty in accurately following user instructions across multiple turns.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
