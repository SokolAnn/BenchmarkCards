# Morphological Analyzer for Gujarati

## 📊 Benchmark Details

**Name**: Morphological Analyzer for Gujarati

**Overview**: This paper presents a Morphological Analyzer for Gujarati, which performs morpheme boundary detection and grammatical feature tagging. It introduces a dataset of Gujarati words with lemma and grammatical features.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Gujarati

**Resources**:
- [Resource](http://http://tdil-dc.in)

## 🎯 Purpose and Intended Users

**Goal**: To develop a morphological analyzer for Gujarati that performs morpheme boundary detection and grammatical feature tagging.

**Target Audience**:
- ML Researchers
- Linguists
- NLP Practitioners

**Tasks**:
- Morpheme Boundary Detection
- Grammatical Feature Tagging

**Limitations**: N/A

## 💾 Data

**Source**: Created from Gujarati Monolingual Text Corpus and TDIL resources.

**Size**: 16,527 unique words

**Format**: Unimorph format

**Annotation**: Manually annotated with lemma and grammatical features.

## 🔬 Methodology

**Methods**:
- Neural network based evaluation
- Bi-Directional LSTM approach

**Metrics**:
- Accuracy
- Precision
- Recall

**Calculation**: Accuracy calculated based on the number of correctly predicted words out of the total number of words in the test set.

**Interpretation**: Higher accuracy indicates better performance in morpheme boundary detection and feature tagging.

**Baseline Results**: Neural model accuracy: Noun 90.57%, Verb 86.96%, Adjective 97.49%. Compared to unsupervised model Morphessor efficiency.

**Validation**: Training and testing split at an 80:20 ratio.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
