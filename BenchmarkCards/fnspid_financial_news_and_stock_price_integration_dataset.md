# FNSPID (Financial News and Stock Price Integration Dataset)

## 📊 Benchmark Details

**Name**: FNSPID (Financial News and Stock Price Integration Dataset)

**Overview**: FNSPID is a comprehensive financial dataset that consists of 29.7 million stock prices and 15.7 million time-aligned financial news records for 4,775 S&P500 companies from the period 1999 to 2023. It uniquely integrates sentiment information with numerical stock price data to enhance market prediction capabilities.

**Data Type**: time-series

**Domains**:
- Finance

**Languages**:
- English
- Russian

**Similar Benchmarks**:
- Benzinga financial news dataset
- Bloomberg financial news dataset
- Reuters financial news dataset

**Resources**:
- [GitHub Repository](https://github.com/Zdong104/FNSPID)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive resource for financial market prediction models by integrating sentiment and numerical data.

**Target Audience**:
- Financial Researchers
- Data Scientists
- Machine Learning Practitioners

**Tasks**:
- Stock Price Prediction
- Sentiment Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Collected from four different stock market news websites and Yahoo Finance's API.

**Size**: 30GB

**Format**: CSV

**Annotation**: Sentiment scores generated using ChatGPT and traditional sentiment analysis methods.

## 🔬 Methodology

**Methods**:
- Machine Learning
- Sentiment Analysis
- Data Integration

**Metrics**:
- Accuracy
- R2 Score

**Calculation**: Metrics are calculated based on model performance against stock price predictions.

**Interpretation**: Higher R2 values indicate better model performance in predicting stock prices.

**Baseline Results**: Transformer model achieved an R2 score of 0.988.

**Validation**: Dataset was validated through experiments comparing various ML models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Maintained compliance with GDPR and CCPA regulations; implemented anonymization techniques.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data collected from publicly available news content.

**Compliance With Regulations**: The data collection adhered to ethical standards and website policies.
