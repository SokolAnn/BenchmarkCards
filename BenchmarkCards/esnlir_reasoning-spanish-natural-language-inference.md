# ESNLIR (Reasoning-Spanish-Natural-Language-Inference)

## 📊 Benchmark Details

**Name**: ESNLIR (Reasoning-Spanish-Natural-Language-Inference)

**Overview**: The paper introduces a novel Spanish multi-genre dataset for Natural Language Inference (NLI) that incorporates causal relationships between sentences, aiming to enhance model generalization capabilities.

**Data Type**: premise-hypothesis pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Spanish

**Similar Benchmarks**:
- XNLI
- SPARTE
- INFERES
- sciNLI
- msciNLI

**Resources**:
- [Resource](https://zenodo.org/records/15002575)
- [Resource](https://zenodo.org/records/15002371)

## 🎯 Purpose and Intended Users

**Goal**: To provide an extensive dataset for Spanish multi-genre NLI that incorporates causal relationships, enabling better evaluation and development of NLI models in Spanish.

**Target Audience**:
- ML Researchers
- Model Developers
- Linguists

**Tasks**:
- Natural Language Inference

**Limitations**: The dataset is primarily evaluated with BERT-based models and may require human annotation of more examples to improve quality.

## 💾 Data

**Source**: 34 Spanish corpora across multiple genres including articles, books, comments, legal, clinical, news, talks, and theses.

**Size**: 7,325,356 training examples, 127,404 validation examples, 128,412 test examples

**Format**: N/A

**Annotation**: Automated extraction using linking phrases for premise-hypothesis pairs.

## 🔬 Methodology

**Methods**:
- BERT-based evaluation
- XGBoost baseline comparison
- Human validation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy and F1 Score metrics are calculated for model performance evaluation.

**Interpretation**: Higher accuracy and F1 scores indicate better model performance in understanding semantic relationships.

**Baseline Results**: XGBoost accuracy: 0.35, BERTIN accuracy: 0.663, XLMRoBERTa accuracy: 0.676.

**Validation**: Double stratification strategy used to maintain class balance across training, validation, and testing splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Analysis of genre representation shows potential bias in non-formal writing categories.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
