# GUS-Net

## 📊 Benchmark Details

**Name**: GUS-Net

**Overview**: The GUS-Net framework addresses social-bias detection in NLP by introducing a multi-label, token-level dataset that categorizes biases into three pathways: Generalizations, Unfairness, and Stereotypes, using a hybrid LLM-human annotation pipeline.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BABE
- NBIAS

**Resources**:
- [GitHub Repository](https://github.com/username/repository)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic method for detecting and addressing biases in natural language, facilitating auditing and mitigation in real-world NLP applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Bias Detection
- Token Classification

**Limitations**: N/A

## 💾 Data

**Source**: Hybrid LLM-human pipeline for dataset generation and annotation.

**Size**: 3,739 sentences with over 69,000 token-level annotations

**Format**: JSON

**Annotation**: Hybrid method using LLM-generated candidate spans and human verification.

## 🔬 Methodology

**Methods**:
- Multi-label BIO tagging
- Encoder-based models evaluation
- Decoder-based models evaluation

**Metrics**:
- Precision
- Recall
- F1 Score
- Hamming Loss

**Calculation**: Focal loss for multi-label classification, monitoring per-channel thresholds for label prediction.

**Interpretation**: Higher Precision, Recall, and F1 indicate better model performance on bias detection.

**Baseline Results**: Best results achieved with encoder-only models against decoder-only models in precise token-level prediction.

**Validation**: Out-of-distribution generalization evaluated using the BABE dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
