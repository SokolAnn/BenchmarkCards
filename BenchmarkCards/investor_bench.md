# INVESTOR BENCH

## 📊 Benchmark Details

**Name**: INVESTOR BENCH

**Overview**: INVESTOR BENCH is a benchmark specifically designed for evaluating LLM-based agents in diverse financial decision-making contexts, providing a comprehensive suite of tasks applicable to financial products including stocks, cryptocurrencies, and exchange-traded funds (ETFs).

**Data Type**: multimodal financial datasets

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FLUE
- Pixiu
- FinBen

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning and decision-making capabilities of LLM-based agents in complex financial scenarios.

**Target Audience**:
- ML Researchers
- Finance Professionals
- Industry Practitioners

**Tasks**:
- Stock Trading
- Cryptocurrency Trading
- ETF Investing

**Limitations**: Currently focusing on single-asset financial decision-making tasks and does not address multi-asset tasks such as portfolio management.

## 💾 Data

**Source**: Utilizes a range of open-source data and incorporates third-party APIs, including Yahoo Finance and SEC EDGAR.

**Size**: Various dataset sizes depending on financial product (not explicitly stated)

**Format**: N/A

**Annotation**: Data collected and curated from multiple sources, including market data and news articles.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Cumulative Return (CR)
- Sharpe Ratio (SR)
- Annualized Volatility (AV)
- Maximum Drawdown (MDD)

**Calculation**: Metrics are calculated based on the performance of the financial agents in different trading environments.

**Interpretation**: Higher CR and SR indicate better performance, while AV and MDD measure risk and stability; lower values are preferable.

**Baseline Results**: Buy & Hold strategy as baseline for performance comparison.

**Validation**: Evaluation is performed across various financial decision-making tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data does not contain personal information and conforms to established ethical guidelines.

**Data Licensing**: Data shared under the MIT license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
