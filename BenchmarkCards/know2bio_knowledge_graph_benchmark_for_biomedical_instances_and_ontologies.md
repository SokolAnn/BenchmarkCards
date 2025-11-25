# Know2BIO (Knowledge Graph Benchmark for Biomedical Instances and Ontologies)

## 📊 Benchmark Details

**Name**: Know2BIO (Knowledge Graph Benchmark for Biomedical Instances and Ontologies)

**Overview**: Know2BIO is a general-purpose heterogeneous knowledge graph benchmark for the biomedical domain, integrating data from 30 diverse sources, currently consisting of ~219,000 nodes and ~6,200,000 edges. It supports automated updating to reflect the latest biomedical knowledge.

**Data Type**: graph

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Yijia-Xiao/Know2BIO)

## 🎯 Purpose and Intended Users

**Goal**: To enable thorough benchmarking of knowledge graph representation learning methods and facilitate biomedical knowledge discovery.

**Target Audience**:
- ML Researchers
- Biomedical Researchers
- Data Scientists

**Tasks**:
- Link Prediction

**Limitations**: Biomedical knowledge representation is inherently incomplete due to the rapidly evolving nature of biological sciences.

## 💾 Data

**Source**: Integrated data from 30 different biomedical sources.

**Size**: 219,000 nodes, 6,200,000 edges

**Format**: CSV

**Annotation**: Data identifiers were aligned through various intermediary resources.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Link prediction tasks

**Metrics**:
- Hits@k
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics are calculated by ranking a set of candidate nodes in the knowledge graph.

**Interpretation**: Higher Hits@k and MRR values indicate better performance in predicting missing nodes.

**Validation**: Training, validation, and test splits were created using the GraPE package.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The source code is released under MIT license; the data is released under respective licenses of data sources.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
