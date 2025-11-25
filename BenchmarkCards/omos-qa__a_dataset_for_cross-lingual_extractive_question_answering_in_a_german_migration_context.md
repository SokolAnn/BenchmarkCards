# OMoS-QA: A Dataset for Cross-Lingual Extractive Question Answering in a German Migration Context

## 📊 Benchmark Details

**Name**: OMoS-QA: A Dataset for Cross-Lingual Extractive Question Answering in a German Migration Context

**Overview**: OMoS-QA is a manually annotated corpus of questions in German and English paired with relevant information documents about social, economic, and legal topics designed for supporting online migration counseling. It consists of 906 question-answer pairs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- German
- English

**Similar Benchmarks**:
- SQuAD
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/digitalfabrik/integreat-qa-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide high-precision, knowledge-grounded answers to users who have freshly immigrated to Germany.

**Target Audience**:
- NLP Researchers
- Developers of AI counseling systems

**Tasks**:
- Extractive Question Answering
- Cross-Lingual Question Answering

**Limitations**: The current version of OMoS-QA is limited to German and English documents and questions.

## 💾 Data

**Source**: Documents were provided by three German municipalities and manually annotated through crowdsourcing.

**Size**: 906 question-answer pairs

**Format**: JSON

**Annotation**: Questions were generated using an open-weight large language model and answers were manually annotated by crowd workers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are computed per question at the sentence level and then macro-averaged over questions.

**Interpretation**: Higher precision indicates fewer, but more accurate responses.

**Validation**: The dataset utilized inter-annotator agreement studies to filter for quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Data includes questions generated from diverse societal topics relevant to the migrant experience.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All annotators participated voluntarily and agreed to anonymized publishing of their annotations.

**Data Licensing**: The dataset will be published under a CC-BY license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
