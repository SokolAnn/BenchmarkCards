# CrashEvent

## 📊 Benchmark Details

**Name**: CrashEvent

**Overview**: CrashEvent is a large-scale traffic crash language dataset summarizing 19,340 real-world crash reports from Washington State, incorporating infrastructure data and various contextual factors. It aims to predict detailed accident outcomes based on complex, unstructured data using large language models.

**Data Type**: text

**Domains**:
- Traffic Safety
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://crashllm.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To develop a predictive framework for analyzing and forecasting traffic crashes using language-based representations of heterogeneous data.

**Target Audience**:
- Traffic Safety Researchers
- Data Scientists
- Policymakers

**Tasks**:
- Crash Severity Prediction
- Total Injury Prediction
- Accident Type Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Crash records from Washington State, including police reports, satellite images, and highway data.

**Size**: 19,340 crash reports, approximately 6.32 million words

**Format**: JSON

**Annotation**: Curated with human-machine cooperative approach, transforming unstructured data into structured formats for text reasoning.

## 🔬 Methodology

**Methods**:
- Fine-tuning large language models
- Text reasoning analysis

**Metrics**:
- F1 Score
- Accuracy
- Precision
- Recall

**Calculation**: Metrics are calculated based on prediction tasks of crash severity, total injuries, and accident types.

**Interpretation**: Higher F1 scores indicate better predictive performance in categorizing traffic crash outcomes.

**Baseline Results**: Compared to existing machine learning models, CrashLLM outperformed with an average F1 score improvement.

**Validation**: Model validated through experiments using split data for testing and training, ensuring performance across various prediction tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Analysis of demographic factors affecting traffic crash outcomes included in dataset.

**Potential Harm**: Potential for biases in predictions due to unrepresentative training data and personal data recorded in crash reports.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data anonymization procedures included to protect personal identifiers in crash reports.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
