# BRIDGING SMART METER GAPS: A BENCHMARK OF STATISTICAL, MACHINE LEARNING AND TIME SERIES FOUNDATION MODELS FOR DATA IMPUTATION

## 📊 Benchmark Details

**Name**: BRIDGING SMART METER GAPS: A BENCHMARK OF STATISTICAL, MACHINE LEARNING AND TIME SERIES FOUNDATION MODELS FOR DATA IMPUTATION

**Overview**: This paper evaluates various models for gap-filling in smart meter electricity consumption data, comparing the effectiveness of traditional statistical methods, machine learning models, and language models for data imputation tasks.

**Data Type**: time-series

**Domains**:
- Energy

**Languages**:
- English

**Similar Benchmarks**:
- TSI-Bench

**Resources**:
- [Resource](https://arxiv.org/abs/2501.07276)

## 🎯 Purpose and Intended Users

**Goal**: To assess whether various models are suitable for handling missing data in smart meter electricity consumption data and to explore the potential of these models for gap-filling tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Data Imputation
- Time Series Forecasting

**Limitations**: N/A

## 💾 Data

**Source**: Public dataset of household energy consumption from London, collected through smart meters.

**Size**: 5,567 households

**Format**: CSV

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Statistical methods
- Machine Learning models
- Language Models
- Time Series Foundation Models

**Metrics**:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Symmetric Mean Absolute Percentage Error (SMAPE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)

**Calculation**: Each metric was computed based on the average of five runs, averaged per household and aggregated across all households.

**Interpretation**: Models with lower error rates indicate better performance in gap-filling tasks.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymization techniques were applied to the dataset to address privacy concerns.

**Data Licensing**: Creative Commons Attribution 4.0 International (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
