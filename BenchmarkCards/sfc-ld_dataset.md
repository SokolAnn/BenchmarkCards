# SFC-LD Dataset

## 📊 Benchmark Details

**Name**: SFC-LD Dataset

**Overview**: The SFC-LD Dataset consists of paired textual representations of Sequential Function Charts (SFC) and Ladder Diagrams (LD) programs that conform to the IEC 61131-3 standard. It aims to facilitate the automation of LD-SFC conversion using Large Language Models (LLMs) by providing a rich data source for training and evaluation.

**Data Type**: text

**Domains**:
- Industrial Automation

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/yimin-up/Converting IEC 61131 LDinto SFC Using LLM Dataset and Testing.git)

## 🎯 Purpose and Intended Users

**Goal**: To create datasets for training Large Language Models to automate the conversion of Ladder Diagrams to Sequential Function Charts in the context of industrial automation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Generation

**Limitations**: The dataset is synthetic and may not fully capture the complexity of real-world industrial PLC programs.

## 💾 Data

**Source**: Synthetic generation from structured representations of SFC and LD.

**Size**: 320 examples

**Format**: CSV

**Annotation**: Automatically generated pairs based on designed structural rules.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Fine-tuning LLMs

**Metrics**:
- Syntax check pass rate
- Structural check pass rate
- Joint pass rate

**Calculation**: Metrics are calculated based on the proportion of generated SFCs passing syntax and structural checks.

**Interpretation**: Higher rates indicate better performance of the LLMs in converting LD to SFC.

**Validation**: Validation is performed through structural comparison and syntax checks during compilation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Robustness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
