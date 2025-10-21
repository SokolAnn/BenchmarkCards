# Morphological Tagging and Lemmatization of Albanian: A Manually Annotated Corpus and Neural Models

## 📊 Benchmark Details

**Name**: Morphological Tagging and Lemmatization of Albanian: A Manually Annotated Corpus and Neural Models

**Overview**: The paper presents the first publicly available part-of-speech and morphologically tagged corpus for the Albanian language, and a neural morphological tagger and lemmatizer trained on it. The corpus contains about 118,000 tokens of naturally occurring text collected from different text sources, with an addition of 67,000 tokens of artificially created simple sentences used only in training. The annotated corpus and trained models are made publicly available under an open license.

**Data Type**: text (token-level annotated text: POS tags, morphological features, lemmas)

**Domains**:
- Natural Language Processing

**Languages**:
- Albanian

**Similar Benchmarks**:
- UniMorph
- Albanian National Corpus
- Kabashi and Proisl (2018) Albanian gold corpus

**Resources**:
- [GitHub Repository](https://github.com/NeldaKote/Albanian-POS2)
- [Resource](https://universaldependencies.org/conll18/conll18_ud_eval.py)

## 🎯 Purpose and Intended Users

**Goal**: To create an openly available corpus of manually annotated part-of-speech tags, morphological features and lemmas for Albanian, and to train and evaluate neural models for segmentation, morphological tagging and lemmatization on this corpus.

**Tasks**:
- Text Segmentation
- Tokenization
- Part-of-Speech Tagging
- Morphological Tagging
- Lemmatization

**Limitations**: Syntactic annotation is not included; extension with syntactic annotation and inclusion into the Universal Dependencies treebank collection is left as future work.

## 💾 Data

**Source**: Naturally occurring text collected from two fiction books, an Albanian grammar book, sentences sampled from the Albanian section of the Leipzig Corpora Collection (web-crawled text and Wikipedia), and artificially created simple sentences based on a list of Albanian verbs from the UniMorph project.

**Size**: 117,686 tokens (6,644 sentences) of naturally occurring text; 66,911 tokens (17,042 sentences) of artificially created simple sentences (used only in training); total 184,597 tokens (22,366 sentences). Dataset split: Training: 160,532 tokens (includes 66,911 artificial tokens), Development: 11,375 tokens, Test: 12,690 tokens.

**Format**: CoNLL-U formatted corpus (Universal Dependencies annotation)

**Annotation**: Manual annotation according to the Universal Dependencies (UD) tagset; initial annotations converted from previous work and manually corrected; pre-tagged data reviewed by two native speakers; lemmas provided for each token.

## 🔬 Methodology

**Methods**:
- Model training and evaluation using the Turku Neural Parser Pipeline
- Automated evaluation using the official CoNLL-2018 evaluation script (conll18_ud_eval.py)
- Manual annotation and manual review by native speakers (for corpus creation)

**Metrics**:
- Accuracy (Token segmentation)
- Accuracy (Sentence segmentation)
- Accuracy (Part-of-Speech tagging)
- Accuracy (Morphological features)
- Accuracy (Lemmatization)

**Calculation**: Performance measured using the official CoNLL-2018 shared task evaluation script (conll18_ud_eval.py) for multilingual parsing from raw text to Universal Dependencies.

**Interpretation**: The authors state that the performance of each step of the pipeline is at a sufficiently high level to support many downstream NLP applications in practice.

**Baseline Results**: Token segmentation: 99.88% Accuracy; Sentence segmentation: 99.51% Accuracy; POS tagging: 92.74% Accuracy; Morphological features: 85.31% Accuracy; Lemmatization: 89.95% Accuracy.

**Validation**: Sentences from the same document are grouped into the same split to avoid lexical overlap. All artificially created UniMorph sentences are placed into the training section to avoid optimistic evaluation. Development set used for early stopping; held-out test set preserved for final evaluation.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Available under an open license (unspecified in the paper).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
