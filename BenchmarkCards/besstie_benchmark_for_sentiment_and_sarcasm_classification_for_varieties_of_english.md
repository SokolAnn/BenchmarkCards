# BESSTIE (Benchmark for Sentiment and Sarcasm classification for Varieties of English)

## 📊 Benchmark Details

**Name**: BESSTIE (Benchmark for Sentiment and Sarcasm classification for Varieties of English)

**Overview**: BESSTIE introduces a benchmark for sentiment and sarcasm classification for three varieties of English: Australian (en-AU), Indian (en-IN), and British (en-UK).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DialectBench

**Resources**:
- [Resource](https://huggingface.co/datasets/unswnlporg/BESSTIE)

## 🎯 Purpose and Intended Users

**Goal**: To provide an evaluative benchmark for future research in equitable LLMs, specifically in terms of language varieties.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Sentiment Classification
- Sarcasm Classification

**Limitations**: Our assumption of national varieties as representative forms of dialect is a simplification.

## 💾 Data

**Source**: Collected datasets from Google Places reviews and Reddit comments using location-based and topic-based filtering.

**Size**: 12,000 comments and reviews per variety

**Format**: N/A

**Annotation**: Manual annotation by native speakers for sentiment and sarcasm labeling.

## 🔬 Methodology

**Methods**:
- Fine-tuning of large language models
- Evaluation on annotated datasets

**Metrics**:
- F-S CORE

**Calculation**: Calculated as macro-averaged metrics across different varieties.

**Interpretation**: Higher F-S CORE indicates better performance on sentiment and sarcasm tasks.

**Baseline Results**: Average F-S CORE of 0.81 for sentiment classification, and 0.59 for sarcasm classification.

**Validation**: Manual annotation and automated validation processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis included consideration of different English language varieties.

**Potential Harm**: BESSTIE aims to address biases in language models towards non-standard English varieties.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset shared in a manner that preserves user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data gathered from publicly available posts through official APIs.

**Compliance With Regulations**: Received ethics approval from the Human Research Ethics Committee at UNSW, Sydney.
