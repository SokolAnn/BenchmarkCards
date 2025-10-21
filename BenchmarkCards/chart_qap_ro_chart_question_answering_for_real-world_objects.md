# CHART QAP RO (Chart Question Answering for Real-World Objects)

## 📊 Benchmark Details

**Name**: CHART QAP RO (Chart Question Answering for Real-World Objects)

**Overview**: CHART QAP RO is a new benchmark for Chart Question Answering that includes 1,341 charts from 157 diverse sources, featuring 1,948 questions across various types, including factoid, multiple-choice, conversational, hypothetical, and unanswerable questions, designed to assess real-world challenges in chart understanding.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ChartQA
- CharXiv

**Resources**:
- [GitHub Repository](https://github.com/visnlp/ChartQAPro)

## 🎯 Purpose and Intended Users

**Goal**: To provide a diverse and challenging benchmark for evaluating the capabilities of vision-language models in chart reasoning.

**Target Audience**:
- Researchers
- Model Developers

**Tasks**:
- Chart Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various platforms including Pew Research Center, Tableau, OWID, etc.

**Size**: 1,341 charts and 1,948 questions

**Format**: N/A

**Annotation**: Human-written and verified question-answer pairs

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on exact match criteria for fact-checked and multiple-choice answers, with relaxed correctness for numeric answers.

**Interpretation**: Performance evaluated against state-of-the-art models to reveal substantial performance drops compared to previous benchmarks.

**Validation**: Experiment run across 21 models with comparisons to determine benchmark effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All images sourced from publicly available platforms and reviewed for harmful content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
