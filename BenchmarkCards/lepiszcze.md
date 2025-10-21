# LEPISZCZE

## 📊 Benchmark Details

**Name**: LEPISZCZE

**Overview**: LEPISZCZE is a new, comprehensive benchmark for Polish NLP with a large variety of tasks and high-quality operationalization. It concentrates public Polish datasets (existing and new) in specific tasks, provides a continuous-submission leaderboard, supports data versioning and model tracking, and is designed to be easily extendable to add new models, datasets, and tasks.

**Data Type**: text (various task-specific formats: classification pairs, sentence pairs, sequence labeling with BIO tags, transcribed audio with punctuation)

**Domains**:
- Natural Language Processing
- Legal
- Spoken Language Understanding
- Social Media
- News
- Customer Reviews
- Wikipedia

**Languages**:
- Polish

**Similar Benchmarks**:
- KLEJ
- GLUE
- SuperGLUE
- KILT

**Resources**:
- [GitHub Repository](https://github.com/CLARIN-PL/LEPISZCZE)
- [Resource](https://wandb.ai/embeddings/LEPISZCZE)
- [Resource](https://huggingface.co/datasets)
- [Resource](http://clarin-pl.eu/index.php/en/home/)
- [Resource](https://arxiv.org/abs/2211.13112)

## 🎯 Purpose and Intended Users

**Goal**: Provide an extensive, flexible, and reproducible benchmark for Polish NLP that expands previous Polish benchmark KLEJ with eight new datasets, offers a unified API, supports data versioning and model tracking, and serves as a blueprint for designing benchmarks for other low-resourced languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Natural Language Inference
- Sequence Labeling
- Aspect-based Sentiment Analysis
- Dialogue Act Classification
- Named Entity Recognition
- Part-of-Speech Tagging
- Question Answering
- Paraphrase Classification
- Punctuation Restoration
- Summarization

**Limitations**: 1) No human baseline scores provided in this version. 2) Initial version evaluates models on predefined original splits (standard split problem not solved in initial release). 3) Initial version does not include baselines with static embeddings.

## 💾 Data

**Source**: Collection of 13 datasets assembled for the benchmark, including previously incorporated KLEJ datasets and eight new datasets: PAC (Polish Abusive Clauses), AspectEmo (extended PolEmo 2.0), CDSC-E, DiaBiz.Kom (Dialogue Acts), DYK (Did You Know?), KPWr-NER, NKJP-POS, PolEmo 2.0, Political Advertising, PSC (Polish Summaries Corpus), Punctuation Restoration, and Dialogue Acts (WIP). Many datasets originate from CLARIN-PL project authors; datasets and data-loading scripts were uploaded to the HuggingFace Datasets repository.

**Size**: Dataset sizes vary per dataset. Examples explicitly stated: DiaBiz.Kom: 1,277,962 tokens in 1,104 transcribed conversations; PAC: 4,129 abusive clause examples and 5,127 non-abusive fragments from >700 contracts; AspectEmo: 1,465 reviews; CDSC-E: 1,000 sentence pairs; DYK: 4,721 question-answer pairs; KPWr-NER: 13,959 training and 4,323 test sentences; NKJP-POS: 85,663 sentences; PolEmo 2.0: 8,216 reviews / 57,466 sentences; PSC: 569 summaries; Punctuation Restoration: 36 hours of transcription, 1,000 texts (800 train, 200 test). Table 1 provides full train/dev/test counts per dataset.

**Format**: Unified HuggingFace Datasets-compatible format (datasets were unified into an accessible and easy-to-process data format and uploaded to HuggingFace Datasets).

**Annotation**: Primarily human annotation. Examples: DiaBiz.Kom annotated by three linguists in a 2+1 system (reported inter-annotator agreement: Positive Specific Agreement 0.78 for borders and categories and 0.86 for borders); KPWr-NER human annotated using BIO notation; NKJP-POS annotated by humans with 35 tags; AspectEmo annotated at aspect level with six sentiment categories; CDSC-E contains human-annotated entailment labels; PAC dataset creation involved the Office of Competition and Consumer Protection and PII checks with removal of a couple of examples.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Hyper-parameter search (Optuna)
- Model-based evaluation (fine-tuning transformer models)
- Continuous-submission leaderboard
- Experiment tracking and MLOps (DVC, Weights & Biases)

**Metrics**:
- F1 Score (macro, micro, weighted)
- Precision (macro, micro, weighted)
- Recall (macro, micro, weighted)
- Accuracy

**Calculation**: Hyper-parameter search used macro averaged F1 as the objective function and was performed on the validation subset (if validation subset missing, 10% of training subset was randomly sampled). For each dataset-model pair, the best configuration by F1-macro on validation was selected, models were retrained five times, and metrics (accuracy, precision, recall, F1 with different averaging) were calculated on test sets. Experimental environment logged metrics, hyper-parameters, dataset information, and package versions via Weights & Biases and DVC.

**Interpretation**: Authors state that comparing models between tasks using different metrics may be misleading; they use homogeneous metrics to compare and score models. Macro F1 was used as the optimization objective in hyper-parameter search. Computational costs and environment metadata are tracked to enable leaderboards that incorporate efficiency.

**Baseline Results**: Baseline results for five language models across 13 datasets are reported in Table 3 (macro F1 per dataset and model; mean ranks provided). Example entries: CDSC-E HerBERT (base, cased) macro F1 90.96 ± 0.73; HerBERT (large) mean rank 1.62. Full per-dataset per-model metrics are presented in Table 3 and expanded metrics in Appendix A.3.

**Validation**: Hyper-parameter search evaluated on validation subsets (or 10% sampled from training when missing). Best configurations were retrained five times for final evaluation. Experiments tracked with DVC and Weights & Biases. The initial version used original predefined splits; authors plan to evaluate multiple/non-original splits in future versions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Transparency
- Governance
- Data Laws
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Data Laws**: Data usage restrictions
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Governance**: Lack of data transparency, Unrepresentative risk testing, Lack of system transparency
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: PAC dataset was checked by Office of Competition and Consumer Protection employees for Personal Identifiable Information (PII) and a couple of such examples were removed. DiaBiz.Kom is available only for internal usage of CLARIN-PL-Biz associates (restricted access).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
