# FROG (Fuzzy Reasoning of Generalized Quantifiers)

## 📊 Benchmark Details

**Name**: FROG (Fuzzy Reasoning of Generalized Quantifiers)

**Overview**: FROG is a benchmark for evaluating fuzzy reasoning capabilities in large language models, consisting of real-world mathematical word problems that incorporate generalized quantifiers.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MathQA

**Resources**:
- [GitHub Repository](https://github.com/Nativeatom/FRoG)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the fuzzy reasoning abilities of large language models and examine challenges associated with fuzzy logic in mathematical reasoning problems.

**Target Audience**:
- Research Scientists
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: The questions constructed may not naturally occur and the masking-based reasoning protocol may not reflect real-world reasoning processes.

## 💾 Data

**Source**: Collected from GSM8K and MathQA datasets

**Size**: 2,044 questions

**Format**: JSON

**Annotation**: Automatically generated based on fuzzy reasoning tasks involving generalized quantifiers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is measured as the proportion of correctly answered questions out of the total questions.

**Interpretation**: Higher accuracy indicates better performance in reasoning tasks, while a lower accuracy indicates challenges in fuzzy reasoning.

**Baseline Results**: The best performing model, GPT-4-turbo, achieved below 50% accuracy across different settings.

**Validation**: Evaluated using several open-sourced LLMs with various masking strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
