# DafnyComp

## 📊 Benchmark Details

**Name**: DafnyComp

**Overview**: DafnyComp is a benchmark of compositional formal programs with auto-formalized specifications for specification reasoning.

**Data Type**: synthetic Dafny programs with specifications

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- DafnyBench

**Resources**:
- [GitHub Repository](https://github.com/Veri-Code/ReForm)
- [Resource](https://huggingface.co/Veri-Code)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the compositional reasoning ability of formal language coding and improve the verification of generated Dafny specifications.

**Target Audience**:
- ML Researchers
- Software Engineers
- Formal Verification Practitioners

**Tasks**:
- Formal Verification
- Specification Generation

**Limitations**: N/A

## 💾 Data

**Source**: Automatic generation of formal specifications from Python functions and existing Dafny data.

**Size**: 20,000 Dafny programs

**Format**: Dafny code with specifications

**Annotation**: Automatically annotated using models without human intervention.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Supervised Fine-Tuning

**Metrics**:
- Validation Rate
- Verification Rate
- Specification Superiority Rate

**Calculation**: Metrics are defined based on the proportion of correct specifications and verification success.

**Interpretation**: Higher rates indicate better performance in generating valid and useful specifications.

**Baseline Results**: SFT models exceeded baseline metrics, significantly outperforming proprietary models like GPT-4.

**Validation**: Regular automation checks through a verification pipeline using Dafny.

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
