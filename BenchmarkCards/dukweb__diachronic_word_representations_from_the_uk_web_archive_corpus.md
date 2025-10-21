# DUKweb: Diachronic word representations from the UK Web Archive corpus

## 📊 Benchmark Details

**Name**: DUKweb: Diachronic word representations from the UK Web Archive corpus

**Overview**: DUKweb is a set of large-scale resources designed for the diachronic analysis of contemporary English, comprising co-occurrence matrices and two types of word embeddings for each year in the JISC UK Web Domain dataset.

**Data Type**: co-occurrence matrices and word embeddings

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.23636/1209)

## 🎯 Purpose and Intended Users

**Goal**: To provide resources for diachronic linguistic analyses of word meaning and to investigate changes in word semantics over time using computational methods.

**Target Audience**:
- ML Researchers
- Linguistic Researchers

**Tasks**:
- Semantic Change Detection
- Word Similarity
- Word Relatedness

**Limitations**: N/A

## 💾 Data

**Source**: JISC UK Web Domain Dataset (1996-2013)

**Size**: 330GB

**Format**: GZIP compressed text and CSV

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Temporal Random Indexing
- Word2Vec
- Orthogonal Procrustes

**Metrics**:
- Recall
- Cosine Similarity

**Calculation**: Metrics are calculated based on the embeddings and the respective evaluations performed on the dataset.

**Interpretation**: Higher recall values and cosine similarity indicate better performance in detecting semantic changes.

**Baseline Results**: N/A

**Validation**: Experimentation with SGNS and TRI models tested for reliability in detecting semantic change.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
