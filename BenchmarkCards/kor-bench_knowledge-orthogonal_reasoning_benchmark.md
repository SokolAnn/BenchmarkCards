# KOR-Bench (Knowledge-Orthogonal Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: KOR-Bench (Knowledge-Orthogonal Reasoning Benchmark)

**Overview**: KOR-Bench is designed to evaluate models’ reasoning abilities across five task categories: Operation, Logic, Cipher, Puzzle, and Counterfactual, while minimizing reliance on domain-specific knowledge.

**Data Type**: rule-driven question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- MMLU-Pro
- GSM8K
- MATH

**Resources**:
- [Resource](https://kor-bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To establish a comprehensive benchmark that evaluates reasoning capabilities while reducing dependency on pre-existing knowledge.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Operation Reasoning
- Logic Reasoning
- Cipher Reasoning
- Puzzle Reasoning
- Counterfactual Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using manual annotation and extensive logical reasoning tasks.

**Size**: 1,250 questions

**Format**: JSON

**Annotation**: Manual annotation by experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Error Rate

**Calculation**: Metrics are calculated based on the correctness of the model's output compared to the expected answers derived from the rules.

**Interpretation**: A higher accuracy score indicates better reasoning capabilities of the model without reliance on specific training data.

**Baseline Results**: O1-Preview and O1-Mini models achieved accuracies of 72.88% and 70.16%, respectively.

**Validation**: The benchmark validation has been conducted through rigorous evaluations across multiple models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: N/A - licensing details are to be specified upon full dataset release.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
