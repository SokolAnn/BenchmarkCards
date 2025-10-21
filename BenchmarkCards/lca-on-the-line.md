# LCA-on-the-Line

## 📊 Benchmark Details

**Name**: LCA-on-the-Line

**Overview**: The LCA-on-the-Line framework benchmarks model generalization for Out-of-Distribution (OOD) performance by utilizing Lowest Common Ancestor (LCA) distance based on class taxonomies. It assesses multiple models trained on ImageNet and their performance on various OOD datasets, revealing significant correlations between the LCA distance and OOD accuracy.

**Data Type**: LCA distance metrics

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2407.16067)

## 🎯 Purpose and Intended Users

**Goal**: To provide a new benchmarking method for assessing Out-of-Distribution (OOD) generalization capabilities of models across various datasets using class taxonomies.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Model Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: ImageNet dataset and its OOD variants, specifically ImageNet-v2, ImageNet-S, ImageNet-R, ImageNet-A, and ObjectNets.

**Size**: 75 pretrained models

**Format**: N/A

**Annotation**: Annotations were derived from class hierarchies using K-means clustering and semantic relationships encoded by WordNet.

## 🔬 Methodology

**Methods**:
- Empirical evaluation using LCA distance metrics
- Statistical measures for correlation (R², Pearson correlation coefficient)

**Metrics**:
- Top-1 Accuracy
- LCA Distance

**Calculation**: LCA distance is calculated based on taxonomic relationships between predicted classes and ground-truth classes within a class hierarchy.

**Interpretation**: Lower LCA distance indicates better generalization performance to OOD datasets.

**Baseline Results**: N/A

**Validation**: Model performance was validated against standard OOD datasets with significant visual shifts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
