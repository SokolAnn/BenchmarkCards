# RTLCoder

## 📊 Benchmark Details

**Name**: RTLCoder

**Overview**: RTLCoder is an open-source large language model (LLM) solution designed for generating RTL code (Verilog) from natural language instructions. It outperforms GPT-3.5 in all representative benchmarks for RTL code generation and addresses the challenge of data availability in IC design tasks through a new automated dataset generation flow.

**Data Type**: instruction-code pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VerilogEval
- RTLLM

**Resources**:
- [GitHub Repository](https://github.com/hkust-zhiyao/RTL-Coder)

## 🎯 Purpose and Intended Users

**Goal**: To provide an open-source LLM solution for RTL code generation that outperforms existing commercial models while ensuring data privacy and accessibility.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Automatically generated based on natural language instructions and RTL design keywords.

**Size**: 27,000 samples

**Format**: N/A

**Annotation**: Automatically filtered and organized from raw outputs using a syntax checker.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- pass @k metric
- pass @5 metric

**Calculation**: Metrics are calculated based on how many designs pass the syntax checks and functionality tests using multiple trials.

**Interpretation**: Models are evaluated based on their success rates in generating valid and functional RTL code as compared to benchmarks.

**Baseline Results**: RTLCoder surpasses GPT-3.5 and shows competitive results against GPT-4 on RTL generation tasks.

**Validation**: Ensured through comparison with established RTL generation benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Privacy
- Model robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Explicit measures are taken to ensure the data privacy of user submissions by using an open-source solution.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
