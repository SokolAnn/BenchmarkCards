# Reefknot: A Comprehensive Benchmark for Relation Hallucination Evaluation, Analysis and Mitigation in Multimodal Large Language Models

## 📊 Benchmark Details

**Name**: Reefknot: A Comprehensive Benchmark for Relation Hallucination Evaluation, Analysis and Mitigation in Multimodal Large Language Models

**Overview**: Reefknot is a comprehensive benchmark targeting relation hallucinations in multimodal large language models, comprising over 20,000 real-world samples with two types of relationships and three evaluation tasks to assess relation hallucinations comprehensively.

**Data Type**: relation-based question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- MMRel
- R-bench

**Resources**:
- [GitHub Repository](https://github.com/JackChen-seu/Reefknot)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and mitigate relation hallucinations in multimodal large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Yes/No Question Answering
- Multiple Choice Question Answering
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Visual Genome scene graph dataset

**Size**: 21,880 questions across 11,084 images

**Format**: N/A

**Annotation**: Expert-based validation

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Hallucination rate
- Rscore

**Calculation**: Rscore is calculated as the average of (1 minus hallucination rate) across three tasks.

**Interpretation**: Lower hallucination rates indicate better performance.

**Baseline Results**: N/A

**Validation**: Multi-turn manual verification by domain experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
