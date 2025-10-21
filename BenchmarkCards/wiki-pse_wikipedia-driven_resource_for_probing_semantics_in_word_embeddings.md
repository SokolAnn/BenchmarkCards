# WIKI-PSE (WIKIpedia-driven resource for Probing Semantics in word Embeddings)

## 📊 Benchmark Details

**Name**: WIKI-PSE (WIKIpedia-driven resource for Probing Semantics in word Embeddings)

**Overview**: A large dataset based on Wikipedia annotations and word senses where word senses from different words are related by semantic classes (S-classes). It is the basis for diagnostic tests that probe word embeddings for semantic classes and analyze embedding space by classifying embeddings into semantic classes.

**Data Type**: text (Wikipedia sentences; word/S-class pairs; token-level S-class annotations)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SEMCAT
- HyperLex
- SemCor
- Supersense annotated Wikipedia (UKP)
- FIGER

**Resources**:
- [GitHub Repository](https://github.com/yyaghoobzadeh/WIKI-PSE)
- [Resource](https://arxiv.org/abs/1906.03608)
- [GitHub Repository](https://github.com/xiaoling/figer)

## 🎯 Purpose and Intended Users

**Goal**: Enable probing of word embeddings for semantic classes (S-classes) and analyze how multiple senses are represented; provide a corpus and dataset for supervised diagnostic classification tests of embedding content.

**Tasks**:
- Text Classification (S-class prediction at word/type level)
- Ambiguity Detection (predict whether a word is single-sense or multi-sense)
- Word Sense Representation Evaluation (probing)

**Limitations**: Annotation contains noise due to distant supervision from Wikipedia anchor links; granularity is reduced by using 34 parent S-classes to reduce noise; resource focuses on common and proper nouns and is based on an English Wikipedia snapshot (2014-07-07).

## 💾 Data

**Source**: English Wikipedia (2014-07-07); annotations derived from Wikipedia anchor links mapped to FIGER types via Freebase mapping (https://github.com/xiaoling/figer); uses distant supervision.

**Size**: 550 million tokens; vocabulary ≈500,000; ≈276,000 annotated words in the vocabulary; ≈343,000 word/S-class pairs; train set: 44,250 examples; test set: 44,250 examples.

**Format**: Plain text (lowercased sentences) with linked mentions marked as '@mention@' and word/S-class tokens; corpus-based dataset of word/S-class pairs.

**Annotation**: Distant supervision from Wikipedia anchor links mapped to FIGER types; token-level S-class annotations; reduced to 34 parent S-classes to reduce noise.

## 🔬 Methodology

**Methods**:
- Supervised probing via binary classification per S-class
- Logistic Regression
- Multi-layer Perceptron (one hidden layer with ReLU)
- K-Nearest Neighbors
- Nearest-neighbor cosine similarity
- Word embedding learning using SkipGram (SKIP) and Structured SkipGram (SSKIP) trained with Wang2Vec

**Metrics**:
- Micro F1
- Accuracy
- Spearman correlation

**Calculation**: S-class prediction: global metric of micro F1 over all test examples and over all S-class predictions. Ambiguity prediction: Accuracy on held-out test set. Similarity evaluation: Spearman correlation between model similarities and human judgments.

**Interpretation**: Micro F1 quantifies how well S-classes are encoded in embeddings; Accuracy quantifies ability to distinguish ambiguous vs. unambiguous words; higher Spearman correlation indicates better alignment with human similarity judgments.

**Baseline Results**: Random baseline micro F1 = 0.273 (Table 2). Ambiguity FREQUENCY baseline accuracy = 64.8% (Table 4). GloVe (6B) MLP F1 = 0.685 on the shared-vocabulary subset (Table 3). FastText (Wiki) MLP F1 = 0.697 on the shared-vocabulary subset (Table 3).

**Validation**: Dataset split into equal-sized train and test sets of 44,250 each with equal numbers of single- and multiclass words; evaluation performed on held-out test sets. Additional subset for public embeddings comparison: 13,000 train and 13,000 test.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Transparency**: Uncertain data provenance

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
