# MathOlympiadEval

## 📊 Benchmark Details

**Name**: MathOlympiadEval

**Overview**: MathOlympiadEval is a diverse dataset of challenging mathematical problems sourced from CMO, IMO, and OpenMathReasoning. Each problem is annotated by human experts for reasoning correctness, revealing a significant gap between answer correctness and the soundness of reasoning processes for large language models.

**Data Type**: mathematical problems with reasoning correctness annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- OpenMathReasoning

**Resources**:
- [Resource](https://arxiv.org/abs/2506.06877)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate a nuanced evaluation of mathematical reasoning in Large Language Models (LLMs) and uncover instances of 'correct answers via flawed reasoning.'

**Target Audience**:
- ML Researchers
- Model Developers
- AI Ethics Researchers

**Tasks**:
- Mathematical Reasoning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: 204 mathematical problems sourced from the China Mathematical Olympiad, the International Mathematical Olympiad, and NVIDIA’s OpenMathReasoning dataset.

**Size**: 204 problems

**Format**: N/A

**Annotation**: Annotated for reasoning correctness by mathematics graduate students.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated reasoning correctness assessment

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics for correctness are calculated by determining the proportion of correct answers versus flawed reasoning paths.

**Interpretation**: A higher F1 Score indicates better performance of the model in accurately identifying reasoning flaws.

**Baseline Results**: N/A

**Validation**: Initial evaluation metrics are validated against human assessed correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
