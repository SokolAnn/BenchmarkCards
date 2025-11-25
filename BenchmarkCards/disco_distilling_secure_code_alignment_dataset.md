# DiSCo (Distilling Secure Code Alignment Dataset)

## 📊 Benchmark Details

**Name**: DiSCo (Distilling Secure Code Alignment Dataset)

**Overview**: DiSCo is a large training set of 10,000 preference pairs of insecure and secure code, along with reasoning on the issues and fixes, aimed at improving secure code generation by teaching models to align towards security.

**Data Type**: code with security reasoning pairs

**Domains**:
- Computer Security

**Languages**:
- Python

**Similar Benchmarks**:
- Security Eval
- LLMSecEval
- CW-Eval

**Resources**:
- [GitHub Repository](https://github.com/StonyBrookNLP/disco-lpo)

## 🎯 Purpose and Intended Users

**Goal**: To improve secure code generation by providing a dataset of secure and insecure code examples along with security reasoning.

**Target Audience**:
- ML Researchers
- Security Analysts
- Model Developers

**Tasks**:
- Secure Code Generation
- Code Quality Improvement

**Limitations**: N/A

## 💾 Data

**Source**: Distilled from frontier LLMs using prompts augmented with security domain information.

**Size**: 10,000 examples

**Format**: N/A

**Annotation**: Generated with reasoning about security issues and fixes.

## 🔬 Methodology

**Methods**:
- Supervised Fine-tuning
- Preference Optimization

**Metrics**:
- Insecurity
- Issues per 100
- pass@1
- pass@5

**Calculation**: Metrics calculated using security analyzers and pass rates based on test cases.

**Interpretation**: Lower insecurity and issues per 100 indicate better secure coding practices; higher pass rates indicate better code utility.

**Baseline Results**: Models trained on DiSCo outperform baseline models significantly in both security and coding utility.

**Validation**: Empirical evaluations using standard security benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
