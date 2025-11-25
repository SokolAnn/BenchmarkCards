# K AIROS

## 📊 Benchmark Details

**Name**: K AIROS

**Overview**: K AIROS is a benchmark simulating quiz contests with peer agents of varying reliability, allowing for systematic investigation of how trust, peer action, and self-confidence influence decisions in LLMs during social interactions.

**Data Type**: multiple-choice question answering

**Domains**:
- Natural Language Processing
- Social Computing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/declare-lab/KAIROS)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate and improve how LLMs perform in socially interactive, trust-sensitive environments.

**Target Audience**:
- Researchers
- Model Developers

**Tasks**:
- Question Answering
- Social Interaction Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Diverse datasets including Reasoning, Knowledge, Common Sense, and Creativity tasks combined into a multiple-choice format.

**Size**: 10,000 training instances, 3,000 testing instances

**Format**: JSON

**Annotation**: Crowdsourced and manually verified

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Utility
- Resistance
- Robustness

**Calculation**: Metrics are calculated based on the model's performance under original and K AIROS settings.

**Interpretation**: Higher accuracy and robustness indicate a model's ability to maintain consistent performance under social interactions.

**Baseline Results**: Results from existing benchmarks like MMLU-Pro and TruthfulQA.

**Validation**: Cross-validation conducted through controlled simulations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
