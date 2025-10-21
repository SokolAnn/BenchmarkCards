# K-Link: Knowledge-Link Graph from LLMs for Enhanced Representation Learning in Multivariate Time-Series Data

## 📊 Benchmark Details

**Name**: K-Link: Knowledge-Link Graph from LLMs for Enhanced Representation Learning in Multivariate Time-Series Data

**Overview**: The paper introduces K-Link, a novel framework that leverages Large Language Models (LLMs) to extract a Knowledge-Link graph, which enhances graph quality for Multivariate Time-Series (MTS) data and improves representation learning through a graph alignment module for various downstream tasks.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Time-Series

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/XXXXXXX.XXXXXXX)

## 🎯 Purpose and Intended Users

**Goal**: To improve the representation learning of MTS data using a Knowledge-Link graph constructed from LLMs to enhance graph quality and reduce bias in representation.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Remaining Useful Life Prediction
- Human Activity Recognition
- Sleep Stage Classification

**Limitations**: N/A

## 💾 Data

**Source**: C-MAPSS dataset for RUL prediction, UCI-HAR for human activity recognition, ISRUC-S3 for sleep stage classification.

**Size**: 32,816 samples for RUL prediction, 7,947 samples for HAR, 5,149 samples for sleep stage classification

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Graph Neural Networks
- Knowledge extraction from LLMs
- Graph alignment module

**Metrics**:
- Root Mean Squared Error (RMSE)
- Score
- Accuracy
- Macro-averaged F1-Score (MF1)

**Calculation**: Metrics are calculated based on the model's predictions compared to the actual labels of the datasets.

**Interpretation**: Lower RMSE and Score indicate better performance for RUL prediction, while higher Accuracy and MF1 denote better performance for HAR and sleep stage classification.

**Baseline Results**: Compared against state-of-the-art methods such as AConvLSTM, DAGN, InFormer, among others.

**Validation**: Extensive experiments across various MTS-related downstream tasks which demonstrate improvement over existing methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
