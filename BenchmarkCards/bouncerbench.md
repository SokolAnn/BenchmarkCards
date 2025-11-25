# BouncerBench

## 📊 Benchmark Details

**Name**: BouncerBench

**Overview**: BouncerBench is a benchmark that evaluates whether LLM-based software agents can refuse to act when inputs are ill-defined or when their own outputs are likely to be incorrect.

**Data Type**: text

**Domains**:
- Software Engineering

**Languages**:
- English

**Resources**:
- [Resource](https://bouncerbench.com)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of BouncerBench is to evaluate the capability of LLM-based agents to abstain from acting on underspecified inputs or incorrect outputs while promoting research in improving their reliability.

**Target Audience**:
- ML Researchers
- Software Engineers
- AI Developers

**Tasks**:
- Input Bouncing
- Output Bouncing

**Limitations**: N/A

## 💾 Data

**Source**: SWE-Bench Verified dataset, human-annotated for vagueness and correctness.

**Size**: 46,238 LLM-generated patches evaluated across 1,699 input tasks and 642 output tasks.

**Format**: N/A

**Annotation**: Annotated by 93 software developers experienced in Python.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro-averaged F-Measure
- I-Score
- O-Score

**Calculation**: Metrics are calculated based on binary classifications of actions as bounce or process, with adjustments for ambiguity and correctness.

**Interpretation**: Higher scores indicate better performance in correctly identifying when to abstain or reject incorrect outputs.

**Baseline Results**: O4-mini achieved a macro-F measure of 0.592 for input bouncing; Codex achieved a macro-F measure of 0.690 for output bouncing.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
