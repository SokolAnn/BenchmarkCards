# PEDANTIC (Patent Definite Examination Dataset)

## 📊 Benchmark Details

**Name**: PEDANTIC (Patent Definite Examination Dataset)

**Overview**: PEDANTIC is a novel dataset of 14,000 US patent claims relating to Natural Language Processing, annotated with reasons for indefiniteness to facilitate automatic examination of patent claims.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/boschresearch/pedantic-patentsemtech)

## 🎯 Purpose and Intended Users

**Goal**: To enable reproducible research on automatic patent definiteness examination.

**Target Audience**:
- Patent AI Researchers
- ML Researchers
- Industry Practitioners

**Tasks**:
- Binary Classification
- Multi-Label Classification

**Limitations**: N/A

## 💾 Data

**Source**: USPTO Office Data Portal API

**Size**: 14,536 claims

**Format**: JSON

**Annotation**: Automatically generated with human validation.

## 🔬 Methodology

**Methods**:
- Logistic Regression
- LLM-based Evaluation
- LLM-as-Judge Evaluation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- AUROC

**Calculation**: Metrics calculated based on model predictions compared to human examiner's rejections.

**Interpretation**: Higher scores indicate a better performance in identifying definiteness in patent claims.

**Baseline Results**: Best model achieved an AUROC score of 60.3.

**Validation**: Human validation using a sample of annotated claims.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
