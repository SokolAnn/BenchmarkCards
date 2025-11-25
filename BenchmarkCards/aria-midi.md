# ARIA-MIDI

## 📊 Benchmark Details

**Name**: ARIA-MIDI

**Overview**: We introduce an extensive new dataset of MIDI files, created by transcribing audio recordings of piano performances into their constituent notes.

**Data Type**: MIDI files

**Domains**:
- Music Information Retrieval

**Languages**:
- N/A

**Similar Benchmarks**:
- MAESTRO
- GiantMIDI
- ATEPP
- PiJAMA

**Resources**:
- [GitHub Repository](https://github.com/loubbrad/aria-midi)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large, high-quality dataset of piano transcriptions to accelerate music information retrieval research.

**Target Audience**:
- Music Information Retrieval Researchers
- Deep Learning Practitioners

**Tasks**:
- Automatic Music Transcription
- Data Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Transcribed audio recordings from YouTube and other publicly accessible sources.

**Size**: 31,186,253 MIDI files, approximately 100,629 hours of transcribed audio

**Format**: MIDI

**Annotation**: Automatically generated using a language model and audio classifiers.

## 🔬 Methodology

**Methods**:
- Automated transcription using the Aria-AMT model
- Data crawling through YouTube and API scoring

**Metrics**:
- Transcription accuracy as assessed on MAESTRO and MAPS test sets

**Calculation**: Accuracy calculated using the mir eval library with default settings.

**Interpretation**: Higher scores indicate better performance in transcription models.

**Baseline Results**: Transcription model achieves over 98% precision on MAESTRO data.

**Validation**: Evaluated against human labels for classification and transcription accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-NC-SA 4.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
