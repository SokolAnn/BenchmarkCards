# Safety-aware Contrastive Decoding (SafeCoDe)

## 📊 Benchmark Details

**Name**: Safety-aware Contrastive Decoding (SafeCoDe)

**Overview**: SafeCoDe is a lightweight and model-agnostic decoding framework that dynamically adjusts token generation based on multimodal context to improve safety alignment in Multimodal Large Language Models (MLLMs).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MSSBench
- MOSSBench
- MM-SafetyBench
- Hades
- FigStep

**Resources**:
- [GitHub Repository](https://github.com/franciscoliu/SafeCoDe)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SafeCoDe is to enhance context-sensitive safety decisions in MLLMs to avoid undersensitivity and oversensitivity in responses.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Safety alignment
- Contextual decision making

**Limitations**: N/A

## 💾 Data

**Source**: MSSBench, MOSSBench, MM-SafetyBench, and others

**Size**: 5,040 image-text pairs

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Rejection Rate

**Calculation**: Metrics are calculated based on performance against human annotations in safety evaluations.

**Interpretation**: Higher accuracy indicates better safety alignment by correctly refusing unsafe queries and complying with benign ones.

**Validation**: Extensive experiments conducted across diverse MLLM architectures and safety benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Decision bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
