# DigiSpon (Digitally Supported Analysis of Spontaneous Speech)

## 📊 Benchmark Details

**Name**: DigiSpon (Digitally Supported Analysis of Spontaneous Speech)

**Overview**: The benchmark introduces a semi-automated approach using NLP methods for language sample analysis of spontaneous speech in Swiss children, aiming to assist speech-language pathologists in diagnosing developmental language disorder (DLD) more efficiently.

**Data Type**: speech transcriptions

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- German

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To leverage NLP methods for semi-automated language sample analysis to assist in diagnosing DLD in children.

**Target Audience**:
- Speech-language pathologists
- NLP Researchers

**Tasks**:
- Speech Recognition
- Language Analysis

**Limitations**: The sample size is low compared to evaluations in other contexts; potential generalized results are limited to the specific speech contexts captured.

## 💾 Data

**Source**: Data collected from 119 children in various Swiss contexts, comprising Swiss German and Swiss Standard German speech samples.

**Size**: 41 recordings

**Format**: transcript files

**Annotation**: Manually annotated by trained students of speech and language therapy.

## 🔬 Methodology

**Methods**:
- Automatic Speech Recognition (ASR)
- Part-of-speech tagging
- Manual transcription

**Metrics**:
- Word Error Rate (WER)
- Character Error Rate (CER)
- F1 Score

**Calculation**: ASR performance is measured via WER, CER on the transcription accuracy and F1 Score for POS tagging.

**Interpretation**: Lower WER and CER indicate better transcription accuracy; higher F1 scores indicate better tagging performance.

**Baseline Results**: Initial ASR models showed higher error rates, but fine-tuning improved transcription performance significantly.

**Validation**: Results are validated through comparisons of manual vs. ASR transcriptions, showing improvements in tagging accuracy post-normalization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes recordings from children across multiple dialects of Swiss German.

**Potential Harm**: Potential ethical concerns regarding the handling of sensitive speech data from children.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is anonymized and all necessary ethical approvals were obtained; parental consent was ensured.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from parents in simplified language.

**Compliance With Regulations**: The study complies with Swiss data protection regulations.
