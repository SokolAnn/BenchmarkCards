# EngiBench

## 📊 Benchmark Details

**Name**: EngiBench

**Overview**: EngiBench is a hierarchical benchmark designed to evaluate large language models (LLMs) on solving engineering problems, spanning three levels of increasing difficulty and covering diverse engineering subfields. It facilitates fine-grained analysis of model performance through controlled problem variants.

**Data Type**: engineering problem-solving tasks

**Domains**:
- Engineering

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- Omni-MATH

**Resources**:
- [GitHub Repository](https://github.com/EngiBench/EngiBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of EngiBench is to systematically evaluate LLMs on real-world engineering problems across different levels of complexity.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Engineering Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Data sourced from existing public benchmarks, university educational materials, and modeling competitions.

**Size**: 1740 problems across three levels and multiple variants.

**Format**: JSON

**Annotation**: Annotated by PhD students and engineering professionals with expert review.

## 🔬 Methodology

**Methods**:
- Binary scoring for closed-form problems
- Rubric-based evaluation for open-ended tasks

**Metrics**:
- Accuracy
- Score on a 10-point rubric

**Calculation**: Performance is calculated as accuracy for Levels 1 and 2, using binary comparison against reference answers.

**Interpretation**: Model performance is interpreted based on accuracy and adherence to rubric criteria for open-ended tasks.

**Validation**: Experimentally validated through scoring against human expert performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
