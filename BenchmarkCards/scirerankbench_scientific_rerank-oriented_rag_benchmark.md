# SciRerankBench (Scientific Rerank-oriented RAG Benchmark)

## 📊 Benchmark Details

**Name**: SciRerankBench (Scientific Rerank-oriented RAG Benchmark)

**Overview**: SciRerankBench is the first benchmark specifically developed to evaluate rerankers within retrieval-augmented generated language models (RAG-LLMs), providing insights into the performance of rerankers in scientific literature question answering tasks across five scientific subjects.

**Data Type**: question-context-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/XXXXXXX.XXXXXXX)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of rerankers in RAG-LLMs for scientific literature question answering.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Derived from over 250 million scholarly works, covering 5 major scientific domains: biology, physics, chemistry, geography, and mathematics.

**Size**: 4,500 question-context-answer pairs

**Format**: JSON

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall@10

**Calculation**: Metrics are calculated based on the proportion of relevant contexts retrieved within the top results.

**Interpretation**: High recall scores indicate effective retrieval and reranking in identifying relevant scientific contexts.

**Baseline Results**: N/A

**Validation**: Evaluated across 13 popular rerankers on 11 open-source LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
