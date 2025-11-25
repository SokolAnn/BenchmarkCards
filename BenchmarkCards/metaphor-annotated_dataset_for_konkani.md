# Metaphor-annotated Dataset for Konkani

## 📊 Benchmark Details

**Name**: Metaphor-annotated Dataset for Konkani

**Overview**: This paper introduces a metaphor-annotated dataset for the Konkani language, specifically designed to facilitate research in metaphor classification using a hybrid model integrating mBERT with a BiLSTM.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Konkani

**Similar Benchmarks**:
- Konidioms Corpus

**Resources**:
- [Resource](https://anonymous.4open.science/r/KonkaniNLP)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to advance NLP for low-resource languages by providing a dataset for metaphor classification and promoting efficiency through model pruning.

**Target Audience**:
- NLP Researchers
- Linguists
- Model Developers

**Tasks**:
- Metaphor Classification
- Idiom Classification

**Limitations**: The corpus may not capture the full range of figurative expressions or dialectal variations present in Konkani.

## 💾 Data

**Source**: The dataset is an extension of the Konidioms Corpus, with 500 newly annotated Konkani sentences for metaphor classification, verified by native speakers.

**Size**: 500 sentences

**Format**: N/A

**Annotation**: Manually labeled by native Konkani speakers

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on model evaluation performance on the metaphor-annotated dataset.

**Interpretation**: An accuracy of 78% for metaphor classification indicates the model's capability to identify metaphorical constructs effectively.

**Validation**: Dataset was validated by splitting into balanced train/test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Annotations included verification by three native speakers to ensure linguistic accuracy.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Engaged native speakers for accuracy and cultural sensitivity in annotations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
