# The BigScience ROOTS Corpus: A 1.6TB Composite Multilingual Dataset

## 📊 Benchmark Details

**Name**: The BigScience ROOTS Corpus: A 1.6TB Composite Multilingual Dataset

**Overview**: A 1.6TB dataset spanning 59 languages assembled by BigScience (Responsible Open-science Open-collaboration Text Sources (ROOTS)). The paper documents data creation and curation efforts, releases a large initial subset of the corpus and the processing tools used to curate, source, clean and inspect the 498 constituent datasets, and was used to train the BigScience BLOOM model.

**Data Type**: text (multilingual natural language text and programming language source code)

**Domains**:
- Natural Language Processing
- Programming Languages (code modeling)

**Languages**:
- Akan
- Arabic
- Assamese
- Bambara
- Basque
- Bengali
- Catalan
- Chewa
- Shona
- Tumbuka
- English
- Fon
- French
- Gujarati
- Hindi
- Igbo
- Indonesian
- Isi Zulu
- Kannada
- Kikuyu
- Kinyarwanda
- Kirundi
- Lingala
- Luganda
- Malayalam
- Marathi
- Nepali
- Northern Sotho
- Odia
- Portuguese
- Punjabi
- Sesotho
- Setswana
- Simplified Chinese
- Spanish
- Swahili
- Tamil
- Telugu
- Traditional Chinese
- Twi
- Urdu
- Vietnamese
- Wolof
- Xhosa
- Xitsonga
- Yoruba

**Similar Benchmarks**:
- The Pile
- C4
- mC4
- CC100
- OSCAR

**Resources**:
- [Resource](https://bigscience.huggingface.co/)
- [Resource](https://hf.co/spaces/bigscience/ethical-charter)
- [Resource](https://hf.co/bigscience-data)
- [GitHub Repository](https://github.com/bigscience-workshop/data-preparation)
- [Resource](https://hf.co/bigscience-catalogue-data)
- [Resource](https://commoncrawl.org/)
- [Resource](https://hf.co/spaces/bigscience-data/corpus-map)
- [Resource](https://hf.co/spaces/bigscience-data/document-sizes)
- [Resource](https://hf.co/spaces/bigscience-catalogue-lm-data/filter_values_distributions)
- [Resource](https://hf.co/spaces/huggingface/text-data-filtering)

## 🎯 Purpose and Intended Users

**Goal**: To assemble and document a 1.6TB multilingual corpus (ROOTS) to support large-scale multilingual language model training, to release a large initial subset and the tooling used for curation and processing, and to stimulate research on large multilingual corpora.

**Target Audience**:
- ML Researchers
- Model Developers
- Multilingual NLP communities
- Domain Experts

**Tasks**:
- Language Modeling (pre-training)
- Multilingual Modeling
- Code Modeling

**Limitations**: Use of Common Crawl introduces privacy and consent limitations; PII filtering is not exhaustive; reliance on medium to large digitized sources over-represents privileged voices and language varieties.

**Out of Scope Uses**:
- Public release is preliminary and gated: access to a large initial subset is subject to committing to the BigScience ethical charter (i.e., unrestricted public release without adherence to the charter is not how the authors describe the initial release).

## 💾 Data

**Source**: Aggregate of 498 constituent datasets: community-selected and documented language data sources collected via the BigScience Catalogue and Masader (62% of bytes), pseudo-crawled website data retrieved from Common Crawl/OSCAR v21.09 (38% of bytes), and code data from GitHub and StackExchange.

**Size**: 1.6TB (total aggregated corpus)

**Format**: JSON documents with two fields: "text" (text content) and "meta" (JSON metadata to trace documents back to original sources)

**Annotation**: Semi-automated with human verification: automated cleaning/filtering pipelines combined with native-speaker review to set filter thresholds and validate processing steps

## 🔬 Methodology

**Methods**:
- Automated cleaning and filtering pipeline (document-scoped and dataset-scoped functions)
- Human-in-the-loop curation (native speakers used a visualization tool to set filter thresholds)
- Pseudo-crawl extraction from Common Crawl WARC snapshots
- Deduplication using SimHash (6-grams) and substring deduplication via Suffix Array; MinHash and LSH for code duplicates
- PII redaction via rule-based regular expressions
- Tokenizer analysis (tokens-per-byte) and statistical analyses

**Metrics**:
- Dataset size (bytes)
- Percentage of documents removed by filters (per language)
- Tokens per byte (tokens-per-byte)
- Median document size (bytes)
- Percentage of duplicated data (bytes)

**Calculation**: Tokens-per-byte computed using tokenizers trained on corpora (e.g., BLOOM tokenizer); percentage removed computed per-language based on filter cutoffs established by native speakers; deduplication measured via SimHash Hamming-distance clusters and substring-suffix-array based deduplication; PII redaction via regex matching for KEY, EMAIL, USER, IP_ADDRESS.

**Interpretation**: Lower tokens-per-byte indicates greater similarity to the compared training corpus; percentage removed indicates amount of noisy or filtered content per language; deduplication percentages indicate fraction of data in bytes considered duplicated; median document size (1,129 bytes) indicates typical document length in the corpus.

**Validation**: Validation included native-speaker review using an interactive visualization tool to set filter thresholds, manual inspection and iterative pipeline refinement, syntax checking for sampled code files (Python and PHP), and reporting of filter removal percentages and deduplication statistics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Governance
- Legal Compliance
- Intellectual Property
- Accuracy
- Transparency
- Societal Impact
- Value Alignment

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Governance**: Incomplete usage definition, Lack of data transparency
- **Legal Compliance**: Model usage rights restrictions
- **Intellectual Property**: Data usage rights restrictions
- **Accuracy**: Unrepresentative data
- **Transparency**: Lack of training data transparency
- **Societal Impact**: Impact on affected communities, Impact on cultural diversity
- **Value Alignment**: Toxic output

**Demographic Analysis**: The paper provides language-level and macroarea breakdowns (byte distribution by language family and per-language document size distributions) and interactive dataset exploration tools; it does not provide demographic group analyses beyond language and language-family breakdowns.

**Potential Harm**: ['Privacy harms from personally identifiable information in web-crawled data', 'Bias and over-representation of privileged voices and language varieties', 'Exposure to pornographic and spam content in crawled data leading to offensive or harmful model outputs', 'Potential for models to memorize and reveal sensitive data (addressed via deduplication and PII redaction efforts)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: PII handling: rule-based regex redaction of KEY (numeric & alphanumeric identifiers), EMAIL, USER (social media handles), and IP_ADDRESS; the paper notes this approach is not exhaustive and that full PII removal is limited by scale and limitations of crawled data.

**Data Licensing**: Release strategy and data licensing are informed by the licensing and governance needs of each data source; no single corpus-wide license is specified in the paper and some tooling/processing encountered license-related issues (e.g., a preprocessing bug that filtered code for GPL licenses only).

**Consent Procedures**: No systematic consent was obtained for web-scraped content; the paper explicitly notes the difficulty of identifying individual contributors and obtaining consent for Common Crawl-derived data and discusses these limitations.

**Compliance With Regulations**: The paper discusses the multi-jurisdiction legal context and the uncertain legal status of web-scraped datasets (e.g., fair use not recognized in all jurisdictions) and describes creation of a framework to inform rights and responsibilities but does not claim full compliance with any specific regulation.
