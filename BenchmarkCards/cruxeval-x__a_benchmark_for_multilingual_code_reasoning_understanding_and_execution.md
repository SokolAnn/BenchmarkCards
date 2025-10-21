# CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution

## 📊 Benchmark Details

**Name**: CRUXEVAL-X: A Benchmark for Multilingual Code Reasoning, Understanding and Execution

**Overview**: CRUXEVAL-X is a multilingual code reasoning benchmark that contains 19 programming languages and is designed to address biases in existing code benchmarks while evaluating the capabilities of large language models in coding.

**Data Type**: input-output reasoning pairs

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java
- C++
- JavaScript
- TypeScript
- Ruby
- PHP
- Rust
- Scala
- Go
- Lua
- Racket
- Shell
- Swift
- D
- Perl
- Julia
- Scala

**Similar Benchmarks**:
- HumanEval
- SWE-bench

**Resources**:
- [Resource](https://arxiv.org/abs/2408.13001)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark that evaluates the reasoning capabilities of large language models across different programming languages.

**Target Audience**:
- ML Researchers
- Software Developers
- Academics

**Tasks**:
- Input Reasoning
- Output Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using an automated pipeline that includes code translation and generation steps

**Size**: 19,000 reasoning pairs

**Format**: N/A

**Annotation**: Automatically generated from existing code examples with iterative repairs based on execution feedback

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass@1

**Calculation**: Pass@1 accuracy is calculated based on the proportion of correctly answered test cases among total cases.

**Interpretation**: A higher Pass@1 indicates a better reasoning capability of the evaluated model.

**Baseline Results**: Results based on 24 mainstream LLMs tested against the benchmark.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
