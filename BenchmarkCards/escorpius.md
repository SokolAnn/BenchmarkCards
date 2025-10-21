# ESCORPIUS

## 📊 Benchmark Details

**Name**: ESCORPIUS

**Overview**: ESCORPIUS is a Spanish crawling corpus obtained from near 1 PB of Common Crawl data. It is presented as the most extensive corpus in Spanish with a high-quality extraction, purification and deduplication pipeline, preserving document and paragraph boundaries and maintaining source web page URL and WARC shard origin for traceability and GDPR compliance.

**Data Type**: text (paragraph-level web crawl documents, JSONL)

**Domains**:
- Natural Language Processing

**Languages**:
- Spanish

**Similar Benchmarks**:
- OSCAR
- mC4
- CC-100
- ParaCrawl
- The Pile

**Resources**:
- [Resource](https://huggingface.co/datasets/LHF/escorpius)
- [Resource](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- [Resource](https://arxiv.org/abs/2206.15147)

## 🎯 Purpose and Intended Users

**Goal**: Provide a massive cleaned and deduplicated Spanish web crawl corpus that preserves document and paragraph boundaries, maintains traceability to original web sources, and offers high-quality data for training language models.

**Target Audience**:
- Natural Language Processing researchers
- Model developers
- NLP community / practitioners

**Tasks**:
- Language Modeling
- Pre-training of Language Models
- Natural Language Generation
- Embedding Training

**Limitations**: The authors prioritized quality over quantity, sacrificing corpus length and processing time for more certain Spanish language identification and cleaner data. The corpus is crawling-based only and the authors propose future work to extend it (e.g., create a The Pile-like Spanish corpus).

## 💾 Data

**Source**: Processed WARC files from Common Crawl (39,502 compressed WARC segments selected from Common Crawl for the period 2015-2022).

**Size**: Compressed information occupied about 180 TB; processed decompressed information estimated to be more than 0.8 PB; deduplicated and cleaned corpus size 346,262,072,705 bytes (322.5 GB). Corpus statistics: 104,073,706 total number of lines; 50,040,055,322 tokens; 1,125,798,968 paragraphs; 2,421,598,201 sentences. Uploaded to HuggingFace in 33 chunk files of 10 GB each.

**Format**: JSONL (one JSON document per line with fields: id (UUIDv4), text, url_warc, url)

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Parallel automated cleaning pipeline (PySpark / Apache Spark on EMR)
- Language detection: two-step process using Compact Language Detector 2 (CLD2) for quick filtering and fastText for verification
- Deduplication: dLHF pipeline with exact matching at document level, paragraph-level normalization deduplication, and Locality Sensitive Hashing adapted for parallel processing
- Parsing and UTF-8 encoding fixing from WARC files; preservation of document and paragraph boundaries

**Metrics**:
- Corpus size (bytes)
- Number of documents
- Number of words / tokens
- Number of lines
- Number of paragraphs
- Number of sentences
- Parsing quality
- Cleaning quality
- Deduplication

**Calculation**: Metrics reported as raw counts and sizes computed from the processed data after cleaning and deduplication. Deduplication performed via the dLHF pipeline (document exact matching, paragraph normalization, and Locality Sensitive Hashing). Language identification validated by CLD2 followed by fastText.

**Interpretation**: As argued by the authors, corpora for language modelling should be compared not only by size but also by quality and traceability; higher quality and traceability improve confidence in model proficiency and GDPR compliance.

**Baseline Results**: Comparison to state-of-the-art Spanish or Spanish-excerpt corpora (from Table 1): OSCAR (Spanish size 381.9 GB, 51M docs, 42,829M words), mC4 (Spanish size 1,600 GB, 416M docs, 433,000M words), CC-100 (Spanish size 53.3 GB, 9,374M words), ParaCrawl v9 (Spanish size 24.0 GB, 4,374M words), ESCORPIUS (deduplicated size 322.5 GB, 104M docs, 50,773M words).

**Validation**: Validation via a two-step language identification (CLD2 then fastText) to ensure Spanish language selection; deduplication validation discussed via dLHF process and comparison of resulting statistics; no human annotation validation reported.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy
- Legal Compliance
- Transparency

**Atlas Risks**:
- **Privacy**: Data privacy rights alignment, Personal information in data
- **Fairness**: Data bias
- **Accuracy**: Data contamination, Poor model accuracy, Unrepresentative data
- **Legal Compliance**: Model usage rights restrictions
- **Transparency**: Lack of training data transparency, Uncertain data provenance

**Potential Harm**: The paper states that low-quality data can have pernicious effects, reducing result quality and creating false impressions of language representation; preserving traceability enables exercising GDPR rights (e.g., right of withdrawal) for individuals whose data appear on websites.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The corpus maintains source web page URL and WARC shard origin to ensure traceability and to permit application of the right of withdrawal under GDPR. The authors state they do not perform URL-based content filtering and expect users to apply filtering if desired.

**Data Licensing**: Released under CC BY-NC-ND 4.0 license (Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The authors state the dataset maintains traceability (source URL and WARC shard origin) to comply with EU regulations such as GDPR and to allow the right to be forgotten.
