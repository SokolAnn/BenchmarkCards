# Exec-CSN

## 📊 Benchmark Details

**Name**: Exec-CSN

**Overview**: Exec-CSN is a dataset created using the CODEBENCH GEN framework, containing 1,931 examples adapted from 367 GitHub repositories to evaluate code generation systems through execution-based benchmarks.

**Data Type**: code examples with test cases

**Domains**:
- Natural Language Processing

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- MBPP
- APPS
- DS1000
- ODEX
- SWE-BENCH

**Resources**:
- [GitHub Repository](https://github.com/yiqingxyq/CodeBenchGen)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the evaluation of code generation systems across diverse scenarios and to provide scalable execution-based benchmarks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: GitHub repositories sampled from the CodeSearchNet dataset.

**Size**: 1,931 examples

**Format**: N/A

**Annotation**: Automatically generated and adapted using the CODEBENCH GEN framework.

## 🔬 Methodology

**Methods**:
- Execution-based evaluation
- Human evaluation

**Metrics**:
- Pass@1
- Pass@2
- Pass@5
- Pass@10

**Calculation**: Metrics are calculated based on the number of examples that pass the generated test cases.

**Interpretation**: Higher Pass@k scores indicate better performance by models in generating correct code.

**Baseline Results**: GPT-4 achieved a Pass@1 score of 37.21%.

**Validation**: The dataset was validated through human studies and iterative execution and debugging methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
