# DomainCodeBench

## 📊 Benchmark Details

**Name**: DomainCodeBench

**Overview**: DomainCodeBench is a multi-domain code generation benchmark designed to systematically evaluate LLMs across 12 software application domains and 15 programming languages. It contains 2,400 manually verified tasks with ground-truth, human-annotated docstrings, and fine-grained dependency information to ensure more coverage of domain-specific challenges.

**Data Type**: programming tasks

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Python
- JavaScript
- TypeScript
- Solidity
- Go
- C#
- C++
- C
- Java
- Rust
- Scala
- PHP
- Lua
- Kotlin
- Swift

**Similar Benchmarks**:
- DomainEval

**Resources**:
- [GitHub Repository](https://github.com/DeepSoftwareAnalytics/DomainCodeBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of DomainCodeBench is to evaluate LLMs' code generation capabilities in a variety of specific application domains.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: High-quality open-source repositories on GitHub spanning 12 specific application domains.

**Size**: 2400 task instances

**Format**: N/A

**Annotation**: Manually annotated through cross-validation involving experienced programmers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- CodeBLEU

**Calculation**: The CodeBLEU score evaluates both textual and semantic matches of the generated code against the ground truth.

**Interpretation**: Higher CodeBLEU scores indicate better alignment of generated code with reference outputs.

**Baseline Results**: The performance comparisons of various LLMs on code generation tasks were conducted.

**Validation**: The code generation tasks were validated through extensive manual checking and dependency analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Domain-specific weaknesses']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
