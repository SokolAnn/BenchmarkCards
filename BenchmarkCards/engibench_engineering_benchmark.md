# EngiBench (Engineering Benchmark)

## 📊 Benchmark Details

**Name**: EngiBench (Engineering Benchmark)

**Overview**: EngiBench is a hierarchical benchmark designed to evaluate large language models on solving engineering problems, spanning three levels of increasing difficulty and covering diverse engineering subfields.

**Data Type**: engineering problem-solving tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- Omni-MATH

**Resources**:
- [GitHub Repository](https://github.com/EngiBench/EngiBench)
- [Resource](https://huggingface.co/datasets/EngiBench/EngiBench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate large language models on real-world engineering problem-solving capabilities.

**Target Audience**:
- ML Researchers
- Engineering Practitioners
- Model Developers

**Tasks**:
- Engineering Problem Solving
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Problems were sourced from existing public benchmarks, educational materials, and modeling competitions.

**Size**: 1,000 engineering problems

**Format**: JSON

**Annotation**: Annotated by a mix of PhD students and engineering professionals with assistance from LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Rubric-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on comparisons to ground truth answers and expert rubrics.

**Interpretation**: Higher scores reflect better performance in reasoning and problem-solving capabilities.

**Baseline Results**: Human experts achieved an average score of 8.58 on open-ended tasks.

**Validation**: Inter-annotator agreement ensured the consistency of evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-NC-4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
