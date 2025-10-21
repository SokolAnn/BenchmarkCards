# CFinBench: A Comprehensive Chinese Financial Benchmark for Large Language Models

## 📊 Benchmark Details

**Name**: CFinBench: A Comprehensive Chinese Financial Benchmark for Large Language Models

**Overview**: CFinBench is a meticulously crafted evaluation benchmark for assessing the financial knowledge of LLMs under the Chinese context, consisting of 99,100 questions spanning 43 second-level categories with three question types.

**Data Type**: question-answering pairs

**Domains**:
- Finance
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMLU
- C-Eval
- Xiezhi
- AGIEval

**Resources**:
- [Resource](https://cfinbench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the financial domain knowledge of large language models in the context of Chinese financial tasks.

**Target Audience**:
- ML Researchers
- Financial Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: Focuses on the Chinese financial system; not suitable for assessing financial knowledge in other countries.

## 💾 Data

**Source**: Mock exams and publicly available materials, including real-world examination questions.

**Size**: 99,100 questions

**Format**: N/A

**Annotation**: Rigorous data processing pipelines including cleaning, de-duplication, LLM-assisted question rephrasing, option shuffling, and human cross-validation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the match between model prediction and gold answer.

**Interpretation**: An accuracy score is interpreted based on model performance in different categories.

**Baseline Results**: The highest average accuracy reported for GPT4 is 60.16%.

**Validation**: Not explicitly stated.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache-2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
