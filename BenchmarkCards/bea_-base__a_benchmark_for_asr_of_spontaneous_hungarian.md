# BEA -Base: A Benchmark for ASR of Spontaneous Hungarian

## 📊 Benchmark Details

**Name**: BEA -Base: A Benchmark for ASR of Spontaneous Hungarian

**Overview**: BEA-Base is a dataset created to provide a benchmark for assessing Automatic Speech Recognition (ASR) of spontaneous Hungarian speech. It is designed to facilitate the training and evaluation of ASR systems, especially for conversational AI applications, by utilizing spontaneous speech from a diverse set of speakers.

**Data Type**: speech recordings

**Domains**:
- Natural Language Processing

**Languages**:
- Hungarian

**Resources**:
- [Resource](https://phon.nytud.hu/bea)

## 🎯 Purpose and Intended Users

**Goal**: To create a benchmark dataset for Hungarian ASR training and evaluation, primarily focusing on spontaneous speech to improve the performance of ASR systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Automatic Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: BEA spoken Hungarian database comprising spontaneous speech of 140 speakers.

**Size**: 71.2 hours of training data, 4.02 hours of development data, 4.91 hours of evaluation data

**Format**: N/A

**Annotation**: Manual transcription and segmentation of speech data.

## 🔬 Methodology

**Methods**:
- Hybrid HMM-DNN
- End-to-end Neural Network using CRDNN and GRU
- Convolutional Models

**Metrics**:
- Word Error Rate (WER)
- Character Error Rate (CER)

**Calculation**: Standard evaluation based on WER and CER calculated against transcriptions of spontaneous speech.

**Interpretation**: A lower WER and CER indicate better performance of the ASR system in recognizing spontaneous Hungarian speech.

**Baseline Results**: Best results achieved are WER of 15.61% and CER of 5.11% on the spontaneous evaluation set.

**Validation**: The spontaneous evaluation set was used for validation during the training of ASR systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
