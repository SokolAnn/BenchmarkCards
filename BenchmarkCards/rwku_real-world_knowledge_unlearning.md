# RWKU (Real-World Knowledge Unlearning)

## 📊 Benchmark Details

**Name**: RWKU (Real-World Knowledge Unlearning)

**Overview**: RWKU is designed for LLM unlearning, utilizing real-world knowledge to evaluate model capabilities in unlearning sensitive information.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WHP (Who is Harry Potter)
- WMDP (Weapons of Mass Destruction Proxy Benchmark)
- TOFU (Task of Fictitious Unlearning)

**Resources**:
- [Resource](http://rwku-bench.github.io)
- [Resource](https://huggingface.co/datasets/jinzhuoran/RWKU)
- [GitHub Repository](https://github.com/jinzhuoran/RWKU)

## 🎯 Purpose and Intended Users

**Goal**: To establish a comprehensive evaluation framework for unlearning knowledge in large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Knowledge Unlearning

**Limitations**: N/A - Not explicitly discussed

## 💾 Data

**Source**: 200 real-world famous people sourced from Wikipedia.

**Size**: 200 targets, 13,131 forget probes, 11,379 neighbor probes

**Format**: JSON

**Annotation**: Probes generated using GPT-4 and validated by human check for format.

## 🔬 Methodology

**Methods**:
- Membership Inference Attack (MIA)
- Adversarial Attack Probes

**Metrics**:
- ROUGE-L recall

**Calculation**: Precision and recall scores for measuring efficacy of knowledge unlearning.

**Interpretation**: Lower ROUGE-L scores indicate improved unlearning effectiveness.

**Baseline Results**: N/A

**Validation**: Extensive experiments conducted across multiple models and scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Robustness
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Robustness**: Prompt injection attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is sourced from public domains (e.g., Wikipedia).

**Data Licensing**: CC BY 4.0

**Consent Procedures**: N/A - Data is publicly available.

**Compliance With Regulations**: Not Applicable
