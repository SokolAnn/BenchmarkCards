# AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios

## 📊 Benchmark Details

**Name**: AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios

**Overview**: AgentSense provides a benchmark for evaluating the social intelligence of language agents through interactive social scenarios constructed from extensive scripts. It aims to assess how well LLMs can navigate complex social interactions.

**Data Type**: social interaction scenarios

**Domains**:
- Natural Language Processing
- Social Science

**Languages**:
- English

**Similar Benchmarks**:
- Socialbench
- Social-IQ

**Resources**:
- [GitHub Repository](https://github.com/ljcleo/agent_sense)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the social intelligence of language models by simulating diverse and challenging social scenarios.

**Target Audience**:
- ML Researchers
- Model Developers
- Social Scientists

**Tasks**:
- Social Interaction Simulation
- Goal Completion Evaluation
- Implicit Reasoning Evaluation

**Limitations**: Although automated, the scenario extraction process may still require manual validation.

## 💾 Data

**Source**: Internet Movie Script Database (IMSDb), with scripts from movies and TV shows.

**Size**: 1,225 scenarios

**Format**: JSON

**Annotation**: Manual annotation by graduate students for social goals and private information validation.

## 🔬 Methodology

**Methods**:
- Simulation of social interactions
- Evaluation through multi-turn interactions and interviews
- Human and model-based evaluations

**Metrics**:
- Goal completion rates
- Implicit reasoning accuracy
- Profile sensitivity index (PSI)

**Calculation**: Metrics are calculated based on agent performance in achieving social goals and reasoning about private information.

**Interpretation**: Higher accuracy indicates better performance in social interactions, while lower PSI indicates stable social intelligence.

**Validation**: Validated through expert reviews and annotations by multiple graduate students.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Includes diverse character profiles across various demographics.

**Potential Harm**: AgentSense aims to prevent unrealistic expectations from LLMs in social simulations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured by constructing fictional characters based on diverse attributes without real identities.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
