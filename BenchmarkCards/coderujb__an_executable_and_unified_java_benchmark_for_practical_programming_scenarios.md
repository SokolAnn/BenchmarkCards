# CoderUJB: An Executable and Unified Java Benchmark for Practical Programming Scenarios

## 📊 Benchmark Details

**Name**: CoderUJB: An Executable and Unified Java Benchmark for Practical Programming Scenarios

**Overview**: CoderUJB is a new benchmark designed to evaluate LLMs across diverse Java programming tasks that are executable and reflective of actual development scenarios, comprising 2,239 programming questions derived from 17 real open-source Java projects and spanning five practical programming tasks.

**Data Type**: programming questions

**Domains**:
- Software Engineering

**Languages**:
- Java

**Similar Benchmarks**:
- HumanEval
- CoderEval

**Resources**:
- [GitHub Repository](https://github.com/WisdomShell/ujb)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the programming capabilities of large language models (LLMs) in real-world Java programming tasks.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Functional Code Generation
- Code-based Test Generation
- Issue-based Test Generation
- Defect Detection
- Automated Program Repair

**Limitations**: N/A

## 💾 Data

**Source**: 17 real open-source Java projects from the Defects4j dataset.

**Size**: 2,239 questions

**Format**: N/A

**Annotation**: Questions derived from software projects through abstract syntax tree analysis and defect report evaluations.

## 🔬 Methodology

**Methods**:
- Functional Code Generation
- Code-based Test Generation
- Issue-based Test Generation
- Defect Detection
- Automated Program Repair

**Metrics**:
- pass @ k
- count @ n
- coverage @ n
- accuracy

**Calculation**: Metrics are counted based on the successful generation of executable solutions and their correctness according to test coverage.

**Interpretation**: Higher values in metrics indicate better performance and more appropriate coding solutions according to the tasks defined.

**Baseline Results**: N/A

**Validation**: Benchmarked against leading open-source and closed-source LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
