# Finance MATH

## 📊 Benchmark Details

**Name**: Finance MATH

**Overview**: Finance MATH is a benchmark designed to evaluate LLMs’ capabilities in solving knowledge-intensive math reasoning problems specifically in finance. It includes 1,200 problems that require college-level knowledge in finance and incorporates both textual and tabular data.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FinQA
- TAT-QA
- MultiHiertt

**Resources**:
- [GitHub Repository](https://github.com/yale-nlp/FinanceMath)
- [Resource](https://financemath-acl2024.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To assess LLMs' abilities in knowledge-intensive math reasoning in the finance domain.

**Target Audience**:
- ML Researchers
- Finance Practitioners
- Model Developers

**Tasks**:
- Mathematical Reasoning
- Data Interpretation

**Limitations**: N/A

## 💾 Data

**Source**: Expert-annotated questions created from a knowledge bank of financial terms.

**Size**: 1,200 examples

**Format**: Python program

**Annotation**: Annotated by experts with detailed solution references.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the correct answers provided by LLMs compared to the ground truth.

**Interpretation**: Accuracy measures how well LLMs solve knowledge-intensive math problems in finance, with a focus on comparing performance against human expert benchmarks.

**Baseline Results**: The best-performing model, GPT-4o, achieves 60.9% accuracy.

**Validation**: Comprehensive validation protocols involving multiple annotators to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
