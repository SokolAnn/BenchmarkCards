# The Corpus Replication Task

## 📊 Benchmark Details

**Name**: The Corpus Replication Task

**Overview**: Generating input text for which word2vec outputs target relations. The Corpus Replication Task is a bottom-up approach to investigate which kinds of relations are representable in continuous space and how relations are built by generating text that causes word2vec to output target relations.

**Data Type**: text (artificially generated sentence corpora)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Semantic-Syntactic Word Relationship Test
- SemEval-2012 Task 2: Measuring Degrees of Relational Similarity

**Resources**:
- [Resource](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/word2vec.html)
- [Resource](http://arxiv.org/abs/1310.4546)
- [Resource](http://arxiv.org/abs/1301.3781)
- [Resource](http://dl.acm.org/citation.cfm?id=2387636.2387693)
- [Resource](https://books.google.de/books?id=swCOtgAACAAJ)
- [Resource](http://www.era.lib.ed.ac.uk/bitstream/1842/563/2/IP030023.pdf)
- [Resource](http://www.aclweb.org/anthology/P14-2050)
- [Resource](http://doi.acm.org/10.1145/1553374.1553518)
- [Resource](http://dl.acm.org/citation.cfm?id=2503308.2188396)
- [Resource](http://arxiv.org/abs/1411.2738)
- [Resource](http://arxiv.org/abs/1402.3722)

## 🎯 Purpose and Intended Users

**Goal**: To investigate which kinds of relations are representable in continuous space and how relations are built by generating input text for which word2vec outputs target relations (the Corpus Replication Task).

**Tasks**:
- Word Representation Learning
- Relation Extraction in Word Embeddings
- Measuring Distributional Similarity

**Limitations**: Experiments presented are limited to two-dimensional word embeddings; solving the higher-dimensional case and evaluation of more complex distributions are left for future work.

## 💾 Data

**Source**: Artificially generated text corpora created by defining base sentences (e.g., 'A king is a man.', 'A queen is a woman.', 'Berlin is the capital of Germany.') and sampling and concatenating copies according to specified probability distributions.

**Size**: Experiments reported with input corpus sizes of 1,000 sentence copies, 10,000 sentence copies, and 100,000 sentence copies.

**Format**: Raw text (concatenated sentences)

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Synthetic corpus generation by sampling and concatenating base sentences
- Model-based evaluation using word2vec Skip-Gram implementation (h2o framework, version 3.14.0.1)
- Distance-based evaluation using Euclidean distance between word vectors

**Metrics**:
- Euclidean distance
- Cosine distance
- Accuracy (syntagmatic similarity percentage, as referenced)

**Calculation**: Metrics are computed as distances between word vectors in the embedding space (experiments compute two-dimensional word vectors and use Euclidean distance; the paper also references cosine distance for similarity measurement).

**Interpretation**: Smaller Euclidean or cosine distance indicates higher similarity; clustering or collapsing of vector pairs indicates paradigmatic or syntagmatic relations (e.g., vector differences approximating each other indicate relational similarity).

**Validation**: Validated through experiments varying window size, corpus size, and sampling distribution (including uniform and non-uniform sampling) and observing resulting vector configurations and relation emergence in 2D visualizations.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
