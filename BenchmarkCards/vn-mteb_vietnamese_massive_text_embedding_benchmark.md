# VN-MTEB (Vietnamese Massive Text Embedding Benchmark)

## 📊 Benchmark Details

**Name**: VN-MTEB (Vietnamese Massive Text Embedding Benchmark)

**Overview**: VN-MTEB is a substantial benchmark consisting of 41 datasets from 6 tasks (retrieval, reranking, classification, clustering, pair classification, and semantic textual similarity), designed to evaluate text embeddings for the Vietnamese language.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Vietnamese

**Similar Benchmarks**:
- MTEB (Massive Text Embedding Benchmark)

**Resources**:
- [Resource](https://huggingface.co/datasets/mteb)

## 🎯 Purpose and Intended Users

**Goal**: To create a large-scale benchmark for comparing different text embedding models in Vietnamese.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Retrieval
- Reranking
- Classification
- Clustering
- Pair Classification
- Semantic Textual Similarity

**Limitations**: N/A

## 💾 Data

**Source**: Translated datasets from the Massive Text Embedding Benchmark into Vietnamese.

**Size**: 41 datasets

**Format**: JSON

**Annotation**: Automatically translated and filtered using a new automated framework.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Evaluation done through similarity scoring between queries and document embeddings using cosine similarity.

**Interpretation**: Higher scores indicate better performance of embedding models in the benchmark tasks.

**Baseline Results**: Results from 18 embedding models averaged from 41 datasets across 6 tasks.

**Validation**: Datasets validated through a filtering pipeline ensuring high-quality translations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0 and other licenses as specified per dataset.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
