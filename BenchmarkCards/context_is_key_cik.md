# Context is Key (CiK)

## 📊 Benchmark Details

**Name**: Context is Key (CiK)

**Overview**: CiK consists of tasks designed to assess a forecasting model’s ability to use both numerical input-output pairs and essential textual context. Accurate forecasts in CiK are made possible only by effectively leveraging both numerical data and key information contained within the accompanying text.

**Data Type**: time-series with textual context

**Domains**:
- Public Safety
- Traffic
- Energy
- Climatology
- Economics
- Retail
- Mechanics

**Languages**:
- English

**Resources**:
- [Resource](https://servicenow.github.io/context-is-key-forecasting/v0/)
- [GitHub Repository](https://github.com/ServiceNow/context-is-key-forecasting)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to advance multimodal forecasting by promoting models that are both accurate and accessible to decision-makers with varied technical expertise.

**Target Audience**:
- ML Researchers
- Forecasting Practitioners
- Domain Experts

**Tasks**:
- Time Series Forecasting

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available datasets from various application domains.

**Size**: 2,644 time series across 71 tasks

**Format**: N/A

**Annotation**: Manual crafting of natural language context and extensive evaluation of tasks.

## 🔬 Methodology

**Methods**:
- DIRECT PROMPT
- LLM processes (LLMP)
- Statistical models

**Metrics**:
- Region of Interest Continuous Ranked Probability Score (RCRPS)

**Calculation**: RCRPS is calculated to evaluate both index scores within relevant and non-relevant contexts.

**Interpretation**: Lower RCRPS indicates better forecasting performance.

**Baseline Results**: Various forecasting models were evaluated showing different performances on the RCRPS metric.

**Validation**: The benchmark includes a panel review by human evaluators to assess the relevance of context in tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
