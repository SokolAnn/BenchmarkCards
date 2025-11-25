# EX-FEVER: A Dataset for Multi-hop Explainable Fact Verification

## 📊 Benchmark Details

**Name**: EX-FEVER: A Dataset for Multi-hop Explainable Fact Verification

**Overview**: EX-FEVER is a pioneering dataset for multi-hop explainable fact verification, comprising over 60,000 claims requiring 2-hop and 3-hop reasoning, each with a veracity label and an accompanying explanation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FEVER
- HOVER

**Resources**:
- [GitHub Repository](https://github.com/dependentsign/EX-FEVER)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for improving explainability in multi-hop fact verification.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Fact Verification

**Limitations**: Evaluating the effectiveness of the system remains challenging, as the Rouge score may inadequately assess explanation quality.

## 💾 Data

**Source**: Created from hyperlinked Wikipedia documents.

**Size**: 60,000 claims

**Format**: CSV

**Annotation**: Manual annotation by crowd workers.

## 🔬 Methodology

**Methods**:
- Document retrieval
- Explanation generation
- Verdict prediction

**Metrics**:
- Accuracy
- F1 Score
- Rouge Score

**Calculation**: Metrics are calculated based on the comparison between predicted labels and ground truth.

**Interpretation**: A higher F1 Score indicates better model performance in generating correct predictions.

**Baseline Results**: Accuracy benchmark results show a significant performance gap between BERT and GEAR models.

**Validation**: Dataset is split into training, validation, and test sets with a 70%-20%-10% split.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Demographic factors are not explicitly analyzed in the dataset.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
