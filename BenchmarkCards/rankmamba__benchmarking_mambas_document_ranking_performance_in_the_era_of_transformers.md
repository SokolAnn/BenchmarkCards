# RankMamba: Benchmarking Mamba’s Document Ranking Performance in the Era of Transformers

## 📊 Benchmark Details

**Name**: RankMamba: Benchmarking Mamba’s Document Ranking Performance in the Era of Transformers

**Overview**: This work examines Mamba’s efficacy through a classical IR task—document ranking, and benchmarks Mamba models against transformer-based models characterized by varying structures, sizes, pre-training objectives, and attention patterns.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Information Retrieval

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/zhichaoxu-shufe/RankMamba)
- [GitHub Repository](https://github.com/state-spaces/mamba)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively assess the performance of Mamba in the document ranking task compared to transformer-based models.

**Target Audience**:
- ML Researchers
- Information Retrieval Practitioners

**Tasks**:
- Document Ranking

**Limitations**: Mamba models have lower training throughput compared to efficient attention implementations.

## 💾 Data

**Source**: MS MARCO document ranking dataset and official document ranking dev set, including TREC DL19 and DL20.

**Size**: 734,008 training samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Normalized Discounted Cumulative Gain (NDCG)

**Calculation**: Metrics calculated based on the official evaluation setup.

**Interpretation**: Higher MRR and NDCG scores indicate better performance in ranking relevance.

**Baseline Results**: Roberta-large achieves 0.4434 MRR on MSMARCO Dev set.

**Validation**: Results cross-validated with multiple datasets including TREC DL19 and DL20.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
