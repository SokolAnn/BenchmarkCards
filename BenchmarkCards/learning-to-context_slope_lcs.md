# Learning-to-Context Slope (LCS)

## 📊 Benchmark Details

**Name**: Learning-to-Context Slope (LCS)

**Overview**: LCS quantifies the effectiveness of in-context learning (ICL) by modeling the slope between learning gain (loss decrease from demonstrations) and contextual relevance (demonstration-input relevance), addressing reliability and attribution issues in performance-based metrics.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU-Pro
- GSM8K
- MATH
- HumanEval
- ARC-Challenge
- FinQA
- Amazon Review

**Resources**:
- [Resource](https://arxiv.org/abs/2506.23146)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable metric for evaluating in-context learning effectiveness.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Problem Solving
- Code Generation
- Question Answering

**Limitations**: The current experimental datasets and models are limited.

## 💾 Data

**Source**: Multiple datasets including GSM8K, MATH, HumanEval, MBPP, ARC-Challenge, MMLU-Pro, FinQA, and Amazon Review.

**Size**: 8 datasets used for experiments

**Format**: Various, depending on the dataset

**Annotation**: Synthetic evaluations and task-specific demonstrations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Synthetic evaluation
- Demonstration selection

**Metrics**:
- Correlation with performance improvement

**Calculation**: The slope is calculated based on the relationship between learning gain and contextual relevance.

**Interpretation**: High LCS indicates effective ICL; low LCS suggests limited learning from demonstrations.

**Validation**: Extensive experiments on multiple datasets to validate the correlation of LCS with task performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Analysis of ICL effectiveness across different model scales and capabilities.

**Potential Harm**: Potential misinterpretation of performance gains could mislead practitioners in their application of ICL.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The datasets and models used are publicly available and follow their respective licenses.

**Data Licensing**: Public datasets with specified licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
