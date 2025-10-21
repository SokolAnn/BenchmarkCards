# TESTEVAL

## 📊 Benchmark Details

**Name**: TESTEVAL

**Overview**: TESTEVAL is a benchmark for evaluating large language models' test case generation capabilities focused on Python programs, involving three distinct tasks: overall coverage, targeted line/branch coverage, and targeted path coverage.

**Data Type**: Python programs

**Domains**:
- Software Engineering

**Languages**:
- Python

**Resources**:
- [GitHub Repository](https://github.com/LLM4SoftwareTesting/TestEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of large language models in generating effective test cases for Python programs.

**Target Audience**:
- ML Researchers
- Software Developers
- Testing Engineers

**Tasks**:
- Test Case Generation
- Overall Coverage Evaluation
- Targeted Line Coverage
- Targeted Branch Coverage
- Targeted Path Coverage

**Limitations**: N/A

## 💾 Data

**Source**: Collected 210 Python programs from LeetCode, focusing on programs with adequate complexity.

**Size**: 210 programs

**Format**: N/A

**Annotation**: Programs are manually filtered and selected based on their cyclomatic complexity and properties.

## 🔬 Methodology

**Methods**:
- Evaluation of model-generated test cases
- Syntactic correctness check
- Execution correctness check
- Assertion correctness check

**Metrics**:
- Overall coverage
- Targeted line coverage
- Branch coverage
- Path coverage

**Calculation**: Metrics are calculated based on the proportion of lines/branches covered by generated test cases.

**Interpretation**: High scores indicate effective test case generation capability while lower scores suggest areas for improvement in LLM logic comprehension.

**Baseline Results**: N/A

**Validation**: Extensive experiments involving 17 different LLMs evaluating on the TESTEVAL benchmark.

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

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data collected from GitHub repository licensed under MIT.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
