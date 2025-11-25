# WXI MPACT BENCH

## 📊 Benchmark Details

**Name**: WXI MPACT BENCH

**Overview**: The first benchmark for evaluating the capacity of LLMs on disruptive weather impacts, which includes two evaluation tasks: multi-label classification and ranking-based question answering.

**Data Type**: disruptive weather impact annotations and question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CLLMate

**Resources**:
- [GitHub Repository](https://github.com/Michaelyya/WXImpactBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of large language models to understand disruptive weather impacts, aiding in climate change adaptation understanding.

**Target Audience**:
- ML Researchers
- Climate Scientists
- Policy Makers

**Tasks**:
- Multi-Label Classification
- Ranking-based Question Answering

**Limitations**: Potential biases in underrepresented historical events and linguistic variations.

## 💾 Data

**Source**: Historical newspaper articles collected and processed through a multi-stage data construction pipeline.

**Size**: 350 historical articles, 1,386 mixed context articles

**Format**: JSON

**Annotation**: Annotated by domain experts following specific guidelines for impact categories.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Hit@1
- nDCG@5
- Recall@5
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics calculated based on model predictions against ground-truth labels.

**Interpretation**: A higher score indicates better understanding of disruptive weather impacts by the models.

**Validation**: Extensive evaluation across various LLMs to benchmark their performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is publicly available under specific collaboration agreements.

**Consent Procedures**: Permission obtained from the organizations preserving the copyright.

**Compliance With Regulations**: Not Applicable
