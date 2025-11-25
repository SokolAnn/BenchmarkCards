# TSGym: Design Choices for Deep Multivariate Time-Series Forecasting

## 📊 Benchmark Details

**Name**: TSGym: Design Choices for Deep Multivariate Time-Series Forecasting

**Overview**: TSGym proposes a framework for large-scale evaluation, analysis, and automated model construction in multivariate time series forecasting (MTSF) tasks. It systematically deconstructs deep MTSF methods into distinct design dimensions and conducts extensive experiments on various datasets.

**Data Type**: time-series

**Domains**:
- Finance
- Energy
- Traffic
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- TSlib
- BasicTS
- TFB
- OpenLTM

**Resources**:
- [GitHub Repository](https://github.com/SUFE-AILAB/TSGym)

## 🎯 Purpose and Intended Users

**Goal**: The goal of TSGym is to conduct fine-grained evaluations of component-level designs in MTSF to inform future model development and streamline automated component selection.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Time Series Forecasting

**Limitations**: N/A

## 💾 Data

**Source**: Nine datasets including ETT variants (ETTh1, ETTh2, ETTm1, ETTm2), Electricity (ECL), Traffic, Weather, Exchange, ILI, and short-term forecasting dataset M4.

**Size**: Varies by dataset

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Component-level evaluations

**Metrics**:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- Overall Weighted Average (OWA)
- Symmetric Mean Absolute Percentage Error (SMAPE)
- Mean Absolute Scaled Error (MASE)

**Calculation**: Metrics are calculated based on the forecasting predictions against ground truth values for each dataset.

**Interpretation**: Lower values in MSE, MAE, OWA, SMAPE, and MASE indicate better performance.

**Baseline Results**: Outperformed multiple state-of-the-art methods in the experiments.

**Validation**: Extensive empirical evaluations performed across various datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
