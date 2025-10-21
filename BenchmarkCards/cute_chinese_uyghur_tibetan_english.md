# CUTE (Chinese, Uyghur, Tibetan, English)

## 📊 Benchmark Details

**Name**: CUTE (Chinese, Uyghur, Tibetan, English)

**Overview**: CUTE is a multilingual dataset constructed to enhance cross-lingual knowledge transfer in low-resource languages, consisting of parallel and non-parallel corpora for Mandarin Chinese, Uyghur, Tibetan, and English.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- Uyghur
- Tibetan
- English

**Resources**:
- [GitHub Repository](https://github.com/CMLI-NLP/CUTE)

## 🎯 Purpose and Intended Users

**Goal**: To advance research and development for Uyghur and Tibetan languages in large language models and validate the effectiveness of machine-translated low-resource data.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Language Model Developers

**Tasks**:
- Text Classification
- Question Answering
- Machine Translation
- Relation Extraction

**Limitations**: The dataset may contain errors due to machine translation, particularly in grammatically complex sentences.

## 💾 Data

**Source**: The CUTE dataset was constructed using machine translation from existing corpora, including data from the SkyPile-150B dataset.

**Size**: 50GB

**Format**: CSV

**Annotation**: Data is translated through machine translation models and assessed for quality by bilingual native speakers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Zero-shot evaluation
- Cross-lingual transfer evaluation

**Metrics**:
- F1 Score
- BLEU Score
- Accuracy

**Calculation**: Metrics were calculated based on classification tasks and reading comprehension evaluations comparing models trained on parallel and non-parallel datasets.

**Interpretation**: Higher scores indicate better performance in zero-shot transfer tasks across languages.

**Validation**: Validated through human assessments and zero-shot transfer capabilities across tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: The dataset includes speakers of Uyghur and Tibetan, aiming to enhance NLP capabilities for these communities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Measures were taken to filter sensitive information in the source data used for translation.

**Data Licensing**: Open-sourced for research purposes; specific licensing details are not provided.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The dataset ensures compliance with data privacy regulations applicable in its context.
