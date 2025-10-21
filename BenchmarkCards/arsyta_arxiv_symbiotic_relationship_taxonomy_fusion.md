# ArSyTa (Arxiv Symbiotic Relationship Taxonomy Fusion)

## 📊 Benchmark Details

**Name**: ArSyTa (Arxiv Symbiotic Relationship Taxonomy Fusion)

**Overview**: We have constructed a dataset ArSyTa comprising 8.27 million comprehensive citation contexts across diverse domains, featuring richer density and relevant features, including taxonomy concepts, to facilitate the task of citation recommendation.

**Data Type**: citation contexts

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/goyalkaraniit/SymTax)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust dataset for citation recommendation that incorporates both local and global context information.

**Target Audience**:
- ML Researchers

**Tasks**:
- Citation Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from 1.7 million scholarly papers spanning STEM disciplines available on arXiv.

**Size**: 8.27 million citation contexts

**Format**: N/A

**Annotation**: Automatic parsing and annotation of citation contexts from scholarly papers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall@K
- Mean Reciprocal Rank (MRR)
- Normalized Discounted Cumulative Gain (NDCG)

**Calculation**: Metrics are calculated based on the position of cited papers in the recommendation list.

**Interpretation**: Higher values of metrics indicate better performance in citation recommendations.

**Baseline Results**: The proposed module improves performance by 22.56% in Recall@5 compared to state-of-the-art.

**Validation**: Extensive experiments and ablation studies conducted.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
