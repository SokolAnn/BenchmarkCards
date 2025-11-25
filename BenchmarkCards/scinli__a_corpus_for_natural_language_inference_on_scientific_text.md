# SCINLI: A Corpus for Natural Language Inference on Scientific Text

## 📊 Benchmark Details

**Name**: SCINLI: A Corpus for Natural Language Inference on Scientific Text

**Overview**: We introduce SCINLI, a large dataset for Natural Language Inference (NLI) that captures the formality in scientific text and contains 107,412 sentence pairs extracted from scholarly papers on NLP and computational linguistics; intended to serve as a benchmark for the evaluation of scientific Natural Language Understanding models.

**Data Type**: text (sentence pairs: premise-hypothesis)

**Domains**:
- Natural Language Processing
- Computational Linguistics

**Similar Benchmarks**:
- SNLI
- MNLI
- SICK
- SCITAIL
- ANLI
- SWAG
- GLUE
- SUPER GLUE

**Resources**:
- [GitHub Repository](https://github.com/msadat3/SciNLI)
- [Resource](https://www.nltk.org/api/nltk.tokenize.html)
- [Resource](https://www.nltk.org/howto/stem.html)
- [Resource](https://huggingface.co/docs/transformers/)

## 🎯 Purpose and Intended Users

**Goal**: Enable deep learning for natural language inference over scientific text by introducing SCINLI and presenting a comprehensive investigation into inference types that occur frequently in scientific text.

**Tasks**:
- Natural Language Inference

**Limitations**: Training set is created using distant supervision based on linking phrases and may be noisy; total size is smaller than SNLI and MNLI (noted by the authors).

## 💾 Data

**Source**: Scientific papers on Natural Language Processing and Computational Linguistics available in the ACL Anthology, published between 2000 and 2019.

**Size**: 107,412 sentence pairs

**Format**: N/A

**Annotation**: Training set labeled via distant supervision using linking phrases; development and test sets manually annotated by three expert annotators with majority vote; examples without majority vote (~5%) receive no gold label; Fleiss-k among annotators reported as 0.62.

## 🔬 Methodology

**Methods**:
- Distant supervision labeling (linking phrases)
- Manual annotation by expert annotators (development and test sets)
- Model-based evaluation (fine-tuning pre-trained language models)
- Baseline experiments with traditional machine learning and neural network models

**Metrics**:
- Macro F1
- Accuracy
- F1 Score (per-class)

**Calculation**: Macro F1 is computed over the four classes (CONTRASTING, REASONING, ENTAILMENT, NEUTRAL). Reported results are averages and standard deviations over three runs with different random seeds. Early stopping during training is based on development Macro F1.

**Interpretation**: Higher Macro F1 and Accuracy indicate better NLI performance. The authors interpret relatively low scores (best Macro F1 78.18% and Accuracy 78.23% with XLNet) as evidence that SCINLI is a challenging benchmark requiring deep semantic understanding.

**Baseline Results**: Lexicalized: Macro F1 47.01%, Accuracy 47.78%. CBOW: Macro F1 51.68%, Accuracy 51.78%. CNN: Macro F1 60.41%, Accuracy 60.53%. BiLSTM: Macro F1 61.12%, Accuracy 61.32%. BERT: Macro F1 75.19%, Accuracy 75.17%. SciBERT: Macro F1 77.53%, Accuracy 77.52%. RoBERTa: Macro F1 78.06%, Accuracy 78.12%. XLNet: Macro F1 78.18%, Accuracy 78.23%.

**Validation**: Development and test sets were manually annotated and cleaned; only examples where the gold label agreed with the distant-supervision label were selected for the benchmark evaluation set (6,904 examples). Splits are done at the paper level to prevent information leakage. Fleiss-k among annotators is 0.62.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
