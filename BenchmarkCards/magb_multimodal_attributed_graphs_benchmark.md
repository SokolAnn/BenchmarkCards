# MAGB (Multimodal Attributed Graphs Benchmark)

## 📊 Benchmark Details

**Name**: MAGB (Multimodal Attributed Graphs Benchmark)

**Overview**: The MAGB dataset is the first benchmark specifically designed for Multimodal Attributed Graph representation learning (MAGRL), consisting of five curated multimodal attributed graphs from various domains with standardized node attributes across textual and visual modalities.

**Data Type**: multimodal attributed graphs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- CS-TAG
- OGB
- DTG
- TEG
- DyTAG

**Resources**:
- [GitHub Repository](https://github.com/sktsherlock/MAGB)

## 🎯 Purpose and Intended Users

**Goal**: To advance the exploration of Multimodal Attributed Graph representation learning and provide a comprehensive benchmark for evaluating various MAG representation learning methods.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Node Classification
- Link Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Curated graphs from e-commerce platforms and social media such as Reddit

**Size**: 5 graphs

**Format**: CSV

**Annotation**: Textual and visual attributes processed via data cleaning and augmentation

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Hits@1
- Hits@3
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics calculated based on standard evaluation procedures for node classification and link prediction tasks.

**Interpretation**: Higher scores indicate better performance in tasks of node classification and link prediction.

**Validation**: Conducted extensive experiments with various settings and random seeds.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for bias in model predictions due to imbalanced training data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
