# RepoTransBench

## 📊 Benchmark Details

**Name**: RepoTransBench

**Overview**: RepoTransBench is a real-world repository-level code translation benchmark designed to evaluate the performance of code translation tools using entire code repositories rather than just snippets or files. It includes 100 repository samples and an automatically executable test suite to ensure functionality.

**Data Type**: repository code samples

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java

**Similar Benchmarks**:
- CoST
- CodeNet
- HumanEval-X
- TransCoder-test

**Resources**:
- [Resource](https://huggingface.co/datasets/bigcode/the-stack)
- [Resource](https://huggingface.co/datasets/bigcode/the-stack-v2)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of RepoTransBench is to provide a comprehensive evaluation framework for repository-level code translation, highlighting the performance of existing LLMs and addressing the common challenges faced in this area.

**Target Audience**:
- Machine Learning Researchers
- Software Engineers
- Developers

**Tasks**:
- Code Translation
- Model Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Real-world repositories collected from The Stack and The Stack v2.

**Size**: 100 repository samples

**Format**: N/A

**Annotation**: Test cases generated through a combination of automated translation and manual verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Execution-based evaluation
- Iterative debugging

**Metrics**:
- Success@k
- Build@k
- Average Pass Rate (APR)

**Calculation**: Metrics are calculated based on the success of repositories passing test cases across multiple attempts.

**Interpretation**: A higher Success@k indicates better performance of the translation model in achieving functional equivalence.

**Baseline Results**: The best-performing LLM, Claude-3.5-Sonnet, achieved 7.33% on Success@1.

**Validation**: Repositories were validated through execution in a controlled environment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
