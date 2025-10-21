# CAPTex (Culturally-Aware Procedural Texts)

## 📊 Benchmark Details

**Name**: CAPTex (Culturally-Aware Procedural Texts)

**Overview**: CAPTex is a benchmark designed to evaluate mLLMs’ ability to process and reason about culturally diverse procedural texts across multiple languages.

**Data Type**: procedural text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Japanese
- Persian
- Hindi
- Indonesian
- Urdu
- Hausa

**Resources**:
- [Resource](https://huggingface.co/datasets/AmirHossein2002/CAPTex)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate multilingual language models’ (mLLMs) ability to reason across culturally specific procedural texts.

**Target Audience**:
- ML Researchers
- Developers of multilingual models

**Tasks**:
- Step Reordering
- Procedure-Based Multiple-Choice Questions
- Conversation-Based Multiple-Choice Questions
- Conversation-Based Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Human-written procedures by native speakers from culturally distinct regions.

**Size**: 1,400 textual procedures

**Format**: text

**Annotation**: Manual creation and translation by native speakers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Spearman's Rank Correlation
- Levenshtein distance
- Kendall's Tau Rank Correlation
- ROUGE-L
- BERTScore

**Calculation**: Metrics are calculated based on model predictions against the correct answers provided in the dataset.

**Interpretation**: Higher values indicate better performance across all tasks except for Levenshtein distance, where lower values are better.

**Baseline Results**: CAPTex has been evaluated on 31 multilingual language models.

**Validation**: Tasks have been validated through automated checks and human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes diverse language representations but is limited to seven cultures due to resource constraints.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
