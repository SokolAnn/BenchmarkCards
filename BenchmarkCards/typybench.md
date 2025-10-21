# TYPYBENCH

## 📊 Benchmark Details

**Name**: TYPYBENCH

**Overview**: TYPYBENCH is a benchmark designed to evaluate LLMs’ type inference across entire Python repositories. It introduces two novel metrics: TYPESIM, which captures nuanced semantic relationships between predicted and ground truth types, and TYPECHECK, which assesses type consistency across codebases.

**Data Type**: source code

**Domains**:
- Software Engineering

**Languages**:
- Python

**Resources**:
- [GitHub Repository](https://github.com/typybench/typybench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized evaluation framework for assessing the type inference capabilities of LLMs in Python repositories.

**Target Audience**:
- ML Researchers
- Software Developers
- Model Developers

**Tasks**:
- Type Inference

**Limitations**: N/A

## 💾 Data

**Source**: Curated dataset of 50 high-quality Python repositories from GitHub and PyPI.

**Size**: 50 repositories

**Format**: N/A

**Annotation**: Manual cleaning and preparation of repositories with type information removed.

## 🔬 Methodology

**Methods**:
- Evaluation of LLMs
- Benchmarking with TYPESIM and TYPECHECK metrics

**Metrics**:
- TYPESIM
- TYPECHECK

**Calculation**: TYPESIM measures functional similarity between predicted and human-annotated types using structural relationships. TYPECHECK uses mypy to assess type consistency across codebases.

**Interpretation**: Higher TYPESIM indicates better semantic similarity, while lower TYPECHECK errors suggest better consistency.

**Validation**: Empirical studies comparing performance across state-of-the-art LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
