# Gutenberg Literary English Corpus (GLEC) and Gutenberg English Poetry Corpus (GEPC)

## 📊 Benchmark Details

**Name**: Gutenberg Literary English Corpus (GLEC) and Gutenberg English Poetry Corpus (GEPC)

**Overview**: The paper describes a corpus assembled from the Project Gutenberg digitized books augmented by a Shakespeare corpus (Gutenberg Literary English Corpus/GLEC) and a cleaned poetry subcorpus (Gutenberg English Poetry Corpus/GEPC). The GLEC contains over 3,000 English texts (~250 million words, ~12 million sentences). The GEPC comprises cleaned poetic texts (116 texts concatenated into 47 compound author texts) with ~1,808,160 words (tokens) and 41,857 types and is presented as particularly suited for research in Digital Humanities, Natural Language Processing or Neurocognitive Poetics, e.g. as training and test corpus or for stimulus development and control.

**Data Type**: text (literary texts and poetry collections)

**Domains**:
- Digital Humanities
- Natural Language Processing
- Neurocognitive Poetics
- Computational Linguistics

**Languages**:
- English

**Similar Benchmarks**:
- Project Gutenberg dataset
- Shakespeare corpus (shakespeare-online)
- a literary corpus of 35 French novels (Bornet and Kaplan, 2017)

**Resources**:
- [Resource](https://web.eecs.umich.edu/~lahiri/gutenberg_dataset.html)
- [Resource](http://www.shakespeare-online.com/sonnets/sonnetintroduction.html)
- [Resource](https://www.researchgate.net/project/Neurocognitive-Poetics)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large English literary corpus (GLEC) and a cleaned poetry subcorpus (GEPC) for use in Computational Linguistics, Digital Humanities and Neurocognitive Poetics, e.g. as training and test corpora, for stimulus development and control, and for Quantitative Narrative Analysis (QNA).

**Target Audience**:
- Computational Linguistics Researchers
- Digital Humanities Researchers
- Neurocognitive Poetics Researchers

**Tasks**:
- Language Modeling
- Topic Modeling
- Text Similarity
- Authorship Attribution
- Sentiment Analysis
- Feature Extraction
- Stimulus Development

**Limitations**: A limitation of the corpus lies in its texts being relatively 'old': due to copyright issues, the GLEC and GEPC contain only texts from 1623 to 1952, the majority of the GEPC stemming from the 19th century (Median = 1885). The GLEC requires further processing (e.g., cleaning, regrouping according to subgenres) before it can be used as a training and/or test corpus.

## 💾 Data

**Source**: Assembled from the digitized books part of Project Gutenberg (https://web.eecs.umich.edu/~lahiri/gutenberg_dataset.html) and augmented with a Shakespeare corpus (http://www.shakespeare-online.com/sonnets/sonnetintroduction.html); resulting corpora named Gutenberg Literary English Corpus (GLEC) and the cleaned subcorpus Gutenberg English Poetry Corpus (GEPC). The GEPC texts were cleaned (manual removal of duplicate poems, prefaces, introductions, indices, postscripts, author notes, footnotes, line/page numbers) and poems in languages other than English were removed. Poems by the same author were concatenated producing 47 compound author texts.

**Size**: GLEC: about 3,000 English texts; ~250 million words; ~12 million sentences. GEPC: described as over 100 poetic texts (116 texts cleaned), concatenated into 47 compound author texts; GEPC total: 1,808,160 words (tokens) and 41,857 types; median author text length ~23,000 words (paper gives per-author length distribution; top and bottom author word counts provided).

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Quantitative Narrative Analysis (QNA)
- Latent Semantic Analysis (document-term-matrix comparisons)
- Non-Negative Matrix Factorization (NMF) for topic extraction
- Document-Term Matrix using sklearn CountVectorizer
- Bayesian group (author) comparison using a Gibbs sampler
- Sentiment/affect computation via WordNet path-similarity
- n-gram/trigram language modeling (surprisal computation)
- Lexical and surface feature computations (type-token ratio, adjective-verb quotient, hapax counts, sonority score, word distinctiveness/keyness)

**Metrics**:
- Type-token ratio (lexical diversity)
- Number of tokens, types, hapaxes
- Adjective-Verb quotient
- Sonority score (mean per poem)
- Valence
- Arousal
- Topic probability distributions (per-author topic probabilities summing to 1)
- Trigram-based surprisal
- Word distinctiveness/keyness measures (unique words, difference-in-rate, Bayesian probability p(delta<0))

**Calculation**: DTM built with sklearn CountVectorizer (minimum term frequency = 1; maximum term frequency = 0.95; NLTK stopwords; SnowballStemmer). Topic extraction via Non-Negative Matrix Factorization producing 20 topics; topic probabilities per author sum to 1. Sonority score: words assigned values from a 10-rank sonority hierarchy of English graphemes, sum divided by grapheme count per word, global poem score is mean of word values. Valence and arousal: for each target word compute WordNet path-similarity to label words and average (procedure described; hit rates reported). Bayesian group comparison: Gibbs sampler (2000 samples reported in example) to estimate posterior distribution of delta for word frequency differences. Trigram probabilities computed from corpus n-gram model to derive surprisal.

**Interpretation**: Trigram probabilities (surprisal) are used as predictors of response measures in reading (e.g., reading time, brain wave amplitudes). Type-token ratio and adjective-verb quotient are described as indicators of linguistic complexity, poetic quality or aesthetic success (example: 'better' Shakespeare sonnets have higher type-token ratio and adjective-verb quotient). Topic probability distributions indicate relative topical importance per author. Bayesian posterior probabilities indicate confidence that word usage differs between authors.

**Baseline Results**: The GEPC summary statistics: 116 cleaned poetic texts (47 compound author texts), GEPC total 1,808,160 words (tokens) and 41,857 types. GLEC: ~3,000 texts, ~250 million words, ~12 million sentences. The paper reports a successful application of the GLEC as a language model with a hit rate of 100% for computation of surprisal values for 464 metaphors (Jacobs & Kinder, 2018).

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Data Laws

**Atlas Risks**:
- **Data Laws**: Data acquisition restrictions
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
