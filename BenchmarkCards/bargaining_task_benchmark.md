# Bargaining task benchmark

## 📊 Benchmark Details

**Name**: Bargaining task benchmark

**Overview**: This work formally formulated the Bargaining task for LLM agents and collected a dataset for the Bargaining task, AmazonHistoryPrice, based on Amazon’s price history. This benchmark helps evaluate the bargaining abilities of various LLMs, focusing on the performance of buyers and sellers in different bargaining scenarios.

**Data Type**: dialogue exchanges

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CraigslistBargaining

**Resources**:
- [GitHub Repository](https://github.com/TianXiaSJTU/AmazonPriceHistory)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models' bargaining abilities in a structured manner.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Bargaining Task

**Limitations**: The dataset used was collected on November 18th, 2023, so actual prices may differ over time, potentially biasing the model's understanding of product prices.

## 💾 Data

**Source**: Collected from the camelcamelcamel website.

**Size**: 930 products

**Format**: CSV

**Annotation**: Data collected included product name, description, features, pricing history, and images.

## 🔬 Methodology

**Methods**:
- Automated evaluation metrics

**Metrics**:
- Normalized Profit (NP)
- Sum of Normalized Profits (SNP)

**Calculation**: Normalized Profits are calculated using the formulas defined for buyer and seller profits based on budgets and costs involved in bargaining sessions.

**Interpretation**: Higher SNP indicates better bargaining ability.

**Baseline Results**: Results from various LLMs such as GPT-4, ChatGPT, and multiple open-source models were compared.

**Validation**: The benchmark was validated using multiple runs across LLMs to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset is focused solely on products from Amazon and does not include a demographic breakdown.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset used does not contain personal information or offensive content.

**Data Licensing**: Data collected from publicly available resources for research purposes under standard fair use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
