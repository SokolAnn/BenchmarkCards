# DI-B ENCH (Dependency Benchmark)

## 📊 Benchmark Details

**Name**: DI-B ENCH (Dependency Benchmark)

**Overview**: DI-B ENCH is a large-scale benchmark and evaluation framework specifically designed to assess LLMs’ capability on dependency inference, featuring 581 repositories across multiple programming languages.

**Data Type**: repositories and configuration files

**Domains**:
- Software Development

**Languages**:
- Python
- C#
- Rust
- JavaScript

**Resources**:
- [GitHub Repository](https://github.com/Microsoft/DI-Bench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate LLMs’ capabilities in accurately inferring dependencies across large-scale software repositories.

**Target Audience**:
- Researchers
- Software Developers
- Machine Learning Practitioners

**Tasks**:
- Dependency Inference

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is sourced from real-world GitHub repositories and includes various configurations for testing dependency inference.

**Size**: 581 repositories

**Format**: CSV and structured text files

**Annotation**: Automated curation of datasets with dependency masking

## 🔬 Methodology

**Methods**:
- Textual Matching
- Execution-based Evaluation

**Metrics**:
- Executability Rate
- Textual Accuracy (Precision, Recall, F1 Score)
- Fake Rate

**Calculation**: Metrics are calculated based on matching generated dependencies against ground truth dependencies and through automated test runs.

**Interpretation**: Higher executability rates indicate better model performance in correctly identifying required dependencies.

**Baseline Results**: The best-performing model achieved a 42.9% executability rate.

**Validation**: Validation is performed through Continuous Integration (CI) pipelines executing tests on the generated code.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
