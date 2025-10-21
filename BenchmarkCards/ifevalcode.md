# IFEvalCode

## 📊 Benchmark Details

**Name**: IFEvalCode

**Overview**: IFEvalCode is a multilingual benchmark designed to evaluate both code correctness and code controllability in LLM-generated code, comprising 1.6K samples across 8 programming languages.

**Data Type**: code generation instructions

**Domains**:
- Computer Science

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- HumanEval
- BigCodeBench
- MBPP
- MultiPL-E

**Resources**:
- [Resource](https://ifevalcode.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capability of generating controlled code that adheres to human requirements and instructions across multiple programming languages.

**Target Audience**:
- ML Researchers
- Software Developers
- Academia

**Tasks**:
- Code Generation

**Limitations**: The current coverage of eight programming languages may not fully represent the diversity and specialized use cases in real-world software development.

## 💾 Data

**Source**: Constructed using human annotators and based on code-related documents and queries.

**Size**: 1,620 samples

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Correctness (Corr.)
- Instruction compliance (Instr.)

**Calculation**: Correctness is calculated by executing generated code against provided test cases, while instruction compliance is checked against specified requirements.

**Interpretation**: Results are interpreted based on the pass rates for correctness and adherence to instructional constraints.

**Baseline Results**: Results are tracked and compared across 40+ Language Models in terms of correctness and instruction compliance.

**Validation**: Extensive experimental results show performance across various models

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The benchmark includes multilingual evaluation across different programming languages and their effectiveness in meeting specific constraints.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
