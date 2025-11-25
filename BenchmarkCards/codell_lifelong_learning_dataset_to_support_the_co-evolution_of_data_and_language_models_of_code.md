# CodeLL (Lifelong Learning Dataset to Support the Co-Evolution of Data and Language Models of Code)

## 📊 Benchmark Details

**Name**: CodeLL (Lifelong Learning Dataset to Support the Co-Evolution of Data and Language Models of Code)

**Overview**: CodeLL is a lifelong learning dataset focused on code changes, capturing code changes across the entire release history of open-source software repositories.

**Data Type**: code change data

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- CodeXGlue
- CodeSearchNet
- CodeChangeNet

**Resources**:
- [GitHub Repository](https://github.com/martin-wey/CodeLL-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: To enable the study of language models of code in lifelong learning settings.

**Target Audience**:
- ML Researchers
- Software Engineers
- Data Scientists

**Tasks**:
- Code Change Analysis
- Lifelong Learning

**Limitations**: Initial version focuses only on machine learning archives, limiting its coverage.

## 💾 Data

**Source**: Software Heritage platform, specifically 71 Python repositories related to machine learning.

**Size**: 2,483 releases, 970,277 files

**Format**: JSONL

**Annotation**: No explicit annotation mentioned; data extracted through direct analysis.

## 🔬 Methodology

**Methods**:
- Code change analysis
- Statistical analysis

**Metrics**:
- Coverage of code changes over time
- Number of releases per repository

**Calculation**: Mapping of files, methods, and API calls between releases.

**Interpretation**: Dataset captures code evolution over time, providing insights into learning from past data.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning, Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
