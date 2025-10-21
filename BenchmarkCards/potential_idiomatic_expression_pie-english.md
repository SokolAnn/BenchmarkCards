# Potential Idiomatic Expression (PIE)-English

## 📊 Benchmark Details

**Name**: Potential Idiomatic Expression (PIE)-English

**Overview**: We present a fairly large, Potential Idiomatic Expression (PIE) dataset for Natural Language Processing (NLP) in English, containing over 20,100 samples with almost 1,200 cases of idioms classified into 10 different classes.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/tosingithub/idesk)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of this work is to create a high-quality corpus of potential idiomatic expressions in the English language and make it publicly available for NLP researchers.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Machine Translation
- Word Sense Disambiguation
- Information Retrieval

**Limitations**: A limitation of the PIE-English dataset, which seems inevitable, is the dominance of metaphors, since metaphors are the most common figures of speech.

## 💾 Data

**Source**: British National Corpus (BNC) and UK Web Pages (UKWaC)

**Size**: 20,174 samples

**Format**: CSV

**Annotation**: Annotated by two independent annotators with an overall inter-annotator agreement (IAA) score of 88.89%.

## 🔬 Methodology

**Methods**:
- Multinomial Naive Bayes Classifier
- Linear SVM
- BERT

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy and F1 Score were calculated for each class and overall across the dataset.

**Interpretation**: Good results are obtained when classifying idioms, especially using BERT which outperformed other classifiers.

**Baseline Results**: BERT: Accuracy 0.934, F1 Score 0.948; SVM: Accuracy 0.766, F1 Score 0.67; mNB: Accuracy 0.747, F1 Score 0.66.

**Validation**: Stratified data-split for training and validation sets was done to address the class imbalance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Contributors are predominantly L2 English speakers, but detailed demographic analysis beyond this is not specified.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
