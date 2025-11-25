# Annotation and Classification of Sentence-level Revision Improvement

## 📊 Benchmark Details

**Name**: Annotation and Classification of Sentence-level Revision Improvement

**Overview**: Introduces a corpus of between-draft revisions of student argumentative essays annotated as to whether each revision improves essay quality (binary labels: Better / NotBetter). Demonstrates usage by developing a machine learning model to predict revision improvement and explores augmenting training data with expert edits from the AESW corpus, showing that blending expert and non-expert revisions can improve prediction performance.

**Data Type**: text (paired original and revised sentences)

**Domains**:
- Natural Language Processing
- Education

**Similar Benchmarks**:
- ArgRewrite
- Automated Evaluation of Scientific Writing (AESW)
- Tan and Lee (2014) sentence-level revisions corpus

**Resources**:
- [Resource](http://argrewrite.cs.pitt.edu)
- [Resource](http://www.petal.cs.pitt.edu/data.html)

## 🎯 Purpose and Intended Users

**Goal**: Predict whether a revised sentence is better than the original (binary classification of revision improvement) and create an annotated corpus to support development of automatic revision-assistance systems for argumentative essays.

**Target Audience**:
- Students
- Writing assistant developers
- Machine Learning Researchers

**Tasks**:
- Text Classification (Revision Improvement: Better vs NotBetter)

**Limitations**: Corpus size is small (940 ArgRewrite modification revisions). Annotation shows low inter-annotator agreement (Fleiss's kappa = 0.201 for all 940; 0.263 for majority ≥5). Annotation does not consider sentence context in paragraph. Class imbalance (784 Better vs 156 NotBetter). Performance on identifying NotBetter revisions remains low for some models.

## 💾 Data

**Source**: ArgRewrite subset (modification revisions) annotated for improvement; additionally two random samples drawn from the AESW corpus (expert edits) referred to as 'AESW all' and 'AESW plaintext'.

**Size**: ArgRewrite: 940 revisions; AESW samples: 5,000 revisions (AESW all) and 5,000 revisions (AESW plaintext).

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk with 7 annotators per revision; binary labels Better or NotBetter determined by majority voting; annotators provided explanatory comments; annotation guidelines provided in supplemental files.

## 🔬 Methodology

**Methods**:
- Random Forest classification (scikit-learn)
- 10-fold cross-validation
- SMOTE oversampling on training folds
- Feature selection on training folds
- Feature engineering using NLP features (unigrams, bigrams, trigrams, edit distance, BLEU, specificity, parse-tree features, language/spelling error counts, asymmetric distance metrics)

**Metrics**:
- Precision
- Recall
- F1 Score
- Fleiss's kappa

**Calculation**: Average unweighted Precision, Recall, and F1 computed across 10-fold cross-validation. Fleiss's kappa computed for annotation agreement. Parameters tuned using AESW development data. SMOTE applied per training fold; feature selection performed per training fold.

**Interpretation**: Higher Precision/Recall/F1 indicates better classification of Better vs NotBetter revisions. Statistical significance versus majority baseline was tested (p < 0.05) as reported.

**Baseline Results**: Majority baseline: Precision 0.417, Recall 0.500, F1 0.454. ArgRewrite only: Precision 0.570, Recall 0.534, F1 0.525. AESW plaintext: Precision 0.511, Recall 0.515, F1 0.473. ArgRewrite + AESW plaintext (best): Precision 0.574, Recall 0.555, F1 0.551.

**Validation**: 10-fold cross-validation with parameter tuning on AESW development set; SMOTE oversampling applied to address class imbalance; feature selection performed within each training fold.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: AESW dataset contains placeholders for anonymization (e.g., MATH, MATHDISP). No additional privacy or anonymization procedures for ArgRewrite are discussed in the paper.

**Data Licensing**: Freely available for research usage (data hosted at http://www.petal.cs.pitt.edu/data.html).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
