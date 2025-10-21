# AbRank: A Benchmark Dataset and Metric-Learning Framework for Antibody–Antigen Affinity Ranking

## 📊 Benchmark Details

**Name**: AbRank: A Benchmark Dataset and Metric-Learning Framework for Antibody–Antigen Affinity Ranking

**Overview**: AbRank introduces a large-scale benchmark and evaluation framework that reframes affinity prediction as a pairwise ranking problem, aggregating over 380,000 binding assays from nine heterogeneous sources. It defines standardized data splits that systematically increase distribution shift to improve the robustness of machine learning models in predicting antibody-antigen binding affinities.

**Data Type**: pairwise ranking data

**Domains**:
- Biomedical Informatics
- Computational Biology

**Languages**:
- English

**Resources**:
- [Resource](https://www.kaggle.com/datasets/aurlienplissier/AbRank)
- [GitHub Repository](https://github.com/biochunan/AbRank-WALLE-Affinity)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous benchmarking framework for evaluating antibody-antigen affinity prediction models based on pairwise ranking, systematically addressing generalization and robustness under distribution shifts.

**Target Audience**:
- ML Researchers
- Computational Biologists
- Biomedicine Researchers

**Tasks**:
- Affinity Prediction
- Pairwise Ranking

**Limitations**: N/A

## 💾 Data

**Source**: Aggregated over 380,000 binding assays from nine heterogeneous sources.

**Size**: 380,000 binding assays

**Format**: N/A

**Annotation**: Pairs of antibody-antigen complexes labeled based on binding affinity differences.

## 🔬 Methodology

**Methods**:
- Pairwise Ranking Loss
- Metric Learning

**Metrics**:
- Area Under ROC Curve (AUC)

**Calculation**: The area under the ROC curve is calculated based on ranking performance across various benchmark splits.

**Interpretation**: Higher AUC indicates better performance in correctly ranking antibody-antigen complexes based on binding affinity.

**Baseline Results**: WALLE-Affinity achieved state-of-the-art AUC scores across multiple benchmark settings.

**Validation**: The benchmark is validated by ensuring no data leakage and using controlled training splits that exclude seen complexes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
