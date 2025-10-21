# ARAACOM: ARAbic Algerian Corpus for Opinion Mining

## 📊 Benchmark Details

**Name**: ARAACOM: ARAbic Algerian Corpus for Opinion Mining

**Overview**: To reduce the gap of publicly-available Arabic datasets for sentiment analysis we have created ARAACOM (ARAbic Algerian Corpus for Opinion Mining), a corpus dedicated for this work. Comments are collected from the website of the Algerian newspaper Echorouk. We propose an approach to classify Arabic comments from Algerian Newspapers into positive and negative classes.

**Data Type**: text (newspaper comments / opinionated comments)

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Modern Standard Arabic

**Similar Benchmarks**:
- OCA
- EVOCA
- ACOM

**Resources**:
- [Resource](https://www.echoroukonline.com)
- [Resource](https://rapidminer.com/)
- [Resource](https://www.aljazeera.net)
- [Resource](https://www.amazon.com)

## 🎯 Purpose and Intended Users

**Goal**: Create a corpus (ARAACOM) of Algerian Arabic newspaper comments to support sentiment analysis and to classify comments into positive and negative classes.

**Target Audience**:
- Researchers in Natural Language Processing
- Researchers in Sentiment Analysis

**Tasks**:
- Sentiment Analysis
- Text Classification

**Limitations**: Small dataset size (92 comments after balancing); neutral comments removed from the corpus; many spelling mistakes requiring manual correction; comments sometimes written partially or totally in French and manually translated to Modern Standard Arabic; corpus built from a single newspaper (Echorouk) limiting domain generality; majority of comments are negative leading to class imbalance; F_measure remains modest and needs more work to improve.

## 💾 Data

**Source**: Comments collected from the Echorouk newspaper website (https://www.echoroukonline.com); articles cover several topics (News, politics, sport, culture).

**Size**: 92 comments (3,354 tokens) after equilibrium; initially 147 comments were collected before balancing (32 positive, 91 negative, 24 neutral).

**Format**: Raw text (UTF-8); no formal dataset file format (e.g., CSV/JSON) specified in the paper.

**Annotation**: Manual annotation by the authors: comments read and labeled into binary classes Positive and Negative; neutral comments removed from the corpus.

## 🔬 Methodology

**Methods**:
- Support Vector Machines (SVM)
- Naïve Bayes (NB)
- 10-fold Cross-Validation
- Preprocessing: tokenization, stop words removal, stemming, manual correction/translation
- Feature extraction: Unigram and Bigram n-grams; Term Occurrence (TO), Term Frequency (TF), TF-IDF, Binary Term Occurrence (BTO)

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy

**Calculation**: Precision = TP / (TP + FP). Recall = TP / (TP + FN). F1_measure = 2 × Precision × Recall / (Precision + Recall).

**Interpretation**: Precision and recall are complementary; F1_measure is used as a compromise between precision and recall. High precision indicates stronger predictive correctness for the positive class; higher recall indicates more complete retrieval of positive instances. The authors report strong precision in many settings but modest F1 overall.

**Baseline Results**: Comparison with OCA [21]: Using SVM (term frequency, Anova kernel): ARAACOM Unigram Precision=96.67%, Recall=72.50%, F1=82.86%; ARAACOM Bigram Precision=100%, Recall=71.67%, F1=83.50%. OCA Unigram Precision=86.99%, Recall=95.20%, Accuracy=90.20%; OCA Bigram Precision=87.38%, Recall=95.20%, Accuracy=90.60%. With Naïve Bayes: ARAACOM Unigram Precision=97.50%, Recall=69.17%, F1=80.93%; OCA Unigram Precision=79.99%, Recall=85.60%, Accuracy=81.80%.

**Validation**: 10-fold cross-validation was used to train and evaluate classifiers; results compared against published results on the OCA corpus.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
