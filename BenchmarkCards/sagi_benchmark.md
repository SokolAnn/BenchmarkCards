# SAGI Benchmark

## 📊 Benchmark Details

**Name**: SAGI Benchmark

**Overview**: The SAGI Benchmark is designed to evaluate speech LLMs across various tasks that represent the characteristics of different levels of speech understanding, from basic ASR to advanced capabilities integrating non-semantic information and abstract acoustic knowledge.

**Data Type**: audio

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured benchmark for evaluating the capabilities of speech LLMs across five defined levels of speech understanding.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Speech Recognition
- Emotion Recognition
- Language Distinction
- Volume Perception
- Cough Type Classification

**Limitations**: The benchmark currently does not cover certain advanced tasks associated with Level 4 and Level 5.

## 💾 Data

**Source**: Various publicly available datasets including LibriSpeech, RA VDESS, and others as detailed in the paper.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Word Error Rate (WER)

**Calculation**: Metrics such as WER are calculated by comparing ASR outputs to reference text. Accuracy is measured by the percentage of correct responses in objective tasks.

**Interpretation**: Higher accuracy indicates better performance in recognition and understanding tasks.

**Baseline Results**: N/A

**Validation**: Reliability of evaluation sets was verified using human tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
