# Causal News Corpus (CNC)

## 📊 Benchmark Details

**Name**: Causal News Corpus (CNC)

**Overview**: CNC is a corpus of news articles annotated with causal information suitable for causal text mining. The paper introduces a shared task with two subtasks: (1) Causal Event Classification and (2) Cause-Effect-Signal Span Detection. Participants uploaded predictions for a held-out test set and ranking was done based on binary F1 for Subtask 1 and macro F1 for Subtask 2.

**Data Type**: text (news articles; sentences with causal sentence labels and cause-effect-signal span annotations)

**Domains**:
- Natural Language Processing
- News

**Languages**:
- English

**Similar Benchmarks**:
- FinCausal
- UniCausal
- CausalTimeBank
- EventStoryLine
- AltLex
- BECAUSE 2.0
- Penn Discourse Treebank V3.0
- SemEval 2010 Task 8

**Resources**:
- [GitHub Repository](https://github.com/tanfiona/CausalNewsCorpus)
- [GitHub Repository](https://github.com/tanfiona/CausalNewsCorpus/blob/master/random_st2.py)
- [GitHub Repository](https://github.com/chakki-works/seqeval)
- [Resource](https://huggingface.co/spaces/evaluate-metric/seqeval)
- [Resource](https://codalab.lisn.upsaclay.fr/competitions/2299)
- [Resource](https://codalab.lisn.upsaclay.fr/competitions/7046)
- [Resource](https://arxiv.org/abs/2211.12154)

## 🎯 Purpose and Intended Users

**Goal**: To provide a corpus (Causal News Corpus) annotated with causal information and to run a shared task to promote modelling for two causal text mining tasks: Causal Event Classification and Cause-Effect-Signal Span Detection.

**Target Audience**:
- ML Researchers
- Model Developers
- Natural Language Processing Researchers

**Tasks**:
- Question: Causal Event Classification
- Question: Cause-Effect-Signal Span Detection

**Limitations**: Span annotations are an on-going effort and only a small subset of the data contains annotated spans at the time of writing.

## 💾 Data

**Source**: Causal News Corpus (CNC) built on randomly sampled news articles from multiple sources and periods; CNC consists of news documents and sentences annotated with causal information (Tan et al., 2022a).

**Size**: 3,559 sentences; 869 news documents. Subtask 1 splits: Train: 2,925 sentences, Dev: 323 sentences, Test: 311 sentences. Subtask 2 splits: Train: 160 sentences, Dev: 15 sentences, Test: 89 sentences. Subtask 2 relations: Train: 183 relations, Dev: 18 relations, Test: 119 relations, Total 320 relations.

**Format**: N/A

**Annotation**: Manual annotation by five annotators using the WebAnno tool. Subtask 1: sentences labeled as Causal or Non-causal; majority vote retained as final label and curator breaks ties. Subtask 2: annotators marked Cause, Effect and Signal spans and linked spans; curator consolidated final span annotations (curator decided final selection when no majority). Annotations were checked with Python scripts to identify avoidable human errors.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Competition evaluation on Codalab
- Token-classification evaluation via seqeval

**Metrics**:
- Accuracy
- Precision
- Recall
- F1
- Matthews Correlation Coefficient (MCC)
- Macro Precision
- Macro Recall
- Macro F1

**Calculation**: Subtask 1: standard binary classification metrics (Acc, P, R, F1, MCC). Subtask 2: participants submitted ARG0/ARG1/SIG marked sentences which were converted to token label sequences; evaluated using token-classification evaluation scheme from seqeval. For Subtask 2, evaluation was at the relation level and code was adjusted to extract the combination of predicted relations that results in the best F1. If number of predicted relations > number of actual relations, only the first n_a predictions were kept; if fewer, missing relations were represented by tokens labeled Other (O).

**Interpretation**: Models were ranked by F1 performance on the competition test set (binary F1 for Subtask 1, macro F1 for Subtask 2). Higher F1 indicates better performance. Reported top test F1 scores were 86.19% (Subtask 1) and 54.15% (Subtask 2).

**Baseline Results**: Subtask 1: BERT baseline F1 = 81.20%, LSTM baseline F1 = 78.22%. Subtask 2: Random baseline F1 = 0.45%.

**Validation**: Inter-annotator agreement reported: Subtask 1 Krippendorff's Alpha (K-Alpha) = 34.99%. Subtask 2 agreement metrics: Exact Match (EM) = 6.96%, One-Side Bound (OSB) = 23.27%, Token Overlap (TO) = 27.31%, K-Alpha = 46.27%. Competition had a trial period and a test period; validation labels were released on August 01, 2022 for trial use; test submissions on Codalab were limited (each participant allowed 5 submissions for test).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
