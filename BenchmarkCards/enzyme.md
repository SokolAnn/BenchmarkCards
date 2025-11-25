# ENZYME

## 📊 Benchmark Details

**Name**: ENZYME

**Overview**: ENZYME is a dataset designed for hierarchical text classification (HTC), comprising 30,523 articles from PubMed for predicting Enzyme Commission (EC) numbers, featuring a four-level single-path hierarchy.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- WOS
- NYT

**Resources**:
- [GitHub Repository](https://github.com/viditjain99/HiGen)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for developing and benchmarking models for hierarchical text classification, particularly in the domain of biomedical literature.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Hierarchical Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Articles from PubMed with associated Enzyme Commission numbers.

**Size**: 30,523 articles

**Format**: PDF, parsed text

**Annotation**: Automatically extracted from PubMed articles

## 🔬 Methodology

**Methods**:
- Sequence generation
- Pretraining

**Metrics**:
- Micro-F1
- Macro-F1

**Calculation**: Micro-F1 and Macro-F1 scores calculated based on predicted and actual hierarchical labels.

**Interpretation**: Higher F1 scores indicate better performance in classifying hierarchical labels.

**Baseline Results**: HiGen outperforms existing methods with Micro-F1 of 92.61 and Macro-F1 of 84.15 on ENZYME.

**Validation**: Extensive experiments across ENZYME, WOS, and NYT datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
