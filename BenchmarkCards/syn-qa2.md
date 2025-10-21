# Syn-(QA)2

## 📊 Benchmark Details

**Name**: Syn-(QA)2

**Overview**: Syn-(QA)2 is a collection of two synthetic English QA datasets generated using entity perturbation on Wikidata and HotpotQA, designed to evaluate the effect of false assumptions in both single-hop and multi-hop question-answering tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- (QA)2

**Resources**:
- [GitHub Repository](https://github.com/ashwindaswanibu/QAQA-Synthetic-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effect of false assumptions in question-answering systems and to provide a dataset for testing model robustness against misleading assumptions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The annotation of false assumptions may lead to dissemination of false claims as part of the dataset’s public release.

## 💾 Data

**Source**: Synthetic questions generated using perturbed relations from Wikidata and HotpotQA.

**Size**: 1,812 question pairs

**Format**: JSON

**Annotation**: Manually verified question pairs

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the binary classification of whether the input question contains a false assumption or not.

**Interpretation**: Higher accuracy indicates better performance in detecting false assumptions.

**Validation**: The dataset underwent manual verification to ensure question quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Potential dissemination of false claims due to annotation errors

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache-2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
