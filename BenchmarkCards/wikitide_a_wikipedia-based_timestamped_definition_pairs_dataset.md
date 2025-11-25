# WIKITIDE (A Wikipedia-based Timestamped Definition Pairs Dataset)

## 📊 Benchmark Details

**Name**: WIKITIDE (A Wikipedia-based Timestamped Definition Pairs Dataset)

**Overview**: WIKITIDE is a dataset derived from pairs of timestamped definitions extracted from Wikipedia, aimed at accelerating diachronic NLP by training models able to scan knowledge resources for core updates concerning concepts, events, or named entities.

**Data Type**: definition pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hsuvas/wikitide)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for training models able to detect changes in definitions over time and facilitate diachronic NLP.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Lexical Semantics
- Knowledge Update Detection

**Limitations**: N/A

## 💾 Data

**Source**: Wikipedia

**Size**: 10,000 definition pairs

**Format**: N/A

**Annotation**: Weakly supervised annotation using a bootstrapping approach with GPT-3

## 🔬 Methodology

**Methods**:
- Bootstrapping
- Weak Supervision

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on the classification results of the model on defined labels from annotated pairs.

**Interpretation**: Higher F1 scores indicate better performance in detecting temporal changes in definitions.

**Baseline Results**: N/A

**Validation**: Model validation using a held-out test set.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Involves potential for incorrect flags due to reliance on Wikipedia as a data source.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
