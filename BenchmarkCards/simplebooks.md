# SimpleBooks

## 📊 Benchmark Details

**Name**: SimpleBooks

**Overview**: A small long-term-dependency dataset with high average token frequency designed as a benchmark and testbed for word-level language modeling and for faster experimentation (e.g., architectural search). Created from Gutenberg books, SimpleBooks includes a 92-million-token version (SimpleBooks-92) and a 2-million-token version (SimpleBooks-2) and provides both tokenized and raw unprocessed text.

**Data Type**: text (word-level tokens; includes raw unprocessed text for character-level language modeling)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Penn TreeBank (PTB)
- WikiText-103
- WikiText-2
- One-Billion Word

**Resources**:
- [Resource](https://dldata-public.s3.us-east-2.amazonaws.com/simplebooks.zip)
- [GitHub Repository](https://github.com/salesforce/awd-lstm-lm)
- [GitHub Repository](https://github.com/kimiyoung/transformer-xl)
- [GitHub Repository](https://github.com/NVIDIA/Milano)
- [GitHub Repository](https://github.com/chiphuyen/lazynlp)

## 🎯 Purpose and Intended Users

**Goal**: Provide a small long-term-dependency dataset with high average token frequency that is representative of larger datasets to serve as a benchmark and testbed for language modeling, and as a more suitable dataset for setups like architectural search and meta-learning.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Word-level Language Modeling
- Character-level Language Modeling
- Word embedding training / Transfer Learning

**Limitations**: N/A

## 💾 Data

**Source**: Downloaded from Gutenberg US (www.gutenberg.org). From an initial set of 39,432 books (after discarding mal-formatted books and books of poems, plays, manuals, recipes, and literary nonsense), a subset of 1,573 books was selected to create the dataset.

**Size**: SimpleBooks-92: 92M word-level tokens (train), 200k tokens validation, 200k tokens test; vocabulary size 98,304. SimpleBooks-2: 2M word-level tokens (train), 200k tokens validation, 200k tokens test; vocabulary size 11,492.

**Format**: Raw text files; tokenized using SpaCy (space-separated tokens with specific number tokenization conventions); tokenized and raw versions provided in the released ZIP.

**Annotation**: No annotation (raw/unlabeled text for unsupervised language modeling)

## 🔬 Methodology

**Methods**:
- Training and evaluation of language models (AWD-LSTM and Transformer-XL)
- Hyperparameter search using Milano (500 hyperparameter sets on first 30 epochs for SimpleBooks-2)
- Transfer learning experiments using word2vec skip-gram embeddings

**Metrics**:
- Perplexity
- Model parameter count

**Calculation**: Perplexity is reported on the held-out validation and test sets (values presented in tables for validation and test perplexities). Model parameter counts are reported for models that achieve near-SOTA results.

**Interpretation**: Lower perplexity indicates better language model performance. The paper reports that Transformer-XL outperformed AWD-LSTM on both SimpleBooks-2 and SimpleBooks-92 (based on validation and test perplexities) and that SimpleBooks reduces required model parameters and training time compared to WikiText-103.

**Baseline Results**: Validation and test perplexities (Table 2): SB-2 AWD-LSTM: Valid 17.16, Test 16.78. SB-2 Transformer-XL: Valid 17.27, Test 16.41. SB-92 AWD-LSTM: Valid 21.45, Test 20.64. SB-92 Transformer-XL: Valid 9.3, Test 8.92.

**Validation**: Held-out validation set of 200k tokens used. Hyperparameter search conducted via Milano on first 30 epochs (500 hyperparameter sets) for SimpleBooks-2; best hyperparameters then trained until convergence.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
