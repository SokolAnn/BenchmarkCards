# ReasoningTrap

## 📊 Benchmark Details

**Name**: ReasoningTrap

**Overview**: ReasoningTrap is a diagnostic dataset designed to assess the reasoning rigidity of language models by evaluating their ability to adhere to explicit instructions in modified mathematical problems and puzzles. It includes specially curated versions of existing benchmarks modified to investigate models' responses to explicit constraints.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- AIME
- MATH500

**Resources**:
- [Resource](https://arxiv.org/abs/2505.17225)

## 🎯 Purpose and Intended Users

**Goal**: To analyze the behavior of reasoning models under explicit instructions and to facilitate research on mitigating reasoning rigidity.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning
- Logic Puzzle Solving

**Limitations**: N/A

## 💾 Data

**Source**: Curated mathematical problems and puzzles adapted from AIME and MATH500 datasets.

**Size**: 164 questions

**Format**: JSON

**Annotation**: Manually verified by experts based on mathematical validity, logical consistency, and divergence of modified problems from original solutions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- p-pass@1
- pass@1
- contamination ratio

**Calculation**: The p-pass@1 score is determined by evaluating whether the model's outputs align with the conditions stated in the modified questions.

**Interpretation**: A high p-pass@1 score indicates that the model adheres to user instructions without defaulting to familiar reasoning patterns.

**Baseline Results**: N/A

**Validation**: Each question was verified by human annotators for compliance with validation criteria.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
