# PANDA – Paired Anti-hate Narratives Dataset from Asia: Using an LLM-as-a-Judge to Create the First Chinese Counterspeech Dataset

## 📊 Benchmark Details

**Name**: PANDA – Paired Anti-hate Narratives Dataset from Asia: Using an LLM-as-a-Judge to Create the First Chinese Counterspeech Dataset

**Overview**: This paper introduces a corpus of Modern Standard Mandarin counterspeech that targets hate speech in Mainland China, providing the first Chinese counterspeech dataset designed for combating hate speech online.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- COLD
- SWSR
- CHSD

**Resources**:
- [GitHub Repository](https://github.com/michaelbennieUFL/PANDA)

## 🎯 Purpose and Intended Users

**Goal**: To create a paired hate-speech–counterspeech corpus in Mandarin Chinese and assess the effectiveness of generated counterspeech in responding to hate speech.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Social Media Analysts

**Tasks**:
- Counterspeech Generation
- Hate Speech Detection

**Limitations**: The dataset is limited in scale and further data collection is needed to validate the pipeline.

## 💾 Data

**Source**: The data is sourced from open-source hate speech datasets, including COLD, SWSR, and CHSD.

**Size**: 12,000 HS–CS pairs

**Format**: JSON

**Annotation**: Manual annotation by trained annotators to identify hate speech and counterspeech.

## 🔬 Methodology

**Methods**:
- LLM-based evaluation
- Simulated annealing for response generation
- Human annotation

**Metrics**:
- JudgeLM
- BLEU
- ROUGE-L
- BERTScore

**Calculation**: Metrics are calculated based on token similarities, sentence structure, and human feedback.

**Interpretation**: Higher scoring indicates better relevance and effectiveness of counterspeech responses.

**Validation**: Validation through human annotation and LLM-based ranking processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data sourced from publicly available datasets; no personal or sensitive information was collected.

**Data Licensing**: The dataset is released under a GPL license, allowing for free usage.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
