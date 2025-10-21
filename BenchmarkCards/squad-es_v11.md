# SQuAD-es v1.1

## 📊 Benchmark Details

**Name**: SQuAD-es v1.1

**Overview**: We develop the Translate-Align-Retrieve (TAR) method to automatically translate the Stanford Question Answering Dataset (SQuAD) v1.1 to Spanish, producing SQuAD-es v1.1 as a large-scale Spanish QA training resource and using it to train Spanish QA systems.

**Data Type**: question-answering pairs (extractive QA: context, question, answer spans)

**Domains**:
- Natural Language Processing

**Languages**:
- Spanish

**Similar Benchmarks**:
- SQuAD v1.1
- MLQA
- XQuAD

**Resources**:
- [GitHub Repository](https://github.com/ccasimiro88/TranslateAlignRetrieve)
- [Resource](https://arxiv.org/abs/1912.05200)

## 🎯 Purpose and Intended Users

**Goal**: Automatically translate the SQuAD v1.1 training dataset to Spanish using the TAR method and provide SQuAD-es v1.1 as a large-scale Spanish training resource for question answering.

**Target Audience**:
- Researchers in Multilingual Question Answering
- Model Developers training Spanish QA systems

**Tasks**:
- Question Answering
- Machine Reading Comprehension (Extractive)

**Limitations**: Noise introduced by the NMT and alignment components that produces misaligned or overlapping answer spans; SQuAD-es v1.1 is larger but noisier while SQuAD-es-small is smaller but more accurate.

## 💾 Data

**Source**: Automatically translated from the Stanford Question Answering Dataset (SQuAD) v1.1 using the Translate-Align-Retrieve (TAR) method; NMT training data collected from WikiMatrix and OPUS resources (Wikipedia, TED-2013, News-Commentary, Tatoeba, OpenSubTitles).

**Size**: SQuAD-es v1.1: 87,595 examples (out of 87,599 original); SQuAD-es-small v1.1: 46,260 examples (≈53% of original).

**Format**: N/A

**Annotation**: Automatically generated via machine translation (NMT) and unsupervised word alignment with post-processing heuristics (Translate-Align-Retrieve); no manual re-annotation reported for the full dataset (manual error analysis performed on sampled articles).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (fine-tuning Multilingual-BERT)
- Manual qualitative error analysis

**Metrics**:
- F1 Score
- Exact Match (EM)
- BLEU Score

**Calculation**: F1 and Exact Match computed using the official evaluation script available in the MLQA repository (a multilingual generalization of the SQuAD evaluation script). BLEU score computed on the NMT test set for NMT evaluation.

**Interpretation**: Higher F1 and Exact Match indicate better QA performance; models trained on SQuAD-es v1.1 achieved state-of-the-art results on Spanish portions of MLQA and XQuAD, and a larger but noisier SQuAD-es v1.1 improved performance compared to a smaller, cleaner SQuAD-es-small.

**Baseline Results**: MLQA: TAR-train + mBERT (SQuAD-es) 68.1 F1 / 48.3 EM; TAR-train + mBERT (SQuAD-es-small) 65.5 F1 / 47.2 EM; MLQA mBERT baseline 64.3 F1 / 46.6 EM; Translate-train + mBERT 53.9 F1 / 37.4 EM; XLM (MLM+TLM) 68.0 F1 / 49.8 EM. XQuAD: TAR-train + mBERT (SQuAD-es) 77.6 F1 / 61.8 EM; TAR-train + mBERT (SQuAD-es-small) 73.8 F1 / 59.5 EM; JointMulti 32k voc 59.5 F1 / 41.3 EM; JointMulti 200k voc (state-of-the-art) 74.3 F1 / 55.3 EM; JointPair variants 68.3/47.8 and 72.5/52.5 (F1/EM).

**Validation**: Evaluation on MLQA and XQuAD Spanish corpora; manual qualitative error analysis on a randomly selected article to characterize error types (Type I misaligned spans, Type II overlapping spans); comparison between full SQuAD-es and SQuAD-es-small to assess impact of noisy examples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
