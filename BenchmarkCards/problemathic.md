# PROBLEMATHIC

## 📊 Benchmark Details

**Name**: PROBLEMATHIC

**Overview**: PROBLEMATHIC is a dataset containing both adversarial and non-adversarial mathematical word problem (MWP) pairs, aimed at studying the susceptibility of large language models (LLMs) to irrelevant numerical information in MWPs.

**Data Type**: math word problem pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM-8K

**Resources**:
- [Resource](https://huggingface.co/datasets/him1411/problemathic)
- [GitHub Repository](https://github.com/him1411/problemathic)

## 🎯 Purpose and Intended Users

**Goal**: To analyze the performance of large language models on mathematical word problems containing irrelevant information and to improve their robustness through adversarial training.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Adversarial and non-adversarial mathematical word problems augmented with irrelevant information.

**Size**: 1,926 samples (1,313 Simple, 613 Complex)

**Format**: N/A

**Annotation**: Manually curated and classified based on problem complexity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Fine-tuning models

**Metrics**:
- Exact Match Accuracy

**Calculation**: Metrics are calculated as the percentage of exactly correct answers over total answers.

**Interpretation**: Higher accuracy indicates better performance in identifying relevant information and solving problems.

**Baseline Results**: Exact match accuracy varies among models, with drops of up to 41.53% on adversarial samples.

**Validation**: Empirical evaluation through multiple model trials and human quality assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
