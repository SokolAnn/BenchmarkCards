# ZeroG : Investigating Cross-dataset Zero-shot Transferability in Graphs

## 📊 Benchmark Details

**Name**: ZeroG : Investigating Cross-dataset Zero-shot Transferability in Graphs

**Overview**: ZeroG is a new framework designed to enable cross-dataset generalization in graph learning, addressing challenges such as feature misalignment, mismatched label spaces, and negative transfer with a focus on zero-shot transfer capabilities.

**Data Type**: graph

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/NineAbyss/ZeroG)

## 🎯 Purpose and Intended Users

**Goal**: To investigate zero-shot transferability in graphs and develop a framework for cross-dataset generalization.

**Target Audience**:
- ML Researchers
- Data Scientists

**Tasks**:
- Node Classification

**Limitations**: N/A

## 💾 Data

**Source**: Multiple public graph datasets including Cora, Citeseer, Pubmed, and custom co-purchase datasets P-Home and P-Tech derived from the ogbn-products dataset.

**Size**: Not explicitly stated

**Format**: Graph

**Annotation**: Manual labeling based on class categories.

## 🔬 Methodology

**Methods**:
- Graph self-supervised learning
- Semantic similarity-based classification
- Prompt-based subgraph sampling

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated by comparing the predicted labels with the actual labels of nodes in different datasets.

**Interpretation**: Higher accuracy indicates better zero-shot transferability performance across datasets.

**Baseline Results**: ZeroG achieved test accuracies of 68.72% on Cora and 78.02% on Pubmed.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
