# MusicUGC-NER (User-Generated Content Named Entity Recognition in Music)

## 📊 Benchmark Details

**Name**: MusicUGC-NER (User-Generated Content Named Entity Recognition in Music)

**Overview**: A novel dataset for named entity recognition (NER) of music entities in user-generated content, collected from platforms like Reddit and YouTube, and benchmarked using large language models (LLMs) in an in-context learning (ICL) setup.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/progsi/YTUnCoverLLM)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of this benchmark is to evaluate the performance of large language models (LLMs) for named entity recognition in the context of music entities found in user-generated content.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition

**Limitations**: The dataset focuses on western popular music and lacks broad representation of covers from other regions; gender diversity cannot be ensured based on available metadata.

## 💾 Data

**Source**: A union of datasets containing YouTube video titles and Reddit posts regarding music, specifically annotated for named entity recognition tasks.

**Size**: 609 annotated items

**Format**: JSON

**Annotation**: Manual annotation by experts with a high agreement (Cohen’s Kappa of 0.93).

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 scores calculated per entity class (Work of Art and Artist) and averaged for a macro score.

**Interpretation**: Higher F1 scores indicate better performance in identifying music entities.

**Baseline Results**: BERT and RoBERTa were used as strong baselines for comparison against the LLMs in the study.

**Validation**: Five-fold cross-validation was performed to validate the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack, Hallucination

**Demographic Analysis**: The dataset does not guarantee gender diversity.

**Potential Harm**: ['The benchmark aims to detect performance issues concerning unseen entities and typographical errors in user-generated content.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Publicly released under applicable licenses but specifics not stated.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
