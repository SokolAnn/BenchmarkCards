# Time Series and Text Explanation Generator (TTGenerator)

## 📊 Benchmark Details

**Name**: Time Series and Text Explanation Generator (TTGenerator)

**Overview**: The TTGenerator is a synthesized dataset for automatically generating time series anomalies with corresponding explanations, used for fine-tuning LLMs to improve performance in time series anomaly detection tasks.

**Data Type**: time-series with explanations

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To generate a dataset that aids in fine-tuning large language models for time series anomaly detection tasks by providing anomalies and explanations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Anomaly Detection

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is synthesized using the Time Series and Text Explanation Generator (TTGenerator).

**Size**: 1000 samples

**Format**: JSON

**Annotation**: Automatically generated descriptions for time series anomalies.

## 🔬 Methodology

**Methods**:
- Prompt engineering using multi-modal instructions
- In-context learning
- Chain-of-thought prompting

**Metrics**:
- F-score
- Range-F

**Calculation**: Metrics are calculated based on the performance of LLMs in detecting anomalies against the benchmark datasets.

**Interpretation**: Higher scores on F-score and Range-F indicate better performance in identifying anomalies.

**Baseline Results**: N/A

**Validation**: Results validated against benchmark datasets for time series anomaly detection.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
