# ToTER (Topical Taxonomy Enhanced Retrieval)

## 📊 Benchmark Details

**Name**: ToTER (Topical Taxonomy Enhanced Retrieval)

**Overview**: ToTER is a framework that enhances PLM-based retrieval in theme-specific applications using a corpus topical taxonomy to identify central topics of queries and documents, and to improve retrieval by supplementing semantic matching.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Information Retrieval

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/SeongKu-Kang/ToTER_WWW24)

## 🎯 Purpose and Intended Users

**Goal**: To improve retrieval accuracy in theme-specific applications by effectively utilizing corpus topical taxonomies.

**Target Audience**:
- Researchers
- Practitioners in Information Retrieval
- Developers of retrieval systems

**Tasks**:
- Document Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: SCIDOCS dataset for academic paper search, Amazon ESCI dataset for product search

**Size**: 25,657 documents for SCIDOCS, 601,354 documents for Amazon ESCI

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Unsupervised multi-label classification
- Retrieval
- Reranking

**Metrics**:
- Recall
- NDCG
- Mean Average Precision (MAP)

**Calculation**: Metrics calculated based on the number of relevant results retrieved and their ranks.

**Interpretation**: Higher values in recall, NDCG, and MAP indicate better retrieval performance.

**Baseline Results**: ToTER consistently improves retrieval metrics over existing methods in the evaluated domains.

**Validation**: Extensive experiments on real-world datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
