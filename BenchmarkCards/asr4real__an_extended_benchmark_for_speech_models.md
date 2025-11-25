# ASR4REAL: An Extended Benchmark for Speech Models

## 📊 Benchmark Details

**Name**: ASR4REAL: An Extended Benchmark for Speech Models

**Overview**: This paper introduces a set of benchmarks matching real-life conditions in Automatic Speech Recognition (ASR) to identify biases and weaknesses in models, particularly focusing on performance discrepancies by accent and socio-economic status.

**Data Type**: audio

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Librispeech

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark that allows researchers to identify strengths and weaknesses of their ASR models in real-world settings.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark utilizes various datasets such as Librispeech, ALLSSTAR, NISP, VoxPopuli, Buckeye, and CORAAL for testing ASR models in different conditions.

**Size**: 960 hours of labeled audio data

**Format**: Audio recordings

**Annotation**: Manually transcribed audio files

## 🔬 Methodology

**Methods**:
- Model evaluation on varied datasets
- Word Error Rate (WER) analysis

**Metrics**:
- Word Error Rate (WER)

**Calculation**: The WER was normalized by speaker to account for the distribution of speaker characteristics.

**Interpretation**: Lower WER indicates better model performance, with a focus on robustness across diverse conditions.

**Baseline Results**: N/A

**Validation**: Cross-comparison of several ASR models and systems under varied testing conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis shows performance discrepancies based on accent and socio-economic status of speakers.

**Potential Harm**: The benchmark addresses harm related to biases in ASR systems, particularly highlighting disparities in performance based on speaker characteristics.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
