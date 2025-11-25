# SWE-Bench+ (Enhanced Coding Benchmark for LLMs)

## 📊 Benchmark Details

**Name**: SWE-Bench+ (Enhanced Coding Benchmark for LLMs)

**Overview**: SWE-Bench+ is created to offer a more rigorous evaluation dataset for Large Language Models in the context of software engineering, particularly focusing on GitHub issues that ensure no solution leakage and are collected after model training cut-off dates.

**Data Type**: GitHub issue-patch pairs

**Domains**:
- Software Engineering

**Similar Benchmarks**:
- SWE-bench
- SWE-bench Lite
- SWE-bench Verified

**Resources**:
- [Resource](https://zenodo.org/records/13879453)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the capabilities of LLMs in resolving software issues without solution leakage and data exposure from training.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Bug Fixing
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: GitHub issues collected from various repositories following a systematic selection process.

**Size**: 548 issues

**Format**: JSON

**Annotation**: Issues were manually screened to ensure that they do not contain solutions or comments with solutions.

## 🔬 Methodology

**Methods**:
- Patch validation study
- Manual validation of model outputs

**Metrics**:
- Resolution Rate

**Calculation**: Resolution rates were calculated based on the number of issues successfully resolved by the model relative to the total number of issues in the dataset.

**Interpretation**: A higher resolution rate indicates a model's better capability in generating valid patches for software issues.

**Validation**: Involves comparing model-generated patches with validated gold patches from GitHub.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
