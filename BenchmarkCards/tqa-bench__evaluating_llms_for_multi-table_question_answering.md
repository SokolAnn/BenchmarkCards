# TQA-Bench: Evaluating LLMs for Multi-Table Question Answering

## 📊 Benchmark Details

**Name**: TQA-Bench: Evaluating LLMs for Multi-Table Question Answering

**Overview**: TQA-Bench is a new multi-table QA benchmark designed to evaluate the capabilities of LLMs in tackling complex QA tasks over relational data, incorporating diverse relational database instances and a flexible sampling mechanism to create tasks with varying multi-table context lengths.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Finance
- Healthcare
- E-commerce

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Relaxed-System-Lab/TQA-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the capabilities of LLMs in processing complex, relational data across multiple tables.

**Target Audience**:
- ML Researchers
- Data Scientists
- AI Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Diverse relational database instances sourced from public datasets such as WorldBank, DataGov, and BIRD.

**Size**: 400 database instances with a total of 56,000 question instances.

**Format**: Markdown

**Annotation**: Automatically generated with symbolic extensions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Evaluation metrics calculated based on the performance of LLMs on question-answering tasks.

**Interpretation**: Model performance will be interpreted based on accuracy metrics calculated across different question types.

**Validation**: Comprehensive evaluation was conducted across 22 LLMs of different scales.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
