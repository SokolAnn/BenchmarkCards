# Is ‘Hope’ a Person or an Idea? A Pilot Benchmark for NER

## 📊 Benchmark Details

**Name**: Is ‘Hope’ a Person or an Idea? A Pilot Benchmark for NER

**Overview**: This pilot study presents a small-scale but carefully annotated benchmark of Named Entity Recognition (NER) performance across six systems: three non-LLM NLP tools (NLTK, spaCy, Stanza) and three general-purpose large language models (LLMs: Gemini-1.5-flash, DeepSeek-V3, Qwen-3-4B).

**Data Type**: token-level NER annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2509.12098)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate NER performance across traditional NLP tools and large language models on a small, ambiguity-rich dataset.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Named Entity Recognition

**Limitations**: The dataset is small (119 tokens) and genre-specific, limiting statistical power and generalizability.

## 💾 Data

**Source**: Manually selected and annotated sentences focusing on named entity recognition (NER) tasks.

**Size**: 119 tokens

**Format**: CSV

**Annotation**: Manual annotation by the author based on established NER conventions.

## 🔬 Methodology

**Methods**:
- Manual annotation
- Quantitative evaluation
- Visual and statistical comparison

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: F1-score was computed for each entity type individually and subsequently macro-averaged.

**Interpretation**: The F1-score is used as the primary evaluation metric due to its effectiveness in handling imbalanced datasets.

**Baseline Results**: Results show that Gemini achieved the highest average F1-score.

**Validation**: The performance of each system was evaluated against the human-annotated gold standard.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
