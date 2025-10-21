# Wiktionary dataset

## 📊 Benchmark Details

**Name**: Wiktionary dataset

**Overview**: A dataset of 255k compound and non-compound words across 56 diverse languages obtained from Wiktionary, introduced to evaluate decompounding (compound segmentation and compound normalization) and to train and evaluate models (including a two-stage self-supervised + supervised procedure and CompoundPiece tokenizers).

**Data Type**: text (compound and non-compound words with normalized constituents)

**Domains**:
- Natural Language Processing

**Languages**:
- Afrikaans
- Azerbaijani
- Belarusian
- Bulgarian
- Bengali
- Catalan
- Czech
- Welsh
- Danish
- German
- Greek
- English
- Esperanto
- Spanish
- Estonian
- Basque
- Persian
- Finnish
- French
- Western Frisian
- Irish
- Galician
- Gujarati
- Hebrew
- Hindi
- Hungarian
- Armenian
- Indonesian
- Icelandic
- Italian
- Georgian
- Kazakh
- Kirghiz
- Latin
- Lithuanian
- Latvian
- Malagasy
- Macedonian
- Malayalam
- Maltese
- Dutch
- Panjabi
- Polish
- Portuguese
- Romanian
- Russian
- Slovak
- Albanian
- Swedish
- Tamil
- Telugu
- Thai
- Turkish
- Ukrainian
- Yiddish
- Yoruba

**Similar Benchmarks**:
- SIGMORPHON 2022 Shared Task
- AuCoPro
- GermaNet

**Resources**:
- [GitHub Repository](https://github.com/bminixhofer/compoundpiece)
- [Resource](https://arxiv.org/abs/2305.14214v2)
- [Resource](https://www.wiktionary.org/)

## 🎯 Purpose and Intended Users

**Goal**: Address the data gap for decompounding by introducing a dataset of 255k compound and non-compound words across 56 languages (from Wiktionary), use it to evaluate large language models on compound segmentation and normalization, and to develop improved decompounding methods (two-stage self-supervised + supervised models) and CompoundPiece tokenizers.

**Tasks**:
- Compound Segmentation
- Compound Normalization

**Limitations**: Stage 2 training is limited to languages with sufficient entries in Wiktionary: this excludes extremely low-resource languages. Furthermore, due to computational constraints we have not trained larger models using CompoundPiece tokenization; hence we are unable to report on its benefits at larger scales and on tasks besides decompounding.

## 💾 Data

**Source**: Primary dataset: words and normalized constituents extracted from Wiktionary (www.wiktionary.org). Stage 1 (self-supervised) training data: hyphenated and non-hyphenated words extracted from a subset of the mC4 corpus (~25M hyphenated words). Negative examples for the Wiktionary dataset are obtained by using normalized compound constituents as non-compound examples.

**Size**: 254,947 examples total (223,470 training examples: 164,713 positives and 58,757 negatives; 31,477 validation examples: 17,539 positives and 13,938 negatives).

**Format**: N/A

**Annotation**: Annotations (normalized constituents / compound labels) are taken from Wiktionary's compound term annotations; top-level splits are recursively split to smallest parts. Negative examples are collected by using normalized compound constituents as non-compound words.

## 🔬 Methodology

**Methods**:
- Automated metrics (averaged accuracy)
- Few-shot in-context evaluation of LLMs
- Baseline comparisons against prior unsupervised and language-specific decompounding tools
- Ablation studies

**Metrics**:
- Accuracy

**Calculation**: Averaged accuracy, i.e., the ratio of examples which are entirely correctly segmented or normalized.

**Interpretation**: Higher averaged accuracy indicates better segmentation/normalization performance. The paper highlights that performance is especially low on 'hard' compounds (compounds where subword token boundaries do not coincide with constituent boundaries), with LLMs performing close to zero (<3%) on hard compounds in some evaluations. Improvements are reported in absolute accuracy percentages (e.g., +13.9% for self-supervised models over prior unsupervised methods).

**Baseline Results**: The paper reports that their self-supervised Stage 1 models outperform the prior best unsupervised decompounding models by 13.9% accuracy on average. Their Stage 2 (supervised fine-tuned) models outperform prior language-specific decompounding tools. A model trained with a CompoundPiece tokenizer achieves a 5.5% improved performance on compound normalization over an otherwise equivalent SentencePiece model.

**Validation**: They include every language with at least 100 words. For evaluation, up to 1,000 words (but at most 50% of total words) per language were selected as evaluation data. Validation set sizes are reported in Table 7 (31,477 validation examples). They also evaluate on established datasets: GermaNet, AuCoPro (Dutch), and the compound-only subset from the SIGMORPHON 2022 Shared Task.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
