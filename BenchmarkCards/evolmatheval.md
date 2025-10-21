# EvolMathEval

## 📊 Benchmark Details

**Name**: EvolMathEval

**Overview**: EvolMathEval is an automated mathematical benchmark generation and evolution framework based on evolutionary testing, designed to dynamically generate unique evaluation instances and eliminate data contamination, ensuring that the benchmark remains challenging for future models.

**Data Type**: mathematical problem instances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH

**Resources**:
- [GitHub Repository](https://github.com/SYSUSELab/EvolMathEval)

## 🎯 Purpose and Intended Users

**Goal**: To dynamically generate and evolve benchmarks for mathematical reasoning to address issues of score saturation and data contamination.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Self-constructed dataset generated via the EvolMathEval framework.

**Size**: 300 problems (EvolMath-300); 1,000 problems (EvolMath-1000)

**Format**: N/A

**Annotation**: Automatically generated via evolutionary techniques.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Run experiments to evaluate model performance

**Metrics**:
- Accuracy

**Calculation**: The fitness function quantifies the difficulty of problems dynamically through a composite score based on multiple dimensions.

**Interpretation**: A lower accuracy on the evolved problems indicates higher challenge and effectiveness of the benchmark.

**Validation**: The framework iteratively enhances problems ensuring they remain challenging for LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark may inadvertently favor certain solving strategies, impacting fairness.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
