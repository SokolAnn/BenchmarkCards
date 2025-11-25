# L0-Bench

## 📊 Benchmark Details

**Name**: L0-Bench

**Overview**: L0-Bench is a synthetic benchmark for evaluating procedural correctness in neural language models via program execution, grading models on their ability to generate step-by-step execution traces from given synthetic Python functions.

**Data Type**: program execution traces

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/SimengSun/L0-reasoning-bench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the procedural correctness of language models in generating accurate execution traces for synthetic Python functions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Program Execution

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation using generative grammar to construct simplified Python programs.

**Size**: 2,000 examples (500 examples per trace length category: short, medium, long, extra long)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Whole-trace accuracy
- Steps to the first error

**Calculation**: Model outputs are aligned with the expected execution traces and evaluated based on exact matches and the number of steps before the first error occurs.

**Interpretation**: High accuracy indicates better procedural correctness and ability to execute rules step-by-step without deviation.

**Baseline Results**: Results from evaluating 20 recent models reveal varying levels of procedural correctness, with larger and reasoning-enhanced models generally performing better.

**Validation**: The benchmark was validated through systematic evaluation of multiple models across different configurations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
