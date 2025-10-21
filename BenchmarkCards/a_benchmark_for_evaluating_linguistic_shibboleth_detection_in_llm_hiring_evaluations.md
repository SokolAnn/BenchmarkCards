# A Benchmark for Evaluating Linguistic Shibboleth Detection in LLM Hiring Evaluations

## 📊 Benchmark Details

**Name**: A Benchmark for Evaluating Linguistic Shibboleth Detection in LLM Hiring Evaluations

**Overview**: This paper introduces a comprehensive benchmark for evaluating how Large Language Models (LLMs) respond to linguistic shibboleths, which are subtle linguistic markers that can reveal demographic attributes. The benchmark consists of 100 validated question-response pairs designed to measure demographic bias in automated evaluation systems.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2508.04939)

## 🎯 Purpose and Intended Users

**Goal**: To establish a benchmark framework for detecting and measuring linguistic shibboleth bias in AI evaluation systems.

**Target Audience**:
- ML Researchers
- AI Fairness Practitioners

**Tasks**:
- Bias Detection
- Evaluative Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Curated interview questions from Indeed, Turing, and Kaggle

**Size**: 100 questions

**Format**: CSV

**Annotation**: Manual validation ensuring semantic equivalence and competency parity

## 🔬 Methodology

**Methods**:
- Controlled linguistic variation generation
- Human evaluation

**Metrics**:
- Accuracy
- Bias score disparity

**Calculation**: Scores calculated on a scale from 1 to 5 based on clarity, relevance, and depth of responses.

**Interpretation**: Higher scores indicate better responses, with a particular focus on mitigating bias against hedged language.

**Baseline Results**: Hedged responses scored lower than confident responses across all models evaluated.

**Validation**: Repeated trials across multiple model architectures to ensure consistency of results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Bias analysis based on demographic characteristics indicated by linguistic shibboleths.

**Potential Harm**: ['Potential exclusion of qualified candidates based on linguistic style rather than substance.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
