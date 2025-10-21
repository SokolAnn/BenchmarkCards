# Profit: Benchmarking Personalization and Robustness Trade-off in Federated Prompt Tuning

## 📊 Benchmark Details

**Name**: Profit: Benchmarking Personalization and Robustness Trade-off in Federated Prompt Tuning

**Overview**: This paper benchmarks fundamental federated learning algorithms applied to prompt tuning large language models to understand the trade-off between personalization and robustness under varying levels of data heterogeneity.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2310.04627)

## 🎯 Purpose and Intended Users

**Goal**: To study the trade-off between personalization and robustness in federated learning scenarios using large language models.

**Target Audience**:
- ML Researchers
- Federated Learning Practitioners
- Domain Experts

**Tasks**:
- Question Answering
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Super-NaturalInstructions (SNI), a collection of diverse NLP tasks.

**Size**: 10,000 instances per partition

**Format**: JSON

**Annotation**: Mined from multi-type instruction datasets.

## 🔬 Methodology

**Methods**:
- Federated Averaging (FedAvg)
- Federated Stochastic Gradient Descent (FedSGD)
- Parameter-efficient fine-tuning methods

**Metrics**:
- ROUGE-L

**Calculation**: Reported scores are computed through the evaluation of local and global test datasets after personalization.

**Interpretation**: Higher ROUGE-L scores indicate better alignment between predicted and actual outputs.

**Baseline Results**: FedAvg(Adam) outperformed other methods in most cases.

**Validation**: Hyperparameters tuned via global validation sets constructed from all validation clients.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Robustness**: Prompt injection attack
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
