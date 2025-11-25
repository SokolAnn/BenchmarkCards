# CORAA (Corpus of Annotated Audios)

## 📊 Benchmark Details

**Name**: CORAA (Corpus of Annotated Audios)

**Overview**: CORAA is a publicly available dataset for Automatic Speech Recognition (ASR) in Brazilian Portuguese, containing 290.77 hours of validated audio-transcription pairs and addressing the lack of spontaneous speech in existing resources.

**Data Type**: audio-transcription pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Portuguese

**Resources**:
- [GitHub Repository](https://github.com/nilc-nlp/CORAA)

## 🎯 Purpose and Intended Users

**Goal**: To improve ASR models in Brazilian Portuguese by providing a large corpus of spontaneous and prepared speech.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Automatic Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: The corpus is assembled from five corpora: ALIP, C-ORAL Brasil I, NURC-Recife, SP2010, and TEDx Portuguese talks.

**Size**: 290.77 hours

**Format**: WAV

**Annotation**: Manually validated for audio-transcription pairs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Word Error Rate (WER)
- Character Error Rate (CER)

**Calculation**: Metrics are calculated based on the counts of errors in the ASR output compared to ground truth transcriptions.

**Interpretation**: Lower WER and CER values indicate better ASR model performance.

**Baseline Results**: Model achieved a WER of 24.18% on CORAA test set.

**Validation**: Validation of audio-transcription pairs was performed through a web interface by multiple annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-ND 4.0 license.

**Consent Procedures**: Informed consent was obtained from participants wherever applicable.

**Compliance With Regulations**: Not Applicable
