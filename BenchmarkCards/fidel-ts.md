# FIDEL-TS

## 📊 Benchmark Details

**Name**: FIDEL-TS

**Overview**: FIDEL-TS is a new large-scale benchmark for time series forecasting developed under principles of high-fidelity benchmarking, addressing issues in existing datasets by sourcing data from live APIs, ensuring causal soundness, and structural clarity.

**Data Type**: time-series

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TimeMMD
- ETT
- M4

**Resources**:
- [Resource](https://anonymous.4open.science/r/Universal-Cross-Modal-Time-Series-Forecasting-Pipeline-7ACD)

## 🎯 Purpose and Intended Users

**Goal**: To establish a credible evaluation standard for the field of time series forecasting and demonstrate the limitations of prior benchmarks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Time Series Forecasting

**Limitations**: N/A

## 💾 Data

**Source**: Live APIs providing real-time data streams.

**Size**: Over 67 million data points across various datasets.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Squared Error (MSE)

**Calculation**: MSE is calculated as the average of the squares of the errors between predicted and actual values.

**Interpretation**: Lower MSE values indicate better model performance.

**Baseline Results**: N/A

**Validation**: Evaluation against previous benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data sources are anonymized and used under proper licenses.

**Data Licensing**: Data are under a CC0 license or sourced from APIs with academic research permissions.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Adheres to ethical guidelines in data sourcing.
