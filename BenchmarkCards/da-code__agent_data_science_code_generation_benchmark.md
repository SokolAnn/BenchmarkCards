# DA-Code: Agent Data Science Code Generation Benchmark

## 📊 Benchmark Details

**Name**: DA-Code: Agent Data Science Code Generation Benchmark

**Overview**: DA-Code is a code generation benchmark specifically designed to assess LLMs on agent-based data science tasks, featuring challenging tasks sourced from diverse real-world data, requiring the use of complex data science programming languages.

**Data Type**: code generation tasks

**Domains**:
- Natural Language Processing

**Languages**:
- Python
- SQL
- Bash

**Similar Benchmarks**:
- DS-1000
- Arcade

**Resources**:
- [Resource](https://da-code-bench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the code generation capabilities of large language models in complex data science tasks.

**Target Audience**:
- ML Researchers
- AI Developers
- Data Scientists

**Tasks**:
- Data Wrangling
- Machine Learning
- Exploratory Data Analysis

**Limitations**: The performance of existing LLMs is modest, achieving approximately 30.5% accuracy, indicating significant room for improvement.

## 💾 Data

**Source**: Real-world data sources from Kaggle, GitHub, and other platforms

**Size**: 500 complex tasks

**Format**: CSV

**Annotation**: Carefully designed tasks by experienced annotators

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on performance benchmarks established within the evaluation suite.

**Interpretation**: Scores represent the effectiveness of LLM agents in completing the designated coding tasks.

**Baseline Results**: DA-Agent baseline achieves a performance score of 30.5% on average.

**Validation**: Cross-validation and red team testing ensure robustness of evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: Analysis of performance across different tasks and models is underway to explore demographic impacts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
