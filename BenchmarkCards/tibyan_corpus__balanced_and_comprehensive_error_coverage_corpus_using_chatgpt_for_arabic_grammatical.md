# Tibyan Corpus: Balanced and Comprehensive Error Coverage Corpus Using ChatGPT for Arabic Grammatical Error Correction

## 📊 Benchmark Details

**Name**: Tibyan Corpus: Balanced and Comprehensive Error Coverage Corpus Using ChatGPT for Arabic Grammatical Error Correction

**Overview**: This study aims to develop an Arabic corpus called 'Tibyan' for grammatical error correction using ChatGPT. The dataset includes pairs of sentences containing grammatical errors matched with error-free sentences. It addresses the limited resources available for Arabic grammatical error correction by augmenting data through ChatGPT.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a comprehensive resource for grammatical error correction in Arabic, utilizing common errors made by native speakers.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Grammatical Error Correction

**Limitations**: N/A

## 💾 Data

**Source**: Collected sentences from Arabic books and the A7'ta corpus, utilizing ChatGPT for generation.

**Size**: 600,000 tokens

**Format**: N/A

**Annotation**: Manual validation by linguistic experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BERTScore

**Calculation**: Precision, Recall, and F1 Score where relevant words in the generated text are compared to the target text.

**Interpretation**: Higher scores indicate better generation quality with respect to human-like grammatical accuracy.

**Baseline Results**: ChatGPT-generated corrected sentences resemble those produced by humans after annotation.

**Validation**: Validated through iterative feedback from linguistic experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
