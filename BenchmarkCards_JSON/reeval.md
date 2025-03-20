# ReEval

## 📊 Benchmark Details

**Name**: ReEval

**Overview**: ReEval is an LLM-based framework designed for automatically generating dynamic evaluation datasets to assess the reliability of retrieval-augmented language models (LLMs) in handling new evidence, specifically targeting hallucination issues arising from static question-answering data.

**Data Type**: Question-Answer pairs with associated evidence

**Domains**:
- Natural Questions
- RealtimeQA

**Similar Benchmarks**:
- Natural Questions
- RealtimeQA

**Resources**:
- [Resource](https://autodebug-llm.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable framework for evaluating the faithfulness and reliability of retrieval-augmented LLMs against hallucination issues.

**Target Audience**:
- Researchers in AI and machine learning
- Developers of language models
- Ethics and compliance analysts

**Tasks**:
- Evaluating LLMs' responses to dynamically generated adversarial examples
- Investigating model reliability in context-based answering
- Mitigating hallucinations in language models

**Limitations**: None

**Out of Scope Uses**:
- Long-form question-answering
- Complex reasoning tasks requiring multi-hop answers

## 💾 Data

**Source**: Natural Questions and RealtimeQA datasets

**Size**: 7189 instances from NQ and 1380 instances from RealtimeQA

**Format**: Question-Answer pairs with supporting evidence

**Annotation**: None specified

## 🔬 Methodology

**Methods**:
- Dynamic data generation through evidence perturbation
- Answer swapping
- Context enriching

**Metrics**:
- Exact Match (EM) accuracy
- Token-level F1
- Entailment accuracy

**Calculation**: Metrics calculated based on model outputs against reference answers.

**Interpretation**: Evaluation of model responses is interpreted to assess compliance with provided supporting evidence.

**Validation**: Results validated through human judgments for generated evidence.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Robustness**: Prompt injection attack, Data poisoning
- **Fairness**: Output bias

**Potential Harm**: ['Generation of inaccurate information', 'Potential spread of misinformation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Generated data does not involve personal data.

**Data Licensing**: Public datasets used are based on existing open-access resources.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
