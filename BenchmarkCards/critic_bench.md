# CRITIC BENCH

## 📊 Benchmark Details

**Name**: CRITIC BENCH

**Overview**: CRITIC BENCH is a comprehensive benchmark designed to assess LLMs’ abilities to critique and rectify their reasoning across various tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://criticbench.github.io)
- [GitHub Repository](https://github.com/CriticBench/CriticBench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically assess critique and correction reasoning in various LLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Critique and Correction Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: 15 existing datasets covering mathematical, commonsense, symbolic, coding, and algorithmic tasks.

**Size**: 3,800 instances

**Format**: N/A

**Annotation**: Responses were validated through rule-based methods, GPT-4 evaluations, and manual review.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy is calculated as the number of correct predictions divided by the total number of questions.

**Interpretation**: Model performance can be compared through accuracy rates in generation, critique, and correction.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through comparisons with existing methods and manual reviews.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness
- Misuse

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Misuse**: Improper usage

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
