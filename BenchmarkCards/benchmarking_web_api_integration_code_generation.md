# Benchmarking Web API Integration Code Generation

## 📊 Benchmark Details

**Name**: Benchmarking Web API Integration Code Generation

**Overview**: This paper presents a dataset and evaluation pipeline designed to assess the ability of large language models (LLMs) to generate web API invocation code. The study reveals that generating API invocations poses significant challenges, resulting in frequent errors.

**Data Type**: API invocation tasks and expected outcomes

**Domains**:
- Software Engineering

**Languages**:
- JavaScript

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://zenodo.org/doi/10.5281/zenodo.13758414)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models in generating web API invocation code.

**Target Audience**:
- Researchers in AI and Software Engineering
- Developers using APIs

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated using an LLM and manually reviewed for correctness.

**Size**: 395 samples

**Format**: JSON

**Annotation**: Manually checked and corrected

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human review

**Metrics**:
- Correct implementations
- Illegal implementations
- Correct URLs
- Illegal URLs
- Correct methods
- Illegal methods
- Mean argument precision
- Mean argument recall
- Mean argument value conditional accuracy

**Calculation**: Metrics are calculated based on functional correctness by executing the generated API invocation code and comparing the results.

**Interpretation**: Higher scores in metrics indicate better performance in generating valid and compliant API invocations.

**Baseline Results**: N/A

**Validation**: The generated code was executed in a controlled environment for correctness evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
