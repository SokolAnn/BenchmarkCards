# UGM ATHBENCH (Undergraduate-Level Mathematical Reasoning with Large Language Models)

## 📊 Benchmark Details

**Name**: UGM ATHBENCH (Undergraduate-Level Mathematical Reasoning with Large Language Models)

**Overview**: UGMathBench is a diverse and dynamic benchmark specifically designed for evaluating undergraduate-level mathematical reasoning with LLMs, comprising 5,062 problems across 16 subjects and 111 topics.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH

**Resources**:
- [GitHub Repository](https://github.com/YangLabHKUST/UGMathBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and fair evaluation of the mathematical reasoning capabilities of LLMs through a dynamic benchmark.

**Target Audience**:
- ML Researchers
- Educational Practitioners

**Tasks**:
- Mathematical Reasoning

**Limitations**: UGMathBench focuses on text-only reasoning and is designed as an English-language benchmark.

## 💾 Data

**Source**: Compiling from an online grading system of undergraduate courses.

**Size**: 5,062 problems

**Format**: LaTeX

**Annotation**: Automatically generated and cleaned problems from student interactions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Effective Accuracy (EAcc)
- Reasoning Gap (∆)

**Calculation**: EAcc measures the percentage of problems solved correctly across randomized versions; ∆ calculates the difference between average accuracy and EAcc.

**Interpretation**: Higher EAcc indicates better reasoning abilities; lower ∆ suggests better performance with variations in problem formulation.

**Validation**: Extensive evaluation of 23 leading LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
