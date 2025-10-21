# FEA-Bench

## 📊 Benchmark Details

**Name**: FEA-Bench

**Overview**: FEA-Bench is a benchmark designed to assess the ability of large language models (LLMs) to perform incremental development within code repositories, specifically focusing on the implementation of new features through a dataset derived from pull requests in 83 GitHub repositories.

**Data Type**: task instances for feature implementation

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- SWE-bench

**Resources**:
- [GitHub Repository](https://github.com/microsoft/FEA-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the repository-level incremental code development capabilities of large language models (LLMs) when implementing new features.

**Target Audience**:
- ML Researchers
- Software Engineers

**Tasks**:
- Code Generation

**Limitations**: The benchmark includes only Python repositories and may exhibit certain limitations regarding data quality and diversity.

## 💾 Data

**Source**: Pull requests from 83 GitHub repositories.

**Size**: 1,401 task instances

**Format**: N/A

**Annotation**: Automatically filtered and paired with unit test files for verification.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Resolved Ratio

**Calculation**: The resolved ratio is defined as the percentage of task instances for which all unit tests pass.

**Interpretation**: A higher resolved ratio indicates better performance in successfully implementing new features.

**Validation**: Each task instance is validated by checking the pass status of related unit tests before and after applying code changes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data obtained from publicly available repositories with appropriate licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
