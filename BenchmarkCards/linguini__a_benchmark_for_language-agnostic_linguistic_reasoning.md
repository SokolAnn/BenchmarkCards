# Linguini: A benchmark for language-agnostic linguistic reasoning

## 📊 Benchmark Details

**Name**: Linguini: A benchmark for language-agnostic linguistic reasoning

**Overview**: We propose a new benchmark to measure a language model’s linguistic reasoning skills without relying on pre-existing language-specific knowledge. The test covers 894 questions grouped in 160 problems across 75 (mostly) extremely low-resource languages, extracted from the International Linguistic Olympiad corpus.

**Data Type**: questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BIG-Bench

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/linguini)

## 🎯 Purpose and Intended Users

**Goal**: To provide a compact and effective benchmark to assess linguistic reasoning without relying on existing language-specific knowledge.

**Target Audience**:
- ML Researchers
- Linguists
- AI Practitioners

**Tasks**:
- Linguistic Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: International Linguistic Olympiad corpus

**Size**: 894 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Few-shot evaluation

**Metrics**:
- Accuracy
- chrF

**Calculation**: Accuracy measured using exact match and chrF scores.

**Interpretation**: Higher scores indicate better performance on linguistic reasoning tasks.

**Baseline Results**: N/A

**Validation**: Leave-one-out cross-validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Problems are shared only for research purposes under the license CC-BY-SA 4.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
