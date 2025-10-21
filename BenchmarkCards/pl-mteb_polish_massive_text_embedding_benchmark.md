# PL-MTEB (Polish Massive Text Embedding Benchmark)

## 📊 Benchmark Details

**Name**: PL-MTEB (Polish Massive Text Embedding Benchmark)

**Overview**: PL-MTEB is a comprehensive benchmark for text embeddings in Polish consisting of 28 diverse NLP tasks from 5 task types, adapted based on previously used datasets by the Polish NLP community.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Polish

**Similar Benchmarks**:
- MTEB
- C-MTEB
- F-MTEB

**Resources**:
- [GitHub Repository](https://github.com/rafalposwiata/pl-mteb)

## 🎯 Purpose and Intended Users

**Goal**: To standardize the evaluation of text embedding models for the Polish language.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Clustering
- Pair Classification
- Information Retrieval
- Semantic Textual Similarity

**Limitations**: N/A

## 💾 Data

**Source**: PLSC (Polish Library of Science Corpus) consisting of titles and abstracts of scientific publications in Polish.

**Size**: 100,000 records

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy
- v-measure
- Average Precision
- Normalized Discounted Cumulative Gain at 10 (nDCG@10)
- Spearman correlation

**Calculation**: Metrics are calculated based on task-specific evaluations and aggregations.

**Interpretation**: Performance is evaluated based on the chosen metrics, with higher scores indicating better performance on respective tasks.

**Baseline Results**: N/A

**Validation**: Cross-evaluations conducted across multiple models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
