# Standardized Project Gutenberg Corpus (SPGC)

## 📊 Benchmark Details

**Name**: Standardized Project Gutenberg Corpus (SPGC)

**Overview**: A standardized, reproducible, curated version of the complete Project Gutenberg data containing more than 50,000 books and more than 3×10^9 word-tokens. The SPGC provides code to automatically download, filter, and process Project Gutenberg into three levels of granularity (raw text, a filtered timeseries of word tokens, and word-type counts), annotated metadata from Project Gutenberg records and bookshelf pages, and a time-stamped static 'frozen' snapshot (SPGC-2018-07-18).

**Data Type**: text (raw text files, timeseries of word tokens, and word-level count lists)

**Domains**:
- Corpus Linguistics
- Natural Language Processing
- Information Retrieval
- Quantitative Linguistics
- Computational Linguistics

**Languages**:
- English
- French
- Finnish
- German
- Dutch
- Italian
- Spanish
- Portuguese
- Greek
- Swedish
- Hungarian
- Esperanto
- Latin
- Danish
- Tagalog
- Catalan
- Polish
- Japanese
- Norwegian
- Welsh
- Czech
- Chinese

**Similar Benchmarks**:
- google-ngram data
- full Wikipedia dataset
- Twitter
- British National Corpus
- Corpus of Contemporary American English

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.2422560)
- [GitHub Repository](https://github.com/pgcorpus/gutenberg)
- [GitHub Repository](https://github.com/pgcorpus/gutenberg-analysis)
- [Resource](https://arxiv.org/abs/1812.08092)
- [GitHub Repository](https://github.com/c-w/gutenberg/blob/master/gutenberg/cleanup/strip_headers.py)

## 🎯 Purpose and Intended Users

**Goal**: Provide a reproducible, pre-processed, full-size version of Project Gutenberg as a scientific resource for corpus linguistics, natural language processing, and information retrieval by publishing the processing methodology, code, and the corpus at multiple granularities.

**Target Audience**:
- Corpus Linguists
- Natural Language Processing Researchers
- Information Retrieval Researchers
- Quantitative Linguists
- Computational Linguists
- Machine Learning Researchers

**Tasks**:
- Text Classification
- Topic Modeling
- Authorship Attribution
- Diachronic Language Analysis
- Machine Translation
- General corpus-based statistical analysis

**Limitations**: The corpus only contains copyright-free (public domain) books, resulting in comparatively few books published after the 1930s; metadata is incomplete for some books (e.g., exact publication year); some books may be duplicated under different Project Gutenberg identifiers; the composition of the corpus is heterogeneous across genres.

## 💾 Data

**Source**: Project Gutenberg (complete Project Gutenberg data), with metadata from Project Gutenberg records (uploader-provided metadata: author name, author birth/death years, language, subject categories, number of downloads) and bookshelf pages (collaborative tagging, 'bookshelf' labels).

**Size**: Frozen snapshot SPGC-2018-07-18: 55,905 books; corpus contains more than 3×10^9 word-tokens; full frozen dataset size: 65GB; one-gram counts size: 3.6GB.

**Format**: Plain text files (.txt) organized per book at four levels of granularity (raw, text, tokens, counts); counts provided as lists of (word, occurrence) tuples in text files.

**Annotation**: Metadata annotations from Project Gutenberg: author name, author year of birth and death, language, subject labels; bookshelf labels obtained from Project Gutenberg bookshelf pages (collaborative tagging).

## 🔬 Methodology

**Methods**:
- Automated preprocessing pipeline to download, filter, clean (remove headers/boilerplate), tokenize (NLTK TreebankWordTokenizer), lowercase and filter tokens, and count word types
- Use of rsync to mirror Project Gutenberg
- Jensen-Shannon divergence to measure distances between word-frequency distributions
- UMAP (Uniform Manifold Approximation and Projection) for 2D visualization of book similarity

**Metrics**:
- Jensen-Shannon divergence
- Token counts (number of word-tokens per book)

**Calculation**: Distance between books i and j (D_i,j) is computed as the Jensen-Shannon divergence between their word-frequency distributions; D_i,j = 0 indicates identical distributions and D_i,j = 1 indicates maximally different distributions (no shared words). Token counts are obtained by counting occurrences of each word-type.

**Interpretation**: Lower Jensen-Shannon divergence indicates more similar word-frequency statistics between books; higher values indicate greater dissimilarity. Examples in the paper show books from the same bookshelf or author have lower divergence and that average divergence increases with time separation.

**Validation**: A static time-stamped snapshot SPGC-2018-07-18 (55,905 books) is provided to ensure reproducibility of reported statistics and figures; the authors provide code and Jupyter notebooks to reproduce processing and analyses (UMAP embeddings, divergence analyses).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Reproducibility
- Data Quality
- Legal/Compliance
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Data contamination
- **Data Laws**: Data usage restrictions
- **Governance**: Lack of data transparency
- **Transparency**: Lack of training data transparency, Uncertain data provenance

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Collection primarily consists of copyright-free (public domain) literary works as archived by Project Gutenberg.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Discusses the impact of the Copyright Term Extension Act of 1998 on the availability of books (affecting which books enter the public domain); no other regulatory compliance procedures (e.g., GDPR) are discussed.
