# Sinhala-English Word Embedding Alignment: Introducing Datasets and Benchmark for a Low Resource Language

## 📊 Benchmark Details

**Name**: Sinhala-English Word Embedding Alignment: Introducing Datasets and Benchmark for a Low Resource Language

**Overview**: This paper introduces a benchmark for Sinhala word embedding alignment and provides alignment datasets for supervised word embedding alignment.

**Data Type**: word embedding alignment pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Sinhala
- English

**Resources**:
- [Resource](https://bit.ly/3t3SKu7)
- [GitHub Repository](https://github.com/facebookresearch/MUSE)

## 🎯 Purpose and Intended Users

**Goal**: To set a benchmark for Sinhala word embedding alignment and to provide aligned embeddings for the Sinhala-English language pair.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Linguists

**Tasks**:
- Word Embedding Alignment

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed from parallel word dictionaries obtained from sources like CCAligned and OpenSubtitles.

**Size**: 5,000 word pairs

**Format**: JSON

**Annotation**: Manual annotation using word relationships identified by statistical evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Procrustes analysis
- RCSLS technique
- CSLS criterion

**Metrics**:
- Top-1 Precision
- Top-5 Precision
- Top-10 Precision

**Calculation**: Metrics are calculated based on the retrieval accuracy of aligned word embedding pairs in pre-defined benchmark datasets.

**Interpretation**: Higher precision values indicate better alignment between Sinhala and English word embeddings.

**Validation**: The alignment dataset's effectiveness was validated through multiple iterations of embedding alignment techniques.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
