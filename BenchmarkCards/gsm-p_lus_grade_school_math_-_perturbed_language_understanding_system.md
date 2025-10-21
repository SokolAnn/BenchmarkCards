# GSM-P LUS (Grade School Math - Perturbed Language Understanding System)

## 📊 Benchmark Details

**Name**: GSM-P LUS (Grade School Math - Perturbed Language Understanding System)

**Overview**: GSM-P LUS is an adversarial benchmark designed to evaluate the robustness of Large Language Models (LLMs) in mathematical problem-solving by testing a wide range of question variations and perturbations.

**Data Type**: open-formed question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- Theoremqa

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the robustness of LLMs in solving math word problems under various perturbations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Mathematical Problem Solving

**Limitations**: GSM-P LUS mainly focuses on the robustness of math reasoning at the elementary school level.

## 💾 Data

**Source**: Developed from the GSM8K dataset by introducing various perturbations.

**Size**: 10,552 question variations

**Format**: Open-formed question-answering pairs

**Annotation**: Human-annotated with a rigorous quality check process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Performance Drop Rate (PDR)
- Percentage of Accurately Solved Pairs (ASP)

**Calculation**: Performance metrics calculated based on model accuracy on both GSM8K and GSM-P LUS datasets.

**Interpretation**: Comparative analysis of performance across benchmarks to assess robustness.

**Baseline Results**: Human performance baseline established using qualified human annotators.

**Validation**: Cross-annotated by multiple evaluators to ensure data quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Fairness

**Atlas Risks**:
- **Robustness**: Data poisoning, Prompt injection attack
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
