# UDA (Unstructured Document Analysis)

## 📊 Benchmark Details

**Name**: UDA (Unstructured Document Analysis)

**Overview**: We propose a benchmark suite, namely Unstructured Document Analysis (UDA), that involves 2,965 real-world documents and 29,590 expert-annotated Q&A pairs to evaluate Retrieval-Augmented Generation (RAG) methodologies in real-world document analysis scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Finance
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/qinchuanhui/UDA-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To advance future research and production in unstructured document analysis.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: While the efficacy of parsing strategies was evaluated through the downstream Q&A performance, a direct comparison of the parsed content was not undertaken.

## 💾 Data

**Source**: 2,965 real-world documents collected from various platforms such as Wikipedia and arXiv.

**Size**: 2,965 documents and 29,590 Q&A pairs

**Format**: PDF and HTML

**Annotation**: Expert-annotated Q&A pairs

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- End-to-end evaluation using various LLMs

**Metrics**:
- F1 Score
- Exact-Match

**Calculation**: Span-level F1-score calculated from the overlap of prediction and ground truth answers treated as bags of words.

**Interpretation**: Higher scores indicate better performance in answering questions accurately.

**Validation**: Performance evaluated on various modules in a typical RAG workflow.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
