# HLS-Eval

## 📊 Benchmark Details

**Name**: HLS-Eval

**Overview**: HLS-Eval is the first comprehensive benchmark and evaluation framework for LLM-driven high-level synthesis (HLS) design tasks, focusing on generating HLS code from natural language descriptions and making HLS-specific code edits to existing HLS code.

**Data Type**: HLS design cases with natural language descriptions and testbenches

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- C2HLSC
- HLSPilot
- Gai et al.

**Resources**:
- [GitHub Repository](https://github.com/stefanpie/hls-eval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and modular benchmarking suite for evaluating LLMs in the context of HLS design tasks.

**Target Audience**:
- Research Community
- Hardware Designers
- Industry Practitioners

**Tasks**:
- Code Generation
- Code Editing

**Limitations**: N/A

## 💾 Data

**Source**: Community HLS benchmarks, academic textbooks, and open-source hardware accelerators

**Size**: 94 designs

**Format**: N/A

**Annotation**: Manually reviewed and structured from existing HLS designs

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human evaluation

**Metrics**:
- Parseability
- Compilability
- Runnability
- Synthesizability

**Calculation**: Metrics are calculated based on pass rates for generated HLS outcomes.

**Interpretation**: Higher pass rates indicate better performance and compatibility of the LLM-generated HLS code.

**Baseline Results**: Evaluated results for multiple open-source LLMs, indicating pass rates for different metrics.

**Validation**: Evaluations conducted using AMD/Xilinx Vitis HLS 2024.1.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
