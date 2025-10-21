# MIMIC-IV-Ext-22MCTS (22 Million-Event Temporal Clinical Time-Series Dataset for Risk Prediction)

## 📊 Benchmark Details

**Name**: MIMIC-IV-Ext-22MCTS (22 Million-Event Temporal Clinical Time-Series Dataset for Risk Prediction)

**Overview**: This paper introduces a time series clinical events dataset consisting of 22,588,586 clinical time series events with timestamps extracted from discharge summaries, aimed at improving clinical risk prediction modeling.

**Data Type**: clinical event and timestamp pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance clinical risk forecasting and provide a dataset for machine learning models in healthcare applications.

**Target Audience**:
- Healthcare Researchers
- Medical Practitioners
- Data Scientists

**Tasks**:
- Clinical Event Extraction
- Timestamp Estimation

**Limitations**: N/A

## 💾 Data

**Source**: Clinical discharge summaries from MIMIC-IV-Note.

**Size**: 22,588,586 clinical events

**Format**: N/A

**Annotation**: Annotations were conducted by clinical experts for event extraction.

## 🔬 Methodology

**Methods**:
- Contextual BM25
- Semantic Search
- Large Language Model Annotation

**Metrics**:
- Accuracy
- NDCG
- Precision
- Recall

**Calculation**: Metrics are calculated based on the performance of models fine-tuned on the dataset compared to baseline model performances.

**Interpretation**: Higher metrics indicate improved clinical prediction capabilities.

**Validation**: Evaluation of model performance using validation datasets from healthcare tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
