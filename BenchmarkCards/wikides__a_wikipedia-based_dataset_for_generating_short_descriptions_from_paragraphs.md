# WikiDes: A Wikipedia-Based Dataset for Generating Short Descriptions from Paragraphs

## 📊 Benchmark Details

**Name**: WikiDes: A Wikipedia-Based Dataset for Generating Short Descriptions from Paragraphs

**Overview**: In this paper, we introduce WikiDes, a novel dataset to generate short descriptions of Wikipedia articles for the problem of text summarization. The dataset consists of over 80k English samples on 6987 topics. WikiDes is a monolingual dataset that uses Wikipedia's first paragraphs as input and Wikidata short descriptions as output to train models for description generation and candidate ranking.

**Data Type**: text (Wikipedia first-paragraph to Wikidata short-description pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Descartes
- XSum
- WikiSum
- WikiHow
- CNNDM (CNN/DailyMail)
- arXiv
- PubMed
- Multi-News

**Resources**:
- [GitHub Repository](https://github.com/declare-lab/WikiDes)
- [Resource](https://arxiv.org/abs/2209.13101)
- [Resource](https://www.wikidata.org/w/api.php)
- [Resource](https://en.wikipedia.org/w/api.php)

## 🎯 Purpose and Intended Users

**Goal**: To construct WikiDes, a dataset for generating short Wikidata-style descriptions from Wikipedia first paragraphs, and to provide a benchmark for two-phase summarization (description generation and candidate ranking) and sentiment-correlation analysis.

**Target Audience**:
- Researchers in Natural Language Processing
- Model Developers
- Researchers working on Wikipedia/Wikidata summarization

**Tasks**:
- Text Summarization (short description generation)
- Candidate Ranking (ranking generated candidate descriptions)
- Sentiment Analysis (distribution comparison / sentiment correlation)

**Limitations**: Monolingual (English) dataset limited to generating short descriptions from Wikipedia first paragraphs; generated descriptions may contain repetitive text and incorrect factual information as noted in the paper; dataset reflects neutrality bias of Wikimedia content (many neutral examples).

## 💾 Data

**Source**: Extracted from English Wikipedia and Wikidata via their public APIs (https://en.wikipedia.org/w/api.php and https://www.wikidata.org/w/api.php).

**Size**: 81,418 examples on 6,987 topics

**Format**: JSON

**Annotation**: Automatically extracted: gold target descriptions are taken from Wikidata short descriptions (no additional manual annotation reported).

## 🔬 Methodology

**Methods**:
- Transfer learning from pre-trained sequence-to-sequence models (T5, BART)
- Two-phase summarization: Phase I description generation and Phase II candidate ranking
- Contrastive learning (margin ranking loss) for ranking models
- Beam search / diverse beam decoding to generate candidate sets
- Human evaluation (pairwise choice and 4-criteria ratings)
- Kolmogorov-Smirnov test for sentiment distribution comparison

**Metrics**:
- ROUGE-1 (F-measure and precision)
- ROUGE-2 (F-measure and precision)
- ROUGE-L (F-measure and precision)
- BertScore
- METEOR
- BLEU
- Cosine similarity (BERT embeddings)
- Harmonic mean fusion of ROUGE and Cosine similarity
- Kolmogorov-Smirnov test (K-S statistic)

**Calculation**: ROUGE-N-precision computed as the number of overlapping n-grams between descriptions and paragraphs divided by the number of n-grams in descriptions. Cosine similarity computed as Cosine(BERT(Y), BERT(X)) using BERT last-hidden-layer embeddings. Fusion score computed as harmonic mean HM = 2 * ROUGE * Cosine / (ROUGE + Cosine). Description generation training used cross-entropy (negative log-likelihood) loss. Ranking used a margin ranking loss: Lranking = Lgold + Lcandidate with gold and candidate margins (details and formulas provided in paper). Validation loss for ranking Lval computed as 1 - average f(˜Yb, ˆYi) over validation examples.

**Interpretation**: Higher ROUGE/BertScore/METEOR/BLEU indicate closer match to gold descriptions; fused metric (ROUGE + Cosine via harmonic mean) used to rank candidates balances lexical and semantic similarity. Ranking models that increase these metric values are interpreted as producing higher-quality descriptions. Human selection rates (e.g., Phase II selected descriptions chosen 45.33% vs Phase I 23.66% against gold) are used as additional quality evidence.

**Baseline Results**: Phase I (generation) highlights: T5-small (topic-exclusive test) R-1 46.49, R-2 26.20, R-L 45.59 (Table 5); BART-base (topic-independent test) R-1 69.59, R-2 54.59, R-L 69.12 (Table 5). Baseline (first instance) topic-exclusive test R-1 36.25, R-2 16.91, R-L 35.73; topic-independent test R-1 20.99, R-2 8.42, R-L 20.77. Phase II (ranking) best results: BART-base-beam + BERT + R-1-F (topic-independent test) R-1 67.79, R-2 54.41, R-L 67.35 (Table 9); T5-small-beam + BERT + R-1-F (topic-exclusive test) R-1 44.48, R-2 27.11, R-L 43.29 (Table 9). Human evaluation: Phase II selected descriptions chosen 45.33% vs Phase I generated chosen 23.66% when compared against gold descriptions.

**Validation**: Data split: training (~80%), validation (~10%), test (~10%) with two split strategies: topic-exclusive (train on popular topics, test on other topics) and topic-independent (random split). Models saved based on best metric values on validation sets using Seq2SeqTrainer. Phase II ranking training used new subsets: training 6000 samples, validation 1000, test 1000. Human evaluation conducted on 100 random samples (50 from each split).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
