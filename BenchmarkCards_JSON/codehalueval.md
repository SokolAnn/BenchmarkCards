# CodeHaluEval

## 📊 Benchmark Details

**Name**: CodeHaluEval

**Overview**: The CodeHaluEval benchmark is designed to systematically evaluate code hallucinations in large language models (LLMs), categorizing hallucinations into four main types and using a dynamic detection algorithm called CodeHalu.

**Data Type**: Code samples

**Domains**:
- Programming

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- APPS
- CodeScope
- MMCode
- SWE-bench

**Resources**:
- [GitHub Repository](https://github.com/yuchen814/CodeHalu)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and understand code hallucinations in large language models to improve their code generation capabilities.

**Target Audience**:
- Researchers
- Developers

**Tasks**:
- Evaluating LLMs for code generation
- Identifying code hallucinations

**Limitations**: Focus is primarily on Python programming language.

**Out of Scope Uses**:
- Other programming languages

## 💾 Data

**Source**: CodeHaluEval benchmark dataset

**Size**: 8,883 samples from 699 tasks

**Format**: Structured code samples

**Annotation**: Code hallucinations categorized into four types.

## 🔬 Methodology

**Methods**:
- Dynamic detection algorithm (CodeHalu)
- Execution verification

**Metrics**:
- Hallucination Rate (HR)

**Calculation**: HR = 1/N * Σ S(i, K) where S(i, K) indicates if the i-th sample is a hallucination.

**Interpretation**: Lower HR indicates less frequent hallucinations in generated code.

**Baseline Results**: Results vary by model, with rates between 20% to 60% across evaluated models.

**Validation**: Experimental validation through execution tests of generated code.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
