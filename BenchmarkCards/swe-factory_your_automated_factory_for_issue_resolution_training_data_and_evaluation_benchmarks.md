# SWE-Factory (Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks)

## 📊 Benchmark Details

**Name**: SWE-Factory (Your Automated Factory for Issue Resolution Training Data and Evaluation Benchmarks)

**Overview**: We propose SWE-Factory, an automatic benchmark construction pipeline for the GitHub issue resolution task, which automates the construction of high-quality GitHub issue resolution datasets through multi-agent framework and exit-code-based methods.

**Data Type**: text

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java
- JavaScript
- TypeScript

**Similar Benchmarks**:
- SWE-bench

**Resources**:
- [GitHub Repository](https://github.com/DeepSoftwareAnalytics/swe-factory)

## 🎯 Purpose and Intended Users

**Goal**: To provide an automatic pipeline for constructing GitHub issue resolution benchmarks with minimal manual intervention.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Issue Resolution

**Limitations**: N/A

## 💾 Data

**Source**: Collected from GitHub issues and repositories using automated processes.

**Size**: 2,441 issues (671 sampled for evaluation)

**Format**: N/A

**Annotation**: Automated validation and grading using exit codes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Multi-agent evaluation
- Exit-code based grading

**Metrics**:
- Valid Rate
- Success Rate
- Precision
- Recall

**Calculation**: Metrics calculated based on manual inspection and automated validation.

**Interpretation**: High Valid Rate and Success Rate indicate effective construction of benchmark instances.

**Baseline Results**: SWE-Factory successfully constructs 269 valid benchmark instances out of 671 issues.

**Validation**: Validation through exit-code-based tests before and after applying patches.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
