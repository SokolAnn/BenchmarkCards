# OSS-BENCH

## 📊 Benchmark Details

**Name**: OSS-BENCH

**Overview**: OSS-BENCH is an automatic benchmark generator that constructs live, large-scale evaluation tasks from real-world open-source software by reusing natural ground truth signals—compilation results, functional test outcomes, and sanitizer checks.

**Data Type**: function-level code

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- BigCodeBench
- LiveCodeBench
- HumanEval-X

**Resources**:
- [Resource](https://oss-bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide rigorous and robust evaluation of the quality of LLM-generated code for various coding tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation
- Code Optimization

**Limitations**: N/A

## 💾 Data

**Source**: Real-world open-source software (OSS) projects

**Size**: 10,534 functions for PHP, 7,321 functions for SQLite3

**Format**: N/A

**Annotation**: Automated evaluation using compilation results and test outcomes

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Memory safety evaluation through sanitizers

**Metrics**:
- Compilability
- Functional Test
- Memory Safety

**Calculation**: Scores are aggregated from compilation success rates, test pass rates, and memory safety alerts.

**Interpretation**: Higher scores indicate better performance, with careful attention to overfitting and innovative code changes.

**Validation**: Benchmarks are continuously updated based on evolving OSS projects.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
