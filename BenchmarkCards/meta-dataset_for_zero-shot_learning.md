# Meta-Dataset for Zero-Shot Learning

## 📊 Benchmark Details

**Name**: Meta-Dataset for Zero-Shot Learning

**Overview**: This paper introduces a meta-dataset aggregating 43 existing classification datasets along with 441 annotated label descriptions in QA format to enhance zero-shot classification performance in language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ruiqi-zhong/Meta-tuning)

## 🎯 Purpose and Intended Users

**Goal**: To improve zero-shot classification performance by meta-tuning language models on a curated collection of classification datasets.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Zero-Shot Classification
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Aggregated datasets from Kaggle, HuggingFace, and existing NLP papers.

**Size**: 43 datasets, 441 label descriptions

**Format**: N/A

**Annotation**: Manual annotation by the authors

## 🔬 Methodology

**Methods**:
- Meta-tuning
- Cross-validation

**Metrics**:
- AUC-ROC

**Calculation**: The change in AUC-ROC is calculated across label descriptions to compare models.

**Interpretation**: A model is considered better if it shows a significant positive change in AUC-ROC on the evaluated tasks.

**Validation**: Leave-one-out cross-validation on similar datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Potential privacy concerns related to user-generated data being used for meta-tuning.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
