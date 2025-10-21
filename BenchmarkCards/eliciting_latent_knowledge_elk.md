# Eliciting Latent Knowledge (ELK)

## 📊 Benchmark Details

**Name**: Eliciting Latent Knowledge (ELK)

**Overview**: ELK aims to find patterns in a neural network's activations that robustly track the true state of the world, introducing 12 datasets and corresponding quirky language models finetuned to make systematic errors in context-dependent scenarios.

**Data Type**: binary classification datasets

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/EleutherAI/elk-generalization)

## 🎯 Purpose and Intended Users

**Goal**: To provide a methodology for eliciting reliable knowledge from language models that output untruthful information.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Binary Classification

**Limitations**: N/A

## 💾 Data

**Source**: 12 binary classification datasets designed to evaluate the performance of ELK methods.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Logistic Regression
- Difference-in-Means
- Linear Discriminant Analysis
- Contrast Consistent Search
- Contrastive Representation Clustering
- Logistic Regression on Contrast Pairs
- Difference-in-Means on Contrast Pairs

**Metrics**:
- Area Under ROC Curve (AUC-ROC)

**Calculation**: Probing methods are evaluated based on their ability to classify examples as true or false accurately in the context of the ELK framework.

**Interpretation**: Higher AUROC indicates better generalization of probes to track truthful knowledge in the presence of untruthful outputs from language models.

**Baseline Results**: N/A

**Validation**: The model's performance is tested for its ability to recover knowledge representations in contexts where the language model produces untruthful outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
