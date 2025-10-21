# PETA (Protein Evaluation Through Amino-acid Tokenization Analysis)

## 📊 Benchmark Details

**Name**: PETA (Protein Evaluation Through Amino-acid Tokenization Analysis)

**Overview**: PETA introduces a benchmark consisting of 33 datasets categorized into 15 distinct protein-related tasks, providing a standardized evaluation framework for protein language models and exploring the influence of vocabulary sizes on performance.

**Data Type**: text

**Domains**:
- Biotechnology
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- TAPE
- ProteinGLUE
- PEER

**Resources**:
- [GitHub Repository](https://github.com/ginnm/ProteinPretraining)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive analysis and benchmark for evaluating protein language models leveraging sub-word tokenization and their performance across various downstream tasks.

**Target Audience**:
- ML Researchers
- Biotechnologists
- Protein Engineers

**Tasks**:
- Protein Fitness Prediction
- Protein-Protein Interaction Prediction
- Subcellular Localization Prediction
- Protein Solubility Prediction
- Protein Structure Prediction

**Limitations**: N/A

## 💾 Data

**Source**: University of Information Science and Engineering database

**Size**: 138 billion sequences

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Spearman Correlation
- Mean Squared Error (MSE)

**Calculation**: Metrics were calculated based on the performance of models trained on protein sequences from benchmark datasets.

**Interpretation**: Higher scores indicate better model performance on downstream tasks.

**Baseline Results**: Per-amino-acid model acts as baseline for vocabulary size testing.

**Validation**: Models were validated using a subset of 100,000 sequences from the UniRef90 database.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
