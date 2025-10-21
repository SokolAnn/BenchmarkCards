# Systolic Array-based Accelerator Data Set (SA-DS)

## 📊 Benchmark Details

**Name**: Systolic Array-based Accelerator Data Set (SA-DS)

**Overview**: SA-DS is the first dataset of systolic array accelerators tailored for LLM-based DNN hardware accelerator design. It includes natural language descriptions of the accelerator’s micro-architecture and a Chisel description, enabling effective learning and generation of optimized designs by LLMs.

**Data Type**: design-description pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ACADLab/SA-DS)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate effective learning and generation of optimized designs by LLMs for hardware accelerator design.

**Target Audience**:
- ML Researchers
- Hardware Designers

**Tasks**:
- Hardware Design Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated using the Gemmini generator.

**Size**: 1536 data points

**Format**: N/A

**Annotation**: Automatically generated with natural language descriptions.

## 🔬 Methodology

**Methods**:
- Manual evaluation
- Automated metrics

**Metrics**:
- Pass/Fail rates

**Calculation**: Pass rates calculated based on the quality of the code generated from prompts.

**Interpretation**: Higher pass rates indicate better alignment of dataset examples with LLM capabilities.

**Validation**: Evaluation conducted through manual code review by experts and using Verilator for automated verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
