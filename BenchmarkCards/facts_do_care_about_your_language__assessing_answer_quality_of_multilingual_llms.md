# Facts Do Care About Your Language: Assessing Answer Quality of Multilingual LLMs

## 📊 Benchmark Details

**Name**: Facts Do Care About Your Language: Assessing Answer Quality of Multilingual LLMs

**Overview**: This work evaluates the correctness of the Llama3.1 family of models in answering factual questions appropriate for middle and high school students across different languages, revealing inconsistencies and biases in language model responses.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Japanese
- Arabic
- French
- Chinese
- Persian
- Hebrew
- Hindi
- Nepali
- Haitian Creole
- Tulu
- Māori
- English

**Similar Benchmarks**:
- Factcheck-Bench

**Resources**:
- [Resource](https://arxiv.org/abs/2506.03051)

## 🎯 Purpose and Intended Users

**Goal**: To measure the factuality and consistency of LLM responses to middle and high school level questions in various languages.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: A set of 54 factual questions covering middle and high school curriculum designed to evaluate LLM factuality.

**Size**: 54 questions

**Format**: N/A

**Annotation**: Manual evaluation by bilingual individuals

## 🔬 Methodology

**Methods**:
- Manual evaluation
- Automated analysis

**Metrics**:
- Keyword Coverage
- Incorrectness Score
- Extraneous Score

**Calculation**: Responses evaluated against predefined target keywords and rated for factual accuracy and extraneous information.

**Interpretation**: Higher scores indicate better keyword coverage and lower incorrectness; lower extraneous scores indicate more relevant answers.

**Validation**: Manual analysis by bilingual evaluators

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
