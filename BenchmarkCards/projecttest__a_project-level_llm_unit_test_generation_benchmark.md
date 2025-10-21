# ProjectTest: A Project-level LLM Unit Test Generation Benchmark

## 📊 Benchmark Details

**Name**: ProjectTest: A Project-level LLM Unit Test Generation Benchmark

**Overview**: ProjectTest is a project-level benchmark for unit test generation covering Python, Java, and JavaScript. It features 20 moderate-sized and high-quality projects per language, providing a comprehensive evaluation of LLMs' unit test generation capabilities.

**Data Type**: unit test generation data

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java
- JavaScript

**Similar Benchmarks**:
- DevBench

**Resources**:
- [GitHub Repository](https://github.com/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable and high-quality benchmark for evaluating unit test generation by LLMs.

**Target Audience**:
- ML Researchers
- Software Developers
- Industry Practitioners

**Tasks**:
- Unit Test Generation

**Limitations**: N/A

## 💾 Data

**Source**: GitHub repositories filtered based on specific criteria for selection.

**Size**: 60 projects (20 per language)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation of LLMs on generated unit tests
- Manual error fixing
- Self-fixing by LLMs

**Metrics**:
- Compilation Rate
- Correctness Rate
- Line Coverage
- Branch Coverage

**Calculation**: Metrics are calculated based on the performance of generated unit tests across different scenarios.

**Interpretation**: Higher rates indicate better performance in generating valid and efficient unit tests.

**Baseline Results**: Performance of nine frontier LLMs evaluated against ProjectTest.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT, GPL-2.0, Apache-2.0 licenses for projects included.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
