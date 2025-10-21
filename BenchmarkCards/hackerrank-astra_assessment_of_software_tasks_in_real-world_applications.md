# HackerRank-ASTRA (Assessment of Software Tasks in Real-world Applications)

## 📊 Benchmark Details

**Name**: HackerRank-ASTRA (Assessment of Software Tasks in Real-world Applications)

**Overview**: The HackerRank-ASTRA Benchmark introduces project-based coding problems that mirror real-world scenarios, specifically evaluating model consistency through multiple runs and incorporating a taxonomy-level analysis to assess sub-skill capabilities.

**Data Type**: project-based coding problems

**Domains**:
- Software Development

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- SWE-bench
- DevEval

**Resources**:
- [Resource](https://huggingface.co/datasets/hackerrank/astra-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for multi-file, project-based software development problems.

**Target Audience**:
- ML Researchers
- Software Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: HackerRank's proprietary library of multi-file, project-based software development problems.

**Size**: 65 project-based coding problems

**Format**: CSV

**Annotation**: Manual preparation by HackerRank’s Content Creation team.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Consistency evaluation using multiple runs

**Metrics**:
- Mean Score
- Mean Pass@1
- Median standard deviation

**Calculation**: Aggregated scores across 32 runs for each problem to compute overall metrics.

**Interpretation**: Higher scores indicate better performance, while lower median standard deviation indicates higher consistency.

**Baseline Results**: Initial evaluations of models using ASTRA showed mean scores around 75%.

**Validation**: Performance evaluated through Docker container against pre-defined test cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
