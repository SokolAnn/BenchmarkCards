# MTOB (Machine Translation from One Book)

## 📊 Benchmark Details

**Name**: MTOB (Machine Translation from One Book)

**Overview**: MTOB is a benchmark for learning to translate between English and Kalamang, a low-resource language with less than 200 speakers, using several hundred pages of field linguistics reference materials.

**Data Type**: sentence-level translation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Kalamang

**Resources**:
- [GitHub Repository](https://github.com/dictionaria/kalamang)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a testbed for language model capabilities and to expand access to language technology for underserved communities.

**Target Audience**:
- ML Researchers
- Language Technologists

**Tasks**:
- Machine Translation

**Limitations**: The task only tests sentence-level translation and may not be socially useful as it addresses translation between Kalamang and English, where all Kalamang speakers also speak Papuan Malay.

## 💾 Data

**Source**: Documentation of the Kalamang language collected during fieldwork.

**Size**: around 250,000 tokens in English and 25,000 tokens in Kalamang

**Format**: Plaintext and LaTeX

**Annotation**: Manual annotation based on linguistic fieldwork.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- chrF
- BLEU Score

**Calculation**: chrF measures character-level n-gram similarity between model outputs and reference translations.

**Interpretation**: Scores indicate the quality of translation, with higher scores being better.

**Baseline Results**: Human performance achieved chrF scores of 51.6 for Kalamang to English and 57.0 for English to Kalamang.

**Validation**: Test set was created from randomly sampled parallel sentences.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was constructed with community consent, and ethical considerations were taken into account.

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Informed consent was obtained from Kalamang community members for data use.

**Compliance With Regulations**: Not Applicable
