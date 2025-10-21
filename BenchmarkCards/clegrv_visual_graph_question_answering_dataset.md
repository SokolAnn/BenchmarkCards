# CLEGRV (Visual Graph Question Answering Dataset)

## 📊 Benchmark Details

**Name**: CLEGRV (Visual Graph Question Answering Dataset)

**Overview**: CLEGRV is a new dataset for benchmarking Visual Question Answering (VQA) systems that focus on images of graphs, particularly inspired by transit networks. The dataset enhances the existing CLEGR dataset by providing images and related questions that can be answered using the visual information provided.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- CLEGR

**Resources**:
- [GitHub Repository](https://github.com/pudumagico/NSGRAPH)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating VQA systems on images of graphs, specifically for questions related to transit networks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated images and questions derived from the existing CLEGR dataset.

**Size**: 3,000 question-answer pairs

**Format**: JSON

**Annotation**: Questions are derived from naturally occurring queries related to the graph images.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the correct answers provided for the questions in the VQA task.

**Interpretation**: An accuracy of 73% indicates the proportion of correctly answered questions by the VQA system.

**Baseline Results**: An average accuracy of 73% on the CLEGRV dataset.

**Validation**: Validation of the benchmark was done through evaluation against existing systems and methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
