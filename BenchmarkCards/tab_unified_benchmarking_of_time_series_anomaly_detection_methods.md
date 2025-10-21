# TAB (Unified Benchmarking of Time Series Anomaly Detection Methods)

## 📊 Benchmark Details

**Name**: TAB (Unified Benchmarking of Time Series Anomaly Detection Methods)

**Overview**: TAB provides a comprehensive evaluation of time series anomaly detection methods, encompassing 29 public multivariate datasets and 1,635 univariate time series from various domains, alongside a unified and automated evaluation pipeline.

**Data Type**: time-series

**Domains**:
- Finance
- Transportation
- Healthcare
- Manufacturing
- Web

**Languages**:
- English

**Similar Benchmarks**:
- NAB
- Exathlon
- TODS
- TSB-UAD
- TimeSeriesBench

**Resources**:
- [GitHub Repository](https://github.com/decisionintelligence/TAB)
- [Resource](https://decisionintelligence.github.io/OpenTS/Benchmarks/overview/)

## 🎯 Purpose and Intended Users

**Goal**: To enable accurate comparison of various TSAD methods through a unified and extensible evaluation benchmark.

**Target Audience**:
- ML Researchers
- Data Scientists
- Industry Practitioners

**Tasks**:
- Time Series Anomaly Detection

**Limitations**: N/A

## 💾 Data

**Source**: Public datasets from various domains, including finance, healthcare, and transportation.

**Size**: 29 multivariate datasets and 1,635 univariate time series

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Non-learning methods
- Machine learning methods
- Deep learning methods
- LLM-based methods
- Time-series pre-trained methods

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- AUC-PR
- AUC-ROC

**Calculation**: Metrics computed based on anomaly scores and derived labels from the pipeline.

**Interpretation**: High scores in metrics indicate better performance in detecting anomalies.

**Baseline Results**: N/A

**Validation**: TAB implements a unified framework to ensure fair comparisons and consistent evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons BY-NC-ND 4.0 International License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
