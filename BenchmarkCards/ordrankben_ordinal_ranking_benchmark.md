# OrdRankBen (Ordinal Ranking Benchmark)

## 📊 Benchmark Details

**Name**: OrdRankBen (Ordinal Ranking Benchmark)

**Overview**: OrdRankBen is a novel benchmark designed to capture multi-granularity relevance distinctions in natural language processing by incorporating structured ordinal labels, facilitating a more precise evaluation of ranking models.

**Data Type**: document ranking and passage ranking pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MSMARCO
- KILT
- BEIR

**Resources**:
- [GitHub Repository](https://github.com/Yan2266336/OrdRankBen)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of ranking models using ordinal relevance scores.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Practitioners

**Tasks**:
- Document Ranking
- Passage Ranking

**Limitations**: N/A

## 💾 Data

**Source**: Microsoft Machine Reading Comprehension (MSMARCO)

**Size**: 678,100 pairs for passage ranking; 579,300 pairs for document ranking

**Format**: N/A

**Annotation**: Ordinal relevance labels assigned based on structured criteria where scores represent degrees of relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Average Precision (MAP)
- Normalized Discounted Cumulative Gain (nDCG)

**Calculation**: Metrics calculated based on ordinal relevance scores that reflect varying degrees of relevance.

**Interpretation**: Cherishing the capacity of models to distinguish multi-granularity differences in relevance.

**Baseline Results**: N/A

**Validation**: Evaluated across multiple models for ranking tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
