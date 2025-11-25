# QUITE (Quantifying Uncertainty in Natural Language Text)

## 📊 Benchmark Details

**Name**: QUITE (Quantifying Uncertainty in Natural Language Text)

**Overview**: QUITE is a question answering dataset of real-world Bayesian reasoning scenarios with categorical random variables and complex relationships, providing verbalizations of premises and evidence statements, expecting numeric probability estimates as answers.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CLADDER
- BLInD

**Resources**:
- [GitHub Repository](https://github.com/boschresearch/quite-emnlp24)

## 🎯 Purpose and Intended Users

**Goal**: To assess uncertainty-based reasoning capabilities in natural language processing through Bayesian reasoning scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The assumptions involve that the entire probability distribution is known, which may not hold in real-world scenarios where distributions are often underspecified.

## 💾 Data

**Source**: Publicly available Bayesian networks compiled from literature.

**Size**: 2,384 instances of premises and questions

**Format**: JSON

**Annotation**: Semi-automatically generated with LLM assistance and manual verification.

## 🔬 Methodology

**Methods**:
- LLM-based evaluation
- Neuro-symbolic approach

**Metrics**:
- Accuracy
- Root Mean Square Error (RMSE)

**Calculation**: Metrics calculated based on numeric estimates and comparing model outputs to ground truth probabilities.

**Interpretation**: An accuracy percentage indicating how many instances were correctly solved by the models.

**Validation**: Instances manually validated for correctness and linguistic quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**
- **Accuracy**
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
