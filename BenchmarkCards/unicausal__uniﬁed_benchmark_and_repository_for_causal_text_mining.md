# UniCausal: Uniﬁed Benchmark and Repository for Causal Text Mining

## 📊 Benchmark Details

**Name**: UniCausal: Uniﬁed Benchmark and Repository for Causal Text Mining

**Overview**: We propose UniCausal, a uniﬁed benchmark for causal text mining across three tasks: (I) Causal Sequence Classification, (II) Cause-Eﬀect Span Detection and (III) Causal Pair Classiﬁcation. We consolidated and aligned annotations of six high quality, mainly human-annotated, corpora, resulting in a total of 58,720, 12,144 and 69,165 examples for each task respectively.

**Data Type**: text (annotated sequences with BIO cause/effect spans and causal pair labels)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- AltLex
- BECAUSE 2.0
- CausalTimeBank (CTB)
- EventStoryLine (ESL)
- Penn Discourse Treebank V3.0 (PDTB)
- SemEval 2010 Task 8 (SemEval)
- CauseNet
- CausalNet
- CausalBank
- FrameNet
- ConceptNet
- FinCausal
- Causal News Corpus
- Son Facebook dataset

**Resources**:
- [GitHub Repository](https://github.com/tanfiona/UniCausal)
- [Resource](https://arxiv.org/abs/2208.09163)

## 🎯 Purpose and Intended Users

**Goal**: Provide a uniﬁed benchmark and resource for causal text mining by consolidating six corpora and aligning annotations to support three tasks (Sequence Classification, Span Detection, Pair Classification), enabling fair comparison and joint model development.

**Target Audience**:
- Researchers

**Tasks**:
- Causal Sequence Classification
- Cause-Effect Span Detection
- Causal Pair Classification

**Limitations**: We only focus on examples that were of three or shorter sentences. At the current stage, we focus on examples with up to three cause-effect relations only. The baseline token classification set-up was too simplistic, and unable to handle multiple cause-effect span relations in the same sequence.

## 💾 Data

**Source**: AltLex; BECAUSE 2.0; CausalTimeBank (CTB); EventStoryLine (ESL); Penn Discourse Treebank V3.0 (PDTB); SemEval 2010 Task 8 (SemEval)

**Size**: 58,720 examples (Sequence Classification), 12,144 examples (Span Detection), 69,165 examples (Pair Classification)

**Format**: Final post-processed datasets stored in CSV. Original source formats include BECAUSE 'brat', ESL 'CAT', CTB 'TimeML'/'XML', PDTB standoff annotations, AltLex CSV, SemEval JSON.

**Annotation**: Mainly human-annotated (with the exception of CTB). Spans converted to BIO-format for two types (Cause (C), Effect (E)) resulting in labels B-C, I-C, B-E, I-E, O. Sequence and pair examples annotated with binary Causal / Non-causal labels.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (BERT fine-tuning baselines)
- Automated metrics (precision/recall/F1/accuracy)
- Evaluation across five random seeds (report mean and standard deviation)

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- Macro Precision
- Macro Recall
- Macro F1

**Calculation**: Sequence and Pair Classiﬁcation: Cross-Entropy (CE) loss with logits from pooled [CLS] embedding. Span Detection: token-level Cross-Entropy loss over BIO-CE labels; predictions obtained via argmax. Span evaluation uses seqeval to revert BIO labels to Cause and Effect spans and reports Macro P/R/F1. Span evaluation is performed at the 'ungrouped' level so every causal relation is evaluated equally.

**Interpretation**: Higher Precision/Recall/F1 indicate better causal detection. Across tasks, pair classiﬁcation yields higher F1 than sequence classiﬁcation; span detection yields substantially lower Macro F1 indicating greater difficulty in identifying exact cause/effect spans.

**Baseline Results**: Baselines (BERT fine-tuned) achieved 70.10% Binary F1 for Sequence Classification, 52.42% Macro F1 for Span Detection, and 84.68% Binary F1 for Pair Classification (averaged across test sets, reported with mean and standard deviation over five random seeds).

**Validation**: Reported mean and standard deviation across five random seeds. Train/test splits used previous works' recommendations where available, otherwise random splits. Span evaluation performed at the ungrouped level to evaluate each causal relation equally.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of testing diversity, Lack of data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
