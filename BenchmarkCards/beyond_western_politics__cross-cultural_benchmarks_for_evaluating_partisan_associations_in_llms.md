# Beyond Western Politics: Cross-Cultural Benchmarks for Evaluating Partisan Associations in LLMs

## 📊 Benchmark Details

**Name**: Beyond Western Politics: Cross-Cultural Benchmarks for Evaluating Partisan Associations in LLMs

**Overview**: The paper introduces two datasets, NeutQA-440 (non-adversarial prompts) and AdverQA-440 (adversarial prompts), designed to evaluate political biases in large language models (LLMs) through comparative plausibility judgments involving political leaders and parties in the USA and India.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hindi

**Resources**:
- [Resource](https://arxiv.org/abs/2509.22711)

## 🎯 Purpose and Intended Users

**Goal**: To audit harmful partisan associations in LLMs through comparative plausibility judgments, with an aim to integrate partisan bias testing into standard LLM benchmarks.

**Target Audience**:
- ML Researchers
- Policy Makers
- Model Developers

**Tasks**:
- Bias Evaluation
- Comparative Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Datasets created by the authors measuring partisan biases in LLMs.

**Size**: 880 examples (440 for each dataset)

**Format**: N/A

**Annotation**: Designed by the authors through carefully constructed prompts.

## 🔬 Methodology

**Methods**:
- Comparative plausibility judgment
- Statistical analysis

**Metrics**:
- Bias susceptibility
- Model agreement rates

**Calculation**: The models' performances were analyzed using a three-step evaluation pipeline focusing on bias detection, directional consistency, and aggregate asymmetry.

**Interpretation**: Higher susceptibility indicates significant partisan bias in LLMs based on provided datasets.

**Baseline Results**: Bias rates exceeding 91% across all models tested.

**Validation**: Systematic findings across multiple LLMs provide validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: The dataset covers political leaders and parties from the USA and India, ensuring a comparative context.

**Potential Harm**: Potential amplification of political division and unintentional reinforcement of biases.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
