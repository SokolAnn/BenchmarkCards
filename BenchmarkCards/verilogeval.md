# VerilogEval

## 📊 Benchmark Details

**Name**: VerilogEval

**Overview**: VerilogEval is a benchmarking framework tailored specifically for evaluating large language models (LLMs) performance in the context of Verilog code generation for hardware design and verification, consisting of 156 problems sourced from HDLBits.

**Data Type**: Verilog coding tasks

**Domains**:
- Computer Science
- Hardware Design

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- APPS

**Resources**:
- [GitHub Repository](https://github.com/NVlabs/verilog-eval)
- [Resource](https://hdlbits.01xz.net/wiki/Problem sets)

## 🎯 Purpose and Intended Users

**Goal**: To create a robust evaluation framework for Verilog code generation and assessment using large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation
- Functionality Testing

**Limitations**: Current evaluations are confined to boilerplate code generation for relatively small-scale designs.

## 💾 Data

**Source**: HDLBits, an instructional website for Verilog code challenges.

**Size**: 156 problems

**Format**: N/A

**Annotation**: Manual review and automated generation for problem descriptions.

## 🔬 Methodology

**Methods**:
- Automated functional correctness testing
- Supervised fine-tuning

**Metrics**:
- pass@k

**Calculation**: A problem is considered solved if any of the k samples pass the unit tests.

**Interpretation**: Higher pass rates indicate better model performance in generating correct Verilog code.

**Baseline Results**: Results show performance improved with supervised fine-tuning.

**Validation**: Validated through extensive testing against known solution outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
