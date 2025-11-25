# StackOverﬂow design-related dataset

## 📊 Benchmark Details

**Name**: StackOverﬂow design-related dataset

**Overview**: A StackOverflow-based dataset of questions and answers (tagged 'design' and non-design) used to evaluate classifiers that detect software design discussions and to study cross-dataset transfer (conclusion stability) of design-mining approaches.

**Data Type**: question-answering pairs (StackOverflow questions and answers)

**Domains**:
- Software Engineering
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Brunet 2014 dataset
- Shakiba 2016 dataset
- Viviani 2018 dataset
- SATD dataset

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.3590126)
- [Resource](https://arxiv.org/abs/2001.01424)

## 🎯 Purpose and Intended Users

**Goal**: RO1: Assess, by replication, whether it is possible to accurately label a natural language discussion as pertaining to software design (strict and operational replication of Brunet et al.). RO2: Evaluate to what extent classifiers trained on one dataset transfer to other datasets and whether transfer-learning approaches (e.g., ULMFiT) improve conclusion stability for design mining.

**Target Audience**:
- Researchers in Software Engineering
- Researchers working on mining software repositories and NLP for software engineering
- Developers of design-mining or automated documentation tools

**Tasks**:
- Text Classification
- Document Classification
- Transfer Learning Evaluation (cross-dataset classification)

**Limitations**: Explicitly stated limitations include limited labeled data (low power), dataset imbalance, overfitting to particular datasets leading to poor conclusion stability, and the improbability of expecting classifiers trained on one dataset to transfer well to totally different datasets without retraining.

## 💾 Data

**Source**: 26,969 StackOverflow questions and answers tagged 'design' (extracted from the SOTorrent dataset) combined with 25,000 random StackOverflow questions not tagged 'design'; other datasets used in experiments include Brunet 2014 (pull requests), Shakiba 2016 (commit messages), Viviani 2018 (pull request paragraphs), and SATD (code comments).

**Size**: 51,969 documents

**Format**: N/A

**Annotation**: Positive examples: posts tagged with 'design' (extracted from SOTorrent). Negative examples: randomly selected StackOverflow questions not tagged 'design'. (Other datasets include manual labeling as reported in their original sources, e.g., Brunet's 1,000 manually labeled discussions.)

## 🔬 Methodology

**Methods**:
- 10-fold cross-validation
- Train-validate-test split (60%/20%/20%) for ULMFiT
- Stratified sampling
- SMOTE oversampling for class imbalance
- Within-dataset and cross-dataset evaluation (cross-dataset transfer tests)

**Metrics**:
- Area Under ROC Curve (AUC)
- Accuracy
- Precision
- Recall
- F1 Score
- Train and validation loss (for ULMFiT model selection)

**Calculation**: Classical learners evaluated using 10-fold cross-validation (means reported). AUC used as a balanced metric for imbalanced datasets. ULMFiT evaluated with a 60/20/20 train/validation/test split and model selection via monitoring train and validation loss; reported AUC and other metrics on held-out test sets.

**Interpretation**: AUC is used as a preferred metric for the minority 'design' class on imbalanced datasets. Higher AUC indicates better balanced classification of design discussions. Within-dataset performance is substantially better than cross-dataset performance; ULMFiT yielded strong within-sample results but did not materially improve cross-dataset conclusion stability compared to classical approaches.

**Baseline Results**: ZeroR baseline (majority-class) is ~0.86 accuracy given average 14% prevalence. Replication of Brunet: Naive Bayes accuracy 0.862 and Decision Tree accuracy 0.931 (original reported values reproduced). Doc2Vec on the StackOverflow corpus: training accuracy 0.934 and held-out test accuracy 0.932 (balanced dataset). NewBest (word embeddings + SVM / or TF-IDF + Logistic Regression variants) achieved AUC up to 0.84. ULMFiT within-sample AUC approximately 0.93 during training, but cross-dataset transfer performance remained poor (transfer AUCs often near or below reasonable baselines).

**Validation**: Validation included stratified folds, SMOTE for imbalance correction, 10-fold cross-validation for classical models, and held-out validation sets for ULMFiT (60/20/20 split) with monitoring of train and validation loss to select models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Governance

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Governance**: Lack of data transparency, Lack of testing diversity

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
