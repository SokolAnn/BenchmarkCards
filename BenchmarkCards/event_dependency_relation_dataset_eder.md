# Event Dependency Relation dataset (EDeR)

## 📊 Benchmark Details

**Name**: Event Dependency Relation dataset (EDeR)

**Overview**: A human-annotated dataset that labels when an event is an argument (required or optional) of another event. Constructed from a sample of documents from the OntoNotes dataset and provides refined semantic role-labelled event representations; intended to support automatic classification of event dependency relations and to improve downstream tasks such as semantic role labelling and coreference resolution.

**Data Type**: text (event pairs with event dependency relation labels)

**Domains**:
- Natural Language Processing
- Information Retrieval

**Languages**:
- English

**Similar Benchmarks**:
- OntoNotes
- TimeBank
- TB-Dense
- MATRES
- CausalTimeBank
- CiRA
- CNC
- HiEve
- CoNLL-2005
- CoNLL-2009
- CoNLL-2012

**Resources**:
- [GitHub Repository](https://github.com/RichieLee93/EDeR)
- [Resource](https://arxiv.org/abs/2304.01612)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality human-annotated dataset of event dependency relations (whether one event is a required/optional argument or non-argument/condition of another) and refined event representations, to enable training and evaluation of models for extracting these relations and to improve downstream tasks such as semantic role labelling and coreference resolution.

**Target Audience**:
- Natural Language Processing researchers
- Information Retrieval researchers

**Tasks**:
- Relation Extraction
- Semantic Role Labeling
- Coreference Resolution

**Limitations**: Dataset size is constrained by the annotation method; label distribution is biased with a majority (just over 75%) of event pairs labelled as 'argument'.

## 💾 Data

**Source**: Subset of the OntoNotes dataset: 275 sampled documents from seven genres (broadcast news, magazine, newswire, pivot corpus, telephone conversation, broadcast conversation, web data). Candidate event pairs extracted where the predicate of one event is contained in the span of another.

**Size**: 11,852 annotated event pairs from 275 documents

**Format**: N/A

**Annotation**: Manual human annotation by trained annotators (English linguistic-major graduate students) using a multi-level qualification-based inspection procedure with quality inspectors and a linguistic expert; annotators selected via screening test (16 annotators selected), iterative inspection and expert review; annotation labels: required argument, optional argument, condition, independent; containing-event refinement performed for non-argument cases.

## 🔬 Methodology

**Methods**:
- Heuristic rules-based method
- Fine-tuning pre-trained Transformer models (BERT, RoBERTa, DistilBERT, XLNet, GPT-2)
- Marked-predicate sentence, Event-Event span, Event-Event-SRL, Event-Event-SRL-DEP input styles
- Use of CRFSRL and modified ED-CRFSRL for semantic role labelling experiments
- Use of coref-HGAT for coreference resolution experiments

**Metrics**:
- Precision
- Recall
- Accuracy
- F1 Score
- ROC_AUC (Area Under ROC Curve)

**Calculation**: Standard classification evaluation metrics (Precision, Recall, Accuracy) applied for relation extraction; ROC_AUC reported for binary task. Semantic role labelling and coreference resolution evaluated using the official CoNLL-2012 evaluation scripts as stated in the paper.

**Interpretation**: Higher ROC_AUC indicates better ranking of positive over negative samples; authors report baseline accuracy up to 82.61% for binary classification and interpret this as the dataset being sufficient to train good predictors. The three-way (required/optional/non-argument) classification is explicitly noted as more challenging, with lower accuracies.

**Baseline Results**: Binary argument/non-argument: best accuracy 82.61% (BERT with marked-predicate sentence input). Three-way (required/optional/non-argument): best accuracy 70.79% (RoBERTa with Event-Event-SRL-DEP input). SRL experiment: CRFSRL-O: Precision 77.07 / Recall 81.03 / F1-score 79.00; ED-CRFSRL (G, using EDeR annotations): Precision 76.09 / Recall 78.81 / F1-score 77.43. For refined events only: ED-CRFSRL (G): Precision 88.11 / Recall 69.51 / F1-score 77.71. Coreference resolution (coref-HGAT): OntoNotes Event Reps. (G): Precision 67.73 / Recall 65.41 / F1-score 66.50; EDeR Event Reps. (G): Precision 69.14 / Recall 65.69 / F1-score 67.40.

**Validation**: Annotation quality controlled via multi-level qualification-based inspection: quality inspectors (QIs) sampled and re-annotated 40% each stage, linguistic expert sampled 15-25% of QI-inspected cases and provided corrections; annotators required to meet accuracy thresholds (screening >=85%, ongoing agreement >=95%); a random sample of 5% of final annotations was verified with at least 95% found correct. Train/dev/test splits follow initial OntoNotes distributions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
