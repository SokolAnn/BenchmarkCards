# XGLUE

## 📊 Benchmark Details

**Name**: XGLUE

**Overview**: A new benchmark dataset that can be used to train large-scale cross-lingual pre-trained models using multilingual and bilingual corpora and evaluate their performance across a diverse set of cross-lingual tasks. XGLUE provides 11 diversified tasks covering both natural language understanding and generation, and for each task it provides labeled data in multiple languages.

**Data Type**: text (multilingual; includes single-input text and paired text: question-answer pairs, passage-question pairs, news body-title pairs, query-ad pairs, query-webpage pairs)

**Domains**:
- Natural Language Processing
- Information Retrieval
- Advertising
- News

**Languages**:
- Arabic
- Bulgarian
- German
- Greek
- English
- Spanish
- French
- Hindi
- Italian
- Dutch
- Polish
- Portuguese
- Russian
- Swahili
- Thai
- Turkish
- Urdu
- Vietnamese
- Chinese

**Similar Benchmarks**:
- GLUE
- XTREME
- XNLI
- MLQA
- PAWS-X
- CoNLL NER
- Universal Dependencies (POS Tagging)

**Resources**:
- [Resource](https://microsoft.github.io/XGLUE/)
- [Resource](https://arxiv.org/abs/2004.01401)
- [Resource](https://commoncrawl.org/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a multilingual benchmark for training and evaluating cross-lingual pre-trained models: (i) to train large-scale cross-lingual pre-trained models using multilingual and bilingual corpora, and (ii) to evaluate generalization capabilities of cross-lingual pre-trained models across a diverse set of cross-lingual tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Named Entity Recognition
- Part-of-Speech Tagging
- Text Classification (News Classification)
- Question Answering (MLQA)
- Natural Language Inference (XNLI)
- Paraphrase Identification (PAWS-X)
- Ad Relevance Classification (Query-Ad Matching)
- Document/Web Page Ranking
- Question-Answer Pair Classification
- Question Generation
- News Title Generation

**Limitations**: For each task, training set is only available in English.

## 💾 Data

**Source**: Pre-training corpora: Small Corpus (Wikipedia raw sentences via WikiExtractor; bilingual sentence pairs extracted from the Web using an in-house pipeline) and Large Corpus (cleaned Common Crawl following Wenzek et al. (2019) plus the Small Corpus). Downstream task data: a mix of existing multilingual datasets (CoNLL-2002/2003 NER, Universal Dependencies v2.5 for POS, MLQA, XNLI, PAWS-X) and six new datasets constructed by this paper from commercial sources (commercial news website and commercial search engine) for Search/Ads/News scenarios.

**Size**: Pre-training: Small Corpus multilingual 101G (100 languages); Small Corpus bilingual 146G (27 languages). Large Corpus multilingual 2,500G (covering 89 languages) plus the 101G multilingual; Large Corpus bilingual 146G (27 languages). Downstream (training set sizes as reported): NER 15.0K examples; POS 25.4K examples; NC 100K examples; MLQA 87.6K examples; XNLI 433K examples; PAWS-X 49.4K examples; QADSM 100K examples; WPR 100K examples; QAM 100K examples; QG 100K examples; NTG 300K examples.

**Format**: N/A

**Annotation**: Combination of existing labeled datasets and human annotation. The paper states that the six new tasks constructed by this paper are labeled by human, except the Spanish, Italian and Portuguese datasets in QG which were obtained by an in-house QA ranker (reported ~80+% accuracy). Existing tasks reuse annotations from CoNLL NER, UD treebanks, MLQA, XNLI and PAWS-X.

## 🔬 Methodology

**Methods**:
- Automated metrics (task-specific) evaluated after fine-tuning
- Model-based evaluation via fine-tuning pre-trained models on English training sets and applying to multilingual test sets
- Fine-tuning strategies: pivot-language (English) fine-tuning, multi-language fine-tuning, multi-task fine-tuning
- Ablation studies (e.g., pre-training task variants and text noising strategies)

**Metrics**:
- F1 Score
- Accuracy
- Normalized Discounted Cumulative Gain (nDCG)
- BLEU-4
- ROUGE-L

**Calculation**: Models are fine-tuned on English training sets (pivot-language) and evaluated on dev/test sets in multiple languages. After each epoch, models are tested on dev sets of all languages and the model with the best average result on the dev sets of all languages is selected. Average scores across tasks/languages (e.g., AVG_U for understanding tasks, AVG_G for generation tasks) are reported.

**Interpretation**: Average scores across languages and tasks are used to compare cross-lingual transfer performance. The paper reports AVG_U (average on 9 understanding tasks) and AVG_G (average on 2 generation tasks) as summary measures. Higher average scores indicate better cross-lingual generalization. (No explicit numeric thresholds for good vs. poor performance are provided.)

**Baseline Results**: Reported averages in the paper (12-layer base models): Understanding average (AVG_U): M-BERT 72.6, XLM-R base 75.8, Unicoder LC 76.2. Generation average (AVG_G): M-BERT 1.8, XLM-R base 1.5, UnicoderxDAE_SC 9.6, UnicoderxFNP_SC 10.7. Per-task detailed results are provided in Table 4 of the paper.

**Validation**: Validation is performed by evaluating fine-tuned models on dev sets of all languages after each epoch and selecting the model with the best average dev performance across languages. Additional validation via ablation studies (pivot-language vs. multi-language vs. multi-task fine-tuning; text noising strategies) is reported.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
