# Next-Year Bankruptcy Prediction from Textual Data: Benchmark and Baselines

## 📊 Benchmark Details

**Name**: Next-Year Bankruptcy Prediction from Textual Data: Benchmark and Baselines

**Overview**: Introduces a reproducible benchmark for text-based (unstructured) next-year bankruptcy prediction, based on novel and established economic datasets, and describes/evaluates classical and neural baseline models to stimulate further research.

**Data Type**: text (10-K reports: Management Discussion and Analysis sections)

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- N/A

**Similar Benchmarks**:
- UCLA-LoPucki Bankruptcy Research Database (BRD)
- EDGAR-CORPUS

**Resources**:
- [GitHub Repository](https://github.com/henriarnoUG/BankruptcyBenchmarkBaselines)
- [Resource](https://lopucki.law.ucla.edu/)
- [Resource](https://www.sec.gov/fast-answers/answersreada10khtm.html)

## 🎯 Purpose and Intended Users

**Goal**: Introduce a reproducible benchmark for text-based next-year bankruptcy prediction using textual data, provide baseline models and evaluation, and enable reproducible comparison between models.

**Target Audience**:
- Researchers

**Tasks**:
- Binary Classification
- Bankruptcy Prediction

**Limitations**: Focuses on prediction from textual disclosures only (does not include combined textual and structured features in this benchmark). The authors state they are not allowed to make the resulting datasets public directly (BRD licensing).

## 💾 Data

**Source**: EDGAR-CORPUS (10-K reports) matched with the UCLA-LoPucki Bankruptcy Research Database (BRD) via the Central Index Key.

**Size**: EDGAR-CORPUS contains 10-K reports spanning 25 years (period 2000-2021). Summary statistics reported: avg. reports per year 7,599 ±1,477; avg. bankruptcies per year 39 ±26; avg. document length 6,492 ±1,138 tokens.

**Format**: N/A

**Annotation**: Firm-year binary labels: for each firm-year, label = 1 if the company filed for bankruptcy during the one-year prediction window after the filing date (T_prediction), otherwise 0. Missing reports are represented with the token 'missing'.

## 🔬 Methodology

**Methods**:
- Baseline models: Binary Bag-of-Words (logistic regression), TF-IDF + logistic regression, Word2Vec mean embedding + feed-forward neural network, Longformer encoder + feed-forward classifier
- Automated metrics (ranking and classification metrics)
- Temporal out-of-period train/validation/test splits (training data up to 2015/2017; validation on 2017 and 2018; test on 2019 and 2020)
- Undersampling of majority class for training (to 90%-10% distribution)
- Hyperparameter optimization (grid search for classical models; Tree-Structured Parzen Estimation via Optuna for neural models)

**Metrics**:
- Area Under the Receiver Operating Curve (AUC)
- Recall@100
- Average Precision (AP)
- Cumulative Accuracy Profile Ratio (CAP)
- Cumulative Decile Rank

**Calculation**: AUC: area under the ROC aggregating true positive vs false positive rates across thresholds. Recall@100: proportion of positive cases (bankrupt firms) present in the 100 highest ranked samples. AP: weighted mean of precision at each threshold with increase in recall as weight. CAP: summarizes the CAP curve (cumulative positives vs percentage of ranked data). Cumulative Decile Rank: cumulative proportion of positives in each decile when ranking by classifier score.

**Interpretation**: AUC quantifies overall binary prediction performance. Recall-oriented metrics (Recall@100, CAP, cumulative decile rank) emphasize the model's ability to detect distressed firms within a fixed investigation budget. AP reports precision-oriented performance across thresholds. The authors prioritize AUC for model selection but consider recall-oriented metrics important for practical use.

**Baseline Results**: Selected AUC results on test sets 2019 (2020) from Table 3 — Single-year history AUCs: Binary 0.79 (0.84), TF-IDF 0.80 (0.85), W2V 0.88 (0.90), Longformer 0.78 (0.79). Three-year history AUCs: Binary 0.90 (0.92), TF-IDF 0.92 (0.96), W2V 0.95 (0.95), Longformer 0.85 (0.84).

**Validation**: Two validation sets (2017 and 2018) are used for hyperparameter tuning. Hyperparameters are tuned to maximize the weighted AUC on the 2017 and 2018 validation data. Final models are trained on data up to 2017 and evaluated on test sets 2019 and 2020. Training uses undersampling of majority class and Optuna/TPE for neural model hyperparameter search.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Data Laws
- Governance

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Data Laws**: Data usage restrictions
- **Governance**: Lack of data transparency, Unrepresentative risk testing

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The UCLA-LoPucki Bankruptcy Research Database (BRD) requires a paid annual subscription or a one-time purchase for academic single use; the authors state they are not allowed to make the resulting reconstructed datasets public directly. EDGAR 10-K reports are public per the U.S. Securities and Exchange Commission.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
