# ALMANACS (Anticipating Language Model Answers in Non-objective And Complex Scenarios)

## 📊 Benchmark Details

**Name**: ALMANACS (Anticipating Language Model Answers in Non-objective And Complex Scenarios)

**Overview**: ALMANACS is a language model explainability benchmark that evaluates explainability methods on simulatability, i.e., how well the explanations improve behavior prediction on new inputs across twelve safety-relevant topics.

**Data Type**: Yes/No questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/edmundmills/ALMANACS)

## 🎯 Purpose and Intended Users

**Goal**: To provide a fully automated benchmark for evaluating the efficacy of language model explainability methods by measuring their simulatability.

**Target Audience**:
- ML Researchers
- Interpretability Researchers

**Tasks**:
- Behavior Prediction

**Limitations**: While ALMANACS is an automated benchmarking tool, it is not a perfect substitute for human evaluations.

## 💾 Data

**Source**: Generative templates created with GPT-4 for various safety-relevant topics.

**Size**: 180,000 train examples and 18,000 test examples

**Format**: Structured text prompts

**Annotation**: Automated with GPT-4

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Kullback-Leibler Divergence (KLD IV)
- Total Variation Distance (TVD IST)
- Spearman Correlation

**Calculation**: Metrics are calculated based on the predicted probabilities of model decisions versus ground truth.

**Interpretation**: Lower values on KLD IV indicate better simulatability.

**Baseline Results**: Baseline evaluation results show no explanation methods consistently improve predictions over the no-explanation control.

**Validation**: ALMANACS scenarios are designed to test distributional shifts in model behavior.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
