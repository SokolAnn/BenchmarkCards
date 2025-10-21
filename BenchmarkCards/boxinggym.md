# BoxingGym

## 📊 Benchmark Details

**Name**: BoxingGym

**Overview**: BoxingGym is a benchmark with 10 environments for systematically evaluating experimental design and model discovery capabilities of language-based agents in real-world scientific contexts.

**Data Type**: generative probabilistic models

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/kanishkg/boxing-gym/tree/v0.1.0-beta)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the performance of language models in automated experimental design and model discovery tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Experimental Design
- Model Discovery

**Limitations**: The environments in BoxingGym offer pre-defined experimental paradigms, whereas real-world science involves designing the experimental method itself; also, it does not consider the time and cost of experiments.

## 💾 Data

**Source**: 10 real-world scientific models implemented as generative probabilistic models.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Quantitative evaluation using expected information gain (EIG)
- Natural language explanations for model discovery

**Metrics**:
- Expected Information Gain (EIG)
- Mean Squared Error (MSE)

**Calculation**: Expected Information Gain (EIG) quantifies the informativeness of an experiment by measuring the reduction in uncertainty about model parameters after running the experiment.

**Interpretation**: Lower standardized prediction error indicates better performance in predicting the environment based on the model discovery.

**Validation**: Experiments were validated through systematic testing of baseline agents in various environments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Decision bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
