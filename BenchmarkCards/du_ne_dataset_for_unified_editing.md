# DU NE (Dataset for Unified Editing)

## 📊 Benchmark Details

**Name**: DU NE (Dataset for Unified Editing)

**Overview**: DU NE is an editing benchmark where edits are natural language sentences aimed at modifying a model’s knowledge or representations to produce desired outcomes, covering diverse editing scenarios such as rectifying reasoning errors, correcting arithmetic mistakes, introducing new information, and mitigating bias.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MQuaKe
- RippleEdits

**Resources**:
- [GitHub Repository](https://github.com/feyzaakyurek/dune)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of DU NE is to provide a benchmark for evaluating model editing techniques across various use cases.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Combination of automated curation and human vetting, utilizing existing datasets for prompting edits and queries.

**Size**: 951 edits, 10,129 queries

**Format**: N/A

**Annotation**: Manual verification by annotators

## 🔬 Methodology

**Methods**:
- Evaluation of editing techniques using model outputs before and after applying edits.

**Metrics**:
- Accuracy

**Calculation**: Calculated through accuracy scores on edit queries.

**Interpretation**: Scores are interpreted to assess how well model outputs align with the expected results following applied edits.

**Baseline Results**: N/A

**Validation**: Validation includes assessing the relevance and accuracy of queries relative to edits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
