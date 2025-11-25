# RapBank

## 📊 Benchmark Details

**Name**: RapBank

**Overview**: RapBank is a rap song dataset collected from the internet, consisting of a large volume of rap songs with corresponding lyrics and various quality-related metrics. It was created to address the scarcity of publicly available rap datasets for rapping voice generation.

**Data Type**: audio-lyrics pairs

**Domains**:
- Natural Language Processing
- Music Generation

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/NZqian/RapBank)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of RapBank is to provide a dataset for rapping synthesis tasks, enabling the training of models for generating rapping vocals.

**Target Audience**:
- ML Researchers
- Music Generation Practitioners

**Tasks**:
- Rapping Voice Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from the internet through automated data crawling from rap-related playlists on YouTube.

**Size**: 92,371 songs, totaling 5,586 hours

**Format**: N/A

**Annotation**: The lyrics were transcribed using automatic speech recognition (ASR) models, and quality-related metrics were calculated for segmentation and filtering.

## 🔬 Methodology

**Methods**:
- Data crawling
- Source separation
- Segmentation
- Lyrics recognition
- Quality filtering

**Metrics**:
- Mean Opinion Score (MOS)
- Word Error Rate (WER)
- Speaker Cosine Similarity (SECS)

**Calculation**: Metrics are calculated based on generated vocals evaluated against human-annotated lyrics and naturalness through listening tests.

**Interpretation**: Higher MOS scores indicate better perceived naturalness and alignment of generated rap vocals with the accompaniment.

**Baseline Results**: N/A

**Validation**: Evaluation through subjective listening tests and objective metrics comparison.

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

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
