# PRMB ENCH

## 📊 Benchmark Details

**Name**: PRMB ENCH

**Overview**: PRMB ENCH is a process-level benchmark specifically designed to assess the fine-grained error detection capabilities of process-level reward models (PRMs). It includes 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- Olympiad Bench
- MMLU

**Resources**:
- [Resource](https://prmbench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of PRMB ENCH is to evaluate the nuanced capabilities of process-level reward models in detecting various error types during the reasoning process.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Error Detection
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Carefully curated using metadata from existing datasets and human filtering.

**Size**: 6,216 instances

**Format**: N/A

**Annotation**: Annotated by professional annotators and filtered for quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- PRMScore
- Negative F1 Score
- Accuracy

**Calculation**: Calculated based on the performance across various tasks assessing error detection in models.

**Interpretation**: Higher scores indicate better performance in detecting errors and reliability in outcomes.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through extensive experiments and performance evaluation of 25 models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
