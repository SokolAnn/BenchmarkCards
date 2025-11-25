# Killkan

## 📊 Benchmark Details

**Name**: Killkan

**Overview**: This paper presents Killkan, the first dataset for automatic speech recognition (ASR) in the Kichwa language, an indigenous language of Ecuador. The dataset contains approximately 4 hours of audio with transcription, translation into Spanish, and morphosyntactic annotation in the format of Universal Dependencies.

**Data Type**: audio-transcription pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Kichwa
- Spanish

**Resources**:
- [GitHub Repository](https://github.com/ctaguchi/killkan)
- [Resource](https://huggingface.co/ctaguchi/killkan_asr)

## 🎯 Purpose and Intended Users

**Goal**: To build resources for automatic speech recognition and language technologies for the endangered Kichwa language.

**Target Audience**:
- ML Researchers
- Linguists
- Language Revitalization Practitioners

**Tasks**:
- Automatic Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: The audio data was retrieved from a publicly available radio program

**Size**: 4 hours of audio

**Format**: WAV

**Annotation**: Time-aligned sentence-level transcriptions, Spanish translations, and morphosyntactic annotations compatible with Universal Dependencies.

## 🔬 Methodology

**Methods**:
- Fine-tuning a pretrained model (Wav2Vec2) for ASR

**Metrics**:
- Character Error Rate (CER)
- Word Error Rate (WER)
- Word Information Lost (WIL)

**Calculation**: CER, WER, and WIL are calculated based on the discrepancies between predicted and actual transcriptions.

**Interpretation**: A lower CER and WER indicate better performance in transcribing the ASR output.

**Baseline Results**: Latest model achieved 2.04% CER on the test set.

**Validation**: The dataset was fine-tuned against different sample sizes to test its performance across various levels of resource availability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons BY-SA license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
