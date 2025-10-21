# naab

## 📊 Benchmark Details

**Name**: naab

**Overview**: naab is a publicly available, cleaned, ready-to-use Farsi textual corpus introduced to improve NLP for the Farsi language. The project provides two releases: naab (cleaned) and naab-raw (unprocessed), and includes a streaming-based pre-processing toolkit. The corpus comprises roughly 130GB of data (billions of words and hundreds of millions of paragraphs) and is hosted on Hugging Face for easy access.

**Data Type**: text (paragraphs / sequences)

**Domains**:
- Natural Language Processing
- Speech Processing

**Languages**:
- Farsi

**Similar Benchmarks**:
- Persian NLP
- OSCAR-fa
- AGP
- LSCP (Large Scale Colloquial Persian Language Understanding)
- Telegram corpus
- Persian Wikipedia
- Miras Text
- Common Crawl - fa
- Leipzig Corpora
- VOA corpus
- Persian poems corpus
- Tehran English-Persian parallel corpus (TEP)

**Resources**:
- [GitHub Repository](https://github.com/Sharif-SLPL/t5-fa/tree/main/preprocess)
- [Resource](https://huggingface.co/datasets/SLPL/naab-raw)
- [Resource](https://huggingface.co/datasets/SLPL/naab)
- [Resource](http://asr-gooyesh.com/en/)
- [Resource](https://commoncrawl.org/)
- [GitHub Repository](https://github.com/persiannlp/persian-raw-text)
- [GitHub Repository](https://github.com/miras-tech/MirasText)
- [GitHub Repository](https://github.com/amnghd/Persian_poems_corpus)
- [GitHub Repository](https://github.com/kharazi/persian-stopwords)
- [Resource](https://jon.dehdari.org/corpora/)
- [Resource](https://abadis.ir/fatofa/%D9%86%D8%A7%D8%A8/)

## 🎯 Purpose and Intended Users

**Goal**: Provide the largest publicly available, cleaned, ready-to-use Farsi textual corpus (naab) and an unprocessed version (naab-raw), along with a streaming-based pre-processing toolkit to facilitate Farsi NLP research and model training.

**Target Audience**:
- NLP Researchers
- Researchers and practitioners focusing on low-resource languages
- Model developers

**Tasks**:
- Language Modeling
- Pre-training / Fine-tuning Language Models
- Text Classification
- Named Entity Recognition
- Part-of-Speech Tagging
- Text Summarization
- Automatic Speech Recognition
- Text-to-Speech

**Limitations**: Stopwords were retained (not removed) to preserve contextual integrity; deduplication was not performed (possible duplicated content); potential presence of personal information despite filtering; slight possibility of corrupted sentences introduced by character filtering.

## 💾 Data

**Source**: Combined cleaned corpora including Persian NLP (aggregating Common Crawl - fa, MirasText, Web to Corpus, Persian Wikipedia, Leipzig Corpora, VOA corpus, Persian poems corpus, Tehran English-Persian Parallel Corpus), OSCAR-fa, AGP (from ASR Gooyesh Pardaz), LSCP (Farsi portion), and a curated Telegram corpus.

**Size**: Approximately 130GB total. Table 1 reports 129.2GB total consisting of 236,976,777 paragraphs and 14,957,936,489 words. The paper also states training: 126GB (>224 million sequences, ~15 billion words) and test: 2.3GB (~11 million sequences, ~300 million words).

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Streaming pre-processing pipeline for cleaning (chunk-based, O(1) memory in streaming fashion)
- Word frequency analysis (word counts and stopword-filtered counts) for corpus analysis

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: Random spot-checking of texts for corrupted sentences was performed and no instances were found in the checked samples. No deduplication was performed; no formal benchmarking validation reported beyond the described analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Misuse

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Data contamination, Poor model accuracy
- **Misuse**: Improper usage

**Potential Harm**: ['Potential presence of personal information in the dataset']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors applied filtering techniques including removal of numerical data that could represent sensitive information (phone numbers, addresses, social security numbers, credit cards) but acknowledge that some identifiable data may still exist and users must ensure ethical/legal compliance.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
