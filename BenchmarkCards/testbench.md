# TestBench

## 📊 Benchmark Details

**Name**: TestBench

**Overview**: TestBench is the first class-level benchmark to evaluate the capability of LLMs on test case generation task. It includes a dataset of 108 Java programs sourced from large-scale open-source projects, and a comprehensive evaluation framework considering five aspects of test cases.

**Data Type**: test case generation

**Domains**:
- Software Engineering

**Languages**:
- Java

**Similar Benchmarks**:
- TestEval

**Resources**:
- [GitHub Repository](https://github.com/iSEngLab/TestBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of TestBench is to evaluate the effectiveness of large language models in generating test cases for software programs.

**Target Audience**:
- Researchers in Software Engineering
- Developers
- Model Evaluators

**Tasks**:
- Test Case Generation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed from 108 Java programs sourced from 9 large-scale open-source projects on GitHub.

**Size**: 108 Java programs

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Syntactic correctness
- Compilation correctness
- Execution correctness
- Coverage rate
- Defect detection rate

**Calculation**: Metrics are calculated based on static analysis for syntax, dynamic compilation for correctness, and mutation testing for defect detection.

**Interpretation**: Higher metrics indicate better performance in generating more reliable and correct test cases.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
