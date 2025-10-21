# CodeFlowBench

## 📊 Benchmark Details

**Name**: CodeFlowBench

**Overview**: CodeFlowBench is the first benchmark designed to comprehensively evaluate LLMs’ ability to perform codeflow – implementing new functionality by reusing existing functions over multiple turns. It comprises 5,258 problems from Codeforces and features a dual assessment protocol and structural metrics.

**Data Type**: programming problems with unit tests

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- DevBench
- SWE-Bench

**Resources**:
- [Resource](https://codeforces.com/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multi-turn, iterative code generation capabilities for codeflow settings in LLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Codeforces problem archive.

**Size**: 5,258 problems

**Format**: N/A

**Annotation**: Automatically verified through an automated pipeline.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Pass@1
- Average Pass Depth (APD)
- Pass Turn (PT)

**Calculation**: Metrics are calculated based on the success of code generation at specific turns and their depth complexity.

**Interpretation**: Higher values in metrics indicate better performance in multi-turn scenarios.

**Baseline Results**: Closed-source models and various configurations of open-source models were tested.

**Validation**: Extensive experiments were carried out on 1,000 selected problems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
