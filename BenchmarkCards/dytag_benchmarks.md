# DyTAG Benchmarks

## 📊 Benchmark Details

**Name**: DyTAG Benchmarks

**Overview**: DyTAG Benchmarks are designed to evaluate Dynamic Text-Attribute Graphs (DyTAGs) which involve time-evolving graph interactions and associated text attributes. The benchmarks include various datasets and tasks related to node classification, link prediction, and destination node retrieval.

**Data Type**: dynamic graph interactions with text attributes

**Domains**:
- Computer Science
- E-commerce
- Social Networks

**Languages**:
- English

**Similar Benchmarks**:
- DGTB (Dynamic Graph Temporal Benchmark)

**Resources**:
- [Resource](https://arxiv.org/abs/2509.18742)

## 🎯 Purpose and Intended Users

**Goal**: To study the recent-global spatio-temporal patterns in DyTAGs and evaluate the proposed DyGRASP model's effectiveness on these patterns.

**Target Audience**:
- ML Researchers
- Data Scientists
- Academics

**Tasks**:
- Node Classification
- Link Prediction
- Destination Node Retrieval

**Limitations**: Performance not validated on diverse real-world datasets beyond DTGB benchmarks.

## 💾 Data

**Source**: Four datasets extracted from various domains including GDELT, Enron, Googlemap, and Stack_elec.

**Size**: Differing sizes across datasets, with GDELT having 6,786 nodes and 1,339,245 edges, and others varying accordingly.

**Format**: Graph structure with text attributes

**Annotation**: Text attributes derived from user reviews, email content, etc.

## 🔬 Methodology

**Methods**:
- Node-centric implicit reasoning
- Explicit reasoning with LLMs
- Temporal GNN integration

**Metrics**:
- Hit@10
- Average Precision (AP)
- ROC-AUC

**Calculation**: Metrics calculated based on the proportion of successful interactions within top-k predictions.

**Interpretation**: A higher Hit@10 percentage indicates better performance in retrieving destination nodes.

**Baseline Results**: DyGRASP outperformed other methods in Hit@10 metric and future link prediction tasks.

**Validation**: Models validated using train-test splits with a rigorous evaluation process.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
