# AQUAMUSE

## 📊 Benchmark Details

**Name**: AQUAMUSE

**Overview**: AQUAMUSE is a scalable methodology for automatically generating datasets for query-based multi-document summarization (qMDS), providing a specific instance with 5,519 query-based summaries derived from a large document corpus.

**Data Type**: query-based summaries

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/google-research-datasets/aquamuse)

## 🎯 Purpose and Intended Users

**Goal**: To generate a high-quality dataset for query-based multi-document summarization, reducing the cost of data collection for summarization models.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Data Scientists

**Tasks**:
- Multi-Document Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Google Natural Questions dataset and Common Crawl corpus.

**Size**: 5,519 examples

**Format**: N/A

**Annotation**: Automatically mined from question answering datasets and large document corpora.

## 🔬 Methodology

**Methods**:
- Automated mining
- Human evaluation

**Metrics**:
- Recall
- Precision

**Calculation**: Metrics calculated based on the semantic similarity between summaries and input documents.

**Interpretation**: Higher scores indicate better performance in generating relevant and coherent summaries.

**Validation**: Validated through human rater experiments and baseline summarization model evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
