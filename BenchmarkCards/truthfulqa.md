# TruthfulQA

## 📊 Benchmark Details

**Name**: TruthfulQA

**Overview**: A benchmark designed to measure how truthful language models are in generating answers to questions. It consists of 817 questions spanning 38 categories, focusing on avoiding false answers that mimic human misconceptions.

**Data Type**: Questions with true and false answers.

**Domains**:
- Health
- Law
- Finance
- Politics
- Misconceptions
- Fiction
- Conspiracies

**Resources**:
- [GitHub Repository](https://github.com/sylinrl/TruthfulQA)

## 🎯 Purpose and Intended Users

**Goal**: To quantify the truthfulness of language models across various contexts.

**Target Audience**:
- Researchers
- AI developers
- Ethical AI practitioners

**Tasks**:
- Measure truthfulness of model-generated answers
- Evaluate the performance of language models against human standards

**Limitations**: The benchmark mainly focuses on general knowledge questions designed to elicit imitative falsehoods and does not cover specialized domains.

**Out of Scope Uses**:
- Long-form text generation
- Interactive settings like chatbots

## 💾 Data

**Source**: Created by the authors using Wikipedia and other reliable sources for reference.

**Size**: 817 questions

**Format**: Multiple choice with true and false answers.

**Annotation**: Each question has sets of true and false reference answers with supporting sources.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Human evaluation of answers
- Automated evaluation using GPT-judge

**Metrics**:
- Truthfulness percentage
- Informative percentage

**Calculation**: Truthfulness determined by comparing model responses to established true/false reference answers.

**Interpretation**: Model answers are evaluated on a scalar truth score from 0 to 1, with 1 being completely truthful.

**Baseline Results**: The best model achieved 58% truthfulness compared to 94% for humans.

**Validation**: Human evaluators assessed the validity of model answers to establish a baseline for truthfulness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Explainability

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Explainability**: Unexplainable output

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sourced primarily from publicly accessible sources.

**Data Licensing**: Questions and reference answers are constructed by the authors.

**Consent Procedures**: No explicit consent procedures necessary since data is derived from public sources.

**Compliance With Regulations**: The benchmark adheres to ethical AI guidelines but does not enforce regulatory compliance.
