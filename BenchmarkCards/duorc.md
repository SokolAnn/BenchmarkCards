# DuoRC

## 📊 Benchmark Details

**Name**: DuoRC

**Overview**: DuoRC is a novel dataset for Reading Comprehension (RC) designed to motivate new challenges for neural approaches in language understanding. It contains 186,089 question-answer pairs created from 7,680 pairs of movie plots, where each pair consists of two versions of the same movie plot (one from Wikipedia and the other from IMDb). Questions are created from one version and answers are obtained from the other version, ensuring low lexical overlap between questions and answer-containing segments and requiring deeper language understanding, external background/common-sense knowledge, multi-sentence reasoning, and detection of unanswerability.

**Data Type**: question-answering pairs (text)

**Domains**:
- Natural Language Processing

**Languages**:
- N/A

**Similar Benchmarks**:
- SQuAD
- TriviaQA
- MS MARCO
- MovieQA
- NarrativeQA
- NewsQA

**Resources**:
- [Resource](https://duorc.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a Reading Comprehension dataset that introduces challenges not addressed by existing RC datasets, including low lexical overlap between questions and answer spans, the need for background and common-sense knowledge, narrative multi-sentence reasoning, and detection of unanswerable questions.

**Target Audience**:
- Reading Comprehension researchers
- Machine Learning researchers
- Model Developers

**Tasks**:
- Question Answering
- Reading Comprehension

**Limitations**: This dataset is not a substitute for existing RC datasets but can be coupled with them to collectively address a large set of challenges in language understanding with RC.

## 💾 Data

**Source**: Parallel movie plots crawled from Wikipedia and IMDb for movies (retained 7,680 movies where both plots were available and longer than 100 words). QA pairs were collected via Amazon Mechanical Turk in two phases: (i) questions created from the shorter version of a plot (SelfRC) and (ii) answers extracted or synthesized from the longer/paraphrased version by a different set of workers (ParaphraseRC).

**Size**: 186,089 question-answer pairs (from 7,680 movie plot pairs); SelfRC: 85,773 QA pairs; ParaphraseRC: 100,316 QA pairs

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk: two-phase annotation (question creation from shorter plot; answer extraction/synthesis or marking unanswerable from longer plot). Workers could select a span, synthesize an answer, or mark a question not-answerable. Quality control included manual and semi-automated inspections, filtering/blacklisting of low-quality annotators, and a 2-3 week wait between phases to reduce information bias.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation using baseline models (SpanModel — BiDAF-based span prediction; GenModel — two-stage span prediction + answer generation)
- Preprocessing with NLP techniques (coreference resolution, paraphrase matching, relevant-sentence extraction)
- Cross-dataset / cross-testing experiments (train/test on SelfRC, ParaphraseRC, combined)

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy: strict exact-match (predicted answer considered correct only if it exactly matches the true answer). F1 Score: token-level overlap F-score that gives credit for partial overlap between predicted and true answers.

**Interpretation**: Lower Accuracy and F1 on DuoRC indicate the dataset is substantially harder than prior RC datasets; e.g., state-of-the-art RC models that achieve near-human performance on SQuAD perform much worse on DuoRC (illustrative comparison: F1 37.42% on DuoRC vs ~86% on SQuAD as reported in the paper).

**Baseline Results**: Key baselines (from the paper): BiDAF-based SpanModel: SelfRC Span Test Acc 46.14, F1 57.49; SelfRC Full Test Acc 37.53, F1 50.56. GenModel (with augmented training data): SelfRC Full Test Acc 15.31, F1 24.05. ParaphraseRC Span Test SpanModel Acc 17.93, F1 26.27; ParaphraseRC Full Test SpanModel Acc 9.78, F1 16.33. Reported aggregate comparison: F1 score of 37.42% on DuoRC versus ~86% on SQuAD.

**Validation**: Train/validation/test split is done by movies to avoid overlap: 70% train, 15% validation, 15% test (ensuring test set contains no movies seen during training). Annotation quality validation included manual and semi-automated inspections, worker filtering/blacklisting, and a waiting period between annotation phases to reduce bias.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
