# AEGIS 2.0 (A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails)

## 📊 Benchmark Details

**Name**: AEGIS 2.0 (A Diverse AI Safety Dataset and Risks Taxonomy for Alignment of LLM Guardrails)

**Overview**: AEGIS 2.0 is a dataset designed to address diverse safety risks in large language models (LLMs) using a taxonomy of 12 core and 9 fine-grained risk categories.

**Data Type**: dialogue samples with human-LLM interactions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/NVIDIA/AEGIS-2.0)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and adaptable dataset for understanding and moderating safety risks associated with LLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Content Moderation
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Human annotations and LLM-generated responses to prompts from diverse sources.

**Size**: 34,248 samples

**Format**: JSON

**Annotation**: Manual annotation by trained experts and automated labeling via a jury of LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on majority voting from human and automated annotations.

**Interpretation**: High scores indicate robust performance in safety classification tasks.

**Baseline Results**: Models fine-tuned on AEGIS 2.0 outperform existing safety models.

**Validation**: Model performance was validated through comparison with established benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset will be released under a commercial-permissive license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
