# Collu-Bench

## 📊 Benchmark Details

**Name**: Collu-Bench

**Overview**: A benchmark for predicting code hallucinations of LLMs across code generation (CG) and automated program repair (APR) tasks.

**Data Type**: Code hallucination instances

**Domains**:
- Code Generation
- Automated Program Repair

**Similar Benchmarks**:
- TruthfulQA
- FELM
- HaluEval
- HalluCode
- CodeHalu

**Resources**:
- [Resource](https://huggingface.co/datasets/lt-asset/collu-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and analyze code hallucinations in LLMs.

**Target Audience**:
- Researchers
- Improvement of LLMs' trustworthiness
- Developers in software engineering

**Tasks**:
- Code generation
- Automated program repair
- Hallucination localization and prediction

**Limitations**: The errors in the target hallucination token index due to automated pipeline challenges.

## 💾 Data

**Source**: Five datasets: MBPP, HumanEval, HumanEval-Java, Defects4J, SWE-bench

**Size**: 13,234 code hallucination instances

**Format**: N/A

**Annotation**: Includes features such as per-step log probabilities, token types, and execution feedback

## 🔬 Methodology

**Methods**:
- Traditional machine learning (e.g., random forest)
- Neural networks (e.g., LSTM)

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on hallucination localization predictions

**Interpretation**: Results highlight the complex nature of predicting hallucinations with achieved accuracies ranging from 22.03% to 33.15%.

**Baseline Results**: N/A

**Validation**: Evaluated through cross-validation with multiple setups (All-in-one, One-per-dataset, One-per-LLM).

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination risk in generated code
- Potential security vulnerabilities

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Potential Harm**: Incorrect and vulnerable code leading to significant financial loss.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
