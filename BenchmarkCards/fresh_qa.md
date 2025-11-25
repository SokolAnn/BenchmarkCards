# FRESH QA

## 📊 Benchmark Details

**Name**: FRESH QA

**Overview**: FRESH QA is a novel dynamic QA benchmark encompassing a diverse range of question and answer types, including questions that require fast-changing world knowledge as well as questions with false premises that need to be debunked.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/freshllms/freshqa)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the factuality of existing large language models (LLMs) and improve their performance on dynamic and factually accurate question-answering tasks.

**Target Audience**:
- NLP Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Questions were collected from NLP researchers and freelancers tasked with writing questions of varying difficulty levels that require up-to-date knowledge.

**Size**: 600 questions

**Format**: CSV

**Annotation**: Manually annotated by NLP researchers and freelancers, with quality control mechanisms implemented.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on correctness and hallucination in a two-mode evaluation procedure: RELAXED and STRICT.

**Interpretation**: Higher accuracy indicates better factual correctness and less hallucination in responses.

**Baseline Results**: N/A

**Validation**: Evaluation involves more than 50,000 human judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Inaccurate information generation in response to user queries.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
