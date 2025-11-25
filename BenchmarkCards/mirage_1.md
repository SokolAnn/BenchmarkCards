# MIRAGE

## 📊 Benchmark Details

**Name**: MIRAGE

**Overview**: MIRAGE is a diagnostic benchmark specifically designed to isolate reasoning-induced hallucinations in multimodal large language models (MLLMs) and assess their visual and logical reasoning capabilities through various evaluation metrics.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- HallusionBench
- MMVP
- POPE
- MathVista

**Resources**:
- [Resource](https://arxiv.org/abs/2505.24238)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework that isolates reasoning hallucinations in multimodal large language models, enabling targeted diagnosis and mitigation strategies.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Visual Reasoning
- Logical Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from various publicly available datasets incorporating seven distinct cognitive taxonomies.

**Size**: 1,329 examples

**Format**: JSON

**Annotation**: Human-AI collaborative verification for reasoning chains.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Factuality
- LLMs Hallucination Score

**Calculation**: Metrics are calculated based on final answers, intermediate reasoning steps, and the overall reasoning chains.

**Interpretation**: Higher scores indicate better performance in avoiding hallucinations and better reasoning consistency.

**Baseline Results**: Logos serves as a baseline on MIRAGE, significantly improving the logical reasoning accuracy of original models.

**Validation**: Evaluated through extensive experiments comparing MLLMs on the MIRAGE benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Bias in machine learning model outputs based on training data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
