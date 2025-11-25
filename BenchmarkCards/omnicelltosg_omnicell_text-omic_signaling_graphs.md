# OmniCellTOSG (OmniCell Text-Omic Signaling Graphs)

## 📊 Benchmark Details

**Name**: OmniCellTOSG (OmniCell Text-Omic Signaling Graphs)

**Overview**: OmniCellTOSG is the first dataset of cell text-omic signaling graphs, representing the signaling graph/system of individual cells with annotations about organ, disease, sex, age, and cell-subtype. It aims to facilitate the development of novel joint LLM and GNN models for decoding complex cell signaling systems.

**Data Type**: graph

**Domains**:
- Healthcare
- Bioinformatics

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/FuhaiLiAiLab/OmniCellTOSG)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of OmniCellTOSG is to provide a comprehensive dataset for integrating cell signaling analysis with textual and numeric omic data to improve understanding of cell signaling systems.

**Target Audience**:
- ML Researchers
- Biologists
- Biomedical Researchers

**Tasks**:
- Graph Modeling
- Cell Type Classification
- Cell Status Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Single-cell RNA sequencing data from CellxGene, GEO, Brain Cell Atlas, and SEA-AD repositories.

**Size**: 547,168 cells

**Format**: H5AD

**Annotation**: Cell type classification by automated methods and manual curation.

## 🔬 Methodology

**Methods**:
- Graph-based evaluation
- Classification using joint LLM and GNN models

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on model predictions for cell types and status.

**Interpretation**: A higher accuracy indicates better predictive performance of the model on the dataset.

**Baseline Results**: Comparison against state-of-the-art graph neural networks (e.g., GCN, GIN).

**Validation**: Validation against existing datasets and baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
