# Scaling Legal AI: Benchmarking Mamba and Transformers for Statutory Classification and Case Law Retrieval

## 📊 Benchmark Details

**Name**: Scaling Legal AI: Benchmarking Mamba and Transformers for Statutory Classification and Case Law Retrieval

**Overview**: This study introduces a new legal NLP benchmark suite for long-context modeling, open source code and datasets to support reproducibility. It benchmarks Mamba against transformer models for statutory classification and case law retrieval.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LexGLUE
- EUR-Lex
- ILDC

**Resources**:
- [Resource](https://arxiv.org/abs/2509.00141)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmarking of Mamba against existing transformer models for legal document classification and case law retrieval.

**Target Audience**:
- Legal Practitioners
- AI Researchers
- Policy Makers

**Tasks**:
- Statutory Classification
- Case Law Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Open-source legal corpora including LexGLUE, EUR-Lex, and ILDC.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Benchmarking various models
- Sliding window mechanism for long-context processing

**Metrics**:
- Accuracy
- Recall@k
- Mean Reciprocal Rank (MRR)
- Normalized Discounted Cumulative Gain (nDCG)
- Throughput (tokens/sec)

**Calculation**: Metrics are calculated based on model performance on designated benchmarks.

**Interpretation**: Results illustrate the efficiency and performance of Mamba compared to transformers during legal tasks.

**Baseline Results**: N/A

**Validation**: Through benchmarking against multiple established datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
