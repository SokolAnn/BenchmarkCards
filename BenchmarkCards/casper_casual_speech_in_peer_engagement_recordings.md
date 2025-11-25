# CASPER (CAsual Speech in Peer Engagement Recordings)

## 📊 Benchmark Details

**Name**: CASPER (CAsual Speech in Peer Engagement Recordings)

**Overview**: The paper introduces a comprehensive speech dataset named CASPER, comprising 200 hours of recorded English conversations, of which 158 hours are spontaneous speech, aiming to address the scarcity of high-quality spontaneous speech data.

**Data Type**: audio

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Switchboard
- GigaSpeech

**Resources**:
- [Resource](https://huggingface.co/datasets/CASPER-SSSD/CASPER/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that captures the natural flow of dialogue, including disfluencies, pauses, and speaker interactions, aimed at improving downstream tasks in speech processing.

**Target Audience**:
- ML Researchers
- Speech Processing Practitioners

**Tasks**:
- Automatic Speech Recognition
- Speaker Diarization
- Topic Detection

**Limitations**: N/A

## 💾 Data

**Source**: Recorded conversations between pairs of participants using personal devices.

**Size**: 200 hours of recorded audio, 158 hours actual speech

**Format**: WAV

**Annotation**: Manual annotation for transcripts and speaker metadata.

## 🔬 Methodology

**Methods**:
- Manual evaluation by transcription
- Automatic Speech Recognition

**Metrics**:
- Word Error Rate (WER)
- Diarization Error Rate (DER)
- Jaccard Error Rate (JER)

**Calculation**: Metrics calculated using reference transcripts compared to model outputs.

**Interpretation**: Lower WER indicates better performance for ASR models on spontaneous speech.

**Baseline Results**: Whisper-large-v3 achieved WER of 0.31, SeamlessM4T-large achieved WER of 0.53.

**Validation**: Random sampling of conversations for evaluation of ASR and diarization tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Includes demographic metadata of speakers such as accent, age, and gender.

**Potential Harm**: Potential exposure of personal data and bias in accent representation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: De-identification of audio and metadata to protect participant identity.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants signed informed consent forms prior to data collection.

**Compliance With Regulations**: Not Applicable
