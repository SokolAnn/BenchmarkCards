# RealBench

## 📊 Benchmark Details

**Name**: RealBench

**Overview**: RealBench is the first benchmark aimed at real-world IP-level Verilog generation tasks, featuring complex, structured designs from open-source IPs, multi-modal and formatted design specifications, and rigorous verification environments.

**Data Type**: Verilog design specifications and Verilog code

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- RTLLMV1.1
- RTLLMV2
- VerilogEval
- ChipGPTV

**Resources**:
- [GitHub Repository](https://github.com/IPRC-DIP/RealBench)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark LLMs’ Verilog generation capability in real-world design workflows and facilitate advancements in hardware design automation.

**Target Audience**:
- ML Researchers
- Hardware Designers
- Model Developers

**Tasks**:
- Verilog Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Real-world open-source IP designs including AES encoder/decoder cores and an SD card controller.

**Size**: N/A

**Format**: Structured format with detailed specifications

**Annotation**: Manually written specifications ensuring completeness and clarity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Formal verification
- Testbench verification

**Metrics**:
- Formal correctness
- Function correctness
- Syntax correctness

**Calculation**: Metrics like func@1 and formal@1 are used to evaluate the correctness of generated Verilog code.

**Interpretation**: Pass rates indicate the correctness of generated modules, with higher rates reflecting successful generation.

**Baseline Results**: N/A

**Validation**: Validation through rigorous testbench and formal verification processes to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
