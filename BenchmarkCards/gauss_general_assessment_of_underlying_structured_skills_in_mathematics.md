# GAUSS (General Assessment of Underlying Structured Skills in Mathematics)

## 📊 Benchmark Details

**Name**: GAUSS (General Assessment of Underlying Structured Skills in Mathematics)

**Overview**: GAUSS evaluates LLMs’ mathematical abilities across twelve core skill dimensions, organized around knowledge, problem solving, and creativity, providing detailed insights into model performance.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FrontierMath

**Resources**:
- [Resource](https://arxiv.org/abs/2509.18122)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured and interpretable benchmark for evaluating the mathematical skills of large language models (LLMs).

**Target Audience**:
- ML Researchers
- Education Practitioners
- Domain Experts

**Tasks**:
- Mathematical Problem Solving
- Skill Assessment

**Limitations**: Limited scope of problems and potential biases in task selection.

## 💾 Data

**Source**: Specifically derived mathematical problems and assessment tasks designed for evaluating LLMs.

**Size**: 10,000 examples

**Format**: CSV

**Annotation**: Manual annotation by experts for the required skill scoring.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Skill Score

**Calculation**: Metrics are calculated based on the detailed performance of LLMs across various mathematical tasks as outlined in the tasks.

**Interpretation**: Results are interpreted in terms of strength and weakness profiles for model capabilities in mathematics.

**Baseline Results**: Results are benchmarked against existing models like GPT-5.

**Validation**: Validation procedures are based on assessing model performance against human-level benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: Evenly distributed coverage across samples to avoid demographic bias.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0 license used for distribution of the benchmark and materials.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
