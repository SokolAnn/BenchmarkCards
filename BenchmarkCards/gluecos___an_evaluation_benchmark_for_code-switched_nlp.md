# GLUECoS : An Evaluation Benchmark for Code-Switched NLP

## 📊 Benchmark Details

**Name**: GLUECoS : An Evaluation Benchmark for Code-Switched NLP

**Overview**: We present an evaluation benchmark, GLUECoS, for code-switched languages, that spans several NLP tasks in English-Hindi and English-Spanish. The benchmark includes Language Identification from text, Part of Speech tagging, Named Entity Recognition, Sentiment Analysis, Question Answering and a new task for code-switching, Natural Language Inference.

**Data Type**: text (word-level labels, sentence-level classification, question-answer pairs, sentence-pair NLI)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hindi
- Spanish

**Similar Benchmarks**:
- GLUE (Generalized Language Evaluation Benchmark)
- SuperGLUE

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/MUSE)
- [GitHub Repository](https://github.com/karlmoritz/bicvm/)
- [GitHub Repository](https://github.com/lmthang/bivec)
- [Resource](https://fasttext.cc/)
- [GitHub Repository](https://github.com/marekrei/sequence-labeler/tree/484a6beb1e2a2cccaac74ce717b1ee30c79fc8d8)
- [GitHub Repository](https://github.com/huggingface/transformers)
- [GitHub Repository](https://github.com/ElizaLo/Question-Answering-based-on-SQuAD)

## 🎯 Purpose and Intended Users

**Goal**: To propose GLUECoS, a language understanding evaluation framework for Code-Switched NLP that evaluates models across multiple tasks and two language pairs (English-Hindi and English-Spanish).

**Tasks**:
- Language Identification
- Part of Speech Tagging
- Named Entity Recognition
- Sentiment Analysis
- Question Answering
- Natural Language Inference

**Limitations**: Current version does not include a multi-task learning evaluation; benchmark contents are limited to English-Hindi and English-Spanish datasets used in this work; for some datasets the authors create their own train/dev/test splits.

## 💾 Data

**Source**: Publicly available datasets and prior shared-task corpora, and one new NLI dataset by the authors. Datasets used include: FIRE LID, UD POS (Bhat et al.), FG POS (ICON 2016), IIITH NER, SAIL Sentiment (ICON 2017), Chandu et al. QA, Khanuja et al. NLI (new dataset), EMNLP 2014 LID, Bangor POS, CALCS NER, En-Es sentiment (Vilares et al.).

**Size**: Varied per dataset; see Table 1 for per-dataset sentence counts (examples: FIRE LID: 2,631 train sentences; SAIL Sentiment: 10,080 train sentences; EMNLP 2014 LID: 10,259 train sentences; CALCS NER: 27,366 train sentences; NLI (R) 1,040 train sentences).

**Format**: N/A

**Annotation**: Word-level language tags (LID); Part-of-speech tags (POS); Named entity labels (NER); sentence-level sentiment labels (positive/negative/neutral); question-answer-context triples for QA; premise-hypothesis labels for NLI.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Baseline model evaluations (cross-lingual word embeddings)
- Pre-trained multilingual model evaluation (mBERT)
- Fine-tuning pre-trained multilingual models on synthetic and small real code-switched data

**Metrics**:
- F1 Score
- Accuracy
- Code-Mixing Index (CMI)
- Average switch-points (SP Avg)
- M-index
- Probability of Switching (I-index)
- Burstiness
- Language Entropy (LE)
- Span Entropy (SE)

**Calculation**: Task metrics (F1 Score and Accuracy) are computed on test sets. Code-switching statistics (CMI, SP Avg, M-index, I-index, Burstiness, LE, SE) are computed as described (Gambäck and Das, 2014; Guzmán et al., 2017) and reported in Table 2.

**Interpretation**: Higher F1 Score or Accuracy indicates better task performance. Authors note that multilingual models (mBERT) outperform cross-lingual embeddings and that fine-tuning mBERT on synthetic plus small real code-switched data often yields the best results. The authors state that low accuracies on tasks such as Sentiment Analysis and NLI indicate these tasks are far from solved for code-switched languages.

**Baseline Results**: Results for baseline and evaluated models are reported in Tables 3-8. Examples: LID En-Hi Mod. mBERT F1 = 96.6; LID En-Es Mod. mBERT F1 = 96.24; NLI En-Hi mBERT Accuracy = 61.09, Mod. mBERT Accuracy = 63.1. (See Tables 3-8 for full per-dataset results.)

**Validation**: For datasets without official splits the authors create balanced 8:1:1 train:dev:test splits. Experiments were run with 5 random seeds and results reported are averages. Early stopping and validation-based model selection were used as described in Appendix B.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Governance

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Governance**: Lack of testing diversity

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
