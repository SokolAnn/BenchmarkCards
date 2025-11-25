# DynaCode: A Dynamic Complexity-Aware Code Benchmark for Evaluating Large Language Models in Code Generation

## 📊 Benchmark Details

**Name**: DynaCode: A Dynamic Complexity-Aware Code Benchmark for Evaluating Large Language Models in Code Generation

**Overview**: DynaCode is a dynamic, complexity-aware benchmark designed to systematically evaluate LLMs on code generation tasks. It generates nested code problems that capture varying levels of code complexity and inter-function dependencies, addressing the limitations of static benchmarks such as data contamination.

**Data Type**: code generation problems

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- CodeXGLUE
- ClassEval

**Resources**:
- [GitHub Repository](https://github.com/HWH-2000/DynaCode)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable benchmark for evaluating the code generation capabilities of large language models (LLMs) through a dynamic evaluation strategy that incorporates code complexity and call-graph structures.

**Target Audience**:
- ML Researchers
- Model Developers
- Software Engineers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated dynamically from a set of existing code problems and complexity metrics.

**Size**: 189,263,141 unique code generation tasks

**Format**: N/A

**Annotation**: Automatically generated with validation against ground truth code.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Dynamic evaluation a strategy using complexity measures

**Metrics**:
- Pass@1 Score

**Calculation**: The percentage of code problems solved correctly by models on the first attempt without additional corrections.

**Interpretation**: Higher Pass@1 scores indicate better generalization capabilities of the LLMs across increasingly complex code problems.

**Baseline Results**: Previous benchmarks include MBPP and MBPP+ with comparative results shown for various LLMs.

**Validation**: Results validated through multiple evaluations across different complexity levels.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Robustness**: Prompt leaking
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
