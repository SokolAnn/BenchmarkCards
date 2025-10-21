# TESTGENEVAL: A REAL WORLD UNIT TEST GENERATION AND TEST COMPLETION BENCHMARK

## 📊 Benchmark Details

**Name**: TESTGENEVAL: A REAL WORLD UNIT TEST GENERATION AND TEST COMPLETION BENCHMARK

**Overview**: TESTGENEVAL is a large-scale benchmark to measure test generation performance, comprising 68,647 tests from 1,210 code and test file pairs across 11 Python repositories. It evaluates test authoring, test suite completion, and code coverage improvements.

**Data Type**: test generation and completion tasks

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- TestEval
- SWT-Bench
- R2E

**Resources**:
- [Resource](https://figshare.com/s/51171ae97cd21d233d4f)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating test generation and completion performance of models in real-world software development scenarios.

**Target Audience**:
- ML Researchers
- Software Engineers
- Code Generation Practitioners

**Tasks**:
- Test Generation
- Test Completion

**Limitations**: While TESTGENEVAL aims to evaluate test generation capabilities, models may struggle with complex execution reasoning and the quality of generated tests, impacting overall performance.

## 💾 Data

**Source**: SWEBench adapted for software testing tasks consisting of real-world code and test files from popular Python repositories.

**Size**: 68,647 tests from 1,210 code and test file pairs

**Format**: raw text files

**Annotation**: Tests are curated from human-written sources and are executed to measure their effectiveness.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Coverage
- Mutation Score
- Pass@1
- Pass@5

**Calculation**: Coverage measures the proportion of lines executed by the test suite, Mutation Score is the percentage of injected bugs detected by the tests.

**Interpretation**: Higher values in coverage and mutation scores indicate better model performance in generating effective test suites.

**Baseline Results**: The best-performing model achieved a coverage of 35.2% with a mutation score of 18.8%.

**Validation**: Models were evaluated on the benchmark with multiple runs to ensure reliability across different configurations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The benchmark includes diverse software projects, but specific demographic analysis of the training data is not available.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
