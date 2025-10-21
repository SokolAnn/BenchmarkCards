# ManyIFEval (Many Instruction-Following Eval) and StyleMBPP (Style-aware Mostly Basic Programming Problems)

## 📊 Benchmark Details

**Name**: ManyIFEval (Many Instruction-Following Eval) and StyleMBPP (Style-aware Mostly Basic Programming Problems)

**Overview**: This paper introduces two specialized benchmarks designed to evaluate the capability of large language models (LLMs) to follow multiple instructions simultaneously, specifically in text generation and code generation tasks.

**Data Type**: text and code generation tasks with multiple instructions

**Domains**:
- Natural Language Processing
- Computer Programming

**Languages**:
- English

**Similar Benchmarks**:
- IFEval
- MBPP
- ComplexBench

**Resources**:
- [GitHub Repository](https://github.com/kenoharada/Multiple-Instructions-Following)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate multiple instructions-following capabilities of LLMs and understand how performance degrades as instruction counts increase.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Text Generation
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: The ManyIFEval and StyleMBPP benchmarks are constructed using task descriptions and instructions curated from existing datasets.

**Size**: 2,160 samples for ManyIFEval and 3,000 samples for StyleMBPP

**Format**: N/A

**Annotation**: Rule-based verification for instruction adherence

## 🔬 Methodology

**Methods**:
- Logistic Regression
- Beta-Binomial Modeling
- Naive Estimators

**Metrics**:
- Prompt-level Accuracy
- Instruction-level Accuracy

**Calculation**: Prompt-level Accuracy measures the rate of satisfying all provided instructions; Instruction-level Accuracy assesses success on individual instructions.

**Interpretation**: Performance degrades as the number of instructions increases across models, indicating complexity in satisfying multiple instructions.

**Baseline Results**: N/A

**Validation**: Benchmarks tested across various state-of-the-art LLMs

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0 International

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
