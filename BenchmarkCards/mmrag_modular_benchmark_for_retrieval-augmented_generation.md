# mmRAG (Modular Benchmark for Retrieval-Augmented Generation)

## 📊 Benchmark Details

**Name**: mmRAG (Modular Benchmark for Retrieval-Augmented Generation)

**Overview**: mmRAG is a modular benchmark designed for evaluating multi-modal Retrieval-Augmented Generation (RAG) systems. It integrates queries from six diverse question-answering datasets covering text, tables, and knowledge graphs, enabling granular evaluation of RAG components such as retrieval accuracy and query routing.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.57967/hf/5475)
- [Resource](https://huggingface.co/datasets/Askio/mmrag_benchmark)
- [GitHub Repository](https://github.com/nju-websoft/mmRAG)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for multi-modal RAG systems that supports the direct evaluation of retrieval, query routing, and generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: mmRAG currently supports only three data modalities: text, tables, and knowledge graphs.

## 💾 Data

**Source**: Integrated from six diverse question-answering datasets covering text, tables, and knowledge graphs.

**Size**: 5,124 queries, 90,998 documents, 3,201,548 chunks

**Format**: N/A

**Annotation**: Annotations are based on standard information retrieval protocols, involving manual and automated relevance assessments.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Normalized Discounted Cumulative Gain (NDCG)
- Mean Average Precision (MAP)
- Hits

**Calculation**: Metrics are calculated based on the relevance labels provided for each query and document chunk.

**Interpretation**: Higher scores in NDCG and MAP indicate better retrieval accuracy, while Hits measures the proportion of queries for which relevant results are found.

**Baseline Results**: Achieved NDCG@1 of 0.617 and Hits@1 of 0.703 for the best-performing retriever (BGE).

**Validation**: mmRAG's modular and multi-modal features are validated through comprehensive evaluation of various RAG implementations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open under the Apache License 2.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
