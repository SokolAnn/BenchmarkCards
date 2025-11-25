# OpenLLM-RTL: Open Dataset and Benchmark for LLM-Aided Design RTL Generation

## 📊 Benchmark Details

**Name**: OpenLLM-RTL: Open Dataset and Benchmark for LLM-Aided Design RTL Generation

**Overview**: This paper presents open-source benchmarks and datasets for developing LLMs to assist in design RTL generation and verification. It includes RTLLM 2.0 for evaluating RTL generation, AssertEval for assertion generation verification, and RTLCoder-Data, a dataset for training LLMs with 80K and 7K verified samples.

**Data Type**: RTL code generation samples and assertion generation samples

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- RTLLM
- VerilogEval

**Resources**:
- [GitHub Repository](https://github.com/hkust-zhiyao/RTLLM)
- [GitHub Repository](https://github.com/hkust-zhiyao/AssertLLM)
- [GitHub Repository](https://github.com/hkust-zhiyao/RTL-Coder)

## 🎯 Purpose and Intended Users

**Goal**: To provide benchmarks and datasets for LLMs in RTL code generation and verification.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- RTL Code Generation
- Assertion Generation

**Limitations**: N/A

## 💾 Data

**Source**: Various open-source circuit designs and specifications.

**Size**: 80,000 samples for RTLCoder-Data, 7,000 verified samples.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation based on performance benchmarks
- Formal Property Verification (FPV)

**Metrics**:
- pass@1
- syntax correctness
- functionality correctness

**Calculation**: Metrics are calculated by comparing generated RTL to expected outputs across several trials.

**Interpretation**: Higher pass rates indicate better model performance in generating correct RTL code.

**Baseline Results**: N/A

**Validation**: Extensive validations included for generated and verified samples using formal verification methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
