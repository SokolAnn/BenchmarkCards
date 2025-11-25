# TAGbank

## 📊 Benchmark Details

**Name**: TAGbank

**Overview**: TAGbank is a corpus of TAG (Tree-Adjoining Grammar) derivations automatically extracted from existing syntactic treebanks. It provides a robust, derivation-based resource to support parsing, grammar induction, and semantic analysis.

**Data Type**: TAG derivations

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Korean

**Similar Benchmarks**:
- CCGbank

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To fill the gap in large-scale corpora grounded in lexicalized grammar by providing a dataset of TAG derivations.

**Target Audience**:
- ML Researchers
- Linguists
- Model Developers

**Tasks**:
- Parsing
- Grammar Induction
- Semantic Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Existing syntactic treebanks such as the Penn Treebank, Penn Chinese Treebank, and Penn Korean Treebank.

**Size**: N/A

**Format**: Proposed TAGbank format with token-aligned representation

**Annotation**: Automatically extracted from existing syntactic annotations

## 🔬 Methodology

**Methods**:
- Automatic extraction from treebanks
- Derivation tree construction

**Metrics**:
- Parsing accuracy

**Calculation**: Metrics are calculated based on the alignment between TAG derivations and syntactic annotations.

**Interpretation**: Higher parsing accuracy indicates better performance of TAG parsers on structured representations.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
