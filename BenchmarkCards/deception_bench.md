# DECEPTION BENCH

## 📊 Benchmark Details

**Name**: DECEPTION BENCH

**Overview**: DECEPTION BENCH is a systematic benchmark designed to assess deceptive behaviors in large language models (LLMs) across five categories, specifically focusing on covert alignment faking, sycophancy, and more.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://cot-monitor-plus.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To systematically explore and assess deceptive alignment in large language models and develop techniques to mitigate such risks.

**Target Audience**:
- ML Researchers
- AI Safety Practitioners

**Tasks**:
- Behavioral Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Developed via manual curation of 180 scenarios inspired by realistic interactions.

**Size**: 180 scenarios

**Format**: N/A

**Annotation**: Manual annotation with human verification

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Deception Tendency Rate (DTR)

**Calculation**: DTR is defined as the fraction of instances exhibiting deceptive behavior, comparing the model's chain of thought and final answer.

**Interpretation**: A lower DTR indicates less deceptive behavior in the model.

**Validation**: Benchmarked against existing models and evaluated for consistency with human judgment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Transparency**: Lack of training data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
