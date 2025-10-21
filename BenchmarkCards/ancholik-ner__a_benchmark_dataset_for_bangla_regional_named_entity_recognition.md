# ANCHOLIK-NER: A Benchmark Dataset for Bangla Regional Named Entity Recognition

## 📊 Benchmark Details

**Name**: ANCHOLIK-NER: A Benchmark Dataset for Bangla Regional Named Entity Recognition

**Overview**: We introduce ANCHOLIK-NER, the first benchmark dataset for Named Entity Recognition (NER) in Bangla regional dialects, comprising 17,405 sentences distributed across five regions. The dataset was sourced from publicly available resources and supplemented with manual translations, ensuring alignment of named entities across dialects.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bangla

**Resources**:
- [Resource](https://doi.org/10.17632/8yy9whnn56.1)

## 🎯 Purpose and Intended Users

**Goal**: To bridge the gap in NER resources for Bangla dialects, which have been underrepresented in computational linguistics.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Data Scientists

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available resources and manual translations.

**Size**: 17,405 sentences

**Format**: CSV

**Annotation**: Annotated using the BIO tagging scheme by native speakers of the respective dialects.

## 🔬 Methodology

**Methods**:
- Evaluation of transformer models: Bangla BERT, Bangla BERT Base, and BERT Base Multilingual Cased

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Precision calculates the proportion of true positive named entities identified out of all entities classified as positive; Recall measures the proportion of true positive identified out of all actual positive entities; F1-Score is the harmonic mean of precision and recall.

**Interpretation**: F1-Score provides a balance between precision and recall. A higher score indicates better performance.

**Baseline Results**: F1-score of 82.611% in Mymensingh with BERT Base Multilingual Cased model.

**Validation**: The dataset was validated by native speakers for consistency and annotation quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset includes translations and annotations with respect to privacy, ensuring no personal identifiers are included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
