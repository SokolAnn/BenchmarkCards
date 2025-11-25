# MovieSum

## 📊 Benchmark Details

**Name**: MovieSum

**Overview**: MovieSum is a new dataset for abstractive summarization of movie screenplays, consisting of 2200 movie screenplay-summary pairs. It aims to stimulate research in the area of movie screenplay understanding and summarization.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ScriptBase-j
- NarrativeQA
- SummScreenFD

**Resources**:
- [GitHub Repository](https://github.com/saxenarohit/MovieSum)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset to advance research in movie screenplay summarization.

**Target Audience**:
- ML Researchers
- Natural Language Processing Practitioners

**Tasks**:
- Summarization

**Limitations**: The dataset consists of movie screenplays and their corresponding summaries only in English.

## 💾 Data

**Source**: Collected from various movie screenplay websites and paired with Wikipedia plot summaries.

**Size**: 2200 examples

**Format**: Formatted text

**Annotation**: Manually formatted by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE Score
- BERTScore

**Calculation**: Metrics are calculated following the standard protocols for summarization evaluation.

**Interpretation**: Higher ROUGE scores indicate better summarization performance.

**Baseline Results**: Lead-512: ROUGE-1: 10.35, ROUGE-2: 1.27, ROUGE-L: 9.84; Longformer: ROUGE-1: 44.85, ROUGE-2: 9.83, ROUGE-L: 43.12.

**Validation**: The dataset was split into train/validation/test sets for evaluating model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: The dataset aims to include a range of movies but may not fully represent all cinematic styles or cultural contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
