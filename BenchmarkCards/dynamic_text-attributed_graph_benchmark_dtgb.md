# Dynamic Text-attributed Graph Benchmark (DTGB)

## 📊 Benchmark Details

**Name**: Dynamic Text-attributed Graph Benchmark (DTGB)

**Overview**: DTGB is a collection of large-scale, time-evolving graphs from diverse domains, with nodes and edges enriched by dynamically changing text attributes and categories. It provides a comprehensive benchmark for evaluating models to handle the interplay between dynamic graph structures and natural language.

**Data Type**: dynamic graphs with text attributes

**Domains**:
- Natural Language Processing
- Computer Science
- Social Networks
- E-commerce

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/zjs123/DTGB)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to foster research on Dynamic Text-attributed Graphs (DyTAGs) and to provide a standardized evaluation framework for models to assess their performance on various tasks involving dynamic graph structures and textual information.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Future Link Prediction
- Destination Node Retrieval
- Edge Classification
- Textural Relation Generation

**Limitations**: N/A

## 💾 Data

**Source**: Eight large-scale DyTAGs sourced from diverse domains including e-commerce, social networks, multi-round dialogues, and knowledge graphs, with nodes and edges associated with rich text descriptions and edge categories.

**Size**: N/A

**Format**: CSV

**Annotation**: Manually extracted and categorized based on predefined criteria related to real-world use cases.

## 🔬 Methodology

**Methods**:
- Benchmarking algorithms against dynamic graph learning models
- Evaluation using large language models

**Metrics**:
- Weighted Precision
- Weighted Recall
- Weighted F1 Score
- Average Precision
- Area Under ROC Curve (AUC-ROC)
- Hits@k
- BERTScore

**Calculation**: Metrics are calculated based on standard definitions for each task as detailed in the methodology section of the paper.

**Interpretation**: Higher scores indicate better performance in the dynamic graph tasks specified.

**Baseline Results**: Comparison performed with 7 popular dynamic graph learning algorithms and 6 large language models.

**Validation**: Cross-validation performed with appropriate dataset splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All used raw data are publicly available and do not contain personally identifiable information.

**Data Licensing**: The datasets are available under MIT License or Apache License 2.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
