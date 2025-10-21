# TaxoBench-CS

## 📊 Benchmark Details

**Name**: TaxoBench-CS

**Overview**: A new benchmark of 156 expert-crafted taxonomies encompassing 11.6k papers, providing the first naturally annotated dataset for taxonomy generation.

**Data Type**: hierarchical taxonomy structures

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/zhukun1020/TaxoBench-CS)

## 🎯 Purpose and Intended Users

**Goal**: Facilitate research in automatic taxonomy generation for scientific literature.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Taxonomy Generation

**Limitations**: N/A

## 💾 Data

**Source**: 156 human-authored taxonomy trees from survey papers on arXiv.

**Size**: 11,600 papers

**Format**: JSON

**Annotation**: Expert-crafted annotations aligning with natural research taxonomy structures.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Normalized Mutual Information (NMI)
- Adjusted Rand Index (ARI)
- Purity
- Heading Soft Recall (HSR)
- Catalogue Edit Distance Similarity (CEDS)

**Calculation**: Metrics are calculated based on clustering quality and structural alignment with oracle taxonomies.

**Interpretation**: Higher scores indicate better coherence and granularity in taxonomies.

**Baseline Results**: Outperformed prior methods, achieving state-of-the-art performance in taxonomy coherence, granularity, and interpretability.

**Validation**: Results validated through both automatic and human evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal information included; data derived from publicly accessible sources.

**Data Licensing**: Shared under a research-only license, compliant with access conditions.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
