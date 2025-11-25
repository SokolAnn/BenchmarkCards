# SWE-bench-java-verified

## 📊 Benchmark Details

**Name**: SWE-bench-java-verified

**Overview**: SWE-bench-java-verified is a Java version of the SWE-bench benchmark designed for evaluating issue resolving capabilities of large language models in Java projects.

**Data Type**: issue instances for GitHub repositories

**Domains**:
- Software Engineering

**Languages**:
- Java

**Similar Benchmarks**:
- SWE-bench

**Resources**:
- [Resource](https://multi-swe-bench.github.io)
- [Resource](https://huggingface.co/datasets/Daoguang/Multi-SWE-bench)
- [GitHub Repository](https://github.com/multi-swe-bench/multi-swe-bench-env)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating issue resolving capabilities of large language models in Java projects.

**Target Audience**:
- Software Engineers
- ML Researchers
- Model Developers

**Tasks**:
- Issue Resolving

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Java open-source repositories on GitHub and the Defects4j database.

**Size**: 91 issues

**Format**: N/A

**Annotation**: Manual verification by experienced software developers.

## 🔬 Methodology

**Methods**:
- Manual verification
- Automated metrics

**Metrics**:
- Resolved Rate

**Calculation**: Resolved Rate is calculated as the proportion of issues that are successfully resolved by large language models.

**Interpretation**: An issue is considered resolved only if all given test cases pass.

**Baseline Results**: N/A

**Validation**: The benchmark was validated by subjecting it to thorough manual verification by experienced Java developers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
