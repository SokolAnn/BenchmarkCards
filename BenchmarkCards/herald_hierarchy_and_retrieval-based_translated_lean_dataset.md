# HERALD (Hierarchy and Retrieval-based Translated Lean Dataset)

## 📊 Benchmark Details

**Name**: HERALD (Hierarchy and Retrieval-based Translated Lean Dataset)

**Overview**: HERALD is a dataset created by applying an augmentation pipeline to Mathlib4, generating a large collection of natural language and formal language pairs for the Lean 4 mathematical library.

**Data Type**: natural language-formal language pairs

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- ProofNet
- InternLM2-Math-Plus-7B
- TheoremLlama

**Resources**:
- [Resource](https://huggingface.co/datasets/FrenzyMath/Herald)
- [GitHub Repository](https://github.com/frenzymath/herald_translator)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the autoformalization of mathematical statements and proofs by providing a dataset of parallel natural language and formal language pairs.

**Target Audience**:
- ML Researchers
- Mathematicians
- Math Educators

**Tasks**:
- Autoformalization
- Translation

**Limitations**: N/A

## 💾 Data

**Source**: Mathlib4 - a large library of mathematical code in Lean 4.

**Size**: 580,000 statement pairs and 44,000 theorem pairs

**Format**: JSON

**Annotation**: Automated and semi-automated methods with human expert verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on model performance on validation datasets like miniF2F-test.

**Interpretation**: Accuracy of the translations is used to gauge the effectiveness of the dataset and models trained on it.

**Baseline Results**: HERALD translator achieves 96.7% accuracy on miniF2F-test.

**Validation**: Validation procedures include checks by the Lean compiler and human expert reviews.

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
