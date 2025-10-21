# CUAD (Contract Understanding Atticus Dataset)

## 📊 Benchmark Details

**Name**: CUAD (Contract Understanding Atticus Dataset)

**Overview**: CUAD is a new dataset for legal contract review, created with experts from The Atticus Project, consisting of over 13,000 annotations across 41 label categories, aiming to help models learn to automatically extract and identify key clauses from contracts.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- SuperGLUE

**Resources**:
- [Resource](https://atticusprojectai.org/cuad)
- [GitHub Repository](https://github.com/TheAtticusProject/cuad)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on contract review and understand the performance of NLP models in specialized legal domains.

**Target Audience**:
- ML Researchers
- Legal Experts
- Industry Practitioners

**Tasks**:
- Contract Analysis
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Contracts collected from the Electronic Data Gathering, Analysis, and Retrieval (EDGAR) system maintained by the U.S. Securities and Exchange Commission (SEC).

**Size**: 510 contracts and 13,101 labeled clauses

**Format**: CSV

**Annotation**: Manual annotation by legal experts, with detailed instructions and training provided.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision @ 80% Recall
- Area Under the Precision-Recall Curve (AUPR)

**Calculation**: Metrics are calculated based on true positives, false positives, and false negatives in extraction tasks.

**Interpretation**: Performance measured by how well models identify relevant clauses, with precision balancing the importance of false positives and false negatives.

**Baseline Results**: DeBERTa-xlarge achieves an AUPR of 47.8%, Precision @ 80% Recall of 44.0%.

**Validation**: 80% of contracts used for training and 20% for testing with empirical evaluation across various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
