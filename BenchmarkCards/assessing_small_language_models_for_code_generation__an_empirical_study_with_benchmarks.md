# Assessing Small Language Models for Code Generation: An Empirical Study with Benchmarks

## 📊 Benchmark Details

**Name**: Assessing Small Language Models for Code Generation: An Empirical Study with Benchmarks

**Overview**: This study presents a comprehensive empirical evaluation of 20 open-source small language models (SLMs) on five diverse code-related benchmarks (HumanEval, MBPP, Mercury, HumanEvalPack, and CodeXGLUE), assessing their capabilities, limitations, and performance trade-offs in code generation tasks.

**Data Type**: code generation tasks

**Domains**:
- Software Engineering

**Languages**:
- Python
- Java
- JavaScript
- PHP
- Ruby
- Go
- C++

**Similar Benchmarks**:
- HumanEval
- MBPP
- Mercury
- HumanEvalPack
- CodeXGLUE

**Resources**:
- [GitHub Repository](https://github.com/bigcode-project/bigcode-evaluation-harness)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the performance of small language models on code generation tasks across established benchmarks.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Code Generation
- Code Synthesis
- Code Summarization
- Code Repair

**Limitations**: N/A

## 💾 Data

**Source**: Benchmarks were derived from empirical tests on open-source small language models.

**Size**: 20 models evaluated

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Zero-shot prompting
- Automated metrics such as pass@k

**Metrics**:
- pass@k
- BLEU Score
- VRAM usage
- Inference time

**Calculation**: Functional correctness measured using pass@k metric; efficiency measured through VRAM usage and inference time.

**Interpretation**: Higher pass@k values indicate better model performance in generating functionally correct code.

**Baseline Results**: Comparison against results from prior benchmarks like HumanEval, MBPP, and Mercury.

**Validation**: Controlled experimental setup with two distinct hardware configurations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
