# FarsEval -PKBETS

## 📊 Benchmark Details

**Name**: FarsEval -PKBETS

**Overview**: FarsEval -PKBETS benchmark is designed for evaluating large language models in Persian, consisting of 4,000 questions across various formats and domains, focusing on linguistic, cultural, and local considerations relevant to the Persian language and Iran.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare
- Legal
- Education

**Languages**:
- Persian

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- MMLU
- TruthfulQA
- BIG-Bench

**Resources**:
- [GitHub Repository](https://github.com/ParsBench/FarsEval-PKBETS)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a robust evaluation platform for measuring and comparing the performance of language models specifically trained for the Persian language.

**Target Audience**:
- ML Researchers
- Model Developers
- Linguists

**Tasks**:
- Text Classification
- Question Answering
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Self-generated and expert-reviewed questions covering various domains and tasks relevant to Persian language and culture.

**Size**: 4,000 questions

**Format**: Various formats including multiple-choice, short-answer, and descriptive

**Annotation**: Expert-reviewed for quality and relevance

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Calculating the accuracy based on correct and semi-correct responses from LLMs across various tasks.

**Interpretation**: Performance is categorized as Correct, Wrong, or Semi-correct based on the model's responses to the benchmark questions.

**Validation**: Supervised by expert reviewers throughout the development phase.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Toxic outputs', 'Cultural insensitivity']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
