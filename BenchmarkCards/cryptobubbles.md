# CryptoBubbles

## 📊 Benchmark Details

**Name**: CryptoBubbles

**Overview**: CryptoBubbles: a novel multi-span identification task for bubble detection and a publicly released dataset comprising tweets, financial data, and speculative bubbles for 400+ cryptocoins over five years. The benchmark is intended for multi-span crypto bubble forecasting and evaluation of models (e.g., hyperbolic sequence-to-sequence models) under standard and zero-shot settings.

**Data Type**: text (social media posts: tweets and Reddit posts) and time-series (daily price data)

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/gtfintechlab/CryptoBubbles-NAACL)
- [Resource](https://arxiv.org/abs/2206.06320)
- [Resource](https://www.cryptocompare.com/)
- [GitHub Repository](https://github.com/pushshift/api)
- [GitHub Repository](https://github.com/ferrine/hyrnn)

## 🎯 Purpose and Intended Users

**Goal**: To formulate CryptoBubbles, a multi-span crypto bubble forecasting task, publicly release a dataset of crypto-related social media and price data, and provide hyperbolic models (MBHN) for modeling power-law dynamics in social media-driven speculative bubbles.

**Target Audience**:
- ML Researchers
- Financial Researchers
- Industry Practitioners

**Tasks**:
- Time Series Forecasting
- Event Detection
- Multi-span Extraction

**Limitations**: MBHN and the benchmark have limited interpretability (MBHN provides limited interpretability to its outputs). The dataset is heavily skewed; the evaluation set contains new cryptos and spans the COVID-19 period, making CryptoBubbles challenging. Potential for exploitation exists as MBHN could be used to hinder market fairness; authors encourage following regulatory and ethical considerations.

## 💾 Data

**Source**: Daily price data (opening, closing, high, low) from CryptoCompare for cryptocoins (1 Mar 2016 to 7 Apr 2021); crypto-related tweets extracted under Twitter's official license via regex ticker queries; zero-shot Reddit posts/comments mined via PushshiftAPI; equities price data from Yahoo Finance and CoinGecko for zero-shot evaluation.

**Size**: Initial selection: 456 cryptocoins; reported overall No. of Bubbles: 1,869; mined ~2.4 million tweets (Train: 1.15M, Validation: 730K, Test: 561K); date range 1 Mar 2016 to 7 Apr 2021. Appendix reports a final set of 404 cryptos after filtering.

**Format**: N/A

**Annotation**: Bubble spans were identified using the PSY model (Phillips et al., 2015b) on closing prices and then reviewed by five experienced financial analysts (Cohen's kappa = 0.93). Reviewers agreed with annotations for 90% of bubbles; majority vote used on disagreements; for 5% all reviewers agreed annotations were incorrect and analysts' proposals were used.

## 🔬 Methodology

**Methods**:
- Automated evaluation using standard metrics (F1-score, Matthews Correlation Coefficient, Exact Match, Accuracy)
- Zero-shot evaluation on a curated Reddit meme-stock dataset
- Ablation studies (component-wise evaluation)
- Qualitative analysis (attention visualizations and case studies)

**Metrics**:
- F1 Score
- Matthews Correlation Coefficient (MCC)
- Exact Match (EM)
- Accuracy

**Calculation**: Metric definitions and equations provided in Appendix: MCC computed from confusion matrix as per formula in Appendix; F1 as harmonic mean of precision and recall; Exact Match measures percentage of predicted bubbles that exactly match true bubble spans.

**Interpretation**: MCC ranges from -1 to +1 where +1 is perfect prediction, 0 is random prediction, and -1 is inverse prediction. F1 is harmonic mean of precision and recall. EM is percentage of predicted bubbles that exactly match true spans.

**Baseline Results**: Baseline comparison (mean of 10 runs) on bubble span task: ARIMA F1 0.02 MCC 0.00 EM 0.02; W-LSTM F1 0.09 MCC 0.04 EM 0.03; A-LSTM F1 0.45 MCC 0.13 EM 0.39; Chaotic F1 0.49 MCC 0.14 EM 0.45; MAN-SF(T) F1 0.49 MCC 0.16 EM 0.46; CH-RNN F1 0.50 MCC 0.19 EM 0.47; SN-HFA F1 0.51 MCC 0.21 EM 0.49; MBHN (Ours) F1 0.53 MCC 0.25 EM 0.53.

**Validation**: Temporal chronological split into Train/Validation/Test with date ranges: Train 03/16 - 07/20, Validation 07/20 - 12/20, Test 12/20 - 04/21. Hyperparameter tuning via grid search on validation MCC; early stopping based on validation Accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Data Laws
- Misuse
- Explainability
- Accuracy

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Privacy**: Data privacy rights alignment
- **Misuse**: Improper usage
- **Explainability**: Unexplainable output
- **Accuracy**: Unrepresentative data

**Potential Harm**: Detect speculative financial bubbles and forecast speculative risks driven by social media hype.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authors use publicly available Twitter and Reddit data in a purely observational and non-intrusive manner. Informed consent of each user was not sought; authors state they follow all ethical regulations set by Twitter and Reddit.

**Data Licensing**: Tweet extraction performed under Twitter's official license; PushshiftAPI used for Reddit. No explicit dataset release license is specified in the paper.

**Consent Procedures**: Informed consent of each user was not sought as it may be deemed coercive (explicitly stated).

**Compliance With Regulations**: Authors state they follow all ethical regulations set by Twitter and Reddit and evaluate only on public data in regulated markets.
