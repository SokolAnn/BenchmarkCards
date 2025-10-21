# LHMKE (Large-scale Holistic Multi-subject Knowledge Evaluation)

## 📊 Benchmark Details

**Name**: LHMKE (Large-scale Holistic Multi-subject Knowledge Evaluation)

**Overview**: LHMKE is designed to provide a comprehensive evaluation of the knowledge acquisition capabilities of Chinese LLMs, encompassing 10,465 questions across 75 tasks covering 30 subjects, including both objective and subjective questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMLU
- C-Eval
- CMMLU
- M3KE

**Resources**:
- [GitHub Repository](https://github.com/tjunlp-lab/LHMKE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate Chinese LLMs across a diverse range of question types and subjects, spanning from elementary school to professional certifications.

**Target Audience**:
- ML Researchers
- Model Developers
- Education Practitioners

**Tasks**:
- Knowledge Evaluation
- Subjective Question Answering
- Objective Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Questions are sourced from realistic standard exams in the Chinese educational system, manually collected online.

**Size**: 10,465 questions

**Format**: N/A

**Annotation**: Questions are collected from standardized exams and categorized into objective and subjective types.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics using GPT-4

**Metrics**:
- Accuracy

**Calculation**: Metrics for objective questions are calculated based on accuracy, while subjective questions are evaluated using GPT-4 as an evaluator.

**Interpretation**: Performance is measured by comparing LLM outputs to reference answers, with scores indicating the correctness of responses.

**Validation**: Evaluations conducted across various Chinese LLMs to ensure their performance is rigorously tested.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data in LHMKE are collected from public sources and scrutinized to exclude examples with ethical concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
