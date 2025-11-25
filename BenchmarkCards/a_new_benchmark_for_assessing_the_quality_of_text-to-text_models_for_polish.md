# a new benchmark for assessing the quality of text-to-text models for Polish

## 📊 Benchmark Details

**Name**: a new benchmark for assessing the quality of text-to-text models for Polish

**Overview**: We introduce a new benchmark for assessing the quality of text-to-text models for Polish. The benchmark consists of diverse tasks and datasets: KLEJ benchmark adapted for text-to-text, en-pl translation, summarization, and question answering. In particular, since summarization and question answering lack benchmark datasets for the Polish language, we describe their construction and make them publicly available.

**Data Type**: text (question-answering pairs, text-summary pairs, parallel English-Polish sentence pairs, classification pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- Polish
- English

**Similar Benchmarks**:
- KLEJ
- MKQA
- WMT20

**Resources**:
- [Resource](https://hf.co/allegro)
- [Resource](https://hf.co/datasets/allegro/summarization-allegro-articles)
- [Resource](https://hf.co/datasets/allegro/polish-question-passage-pairs)
- [GitHub Repository](https://github.com/sdadas/polish-nlp-resources#bart)
- [Resource](https://hf.co/flax-community/papuGaPT2)
- [Resource](https://hf.co/allegro/plt5-base)
- [Resource](https://hf.co/datasets/polsum)
- [Resource](https://allegro.pl/artykuly)
- [GitHub Repository](https://github.com/google/sentencepiece)
- [GitHub Repository](https://github.com/google-research/text-to-text-transfer-transformer)

## 🎯 Purpose and Intended Users

**Goal**: Assess the quality of text-to-text models for Polish across multiple tasks: KLEJ (adapted to text-to-text), machine translation (en-pl), summarization, and question answering.

**Tasks**:
- Text Classification
- Machine Translation
- Summarization
- Question Answering

**Limitations**: We did not explore the possibility of optimizing prefixes and labels for the text-to-text KLEJ benchmark; thus, results reported in Table 3 need to be treated as the lower bound. Summarization dataset includes summaries of different lengths, which introduces additional ambiguity during evaluation. Source trimming due to model/memory limits means models did not see full source texts for some summarization and QA tasks.

## 💾 Data

**Source**: KLEJ benchmark (adapted to text-to-text); Allegro Articles (scraped from https://allegro.pl/artykuly) for summarization; Polish Summaries Corpus (PSC) for summarization; MKQA (manually translated subset) and MKQA-derived sources; Jeden z Dziesi˛ eciu question-answer pairs; Poleval 2021 question-answering dataset; WMT20 parallel corpora (EuroParl v10, TildeRapid, WikiTitles v2, ParaCrawl v5.1) for machine translation; additionally created Polish question-passage pairs via manual annotation and retrieval.

**Size**: Allegro Articles (AA) body2lead: 380,351 examples (train), 41,966 examples (dev), 104,514 examples (test). AA body+lead2title: 380,351 examples (train), 41,966 examples (dev), 104,514 examples (test). PSC whole: 512,201 examples (train), 57,180 examples (dev), 141,293 examples (test). PSC extract: 413,139 examples (train), 45,413 examples (dev), 112,880 examples (test). PSC abstract: 100,043 examples (train), 11,222 examples (dev), 27,976 examples (test). Polish question-passage pairs / QA resources: final combined training set 3,879 questions, test set 2,500 questions. (Numbers taken from Appendix A and main text.)

**Format**: N/A

**Annotation**: PSC summaries: created by human annotators (multiple extractive and abstractive summaries per article). MKQA: manual translations from English to Polish. Question-passage pairs: 10k manually annotated question-passage pairs indicating whether passage contains the correct answer. Other datasets: original annotations from source datasets preserved or filtered as described.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (fine-tuning and test runs)
- Statistical aggregation across multiple runs (medians)

**Metrics**:
- F1 Score
- Accuracy
- Spearman correlation
- Mean Absolute Error (MAE)-based score
- BLEU Score
- ROUGE-1
- ROUGE-2
- ROUGE-L

**Calculation**: KLEJ (text-to-text): generated label must exactly match target label (exact match). Summarization: arithmetic mean of ROUGE-1, ROUGE-2 and ROUGE-L f-measures reported. Machine Translation: BLEU score on WMT20 dev set, generation with beam search (5 beams), max sequence length 100. QA: Accuracy and F1 as reported; CDSC-R uses Spearman correlation; AR uses MAE-based score (Rybak et al., 2020). Reported model scores are medians across multiple runs (median of 7 runs for small and base architectures, median of 3 runs for large architectures unless noted otherwise).

**Interpretation**: Higher metric values indicate better performance. For KLEJ tasks an exact-match generation is considered correct. For summarization be cautious: the paper notes ROUGE is imperfect for abstractive summaries and reports baselines and human upper bounds to contextualize model scores. The authors state reported KLEJ results may be lower bounds because prefix/label optimization was not explored. Larger models and encoder-decoder architectures generally perform better except for summarization where plBART performed best.

**Baseline Results**: Summarization baselines: copying n=3 leading sentences and adaptive lead baseline (copy n leading sentences matching target length). Upper bound (human performance) computed for PSC via ROUGE between different human summaries. Models were typically 2-3pp above adaptive baseline on many summarization tasks; detailed baseline numbers are reported in Table 4 and Appendix C.

**Validation**: Used validation splits from original datasets for hyperparameter tuning and learning rate selection. Summarization splits created via stratified 80/20 train-test with 10% of train saved for validation. Learning rate tuning used validation sets; KLEJ tuning used tasks with validation sets. Results aggregated via median across multiple seeds/runs as specified.

## ⚠️ Targeted Risks

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
