# Scene Text Visual Question Answering (ST-VQA)

## 📊 Benchmark Details

**Name**: Scene Text Visual Question Answering (ST-VQA)

**Overview**: We present a new dataset, ST-VQA, that aims to highlight the importance of exploiting high-level semantic information present in images as textual cues in the Visual Question Answering process. The dataset defines a series of tasks of increasing difficulty that require reading scene text to answer questions, and introduces a new evaluation metric (Average Normalized Levenshtein Similarity) to account for reasoning errors as well as shortcomings of the text recognition subsystem.

**Data Type**: image (images with scene text) and question-answering pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Similar Benchmarks**:
- TextVQA
- VQA 2.0
- Textbook Question Answering (TQA)
- DVQA
- COCO-Text

**Resources**:
- [Resource](https://rrc.cvc.uab.es/?ch=11)
- [Resource](https://arxiv.org/abs/1905.13648)

## 🎯 Purpose and Intended Users

**Goal**: Provide a dataset (ST-VQA) that highlights the importance of exploiting scene text as high-level semantic information for Visual Question Answering, define tasks of increasing difficulty that require reading scene text, and propose an evaluation metric to account for OCR and reasoning errors.

**Target Audience**:
- Researchers

**Tasks**:
- Visual Question Answering
- Question Answering
- Strongly contextualised
- Weakly contextualised
- Open vocabulary

**Limitations**: Dictionaries defined over single words are limited. Existing VQA models that treat the problem as a classification task cannot deal with out-of-vocabulary answers and learning very large vocabularies is not feasible. (These limitations are explicitly discussed in the paper.)

## 💾 Data

**Source**: Images sourced from a combination of public datasets: ICDAR 2013, ICDAR 2015, ImageNet, VizWiz, IIIT Scene Text Retrieval, Visual Genome and COCO-Text.

**Size**: 23,038 images; 31,791 question-answer pairs. Train split: 19,027 images - 26,308 questions. Test split: 2,993 images - 4,163 questions.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk with a two-step collection and verification process: workers wrote up to three question-answer pairs per image; a second AMT task verified answers; ambiguous questions were filtered or corrected by the authors. Some questions have up to two valid answers.

## 🔬 Methodology

**Methods**:
- Automated metrics (ANLS)
- Accuracy (exact-match)
- Baseline model evaluation using standard VQA models (SAAA, SAN)
- OCR-based baselines (Scene Text Retrieval, Scene Image OCR)
- Online evaluation service for public validation/test evaluation

**Metrics**:
- Average Normalized Levenshtein Similarity (ANLS)
- Accuracy

**Calculation**: ANLS = (1/N) * sum_i max_j s(a_ij, o_qi), where s(a_ij, o_qi) = (1 - NL(a_ij, o_qi)) if NL(a_ij, o_qi) < δ, else 0. NL(a, o) is the normalized Levenshtein distance between the ground-truth answer a and output o. The threshold δ is defined as 0.5.

**Interpretation**: ANLS softly penalizes OCR mistakes and reasoning errors: outputs with normalized Levenshtein distance greater than 0.5 are scored 0; otherwise the score is 1 - normalized Levenshtein distance, producing a smooth penalty for OCR errors. Accuracy is the strict exact-match metric.

**Baseline Results**: Table 2 reports baseline results. Examples: Random baseline ANLS 0.015 (Accuracy 0.96%) on Task 1. STR (retrieval) on Task 1: ANLS 0.171, Accuracy 13.78%. Standard VQA models (SAAA, SAN) obtain ANLS ≈ 0.085–0.102 and Accuracy ≈ 6.36%–7.78% on the tasks. SAN(LSTM)+STR (5k cls) on Task 1: ANLS 0.136, Accuracy 10.34%.

**Validation**: Verification via a second AMT task for each question to confirm answers; ambiguous questions were filtered or author-corrected. An experiment collecting 10 answers for a 1,000-question subset was performed to assess agreement. An online evaluation service and challenge were provided for validation on public validation/test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
