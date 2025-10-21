# DeepFund

## 📊 Benchmark Details

**Name**: DeepFund

**Overview**: DeepFund is a live fund benchmark tool designed to rigorously evaluate LLMs in real-time market conditions, preventing information leakage from historical data. It assesses the ability of LLMs to make effective investment decisions utilizing a multi-agent architecture that interacts with real-time stock market data.

**Data Type**: multimodal

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- TAT-QA
- FinanceBench
- FinBen
- InvestorBench

**Resources**:
- [GitHub Repository](https://github.com/HKUSTDial/DeepFund)
- [Resource](https://deepfund.streamlit.app/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and compare the performance of various LLMs in real-time fund investment contexts.

**Target Audience**:
- ML Researchers
- Financial Analysts
- Industry Practitioners

**Tasks**:
- Portfolio Management
- Investment Decision Making

**Limitations**: The current implementation simplifies the trading process and does not account for many practical considerations such as transaction fees and market trading restrictions.

## 💾 Data

**Source**: Real-time stock market data integrated from financial provider APIs like Alpha Vantage and Yahoo Finance

**Size**: Covering market data from March 17 to April 17, 2025

**Format**: JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Live Forward Testing
- Multi-Agent Decision Framework

**Metrics**:
- Cumulative Return
- Sharpe Ratio
- Maximum Drawdown
- Win Rate
- Beta
- Alpha

**Calculation**: Metrics are calculated based on trading performance over a set period combined with specific financial definitions.

**Interpretation**: Positive values in cumulative return indicate trading gains, while negative values represent losses. A high Sharpe Ratio suggests better risk-adjusted returns.

**Validation**: Rigorous interaction with various LLMs to assess trading performance against real-time market conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
