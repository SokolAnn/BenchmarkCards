# FINAUDIO

## 📊 Benchmark Details

**Name**: FINAUDIO

**Overview**: FINAUDIO is the first benchmark designed to evaluate the capacity of Audio Large Language Models (AudioLLMs) in the financial domain, focusing on tasks such as automatic speech recognition (ASR) for both short and long financial audio, as well as summarization of financial audio data.

**Data Type**: audio

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- AirBench
- AudioBench
- FLUE
- FinBen
- PIXIU

**Resources**:
- [Resource](https://arxiv.org/abs/2503.20990)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive open-source evaluation benchmark for AudioLLMs in the financial audio domain.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- ASR for short financial audio clips
- ASR for long financial audio recordings
- Financial Audio Summarization

**Limitations**: Due to the limited availability of financial audio data, FinAudio primarily focuses on ASR-related tasks and does not address financial audio scenarios involving languages other than English.

## 💾 Data

**Source**: Four open-source financial audio datasets related to earnings conference calls and financial discussions.

**Size**: 400 hours of audio

**Format**: N/A

**Annotation**: Annotated based on sentence-level segmentation aligned with transcripts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Word Error Rate (WER)
- Rouge-L
- BERTScore

**Calculation**: Metrics like WER are calculated based on the number of substitutions, deletions, and insertions compared to the reference transcript.

**Interpretation**: Lower WER indicates better ASR performance; higher scores in Rouge-L and BERTScore suggest better summarization quality.

**Baseline Results**: Evaluation of seven prevalent AudioLLMs revealed performance variations across ASR tasks and summarization.

**Validation**: Evaluation conducted over multiple repetitions to ensure reliability of results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The publicly available datasets used in FINAUDIO do not contain personal information and conform to established ethical guidelines.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
