# LegalBench-RAG

## 📊 Benchmark Details

**Name**: LegalBench-RAG

**Overview**: LegalBench-RAG is the first benchmark specifically designed to evaluate the retrieval step of Retrieval-Augmented Generation (RAG) pipelines within the legal space, focusing on extracting minimal, highly relevant text segments from legal documents.

**Data Type**: question-answering pairs

**Domains**:
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- LegalBench

**Resources**:
- [GitHub Repository](https://github.com/zeroentropy-cc/legalbenchrag)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust framework for assessing retrieval precision and recall in legal RAG systems.

**Target Audience**:
- Researchers
- Industry Practitioners

**Tasks**:
- Information Retrieval

**Limitations**: Queries are answered by exactly one document, and the benchmark does not assess structured numerical data parsing or multi-document reasoning.

## 💾 Data

**Source**: Derived from four unique legal datasets including PrivacyQA, CUAD, MAUD, and ContractNLI.

**Size**: 6,889 query-answer pairs

**Format**: JSON

**Annotation**: Human-annotated by legal experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall

**Calculation**: Metrics are computed based on the accuracy of retrieval for each query.

**Interpretation**: Higher precision indicates more relevant documents retrieved, while higher recall indicates more documents retrieved overall.

**Validation**: Validated through rigorous manual inspection of each query and its corresponding annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
