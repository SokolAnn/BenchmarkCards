# L3Cube-HingCorpus

## 📊 Benchmark Details

**Name**: L3Cube-HingCorpus

**Overview**: L3Cube-HingCorpus, the first large-scale real Hindi-English code mixed data in a Roman script. It consists of 52.93M sentences and 1.04B tokens, scraped from Twitter. A subset is released as a benchmark code mixed Hindi-English language identification dataset L3Cube-HingLID.

**Data Type**: text (code-mixed Hindi-English tweets)

**Domains**:
- Natural Language Processing
- Social Media

**Languages**:
- Hindi
- English

**Similar Benchmarks**:
- GLUECoS

**Resources**:
- [GitHub Repository](https://github.com/l3cube-pune/code-mixed-nlp)
- [Resource](https://huggingface.co/l3cube-pune/hing-bert)
- [Resource](https://huggingface.co/l3cube-pune/hing-mbert)
- [Resource](https://huggingface.co/l3cube-pune/hing-mbert-mixed)
- [Resource](https://huggingface.co/l3cube-pune/hing-roberta)
- [Resource](https://huggingface.co/l3cube-pune/hing-robera-mixed)
- [Resource](https://huggingface.co/l3cube-pune/hing-gpt)
- [Resource](https://huggingface.co/l3cube-pune/hing-gpt-devanagari)
- [Resource](https://huggingface.co/l3cube-pune/hing-bert-lid)
- [GitHub Repository](https://github.com/twintproject/twint)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale real Hindi-English code-mixed corpus (L3Cube-HingCorpus) and release a benchmark L3Cube-HingLID to enable pre-training of language models and improve performance on downstream code-mixed NLP tasks.

**Target Audience**:
- Researchers in Natural Language Processing
- Model Developers

**Tasks**:
- Language Identification
- Part of Speech tagging
- Named Entity Recognition
- Sentiment Analysis

**Limitations**: N/A

## 💾 Data

**Source**: HingCorpus: scraped from Twitter using the Twint framework with an iteratively built vocabulary of commonly spoken Hindi words; filtered to Roman script and preprocessed to remove non-English characters and user mentions. HingLID: an in-house token-level Hindi-English language identification dataset created via a semi-supervised iterative labeling process (initial 5k labelled sentences, pseudo-labeling, manual verification).

**Size**: HingCorpus: 52.93M sentences (1.04B tokens). Training split: 47.79M sentences (944M tokens). Validation split: 5.13M sentences (99M tokens). L3Cube-HingLID: Train 31,756 samples, Test 6,420 samples, Validation 6,279 samples (average ~30 tokens per sentence).

**Format**: N/A

**Annotation**: HingCorpus: unsupervised (scraped). HingLID: token-level labels created via semi-supervised pseudo-labeling starting from a 5k manually labelled dataset, with manual verification and correction of low-confidence pseudo-labels; labels include EN, HI, OTHER.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Fine-tuning of pre-trained models on downstream tasks
- Perplexity for masked language model validation

**Metrics**:
- F1 Score
- Perplexity

**Calculation**: Pre-training: MLM objective with masking probability 15%, trained for 2 epochs. Fine-tuning: models fine-tuned for 5 epochs using early stopping with respect to validation F1 score; batch size 64 and learning rate 3e-5 for downstream tasks.

**Interpretation**: Higher F1 Score indicates better task performance on downstream tasks. Perplexity is used to validate MLM pre-training (lower perplexity indicates better masked token prediction).

**Baseline Results**: Reported F1 scores (Roman script, Table 4): BERT: LID 78.69, POS-UD 83.70, POS-FG 70.75, NER 79.27, Sentiment 59.16, HingLID 96.04. m-BERT: LID 82.56 ... XLMRoBERTa: LID 85.93 ... HingBERT: LID 84.44 ... HingMBERT: LID 84.90 ... HingRoBERTa: LID 86.69 ... HingBERT-LID: HingLID 98.77. (Full tables are provided in the paper.)

**Validation**: HingCorpus: held-out validation of 5.13M sentences. L3Cube-HingLID: separate train/validation/test splits (no leakage); the HingBERT-LID model reported 98% accuracy on the unseen test set used for selecting sentences for HingCorpus.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Data contamination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User mentions in tweets were removed to avoid privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
