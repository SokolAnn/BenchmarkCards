# An Annotated Dataset for Explainable Interpersonal Risk Factors of Mental Disturbance in Social Media Posts

## 📊 Benchmark Details

**Name**: An Annotated Dataset for Explainable Interpersonal Risk Factors of Mental Disturbance in Social Media Posts

**Overview**: We construct and release a new annotated dataset with human-labelled explanations and classification of Interpersonal Risk Factors (IRF) affecting mental disturbance on social media: (i) Thwarted Belongingness (TBE), and (ii) Perceived Burdensomeness (PBU).

**Data Type**: text (Reddit social media posts) with extractive explanations (text-span annotations) and binary labels

**Domains**:
- Natural Language Processing
- Healthcare
- Mental Health

**Languages**:
- English

**Similar Benchmarks**:
- SDCNL dataset
- Suicide Notes

**Resources**:
- [GitHub Repository](https://github.com/drmuskangarg/Irf)
- [Resource](https://arxiv.org/abs/2305.18727)

## 🎯 Purpose and Intended Users

**Goal**: To construct and release an annotated Reddit dataset for discovering interpersonal risk factors through human-annotated extractive explanations (text-spans) and binary labels for Thwarted Belongingness (TBE) and Perceived Burdensomeness (PBU) to support research and applications in mental health screening and explainable NLP.

**Target Audience**:
- Social NLP research community
- Clinical psychologists and mental health practitioners
- Machine learning researchers and model developers

**Tasks**:
- Text Classification
- Binary Classification
- Extractive Explanation (text-span extraction)

**Limitations**: There might be linguistic discrepancies between Reddit users and Twitter users; social media users may intentionally post such thoughts to gain attention but for simplicity the authors assume posts are credible; annotation is subjective and interpretation about wellness dimensions may vary between annotators.

**Out of Scope Uses**:
- Clinical diagnosis

## 💾 Data

**Source**: Collected Reddit posts from r/depression and r/SuicideWatch via PRAW API from 02 December 2021 to 04 January 2022 combined with 1,896 posts from the SDCNL dataset; final corpus filtered and limited to posts up to 300 words resulting in 3,522 posts.

**Size**: 3,522 posts

**Format**: N/A

**Annotation**: Manual annotation by three trained postgraduate annotators guided and validated by a team of three experts (clinical psychologist, rehabilitation counselor, social NLP expert); majority voting for binary labels <TBE,PBU>; extractive text-span explanations provided for positive instances; inter-annotator agreement reported via Fliess' Kappa (78.83% for TBE, 82.39% for PBU) and group annotation agreement metrics.

## 🔬 Methodology

**Methods**:
- Automated model evaluation (RNNs: LSTM, GRU; Transformer-based models: BERT, RoBERTa, DistilBERT, MentalBERT; OpenAI embeddings + classifiers: Logistic Regression, Random Forest, SVM, MLP, XGBoost)
- Explainability evaluation using LIME and SHAP compared against ground-truth explanations
- Human annotation with majority-vote aggregation

**Metrics**:
- Precision
- Recall
- F1-score
- Accuracy
- ROUGE Precision/Recall/F1 (for comparing extracted explanations to ground truth)
- Pearson Correlation Coefficient (PCC)
- Fliess' Kappa (inter-annotator agreement)

**Calculation**: All classification metrics (Precision/Recall/F1/Accuracy) computed on the test set (30% of dataset). ROUGE scores used to compare top keywords/text-spans from LIME/SHAP to ground-truth explanations. Fliess' Kappa used to compute inter-annotator agreement. Pearson Correlation Coefficient computed between TBE and PBU labels.

**Interpretation**: Higher Precision/Recall/F1/Accuracy indicate better classification performance; ROUGE P/R/F measure overlap between generated explanations and ground-truth text-spans; authors note moderate model performance and emphasize the need to reduce false negatives for practical mental health triaging; high recall in explainability indicates ability to identify relevant text-spans but with scope to reduce superfluous spans.

**Baseline Results**: MentalBERT achieved F1-scores of 76.73% (TBE) and 62.77% (PBU). OpenAI embeddings + Logistic Regression achieved F1-score 81.23% (TBE). OpenAI embeddings + SVM achieved F1-score 76.90% (PBU). (See Table 3 in paper for full precision, recall, F1, and accuracy per model.)

**Validation**: Dataset split into train/validation/test with test set = 30% of data. Grid search used for hyperparameter optimization. Inter-annotator agreement validated using Fliess' Kappa and group annotation agreement metrics for extractive explanations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy
- Misuse

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Misuse**: Improper usage

**Demographic Analysis**: N/A

**Potential Harm**: We recognize the huge impact of false negatives in practical use of applications such as mental health triaging.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Users' IDs are anonymized. All sample posts shown are anonymized, obfuscated, and paraphrased for user privacy and to prevent misuse. The authors state that this study does not require ethical approval.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
