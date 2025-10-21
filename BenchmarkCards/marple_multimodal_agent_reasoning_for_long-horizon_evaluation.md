# MARPLE (Multimodal Agent Reasoning for Long-Horizon Evaluation)

## 📊 Benchmark Details

**Name**: MARPLE (Multimodal Agent Reasoning for Long-Horizon Evaluation)

**Overview**: MARPLE is a benchmark for evaluating long-horizon inference capabilities using multi-modal evidence. It features agents interacting with simulated households, supporting visual, language, and auditory stimuli to infer causal relationships in household scenarios, primarily focused on 'whodunit' style questions.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Cognitive Science

**Languages**:
- English

**Resources**:
- [Resource](https://marple-benchmark.github.io/)
- [GitHub Repository](https://github.com/marple-benchmark/marple)

## 🎯 Purpose and Intended Users

**Goal**: To assess models' abilities to perform long-horizon multimodal inference in complex household scenarios.

**Target Audience**:
- ML Researchers
- Cognitive Scientists
- AI Practitioners

**Tasks**:
- Inference
- Causal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Procedurally generated multimodal data from the MARPLE Household Simulator.

**Size**: 5000 trajectories for training datasets, 500 trajectories for test datasets.

**Format**: ZIP files containing JSON representations

**Annotation**: Automatically generated through the MARPLE Household Simulator.

## 🔬 Methodology

**Methods**:
- Monte Carlo Tree Search
- Large Language Model evaluation
- Human evaluation

**Metrics**:
- Inference accuracy at various time steps

**Calculation**: Inference accuracy is calculated based on the probability of correctly identifying the agent responsible for a query state.

**Interpretation**: Higher inference accuracy indicates a better understanding and prediction of agent behaviors and state changes.

**Baseline Results**: Human participants achieved an average accuracy of 0.8 with 48% of evidence.

**Validation**: Benchmarks were validated through comparisons with human performance and established baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
