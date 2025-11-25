# Sentence-Bench

## 📊 Benchmark Details

**Name**: Sentence-Bench

**Overview**: The first sentence-level benchmarking dataset designed to assess G2P performance on sentence-level phonetic challenges of the Persian language.

**Data Type**: sentence-level phoneme sequences

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Resources**:
- [Resource](https://huggingface.co/datasets/MahtaFetrat/SentenceBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate G2P tools on sentence-level challenges and improve pronunciation prediction for polyphone words and context-sensitive phonemes in Persian.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Grapheme-to-Phoneme Conversion

**Limitations**: N/A

## 💾 Data

**Source**: Annotated sentences selected from CommonVoice and ManaTTS datasets, along with constructed sentences containing polyphone words.

**Size**: 400 sentences

**Format**: N/A

**Annotation**: Manual annotation of phonetic sequences for selected sentences.

## 🔬 Methodology

**Methods**:
- Prompting techniques
- Post-processing methods

**Metrics**:
- Phoneme Error Rate (PER)
- Polyphone accuracy
- Ezafe prediction accuracy

**Calculation**: Metrics calculated based on the model's performance in phoneme prediction.

**Interpretation**: Lower PER indicates better phonetic accuracy; higher accuracy in polyphone predictions signifies better contextual understanding.

**Validation**: Performed by comparing model outputs against phoneme-annotated sentences.

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

**Data Licensing**: Released under a GNU license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
