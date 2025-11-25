# A large -scale Twitter dataset for drug safety applications mined from publicly existing resources

## 📊 Benchmark Details

**Name**: A large -scale Twitter dataset for drug safety applications mined from publicly existing resources

**Overview**: Re-purpose a publicly available archived dataset of more than 9.4 billion Tweets with the objective of creating a very large dataset of drug usage-related tweets; provide a publicly available dataset of 1,181,993 tweet ids and code/procedure to extract these tweets for researchers to use in Pharmacovigilance research.

**Data Type**: text (Tweet IDs)

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/thepanacealab/InternetArchive-Pharmacovigilance-Tweets)
- [Resource](https://zenodo.org/record/3606863)

## 🎯 Purpose and Intended Users

**Goal**: Create a very large dataset of drug usage-related tweets to help train machine learning and deep learning models for Pharmacovigilance and drug safety research, and to provide code and tweet ids for reproducible extraction.

**Target Audience**:
- Researchers
- Machine Learning/Deep Learning researchers
- Pharmacovigilance researchers

**Tasks**:
- Text Classification
- Adverse Drug Reaction identification

**Limitations**: Only English tweets are used; no spelling correction module was employed (eliminating tweets with incorrect drug spellings); annotated training tweets were collected from publicly available sources (no new manual annotation was performed) and edge cases/ambiguous tweets were not considered.

## 💾 Data

**Source**: Internet Archive Twitter dataset (publicly available archived dataset of tweets for years 2012-2018) filtered using a drug dictionary and classification models.

**Size**: 1,181,993 tweets

**Format**: List of Tweet IDs (text); tweet text is NOT shared due to Twitter's terms of service

**Annotation**: No manual annotation of the released dataset; tweets were automatically classified (relevance) using machine learning models (trained on externally sourced annotated tweet datasets).

## 🔬 Methodology

**Methods**:
- Classical machine learning classification (Naive Bayes, Logistic Regression, Support Vector Machine, Random Forest, Decision Tree)
- Mixture model-based cutoff/threshold selection for probability scores
- Validation experiments using external annotated test sets

**Metrics**:
- Precision
- Recall
- F-measure
- Accuracy

**Calculation**: Metrics (precision, recall, F-measure, accuracy) were calculated on a stratified 75-25% (training-test) split of the annotated training set. Validation experiments used external annotated test sets (7,414 drug tweets and 7,414 non-drug tweets = 14,828 test tweets). Probability cutoffs for selecting tweets were determined by fitting a mixture of two Gaussians to model probability scores and selecting the deepest valley between peaks as threshold.

**Interpretation**: SVM was selected as the best model based on F-measure and Accuracy. High precision/recall/accuracy in validation experiments are presented as evidence that the dataset can be used to train models for Pharmacovigilance.

**Baseline Results**: Classical models (Table 6) on stratified 75-25% split: SVM — Precision 0.7773, Recall 0.8091, F-measure 0.7929, Accuracy 0.8456. Validation experiments (Table 8) — Experiment 1 best model SVM: Precision 0.9964, Recall 0.8331, F-measure 0.9075, Accuracy 0.9150; Experiment 2 best model SVM: Precision 0.9982, Recall 0.8369, F-measure 0.9104, Accuracy 0.9177.

**Validation**: Two bimodal classification validation experiments using classical machine learning models. Table 7 reports: Experiment 1 — Train data: 2,000,000 tweets; Test data: 14,828 tweets. Experiment 2 — Train data: 134,063,321 tweets; Test data: 14,828 tweets. The test set consists of 7,414 annotated drug tweets and 7,414 annotated non-drug tweets obtained from publicly available resources.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Legal

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Fairness**: Data bias

**Potential Harm**: Adverse Drug Reactions (ADRs) detection

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Due to Twitter's terms of service, tweet text cannot be shared; only tweet ids are publicly made available.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complies with Twitter's terms of service by sharing only tweet ids; no other regulatory compliance (e.g., GDPR) is discussed.
