# SSLD-200 (Song Structure and Lyric Dataset)

## 📊 Benchmark Details

**Name**: SSLD-200 (Song Structure and Lyric Dataset)

**Overview**: The SSLD-200 dataset comprises 200 songs, 100 Chinese and 100 English, collected from YouTube with detailed structural information and lyrics, aimed at evaluating structured lyrics recognition.

**Data Type**: structured song data

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Chinese
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/waytan22/SSLD-200)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized dataset for evaluating structured lyrics recognition models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Lyric Recognition
- Structure Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Songs collected from YouTube, containing both audio and corresponding lyrics.

**Size**: 200 songs, total duration of 13.9 hours

**Format**: N/A

**Annotation**: Manual annotations of structure and lyrics for each song.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Diarization Error Rate (DER)
- Word Error Rate (WER)

**Calculation**: Metrics are calculated based on the output of structure analysis and lyric recognition modules.

**Interpretation**: Lower DER indicates better structural accuracy, and lower WER indicates better lyric transcription accuracy.

**Validation**: Evaluated on the proposed SSLD-200 dataset.

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
