# Web-Bench

## 📊 Benchmark Details

**Name**: Web-Bench

**Overview**: Web-Bench is a new benchmark containing 50 projects, each consisting of 20 tasks with sequential dependencies, simulating real-world human development workflows in web development using Web Standards and Web Frameworks.

**Data Type**: tasks with sequential dependencies

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- JavaScript
- TypeScript

**Similar Benchmarks**:
- HumanEval
- MBPP
- SWE-Bench
- RepoBench

**Resources**:
- [GitHub Repository](https://github.com/bytedance/web-bench)
- [Resource](https://huggingface.co/datasets/bytedance-research/Web-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more realistic evaluation of large language models in coding by simulating the complexities of real-world software development.

**Target Audience**:
- ML Researchers
- Software Engineers
- LLM Developers

**Tasks**:
- Code Generation
- Software Development

**Limitations**: The current version of Web-Bench is limited to covering core standards and frameworks, and does not yet include all possible web technologies due to workload constraints.

## 💾 Data

**Source**: Dynamic tasks based on real-world software engineering domains

**Size**: 50 projects, each with 20 tasks

**Format**: JSON, YAML

**Annotation**: Automatically generated with expert reference

## 🔬 Methodology

**Methods**:
- End-to-end testing
- Automated evaluation metrics

**Metrics**:
- Pass@1
- Pass@2

**Calculation**: Pass@1 is the percentage of tasks passing all end-to-end tests on the first attempt; Pass@2 includes retries.

**Interpretation**: Higher Pass@1 and Pass@2 scores indicate better performance of LLMs in code generation tasks.

**Baseline Results**: Claude 3.7 Sonnet achieved a Pass@1 of 25.1% on the Web-Bench.

**Validation**: Validated through multiple passes and comparison with existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
