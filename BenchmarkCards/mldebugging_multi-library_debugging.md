# MLDebugging (Multi-Library Debugging)

## 📊 Benchmark Details

**Name**: MLDebugging (Multi-Library Debugging)

**Overview**: MLDebugging is a comprehensive benchmark designed to assess debugging challenges within multi-library Python code, encompassing 126 distinct Python libraries and categorized into seven types of multi-library code issues.

**Data Type**: code snippets

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- DebugBench
- xCodeEval
- HumanEval

**Resources**:
- [GitHub Repository](https://github.com/hjyTsuki/MLDebugging)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate debugging capabilities of models in complex multi-library scenarios.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Code Debugging

**Limitations**: The dataset primarily consists of automatically generated data, which may differ from real-world scenarios.

## 💾 Data

**Source**: Generated from a mix of common programming tasks and based on multiple libraries.

**Size**: 1,175 samples

**Format**: JSON

**Annotation**: Manual annotation by experts and debugging through multiple LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass rate

**Calculation**: The pass rate is calculated based on the proportion of code that passes all test cases.

**Interpretation**: A higher pass rate indicates better debugging capabilities of the models on the multi-library tasks.

**Validation**: Cross-checked by experienced programmers for quality control.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: Not discussed

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
