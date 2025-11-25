# COMPASS (COdility’s Multi-dimensional Programming ASSessment)

## 📊 Benchmark Details

**Name**: COMPASS (COdility’s Multi-dimensional Programming ASSessment)

**Overview**: COMPASS is a comprehensive evaluation framework that assesses code generation across three dimensions: correctness, efficiency, and quality. It consists of 50 competitive programming problems from real Codility competitions and provides extensive human performance baselines.

**Data Type**: programming problems

**Domains**:
- Natural Language Processing

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- MBPP
- HackerRank-ASTRA

**Resources**:
- [Resource](https://arxiv.org/abs/2508.13757)

## 🎯 Purpose and Intended Users

**Goal**: To provide a tool for evaluating not just whether models can solve problems, but how they solve them and at what cost.

**Target Audience**:
- Researchers
- Practitioners
- Model Developers

**Tasks**:
- Code Generation
- Algorithmic Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Real coding competitions hosted by Codility from 2011 to 2021.

**Size**: 50 problems

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Correctness
- Efficiency
- Code Quality

**Calculation**: Correctness is the percentage of test cases passed; efficiency is evaluated under strict runtime thresholds; quality is assessed using static analysis through CodeScene.

**Interpretation**: Higher scores indicate better performance in correctness, efficiency, and code quality.

**Baseline Results**: Human performance data from 393,150 submissions shows average scores across all tasks.

**Validation**: Validation included correlation analyses and PCA to confirm distinct contributions from each performance dimension.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
