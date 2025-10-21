# OPTIBENCH

## 📊 Benchmark Details

**Name**: OPTIBENCH

**Overview**: OPTIBENCH is a benchmark for end-to-end optimization problem-solving with human-readable inputs and outputs. It contains rich optimization problems, including linear and non-linear programming with or without tabular data, which can comprehensively evaluate LLMs’ solving ability.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NL4OPT
- ComplexOR
- NLP4LP

**Resources**:
- [Resource](https://arxiv.org/abs/2407.09887)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of OPTIBENCH is to evaluate the capability of large language models to solve optimization problems end-to-end.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Optimization Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from textbooks and university assignments, manually verified for quality.

**Size**: 605 examples

**Format**: JSON

**Annotation**: Manual annotation by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Performance is measured by the accuracy of the numerical answers produced by the models against ground truth values from the benchmarks.

**Interpretation**: Performance is evaluated based on how well models can solve optimization problems with various constraints and objective functions.

**Baseline Results**: GPT-4 achieved the highest accuracy, followed by Llama-3-8B-Instruct after fine-tuning with R ESOCRATIC-29K.

**Validation**: The benchmark includes 605 diverse optimization problems created and validated through rigorous selection and expert review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
