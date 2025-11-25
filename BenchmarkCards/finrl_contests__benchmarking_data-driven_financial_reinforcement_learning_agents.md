# FinRL Contests: Benchmarking Data-driven Financial Reinforcement Learning Agents

## 📊 Benchmark Details

**Name**: FinRL Contests: Benchmarking Data-driven Financial Reinforcement Learning Agents

**Overview**: The FinRL Contests provide standardized task definitions, curated market datasets, GPU-optimized parallel market environments, and defined evaluation metrics to ensure reproducibility and comparability across financial applications such as stock trading, cryptocurrency trading, and the integration of signals from large language models.

**Data Type**: tabular

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FinRL-Meta

**Resources**:
- [GitHub Repository](https://github.com/Open-Finance-Lab/FinRL_Contest_2023/tree/main/Task_1)
- [GitHub Repository](https://github.com/AI4Finance-Foundation/FinRL-Meta)
- [Resource](https://huggingface.co/datasets/SecureFinAI-Lab/FinRL_BTC_news_signals)
- [Resource](https://huggingface.co/datasets/edaschau/bitcoin_news)

## 🎯 Purpose and Intended Users

**Goal**: To promote reproducibility, transparency, and benchmarking in financial reinforcement learning through community-driven contests.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Stock Trading
- Crypto Trading
- Portfolio Management

**Limitations**: N/A

## 💾 Data

**Source**: Daily OHLCV and LOB data from financial markets, financial news articles, and generated signals from LLMs.

**Size**: 3,352 trading days for stocks, 14 days for crypto trading

**Format**: CSV

**Annotation**: Automated data curation and signal generation via market feedback.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Cumulative return
- Annualized return
- Annualized volatility
- Sharpe ratio
- Maximum drawdown
- Calmar ratio

**Calculation**: Metrics are calculated using financial trading performance data against held-out market conditions.

**Interpretation**: Higher values for returns and ratios indicate better performance, while lower drawdown values indicate better risk management.

**Baseline Results**: Comparison against indices like DJIA and S&P 500.

**Validation**: Results are validated through controlled rolling windows.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under CC-BY-NA 4.0 for academic purposes and other licenses as specified.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
