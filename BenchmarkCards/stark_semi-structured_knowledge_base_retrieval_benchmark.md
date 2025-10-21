# STARK (Semi-structured Knowledge Base Retrieval Benchmark)

## 📊 Benchmark Details

**Name**: STARK (Semi-structured Knowledge Base Retrieval Benchmark)

**Overview**: STARK is a large-scale benchmark designed to evaluate retrieval systems on semi-structured knowledge bases, integrating both textual and relational information to support complex queries across domains like product search, academic papers, and precision medicine.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare
- E-commerce

**Languages**:
- English

**Resources**:
- [Resource](https://stark.stanford.edu/)
- [GitHub Repository](https://github.com/snap-stanford/STaRK)
- [Resource](https://stark.stanford.edu/skb_explorer.html)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive testbed for evaluating the performance of retrieval systems driven by large language models in handling complex queries across semi-structured knowledge bases.

**Target Audience**:
- ML Researchers
- Engineers
- Domain Experts

**Tasks**:
- Question Answering
- Information Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Constructed semi-structured knowledge bases from public data, including Amazon product reviews, Microsoft Academic Graph, and PrimeKG datasets.

**Size**: 54,378 queries total (9,100 STARK-AMAZON + 13,323 STARK-MAG + 11,204 STARK-PRIME)

**Format**: CSV

**Annotation**: Human-generated and synthesized queries validated through human evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Hit@1
- Hit@5
- Recall@20
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics are calculated based on user query performances and system responses across generated test sets.

**Interpretation**: A higher Hit@k score indicates better performance for retrieval systems in returning the correct items within the top-k ranked results.

**Validation**: Extensive human evaluation and comparison with baseline retrieval models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymization protocols are in place for the datasets involved.

**Data Licensing**: Data sourced from publicly available datasets with adherence to specific licenses.

**Consent Procedures**: Consent obtained through participants involved in query generation.

**Compliance With Regulations**: Not Applicable
