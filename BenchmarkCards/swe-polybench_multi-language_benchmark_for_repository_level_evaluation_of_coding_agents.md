# SWE-PolyBench (Multi-language Benchmark for Repository Level Evaluation of Coding Agents)

## 📊 Benchmark Details

**Name**: SWE-PolyBench (Multi-language Benchmark for Repository Level Evaluation of Coding Agents)

**Overview**: SWE-PolyBench is a new multi-language benchmark for repository-level, execution-based evaluation of coding agents, containing 2110 instances from 21 repositories across Java, JavaScript, TypeScript, and Python, involving bug fixes, feature additions, and code refactoring.

**Data Type**: code modifications (pull requests)

**Domains**:
- Software Engineering

**Languages**:
- Java
- JavaScript
- TypeScript
- Python

**Similar Benchmarks**:
- SWE-Bench

**Resources**:
- [GitHub Repository](https://github.com/amazon-science/SWE-PolyBench)
- [Resource](https://huggingface.co/datasets/AmazonScience/SWE-PolyBench)

## 🎯 Purpose and Intended Users

**Goal**: To drive progress in developing versatile and robust AI coding assistants for real-world software engineering by providing a comprehensive multi-language evaluation framework.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Bug Fixing
- Feature Addition
- Code Refactoring

**Limitations**: While diverse in terms of languages and tasks, SWE-PolyBench has several limitations including a long tail of everyday coding tasks that are not addressed.

## 💾 Data

**Source**: Pull requests and issues from 21 repositories in Java, JavaScript, TypeScript, and Python.

**Size**: 2110 instances

**Format**: JSON

**Annotation**: Automatically generated for task descriptions and code patches.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Execution-based testing

**Metrics**:
- Pass Rate
- Node-level retrieval metrics
- File-level retrieval metrics

**Calculation**: Pass rate is defined as the percentage of tests that pass after applying the generated code changes, calculated over the entire dataset.

**Interpretation**: A higher pass rate indicates better performance by coding agents on the benchmark tasks.

**Validation**: Validation through execution of test suites associated with the pull requests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The dataset includes instances from diverse programming languages.

**Potential Harm**: ['Potential for code generation that does not adhere to best practices.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
