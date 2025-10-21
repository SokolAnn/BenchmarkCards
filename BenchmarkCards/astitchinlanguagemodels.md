# AStitchInLanguageModels

## 📊 Benchmark Details

**Name**: AStitchInLanguageModels

**Overview**: A novel dataset of naturally occurring sentences containing multiword expressions (MWEs) manually classified into a fine-grained set of meanings, designed to improve representation of MWEs in pre-trained language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Portuguese

**Resources**:
- [GitHub Repository](https://github.com/H-TayyarMadabushi/AStitchInLanguageModels)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset and tasks for evaluating idiomaticity detection and representation in language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Idiomaticity Detection
- Idiomaticity Representation

**Limitations**: N/A

## 💾 Data

**Source**: Naturally occurring sentences containing multiword expressions (MWEs) annotated with a fine-grained set of meanings.

**Size**: 4,558 English examples, 1,872 Portuguese examples

**Format**: N/A

**Annotation**: Annotated by judges with a Cohen’s kappa coefficient of 0.887 for English and 0.807 for Portuguese.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Spearman correlation

**Calculation**: Metrics are calculated based on model predictions against the ground truth labels provided in the dataset.

**Interpretation**: A higher F1 Score indicates better performance in correctly identifying idiomatic versus non-idiomatic usages.

**Baseline Results**: XLNet base (cased) achieved a development F1 score of 0.959 in few-shot scenarios for idiomaticity detection.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
