# PulseReddit

## 📊 Benchmark Details

**Name**: PulseReddit

**Overview**: PulseReddit is a novel dataset that aligns large-scale Reddit discussion data with high-frequency cryptocurrency market statistics for short-term trading analysis.

**Data Type**: text

**Domains**:
- Finance

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/7huahua/RedditDataset)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to facilitate research into the impact of social sentiment on cryptocurrency trading and to serve as a benchmark for developing advanced trading agents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Market Analysis
- High-Frequency Trading

**Limitations**: The dataset focuses on four major cryptocurrencies and Reddit as the primary social media source, which may limit generalizability to other assets or platforms.

## 💾 Data

**Source**: Reddit discussions from multiple cryptocurrency-related subreddits.

**Size**: N/A

**Format**: N/A

**Annotation**: Data is curated and cleaned through a systematic pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Total Return
- Sharpe Ratio

**Calculation**: Total Return is calculated as (wend - wstart) / wstart, where wstart and wend denote the initial and final net worth, respectively.

**Interpretation**: Higher returns indicate better performance of trading strategies.

**Baseline Results**: Baseline strategies include Buy and Hold, Oracle upper bound, and various technical indicators.

**Validation**: Performance is validated across multiple market regimes and time granularities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is collected in compliance with Reddit's Data API Terms.

**Data Licensing**: The dataset is publicly available for non-commercial, research, and personal purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
