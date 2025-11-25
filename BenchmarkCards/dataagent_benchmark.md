# DataAgent Benchmark

## 📊 Benchmark Details

**Name**: DataAgent Benchmark

**Overview**: The DataAgent Benchmark evaluates the performance of Large Language Models (LLMs) in answering zero-shot queries related to various datasets, measuring their ability to extract correlations and insights through data analysis tasks.

**Data Type**: datasets of both numerical and categorical data

**Domains**:
- Natural Language Processing
- Data Science

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2404.00188v1)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the efficacy of Large Language Models as a Language Data Scientist for answering queries in data science.

**Target Audience**:
- Data Scientists
- Machine Learning Researchers

**Tasks**:
- Data Analysis
- Query Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated using GPT-3.5, representing a variety of scenarios in data science.

**Size**: 15 benchmark datasets of varying sizes (50 to 300 rows each)

**Format**: N/A

**Annotation**: Manually created answers for the benchmarks.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy was calculated by comparing the model's predicted outputs against manually calculated and supervised answers.

**Interpretation**: An accuracy score reflects how many queries were answered correctly compared to the total number of queries.

**Validation**: The model's outputs were tested against a set of manually created questions and answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
