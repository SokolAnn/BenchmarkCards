# UQ (Unsolved Questions)

## 📊 Benchmark Details

**Name**: UQ (Unsolved Questions)

**Overview**: We introduce UQ, a testbed of 500 challenging, diverse questions sourced from Stack Exchange, probing capabilities including reasoning, factuality, and browsing.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Education
- Mathematics
- Science
- Engineering

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- Humanity’s Last Exam

**Resources**:
- [Resource](https://uq.stanford.edu)

## 🎯 Purpose and Intended Users

**Goal**: To assess the capabilities of AI models on unsolved questions that reflect real-world challenges and have not been definitively answered by human experts.

**Target Audience**:
- AI Researchers
- Machine Learning Practitioners
- Educators
- Domain Experts

**Tasks**:
- Question Answering
- Reasoning

**Limitations**: The evaluation may not encompass all unsolved questions in a variety of domains as it primarily utilizes sources from Stack Exchange.

## 💾 Data

**Source**: Curated from Stack Exchange using a multi-stage filtering pipeline involving rule-based, LLM-based, and human review filtering stages.

**Size**: 500 questions

**Format**: JSON

**Annotation**: Filtered and verified through rule-based methods, LLM evaluations, and human reviews.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance of AI models on the UQ dataset, including evaluation metrics established by LLM validators and subsequent human reviews.

**Interpretation**: High scores indicate strong performance on difficult unsolved questions reflective of real-world tasks; low scores indicate challenges remaining in modeling such questions.

**Baseline Results**: Initial human evaluations identified that top-performing models passed validation on only 15% of questions.

**Validation**: The benchmark allows continuous updates and validations through community engagement and feedback.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: Analysis of demographic factors is not explicitly provided but is a consideration during question selection.

**Potential Harm**: ['Potential reinforcement of existing biases in AI responses through unsolved, sensitive questions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is sourced from Stack Exchange, subject to CC BY-SA licensing requirements.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
