# CaseHOLD (Case Holdings On Legal Decisions)

## 📊 Benchmark Details

**Name**: CaseHOLD (Case Holdings On Legal Decisions)

**Overview**: CaseHOLD is a new dataset comprised of over 53,000 multiple choice questions designed to identify the relevant holding of a cited case, which is a fundamental task for lawyers. This dataset addresses the difficulty of existing legal NLP tasks and presents significant challenges from an NLP perspective.

**Data Type**: multiple choice question-answering pairs

**Domains**:
- Legal

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/reglab/casehold)

## 🎯 Purpose and Intended Users

**Goal**: To create a benchmark for a fundamental legal task, improving challenges in identifying legal holdings and informing on when domain pretraining is beneficial.

**Target Audience**:
- ML Researchers
- Legal Researchers
- Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Harvard Law Library case law corpus

**Size**: 53,137 examples

**Format**: N/A

**Annotation**: Extracted using legal citation rules

## 🔬 Methodology

**Methods**:
- Fine-tuning on Legal-BERT
- Cross-validation

**Metrics**:
- F1 Score
- Macro F1 Score

**Calculation**: F1 score calculated through 10-fold cross-validation

**Interpretation**: Higher F1 scores indicate better model performance in selecting the correct legal holding.

**Baseline Results**: BiLSTM F1: 0.4, BERT F1: 0.6

**Validation**: 10-fold cross-validation for model evaluation

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
