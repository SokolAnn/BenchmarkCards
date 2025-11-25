# Multi-Source Knowledge Pruning Benchmark

## 📊 Benchmark Details

**Name**: Multi-Source Knowledge Pruning Benchmark

**Overview**: This benchmark standardizes a dataset that integrates structured and unstructured knowledge across diverse domains for retrieval-augmented generation (RAG). It provides a foundation for future research in mitigating hallucinations and improving reasoning capabilities in LLMs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RGB
- CRUD-RAG
- RAG-Bench
- RAGEval

**Resources**:
- [GitHub Repository](https://github.com/USTCAGI/PruningRAG)

## 🎯 Purpose and Intended Users

**Goal**: To standardize a dataset that incorporates multiple knowledge sources and to introduce the PruningRAG framework for optimizing retrieval-augmented generation.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: KDD Cup 2024 CRAG competition dataset which comprises both structured API data and unstructured web content.

**Size**: 4,409 QA pairs

**Format**: Markdown

**Annotation**: The external knowledge in the dataset is not annotated.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Hallucination Rate
- Missing Rate

**Calculation**: Accuracy is calculated based on matching predicted answers with ground truth; hallucination is gauged through semantic alignment comparisons.

**Interpretation**: Higher accuracy signifies better information retrieval while lower hallucination rates signify fewer misleading outputs.

**Baseline Results**: Performance comparison with several RAG frameworks was conducted, demonstrating improved accuracy and reduced hallucination with the PruningRAG framework.

**Validation**: Evaluation involved metrics comparing RAG performance under various knowledge sources.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
