# DBiDAF, DBERT, DRoBERTa

## 📊 Benchmark Details

**Name**: DBiDAF, DBERT, DRoBERTa

**Overview**: Investigation of a model-in-the-loop adversarial annotation methodology for Reading Comprehension (RC). The authors apply the methodology with three progressively stronger models in the annotation loop, collecting three datasets of 12,000 samples each (36,000 total), to study reproducibility of the adversarial effect, transfer between datasets collected with different model-in-the-loop strengths, and generalisation to non-adversarially collected data.

**Data Type**: question-answering pairs (text)

**Domains**:
- Natural Language Processing

**Languages**:
- N/A

**Similar Benchmarks**:
- SQuAD1.1
- DROP
- NaturalQuestions
- Quoref
- AdversarialNLI
- CODAH
- SWAG
- HellaSWAG
- ReCoRD
- HotpotQA

**Resources**:
- [Resource](https://arxiv.org/abs/2002.00293)

## 🎯 Purpose and Intended Users

**Goal**: Investigate the model-in-the-loop adversarial annotation paradigm for Reading Comprehension: study reproducibility of adversarial examples, transfer between datasets collected with different adversary strengths, and generalisation to non-adversarial datasets.

**Target Audience**:
- ML Researchers
- Dataset creators
- Natural Language Processing researchers

**Tasks**:
- Question Answering
- Reading Comprehension

**Limitations**: Datasets constructed with weaker models in the loop may become outdated as stronger models emerge; the validation procedure can result in valid questions being discarded (the authors explicitly note this when enforcing human answerability); some models (e.g., BiDAF) may be unable to learn from adversarially collected samples.

## 💾 Data

**Source**: Passages sourced from SQuAD1.1; adversarial question-answer pairs crowdsourced via Amazon Mechanical Turk with an in-the-loop model (BiDAF, BERT LARGE, or RoBERTa LARGE) guiding annotation. Resulting datasets are named DBiDAF, DBERT, and DRoBERTa. A modified version of SQuAD is referred to as DSQuAD.

**Size**: DBiDAF: 10,000 training examples, 1,000 validation examples, 1,000 test examples (12,000 total); DBERT: 10,000 training, 1,000 validation, 1,000 test (12,000 total); DRoBERTa: 10,000 training, 1,000 validation, 1,000 test (12,000 total); Total adversarially collected samples: 36,000 examples. DSQuAD: 87,599 training examples, 5,278 dev examples, 5,292 test examples (as reported in Table 3).

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk (workers based in Canada, the UK, or the US; HIT Approval Rate >98%; at least 1,000 previously completed HITs). Annotators generate a question q for a passage p and highlight the human answer span ah. The (p,q) pair is sent to the model-in-the-loop which returns a predicted answer am. A word-overlap F1 between ah and am is computed; a threshold of 40% F1 is used to determine a model 'win' (if F1 > 40% the model wins and the question is rejected). Only questions where the model fails to answer correctly are retained. Workers complete qualification tasks; manual worker validation is applied (workers falling below an 80% success threshold are disqualified). Answerability is checked by at least three additional non-expert validators; questions without at least one matching validator answer are discarded from validation and test sets. Payment: USD 2.00 per question-generation HIT.

## 🔬 Methodology

**Methods**:
- Crowdsourcing via Amazon Mechanical Turk
- Model-in-the-loop adversarial annotation
- Human validation (multi-validator answerability checks)
- Manual worker training and qualification
- Model training and evaluation (retraining experiments and cross-dataset evaluation)
- Qualitative annotation of comprehension requirement types

**Metrics**:
- Exact Match (EM)
- Word-overlap F1 (F1)

**Calculation**: Word-overlap F1 between human answer ah and model answer am is computed; a threshold of 40% F1 determines whether the model 'wins' during annotation (if model F1 > 40% the question is rejected). Evaluation metrics for models are Exact Match (EM) and word-overlap F1 computed as in SQuAD.

**Interpretation**: Higher EM and F1 indicate better model performance on the dataset/tasks. Human answerability is defined as at least one of three non-expert validators providing an answer matching the original. The authors interpret progressive decreases in EM/F1 when evaluating on datasets constructed with stronger model-in-the-loop adversaries as indicating increased difficulty and distributional shift.

**Baseline Results**: Models (on SQuAD1.1 validation) achieve EM/F1: BiDAF 65.5/77.5, BERT LARGE 82.7/90.3, RoBERTa LARGE 86.9/93.6. Non-expert human performance (Table 2) on validation: DBiDAF 63.0 EM / 76.9 F1; DBERT 59.2 EM / 74.3 F1; DRoBERTa 58.1 EM / 72.0 F1. The paper reports numerous model training and cross-evaluation results across DBiDAF, DBERT, DRoBERTa, DSQuAD, DDROP, and DNQ (see Tables 5-8).

**Validation**: The existing SQuAD1.1 validation set was split in half (stratified by document title) to create an official test set. Passage consistency was maintained across splits. Worker outputs were manually screened during qualification; samples of every worker's HITs were manually reviewed after each annotation batch and workers below an 80% success threshold were disqualified and their work discarded. Answerability checks were performed on validation and test sets using at least three validators; only questions with at least one matching validator answer were retained. The authors report answerability scores of 87.95% (DBiDAF), 85.41% (DBERT), and 82.63% (DRoBERTa) for validation/test.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Governance**: Unrepresentative risk testing, Lack of testing diversity

**Demographic Analysis**: N/A

**Potential Harm**: Detecting model blind spots and dataset biases; probing model robustness to adversarially authored questions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
