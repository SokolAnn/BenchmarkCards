# Cross-lingual Question Answering Dataset (XQuAD)

## 📊 Benchmark Details

**Name**: Cross-lingual Question Answering Dataset (XQuAD)

**Overview**: A cross-lingual extractive question answering benchmark released by the authors, consisting of translated subsets of SQuAD v1.1 to evaluate cross-lingual generalization. The paper describes XQuAD as a more comprehensive cross-lingual benchmark, which comprises 240 paragraphs and 1,190 question-answer pairs from SQuAD v1.1 translated into ten languages by professional translators.

**Data Type**: question-answering pairs (extractive question answering)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- German
- Greek
- Russian
- Turkish
- Arabic
- Vietnamese
- Thai
- Chinese
- Hindi

**Similar Benchmarks**:
- SQuAD v1.1
- MLQA

**Resources**:
- [GitHub Repository](https://github.com/deepmind/xquad)
- [Resource](https://arxiv.org/abs/1910.11856)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more comprehensive cross-lingual benchmark for evaluating cross-lingual models on extractive question answering and to better understand cross-lingual generalization.

**Tasks**:
- Question Answering
- Extractive Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: A subset of the development set of SQuAD v1.1 (240 context paragraphs and their corresponding questions/answers) together with professional human translations into ten languages (Spanish, German, Greek, Russian, Turkish, Arabic, Vietnamese, Thai, Chinese, Hindi). Translations were done by professional translators via Gengo, with placeholders marking answer spans and translators instructed to keep these placeholders.

**Size**: 240 paragraphs and 1,190 question-answer pairs

**Format**: N/A

**Annotation**: Professional human translation (via Gengo) of context paragraphs and questions; the most frequent answer for each question was marked in the context with placeholder symbols and translators were instructed to keep the placeholders in the translations. Translators had access to an online validator to verify format; paragraphs/questions from the same document were submitted in the same batch to ensure consistency.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Zero-shot cross-lingual evaluation

**Metrics**:
- F1 Score
- Exact Match

**Calculation**: F1 and Exact Match scores are reported for XQuAD (Exact Match scores reported in Appendix C). The paper does not provide further detailed metric calculation procedures beyond reporting these metrics.

**Interpretation**: N/A

**Baseline Results**: Baseline results reported in the paper include (XQuAD, F1): mBERT average 65.0; JOINT MULTI (200k vocabulary) average 65.7; MONO_TRANS + adapters average 66.8.

**Validation**: Translations performed by professional translators via Gengo; translators instructed to keep placeholder symbols marking answer spans. Translators had access to an online validator to automatically verify output format. Paragraphs and questions from the same SQuAD document were submitted in the same batch to ensure translation consistency.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
