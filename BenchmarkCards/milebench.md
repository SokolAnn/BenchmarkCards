# MILEBENCH

## 📊 Benchmark Details

**Name**: MILEBENCH

**Overview**: MILEBENCH is a pioneering benchmark designed to test the MultImodal Long-cont Ext capabilities of Multimodal Large Language Models (MLLMs). It comprises multimodal long contexts and multiple tasks requiring both comprehension and generation. Two distinct evaluation sets, diagnostic and realistic, are established to assess MLLMs' long-context adaptation capacity.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://milebench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the multimodal long-context capabilities of MLLMs.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Object Detection
- Action Understanding
- Visual Navigation
- Knowledge Grounded QA
- Visual Relation Inference

**Limitations**: Some results from closed-source MLLMs may vary over time, and there is a risk of data leakage.

## 💾 Data

**Source**: Collected from 21 pre-existing or self-constructed datasets.

**Size**: 6,440 examples

**Format**: N/A

**Annotation**: Manually verified with an Inter-annotator Agreement of 95%.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy
- ROUGE-L

**Calculation**: Metrics for each dataset are consistent with the original work for tasks built on previous datasets.

**Interpretation**: Higher scores indicate better performance in long-context tasks.

**Baseline Results**: Closed-source MLLMs, specifically GPT-4V and GPT-4o, achieved the highest performance.

**Validation**: 10% of the data is manually verified for precision.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The benchmark assesses performance across different MLLM types without specific demographic breakdown.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset used is composed of publicly accessible datasets licensed under Creative Commons (CC-BY) or other open-source licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The study followed all required legal procedures for data incorporation.
