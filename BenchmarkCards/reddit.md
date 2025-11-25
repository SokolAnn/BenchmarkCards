# ReDDIT

## 📊 Benchmark Details

**Name**: ReDDIT

**Overview**: A novel annotated dataset of Reddit texts classified into three classes: Regret by Action, Regret by Inaction, and No Regret; additionally each text is annotated with a domain label. The dataset is used to investigate language expressing regret on Reddit and to identify domains most commonly associated with regret, and to benchmark several machine learning and deep learning models.

**Data Type**: text (Reddit posts: title + main text)

**Domains**:
- Natural Language Processing
- Social Media Analysis

**Languages**:
- English

**Similar Benchmarks**:
- REGRETS
- PolyHope

**Resources**:
- [Resource](https://arxiv.org/abs/2212.07549)
- [GitHub Repository](https://github.com/pushshift/api)
- [Resource](https://pypi.org/project/pmaw/)

## 🎯 Purpose and Intended Users

**Goal**: To present and analyze the first annotated dataset for regret detection and domain identification in English Reddit posts, and to benchmark baseline and state-of-the-art models on these tasks.

**Target Audience**:
- Natural Language Processing researchers
- Social media platform designers

**Tasks**:
- Text Classification (Regret Detection)
- Text Classification (Domain Identification)

**Limitations**: Imbalanced label distribution in the dataset (e.g., majority of posts related to Romance and Relationships, fewer posts for Health) which may impact model performance.

## 💾 Data

**Source**: Scraped Reddit posts from three subreddits: "regret", "regretfulparents", and "confession" for the period 01-01-2000 to 10-09-2022 using the Pushshift API and the PMAW framework. Empty or deleted posts were discarded; sampling and filtering steps applied (see paper).

**Size**: 3,425 posts

**Format**: N/A

**Annotation**: Manual annotation by three annotators (backgrounds in IT and computer science) following provided guidelines. Labels: Regret Detection (Regret by Action, Regret by Inaction, No Regret) and Domain Identification (Education, Health, Career and Finance, Romance and Relationships, Other Domains). Fleiss' kappa reported.

## 🔬 Methodology

**Methods**:
- Traditional machine learning baselines (Logistic Regression, SVM with RBF and linear kernels, Random Forest Classifier, XGBoost, AdaBoost) with uni-gram TF-IDF features
- Deep learning models (CNN, BiLSTM) with pre-trained word embeddings (GloVe, fastText)
- Five-fold cross-validation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- Averaged-weighted F1
- Averaged-macro F1

**Calculation**: Metrics computed as averages over five-fold cross-validation; both averaged-weighted and averaged-macro scores are reported for experiments.

**Interpretation**: Performance is reported using averaged-weighted and averaged-macro scores over five-fold cross-validation. The paper reports that deep learning models using GloVe embeddings outperformed other models; e.g., CNN with GloVe (text+title) obtained an averaged-macro F1 of 0.715 for regret detection, and BiLSTM with GloVe (text+title) obtained an averaged-macro F1 of 0.629 for domain identification.

**Baseline Results**: Best reported results: Regret Detection — CNN with GloVe (text + title): averaged-macro F1 = 0.715 (averaged-weighted F1 = 0.759, Accuracy = 0.764). Domain Identification — BiLSTM with GloVe (text + title): averaged-macro F1 = 0.629 (averaged-weighted F1 = 0.816, Accuracy = 0.814). Logistic Regression baselines: regret detection (only text) averaged-macro F1 = 0.559; domain identification (text+title) averaged-macro F1 = 0.579.

**Validation**: Annotation inter-annotator agreement measured with Fleiss' kappa: 0.78 for regret detection and 0.84 for domain identification. Models evaluated using five-fold cross-validation and average scores reported.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
