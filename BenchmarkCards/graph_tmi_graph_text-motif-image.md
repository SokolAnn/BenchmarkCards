# GRAPH TMI (Graph Text-Motif-Image)

## 📊 Benchmark Details

**Name**: GRAPH TMI (Graph Text-Motif-Image)

**Overview**: The GRAPH TMI benchmark is introduced for evaluating LLMs in graph structure analysis, focusing on homophily, motif presence, and graph difficulty across three modalities: text, motif, and image.

**Data Type**: graph-structure with text, motif, and image encodings

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2311.09862)

## 🎯 Purpose and Intended Users

**Goal**: To advance the understanding of how different graph structures and modalities affect LLM prompting and node classification tasks.

**Target Audience**:
- ML Researchers
- Data Scientists

**Tasks**:
- Node Classification

**Limitations**: The computational demands of detecting network motifs and the simplistic approach to estimating homophily pose limitations.

## 💾 Data

**Source**: CORA, Citeseer, and Pubmed citation network datasets.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Denial rate
- Mismatch rate
- Token limit fraction

**Calculation**: Accuracy rate = Correct predictions / Total samples; Denial rate = Predictions = -1 / Total samples; Mismatch rate = Incorrect predictions / Total samples; Token limit fraction = Number of usage tokens / Token limit constraint.

**Interpretation**: Understands classification accuracy and the efficacy of encoding modalities in relation to task difficulty.

**Baseline Results**: GNN models such as GCN, GAT, and GraphSage were compared against LLM results.

**Validation**: Performance assessed by various graph and encoding modalities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
