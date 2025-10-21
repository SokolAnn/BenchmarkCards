# ALAS (Automatic Latent Alignment Score)

## 📊 Benchmark Details

**Name**: ALAS (Automatic Latent Alignment Score)

**Overview**: ALAS is a metric for assessing alignment quality in speech-text multimodal Large Language Models (LLMs), designed to measure correlations between audio and text representations across transformer layers.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To measure the semantic alignment between audio and text modalities in spoken language understanding with multimodal LLMs.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering
- Emotion Recognition

**Limitations**: N/A

## 💾 Data

**Source**: LibriSQA and IEMOCAP datasets

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Comparison against reference alignment from Whisper
- Quantitative analysis of alignment scores

**Metrics**:
- Alignment Score

**Calculation**: ALAS score is calculated using cross-modal similarities and the monotonic-alignment-search algorithm.

**Interpretation**: Higher ALAS scores indicate better alignment between audio and text representations.

**Validation**: Validated through quantitative comparisons with existing multimodal LLMs' performances on tasks.

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
