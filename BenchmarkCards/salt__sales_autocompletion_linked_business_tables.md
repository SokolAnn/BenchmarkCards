# SALT: Sales Autocompletion Linked Business Tables

## 📊 Benchmark Details

**Name**: SALT: Sales Autocompletion Linked Business Tables

**Overview**: The SALT dataset is specifically curated to mirror customer interactions within an Enterprise Resource Planning (ERP) system, designed to support research in table representation learning.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GitTables
- WebTables
- TabLib

**Resources**:
- [GitHub Repository](https://github.com/sap-samples/SALT)

## 🎯 Purpose and Intended Users

**Goal**: To stimulate advancements in table representation learning and enhance the applicability of models for real-world business contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multiclass Classification

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from an Enterprise Resource Planning (ERP) system.

**Size**: 500,908 sales orders

**Format**: N/A

**Annotation**: The dataset has undergone minimal pre-processing primarily aimed at addressing privacy concerns.

## 🔬 Methodology

**Methods**:
- Gradient-boosted decision tree models
- Deep learning methods

**Metrics**:
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics were calculated based on the performance of baseline models on various prediction tasks.

**Interpretation**: A higher MRR indicates better model performance in predicting the target variables.

**Baseline Results**: XGBoost achieved MRR of 0.99 for several target variables.

**Validation**: Validation segments were derived from temporal splits of the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset has undergone anonymization to mitigate privacy-related issues.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
