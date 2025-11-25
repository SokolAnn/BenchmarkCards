# ReC4TS

## 📊 Benchmark Details

**Name**: ReC4TS

**Overview**: ReC4TS is the first benchmark designed to systematically evaluate the effectiveness of popular reasoning strategies in zero-shot time series forecasting (TSF) tasks. It conducts comprehensive evaluations across datasets spanning eight domains, covering both unimodal and multimodal forecasting tasks.

**Data Type**: multimodal, text and numerical time series

**Domains**:
- Economics
- Urban Computing
- Epidemiology
- Climate
- Agriculture
- Energy
- Health
- Traffic

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AdityaLab/OpenTimeR)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of reasoning strategies for zero-shot time series forecasting.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Time Series Forecasting

**Limitations**: N/A

## 💾 Data

**Source**: Datasets covering various domains with numerical time series and aligned textual context series for forecasting tasks.

**Size**: 8 datasets across multiple domains

**Format**: N/A

**Annotation**: Reasoning trajectories from multiple advanced LLMs annotated in the Time-Thinking dataset.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Squared Error (MSE)

**Calculation**: MSE is calculated as the average of the squares of the errors, which is the average squared differences between predicted and actual values.

**Interpretation**: Lower MSE values indicate better forecasting accuracy.

**Baseline Results**: N/A

**Validation**: Validation conducted through comprehensive experiments across various datasets and reasoning strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
