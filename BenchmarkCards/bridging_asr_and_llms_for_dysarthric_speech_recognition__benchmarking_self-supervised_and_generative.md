# Bridging ASR and LLMs for Dysarthric Speech Recognition: Benchmarking Self-Supervised and Generative Approaches

## 📊 Benchmark Details

**Name**: Bridging ASR and LLMs for Dysarthric Speech Recognition: Benchmarking Self-Supervised and Generative Approaches

**Overview**: This study benchmarks self-supervised ASR models for dysarthric speech recognition, comparing their performance with LLM-enhanced decoding to improve transcription intelligibility.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2508.08027)

## 🎯 Purpose and Intended Users

**Goal**: To systematically benchmark ASR architectures and integrate LLM-based decoding for dysarthric speech recognition to enhance intelligibility.

**Target Audience**:
- ML Researchers
- Speech Recognition Practitioners
- Dysarthric Speech Researchers

**Tasks**:
- Speech Recognition

**Limitations**: Cross-dataset generalization is poor, high WER increases on unseen data, and limited dysarthric speech data restricts robustness.

## 💾 Data

**Source**: TORGO and UASpeech datasets

**Size**: 21 hours for TORGO, 102.7 hours for UASpeech

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Word Error Rate (WER)
- Character Error Rate (CER)

**Calculation**: Metrics calculated based on transcription outputs compared to ground truth.

**Interpretation**: Lower WER and CER indicate better performance in recognizing dysarthric speech.

**Baseline Results**: HuBERT-CTC (0.50 TORGO, 0.54 UASpeech); Whisper (0.38 TORGO, 0.40 UASpeech).

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
