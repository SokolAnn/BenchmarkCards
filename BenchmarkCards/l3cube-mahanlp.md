# L3Cube-MahaNLP

## 📊 Benchmark Details

**Name**: L3Cube-MahaNLP

**Overview**: With L3Cube-MahaNLP, we aim to build resources and a library for Marathi natural language processing. We present datasets and models for supervised tasks like sentiment analysis, named entity recognition, and hate speech detection. We have also published a monolingual Marathi corpus for unsupervised language modeling tasks. Overall we present MahaCorpus, MahaSent, MahaNER, and MahaHate datasets and their corresponding MahaBERT models fine-tuned on these datasets.

**Data Type**: text (monolingual corpus; tweet and sentence classification pairs; token-level NER annotations)

**Domains**:
- Natural Language Processing

**Languages**:
- Marathi

**Similar Benchmarks**:
- multilingual-BERT
- XLM-R
- IndicBERT
- inlpsuite

**Resources**:
- [GitHub Repository](https://github.com/l3cube-pune/MarathiNLP)
- [Resource](https://huggingface.co/l3cube-pune/marathi-bert)
- [Resource](https://huggingface.co/l3cube-pune/marathi-roberta)
- [Resource](https://huggingface.co/l3cube-pune/marathi-albert)
- [Resource](https://huggingface.co/l3cube-pune/marathi-albert-v2)
- [Resource](https://huggingface.co/l3cube-pune/marathi-gpt)
- [Resource](https://huggingface.co/l3cube-pune/MarathiSentiment)
- [Resource](https://huggingface.co/l3cube-pune/marathi-ner)
- [Resource](https://huggingface.co/l3cube-pune/mahahate-bert)
- [Resource](https://huggingface.co/l3cube-pune/mahahate-multi-roberta)

## 🎯 Purpose and Intended Users

**Goal**: To build resources and a dedicated library for Marathi natural language processing by releasing datasets (MahaCorpus, MahaSent, MahaNER, MahaHate) and pretrained/finetuned models (MahaBERT variants, MahaGPT, MahaFT) to enable downstream tasks such as sentiment analysis, named entity recognition, and hate speech detection.

**Tasks**:
- Sentiment Analysis
- Named Entity Recognition
- Hate Speech Detection
- Language Modeling (Next Token Prediction)
- Tokenization
- Word Embedding (Word Vectors)

**Limitations**: N/A

## 💾 Data

**Source**: MahaCorpus: scraped from the internet using news and non-news sources; MahaSent: Marathi tweets; MahaNER: manually tagged sentences; MahaHate: tweets curated from Twitter and manually annotated.

**Size**: MahaCorpus: 24.8M sentences and 289M tokens (752M tokens when combined with other publicly available resources); MahaSent: 12,114 train, 2,250 test, 1,500 validation examples; MahaNER: 25,000 manually tagged sentences (21,500 train, 2,000 test, 1,500 validation); MahaHate: over 25,000 distinct tweets (21,500 train, 2,000 test, 1,500 validation).

**Format**: N/A

**Annotation**: MahaCorpus: unlabeled monolingual corpus for unsupervised language modeling; MahaSent: labeled tweets for sentiment (positive/negative/neutral); MahaNER: manually annotated NER labels (eight entity classes) released in IOB and non-IOB notations; MahaHate: manually annotated tweets labeled as hate, offensive, profane, and not.

## 🔬 Methodology

**Methods**:
- Masked Language Modeling pretraining (used for MahaBERT variants)
- Causal Language Modeling pretraining (used for MahaGPT)
- Model fine-tuning of pretrained transformer models (BERT variants) on downstream datasets

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: Datasets provide train/test/validation splits as specified for each dataset (MahaSent, MahaNER, MahaHate).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
