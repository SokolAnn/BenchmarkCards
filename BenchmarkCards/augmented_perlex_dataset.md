# Augmented PERLEX dataset

## 📊 Benchmark Details

**Name**: Augmented PERLEX dataset

**Overview**: Using PERLEX as the base dataset, the authors apply text preprocessing and data augmentation techniques to increase the size of PERLEX and improve generalization and robustness of Persian relation extraction models; they present the augmented dataset and results from models (submitted to the NSURL 2021 shared task).

**Data Type**: text (relation-labeled sentences with entity markers)

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Similar Benchmarks**:
- PERLEX
- SemEval-2010-Task-8
- TACRED

**Resources**:
- [Resource](https://pypi.org/project/googletrans/)
- [Resource](https://arxiv.org/abs/2203.15323)

## 🎯 Purpose and Intended Users

**Goal**: Increase the size of the PERLEX dataset via text preprocessing and augmentation and improve performance (generalization and robustness) of Persian relation extraction models.

**Tasks**:
- Relation Extraction
- Sentence-level Relation Extraction

**Limitations**: N/A

## 💾 Data

**Source**: PERLEX (Persian expert-translated version of SemEval-2010-Task-8); augmented via preprocessing and data augmentation techniques including random token deletion, random token swapping, and back-translation using the googletrans API.

**Size**: 18762 sentences (after augmentation); original PERLEX: 10,717 sentences; after preprocessing: 9,381 sentences

**Format**: N/A

**Annotation**: Expert-translated; entity boundaries marked with <e1>, </e1>, <e2>, </e2> tags.

## 🔬 Methodology

**Methods**:
- Automated metrics (Macro-averaged F1)
- Model-based evaluation (fine-tuning ParsBERT and Multilingual BERT with R-BERT and RIFRE)
- Data preprocessing and augmentation (token deletion, token swap, back-translation)

**Metrics**:
- Macro-averaged F1-score (Macro-F1)

**Calculation**: Followed official SemEval-2010-Task-8 evaluation: (9+1)-way classification (nine main classes plus 'Other'); 'Other' class is present in training/testing but ignored when computing Macro-F1; directionality is taken into account.

**Interpretation**: Higher Macro-F1 indicates better performance; models are compared by Macro-F1 (the paper reports simple R-BERT as the best-performing model on PERLEX).

**Baseline Results**: Performance on PERLEX (F1-score): Simple R-BERT 83.86%; R-BERT V1 83.02%; R-BERT V2 83.11%; R-BERT V3 83.08%; RIFRE 79.54%. Reported test results: best model obtained 64.67% Macro-F1 on the NSURL shared task test and 83.68% Macro-F1 on the PERLEX test set.

**Validation**: Development evaluation performed on PERLEX; test evaluation on the NSURL 2021 shared task test data; evaluation uses the official SemEval-2010-Task-8 procedure (9+1 classes, Macro-F1, directionality considered).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
