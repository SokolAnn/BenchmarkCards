# CIBench

## 📊 Benchmark Details

**Name**: CIBench

**Overview**: CIBench is an interactive evaluation framework designed to assess LLMs' ability to utilize code interpreters for data science tasks through consecutive and interactive IPython sessions.

**Data Type**: data science tasks with code interpreter usage

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- GSM8K
- MathBench
- HumanEval
- MINT
- QwenAgent
- CodeGen
- DS-1000

**Resources**:
- [GitHub Repository](https://github.com/open-compass/CIBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CIBench is to provide a comprehensive evaluation of LLMs' proficiency in leveraging code interpreters for solving complex data science problems.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Data Analysis
- Data Visualization
- Machine Learning

**Limitations**: CIBench is currently limited to Python, and the evaluation metrics may not effectively measure certain data science tasks involving randomness.

## 💾 Data

**Source**: Evaluative tasks generated through an LLM-human cooperative approach based on Python libraries relevant to data science.

**Size**: 234 tasks, 1900+ questions

**Format**: Jupyter Notebook

**Annotation**: Tasks are refined and verified by human experts to ensure quality and clarity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Tool Call Rate
- Executable Rate
- Numeric Accuracy
- Text Score
- Visualization Score

**Calculation**: Metrics are calculated based on both process-oriented and output-oriented evaluations of model performance.

**Interpretation**: Higher scores signify better model performance in correctly following instructions and executing code.

**Baseline Results**: Comparison against previous benchmarks indicates the relative performance of LLMs on task completion.

**Validation**: Comprehensive tests were conducted using multiple models to validate the framework's effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Care was taken to exclude personal information in data collection processes.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
