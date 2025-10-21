# Parallel Idiom Datasets for Persian-English Translation

## 📊 Benchmark Details

**Name**: Parallel Idiom Datasets for Persian-English Translation

**Overview**: This paper introduces two parallel datasets of sentences containing idiomatic expressions for Persian-English and English-Persian translations, with Persian idioms sampled from a new resource that includes idioms and their meanings, along with evaluation of various models.

**Data Type**: sentence pairs containing idiomatic expressions

**Domains**:
- Natural Language Processing

**Languages**:
- Persian
- English

**Resources**:
- [GitHub Repository](https://github.com/Sara-Rezaeimanesh/Fa-En-Idiom-Translation)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of various LLMs and NMT models on idiom translation between Persian and English.

**Target Audience**:
- ML Researchers
- Translation Researchers
- Natural Language Processing Practitioners

**Tasks**:
- Idiom Translation

**Limitations**: The datasets contain only 200 examples for each translation direction.

## 💾 Data

**Source**: Persian Idioms resource containing 2,200 idioms and examples, with 200 sentence pairs for each translation.

**Size**: 200 examples for each translation direction

**Format**: N/A

**Annotation**: Manually reviewed by native Persian speakers for accuracy and cultural relevance.

## 🔬 Methodology

**Methods**:
- Manual evaluation
- Automatic evaluation using LLMs and NMT models

**Metrics**:
- Idiomatic Translation Accuracy
- Fluency
- BLEU Score
- BERTScore

**Calculation**: Correlation between manual and automatic evaluation scores.

**Interpretation**: A higher score indicates better idiomatic translation and fluency.

**Baseline Results**: Claude-3.5-Sonnet performs best in both translation directions.

**Validation**: Manual inspections and evaluations by multiple native speakers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
