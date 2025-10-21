# VERT (Verilog Assertion Dataset)

## 📊 Benchmark Details

**Name**: VERT (Verilog Assertion Dataset)

**Overview**: VERT is an open-source dataset specifically designed for SystemVerilog assertion generation to enhance the capabilities of Large Language Models (LLMs) in hardware verification.

**Data Type**: Verilog code snippets paired with SystemVerilog assertions

**Domains**:
- Computer Vision
- Hardware

**Languages**:
- English

**Similar Benchmarks**:
- MG-Verilog
- RTL-Repo
- OpenLLM-RTL
- VerilogEval
- Vul-FSM

**Resources**:
- [GitHub Repository](https://github.com/AnandMenon12/VERT)

## 🎯 Purpose and Intended Users

**Goal**: To automate the generation of SystemVerilog assertions, enabling more efficient and scalable hardware verification using LLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Assertion Generation
- Formal Verification

**Limitations**: N/A

## 💾 Data

**Source**: Synthesized from open-source HDL repositories and systematic variable augmentation.

**Size**: 20,000 samples

**Format**: Synthetic Verilog code and SystemVerilog assertions

**Annotation**: Automatically generated assertions based on defined rules and conditions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Syntactic correctness
- Functional correctness
- Complete Path Coverage (CPC)

**Calculation**: Metrics are calculated based on the verification of assertions against functional specifications.

**Interpretation**: Syntactic correctness checks adherence to HDL standards while functional correctness evaluates if assertions accurately reflect hardware behavior.

**Baseline Results**: Performance metrics compared against GPT-4o and base models of LLMs.

**Validation**: Combination of mutation testing, formal verification, and simulation-based analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures implemented through local fine-tuning of models to safeguard sensitive data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
