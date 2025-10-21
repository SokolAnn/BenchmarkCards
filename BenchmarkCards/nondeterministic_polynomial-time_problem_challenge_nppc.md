# Nondeterministic Polynomial-time Problem Challenge (NPPC)

## 📊 Benchmark Details

**Name**: Nondeterministic Polynomial-time Problem Challenge (NPPC)

**Overview**: NPPC is an ever-scaling reasoning benchmark for LLMs that includes unified interfaces for generating instances of NP-complete problems, evaluating these problems against LLMs, and analyzing LLM performance. It aims to be uncrushable, unhackable, and auto-verifiable.

**Data Type**: problem instances and solutions

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MMLU
- SWE-bench
- ARC-AGI

**Resources**:
- [GitHub Repository](https://github.com/SMU-DIGA/nppc)

## 🎯 Purpose and Intended Users

**Goal**: To provide an ever-scaling reasoning benchmark for evaluating the capabilities of large language models (LLMs) and to serve as a testbed for progress toward artificial general intelligence (AGI).

**Target Audience**:
- AI Researchers
- ML Engineers
- Model Developers

**Tasks**:
- Reasoning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Generated instances of NP-complete problems.

**Size**: Infinite number of instances

**Format**: Custom problem and solution representation

**Annotation**: Automatically generated with verification protocols.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Mean
- Interquartile Mean (IQM)
- Median
- Optimality Gap

**Calculation**: Performance metrics aggregated over multiple instances and difficulty levels, using statistical methods.

**Interpretation**: Higher scores indicate better reasoning capability of LLMs under the benchmark conditions.

**Baseline Results**: N/A

**Validation**: Statistical validation using stratified bootstrap confidence intervals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
