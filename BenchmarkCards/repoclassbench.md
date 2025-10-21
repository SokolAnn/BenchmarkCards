# RepoClassBench

## 📊 Benchmark Details

**Name**: RepoClassBench

**Overview**: RepoClassBench is a comprehensive benchmark designed to rigorously evaluate LLMs in generating complex, class-level code within real-world repositories, including tasks across Java, Python, and C#. It includes classes with cross-file dependencies and corresponding test cases.

**Data Type**: class generation tasks

**Domains**:
- Software Engineering

**Languages**:
- Java
- Python
- C#

**Similar Benchmarks**:
- HumanEval
- MBPP
- ClassEval

**Resources**:
- [GitHub Repository](https://github.com/microsoft/RepoClassBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating LLMs in the context of class-level code generation within software repositories.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Class Generation

**Limitations**: N/A

## 💾 Data

**Source**: Public GitHub repositories, focusing on Java, Python, and C# classes with dependencies.

**Size**: 130 Java classes, 97 Python classes, 60 C# classes

**Format**: N/A

**Annotation**: Each class is validated with corresponding test cases.

## 🔬 Methodology

**Methods**:
- Test case evaluation
- Static analysis with repository tools
- Tool-based feedback mechanisms

**Metrics**:
- Test Rate (TR)
- Pass@K

**Calculation**: Metrics are calculated based on the percentage of test cases passed for the generated classes.

**Interpretation**: Higher scores on metrics indicate better performance in code generation tasks.

**Baseline Results**: Compared against existing benchmarks like HumanEval and ClassEval.

**Validation**: The benchmark was validated through test feedback and code compilation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
