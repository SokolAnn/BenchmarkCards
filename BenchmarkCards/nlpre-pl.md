# NLPre-PL

## 📊 Benchmark Details

**Name**: NLPre-PL

**Overview**: NLPre-PL is a newly proposed benchmark for evaluating and ranking natural language preprocessing systems for Polish, providing automated assessment and a publicly accessible leaderboard.

**Data Type**: tokenization and tagging datasets

**Domains**:
- Natural Language Processing

**Languages**:
- Polish

**Similar Benchmarks**:
- GLUE

**Resources**:
- [Resource](https://sites.google.com/view/nlpre-benchmark)
- [Resource](https://nlpre-pl.clarin-pl.eu)
- [Resource](https://nlpre-zh.clarin-pl.eu)
- [Resource](https://nlpre-ga.clarin-pl.eu)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation and ranking system for NLPre tools focused on the Polish language.

**Target Audience**:
- NLP Researchers
- Developers of NLPre tools
- Academic institutions

**Tasks**:
- Tokenization
- Part-of-Speech Tagging
- Dependency Parsing
- Morphological Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Developed from existing Polish datasets including NKJP1M and PDB-UD.

**Size**: 1.2M tokens

**Format**: CoNLL-X, CoNLL-U, DAG, TEI

**Annotation**: Manually and consistently annotated based on the Morfeusz and Universal Dependencies tag sets.

## 🔬 Methodology

**Methods**:
- Automated performance evaluation

**Metrics**:
- F1 Score
- Aligned Accuracy

**Calculation**: Metrics are calculated based on standard evaluation scripts following the CoNLL shared task format.

**Interpretation**: Higher F1 and aligned accuracy scores indicate better performance in NLPre tasks.

**Baseline Results**: COMBO and Stanza achieved the highest F1 scores in evaluation.

**Validation**: Benchmark results are validated against predefined test sets with hidden references to prevent result manipulation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
