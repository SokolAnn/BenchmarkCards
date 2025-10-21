# Vistaar

## 📊 Benchmark Details

**Name**: Vistaar

**Overview**: Vistaar is a set of 59 benchmarks across various language and domain combinations for evaluating and improving Automatic Speech Recognition (ASR) systems in Indian languages.

**Data Type**: word-error rate values

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali
- Gujarati
- Hindi
- Kannada
- Malayalam
- Marathi
- Odia
- Punjabi
- Sanskrit
- Tamil
- Telugu
- Urdu

**Similar Benchmarks**:
- Gramvaani
- FLEURS
- CommonVoice
- IndicTTS
- MUCS

**Resources**:
- [GitHub Repository](https://github.com/AI4Bharat/vistaar)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of ASR systems across diverse benchmarks that capture linguistic diversity in Indian languages.

**Target Audience**:
- ASR Researchers
- ML Researchers
- Industry Practitioners

**Tasks**:
- Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available training datasets across 12 Indian languages.

**Size**: 10,700 hours

**Format**: Multiple formats

**Annotation**: Various collection methods including crowdsourcing and professional recordings.

## 🔬 Methodology

**Methods**:
- Model evaluation
- Word-error rate comparison

**Metrics**:
- Word Error Rate (WER)

**Calculation**: Average WER calculated across benchmarks for each language.

**Interpretation**: Lower WER indicates better ASR performance.

**Baseline Results**: IndicWhisper achieves the lowest average WER across benchmarks.

**Validation**: Evaluation against multiple ASR systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Exposing personal information

**Demographic Analysis**: Analysis of linguistic diversity included.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-source under appropriate licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
