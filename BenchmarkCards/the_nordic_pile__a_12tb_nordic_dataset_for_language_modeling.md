# The Nordic Pile: A 1.2TB Nordic Dataset for Language Modeling

## 📊 Benchmark Details

**Name**: The Nordic Pile: A 1.2TB Nordic Dataset for Language Modeling

**Overview**: To facilitate the development of LLMs in the Nordic languages, we curate a high-quality dataset consisting of 1.2TB of text in the major North Germanic languages (Danish, Icelandic, Norwegian, and Swedish), as well as some high-quality English data. The paper details considerations and processes for collecting, cleaning, and filtering the dataset.

**Data Type**: text (cleaned and deduplicated multilingual text documents for language modeling; stored in JSON Lines format)

**Domains**:
- Natural Language Processing

**Languages**:
- Danish
- English
- Icelandic
- Norwegian
- Swedish

**Similar Benchmarks**:
- The Pile
- C4
- mC4
- OSCAR
- ROOTS
- MassiveText
- CCNet

**Resources**:
- [GitHub Repository](https://github.com/SeverineVerlinden/data_analysis_base_pile)
- [GitHub Repository](https://github.com/JoeyOhman/Megatron-deduplication)
- [Resource](https://huggingface.co/bigscience/bloom)

## 🎯 Purpose and Intended Users

**Goal**: Create a large, high-quality Nordic multilingual dataset (1.2TB) to enable training of state-of-the-art Nordic large language models.

**Target Audience**:
- Model developers
- ML researchers working on Large Language Models for Nordic languages

**Tasks**:
- Language Modeling
- Pre-training of Large Language Models

**Limitations**: The processed dataset cannot be distributed due to current European legislation; deduplication was constrained by available memory (machines with at most 256GB RAM) which required sharding and may affect completeness of deduplication; filter parameters were fixed for simplicity and not fully specialized per language.

## 💾 Data

**Source**: Composite of multiple existing sources and some scraped/curated sources: Common Crawl derivatives (e.g., OSCAR, mC4, Web CC), The Pile subsets (ArXiv, PubMed, Books S3, Open Web Text, Stack Exchange), Wikipedia dumps, OPUS parallel data, Pushshift Reddit data, generated mathematics datasets, Code Parrot GitHub code corpora (Bash, JavaScript, Python, SQL), various web scrapes and other curated sources listed in Appendix C.

**Size**: Final: 1,208.7 GB (1.2TB) of training data (659.48 million final documents). Collected before processing: 1,500.41 GB (1.5TB).

**Format**: JSON Lines (document-level JSON Lines format with metadata)

**Annotation**: Automatically generated document-level metadata: language identified using fastText; num_chars; num_utf8bytes; num_words; num_sents; md5 (128-bit MD5 hash as hexadecimal string).

## 🔬 Methodology

**Methods**:
- Normalization (non-printing character removal, whitespace normalization, Unicode NFC normalization)
- Document-level metric computation (language via fastText, character/word/sentence counts, MD5)
- Quality filtering using 16 filters (e.g., Alpha Present, Blacklist URLs, Digit Fraction, Document Length, Repetitive Gopher/BSP, Stop Word, Supported Language, etc.)
- Exact deduplication using MD5 hashes
- Language segmentation (separate subsets per language)
- Fuzzy deduplication using MinHash LSH (with sharding: intra-shard and inter-shard approaches)
- Merging of shards and duplicate groups

**Metrics**:
- Document-level metrics: language (fastText), number of characters (num_chars), number of UTF-8 bytes (num_utf8bytes), number of words (num_words), number of sentences (num_sents), MD5 hash
- Dataset-level statistics: total size in GB, per-language and per-category sizes and fractions, data removed per filter (GB), distribution of fuzzy duplicate group sizes

**Calculation**: Language identification performed using fastText; MD5 computed as 128-bit hex string; document counts and size statistics computed after normalization and filtering. MinHash LSH used for fuzzy deduplication with p=10 hash functions, 10-character shingling, b=2 bands, Jaccard similarity threshold 0.5. Exact deduplication used MD5 hash set lookup.

**Interpretation**: The pipeline reduced the collected data from 1.5TB to 1.2TB (approximately 300GB or ~20% removed). Quality filtering and fuzzy deduplication were the most prominent removal steps. The resulting dataset is intended to be sufficiently large and diverse to train multi-billion parameter LLMs in Nordic languages.

**Validation**: Validation comprised quantitative and qualitative evaluation of filter thresholds, analysis and visualization of data removed by each filter, distribution over duplicate group sizes, and per-language/category remaining data after pipeline steps. No model pre-training results or downstream evaluation provided in the paper.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Data Laws

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Privacy**: Personal information in data

**Demographic Analysis**: The paper provides language and category composition analysis with per-language sizes and fractions (Danish, English, Icelandic, Norwegian, Swedish) and highlights the difficulty of collecting data for low-resource Icelandic.

**Potential Harm**: ['Risk of model divergence and other problematic behaviors during LLM pre-training from low-quality documents (motivating aggressive quality filtering)', 'Risk of privacy breaches from personal information present in source text (sources likely to contain large amounts of personal information were excluded)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors state they made significant efforts to comply with GDPR and excluded sources known or likely to contain large amounts of personal information. They did not, however, filter potentially controversial text content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The authors explicitly considered GDPR compliance and state that current European legislation does not allow them to distribute or share the processed dataset.
