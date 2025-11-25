# REPOEXEC

## 📊 Benchmark Details

**Name**: REPOEXEC

**Overview**: REPOEXEC is a benchmark for evaluating repository-level code generation, focusing on executability, functional correctness, and dependency utilization.

**Data Type**: code snippets with dependencies

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- RepoBench
- RepoCoder
- CrossCodeEval
- CoCoMIC
- DevEval

**Resources**:
- [GitHub Repository](https://github.com/FSoft-AI4Code/RepoExec)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to ensure both functional correctness and effective dependency utilization in code generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Auto-generated test cases from large language models and existing repository data.

**Size**: 355 samples

**Format**: CSV

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Automated metrics
- Execution-based evaluation

**Metrics**:
- Pass@1
- Dependency Invocation Rate (DIR)

**Calculation**: DIR is calculated as the number of dependencies invoked in the solution relative to the total number of provided dependencies.

**Interpretation**: Higher Pass@1 indicates correct code generation. Higher DIR indicates better utilization of provided dependencies.

**Validation**: Code functionality is validated through automated test case execution.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
