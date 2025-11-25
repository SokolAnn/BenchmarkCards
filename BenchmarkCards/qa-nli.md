# QA-NLI

## 📊 Benchmark Details

**Name**: QA-NLI

**Overview**: Automatically deriving large-scale Natural Language Inference (NLI) datasets from existing question answering (QA) datasets by learning a sentence transformation model (QA2D) that converts question-answer pairs into declarative sentences, producing a new freely available dataset of over 500k NLI examples.

**Data Type**: question-answering pairs converted to premise-hypothesis (declarative sentence) pairs

**Domains**:
- Movie plots
- Newswire text
- Wikipedia
- English exams
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SNLI
- MultiNLI
- SciTail

**Resources**:
- [Resource](https://bit.ly/2OMm4vK)
- [Resource](https://arxiv.org/abs/1809.02922)

## 🎯 Purpose and Intended Users

**Goal**: To augment and diversify NLI datasets by automatically deriving large-scale NLI datasets from existing question answering datasets using a QA2D sentence transformation model.

**Tasks**:
- Natural Language Inference
- Sentence transformation (question-answer pair to declarative sentence)

**Limitations**: When performing automated QA2D, only a two-way distinction between entailment and non-entailment can be reliably made.

## 💾 Data

**Source**: Converted from five QA datasets: SQuAD, MovieQA, NewsQA, QAMR, and RACE (as described in Table 1).

**Size**: Over 500,000 NLI examples derived in total; additionally collected 100,000 human-annotated (Q, A, D) triples used to train the QA2D model.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk. Two collection setups: Setup S (write declarative sentence from scratch) and Setup E (post-edit rule-based output). Dev/test examples have three human annotations; training examples largely one annotation. Setup S was used for evaluation data.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Crowdsourced human evaluation (Amazon Mechanical Turk)
- Model-based evaluation (rule-based baseline vs neural sequence model)

**Metrics**:
- BLEU Score
- Exact match (string match ignoring case and punctuation)
- Human rating scales for grammaticality, naturalness, and completeness (1-5)

**Calculation**: BLEU and string match (ignoring case and punctuation). Exact match is percentage of model outputs that exactly match the human gold answer. Human agreement computed as maximum BLEU when comparing each of 3 human annotations against the two others; model outputs compared against the 3 human annotations. Models evaluated on top-1 output and top-5 beam (best of beam).

**Interpretation**: Higher BLEU and higher exact match indicate closer match to human-produced declarative sentences. Human ratings use 1-5 scales for grammaticality, naturalness, and completeness (e.g., 4 = 'Good but slightly unnatural').

**Baseline Results**: Neural QA2D model outperforms rule-based: on average +2.6 BLEU points and +6.2% exact match. Reported top-1 BLEU per dataset ranges ~80–86 and exact match ranges ~30–57; top-5 BLEU up to ~91 and top-5 exact match up to ~67 (see Table 4).

**Validation**: Evaluated on a held-out test set composed from all five QA datasets with three human annotations per example; additional crowdsourced human evaluation for grammaticality/naturalness/completeness; crowdsourced labeling of 2000 premise-hypothesis pairs to validate inference label assumptions; analyses of annotation artifacts compared to SNLI/MultiNLI.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Annotation artifacts
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
