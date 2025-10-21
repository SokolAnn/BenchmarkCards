# HumanEvo (An Evolution-aware Benchmark for More Realistic Evaluation of Repository-level Code Generation)

## 📊 Benchmark Details

**Name**: HumanEvo (An Evolution-aware Benchmark for More Realistic Evaluation of Repository-level Code Generation)

**Overview**: HumanEvo is a novel evolution-aware repository-level code generation benchmark that simulates real-world software development processes by reflecting the dynamic nature of software projects over time. It aims to accurately evaluate the performance of Large Language Models (LLMs) in generating code that aligns with historical project states.

**Data Type**: programming tasks with dependency levels

**Domains**:
- Software Development

**Languages**:
- Python
- Java

**Similar Benchmarks**:
- CoderEval
- RepoBench
- EvoCodeBench
- RepoEval

**Resources**:
- [GitHub Repository](https://github.com/DeepSoftwareAnalytics/HumanEvo)
- [Resource](https://anonymous.4open.science/r/HumanEvo/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LLMs' performance in repository-level code generation that incorporates the temporal evolution of software projects.

**Target Audience**:
- ML Researchers
- Software Developers
- Benchmark Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: High-quality repositories from GitHub having over 50 common development domains.

**Size**: 400 task instances (200 for Python and 200 for Java)

**Format**: N/A

**Annotation**: Manual annotation by experienced programmers, including category labeling and docstring rewriting.

## 🔬 Methodology

**Methods**:
- Automated execution-based evaluation
- Human evaluation

**Metrics**:
- Accuracy
- Pass@1

**Calculation**: Metrics computed based on the execution correctness of generated code.

**Interpretation**: Higher accuracy indicates better performance of LLMs in generating contextually relevant code.

**Baseline Results**: Performance comparisons against traditional evolution-ignored methods showing discrepancies in results.

**Validation**: Rigorous execution-based validation ensuring task instances are covered by the project's test framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
