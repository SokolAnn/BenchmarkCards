# QuAC : Question Answering in Context

## 📊 Benchmark Details

**Name**: QuAC : Question Answering in Context

**Overview**: We present QuAC, a dataset for Question Answering in Context that contains 14K information-seeking QA dialogs (100K questions in total). The dialogs involve two crowd workers: (1) a student who poses a sequence of freeform questions to learn as much as possible about a hidden Wikipedia text, and (2) a teacher who answers the questions by providing short excerpts from the text.

**Data Type**: question-answering pairs (multi-turn text-based dialogs with answer spans and dialog acts)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CoQA
- SQuAD 2.0
- SQuAD
- TriviaQA
- NewsQA
- MS Marco
- NarrativeQA
- CSQA
- CQA
- SQA

**Resources**:
- [Resource](http://quac.ai)
- [Resource](http://quac.ai/datasheet.pdf)
- [Resource](https://arxiv.org/abs/1808.07036)

## 🎯 Purpose and Intended Users

**Goal**: Introduce QuAC, a large-scale dataset of information-seeking dialogs over sections from Wikipedia articles to enable research on Question Answering in Context (multi-turn, dialog-based reading comprehension).

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Question Answering
- Reading Comprehension
- Dialog Systems

**Limitations**: Filtering steps bias the data towards articles about people (entertainers); teachers must select contiguous spans (limits expressivity of answers); maximum answer length set to 30 tokens. Training sections can be shorter than evaluation sections due to allowing multiple dialogs per section only in training.

## 💾 Data

**Source**: Sections from Wikipedia articles (articles selected using Wikimedia tools and filtered by category and popularity). Dialogs were collected via Amazon Mechanical Turk with two crowd workers playing teacher and student roles.

**Size**: Approximately 13,594 dialogs; 98,407 questions/answer pairs (train/dev/test splits: 83,568 / 7,354 / 7,353 questions; dialogs: 11,567 / 1,000 / 1,002); 8,854 unique sections overall; average tokens / section: 401.0; average tokens / answer: 14.6.

**Format**: N/A

**Annotation**: Teacher-provided answer spans (contiguous span indices into the section text) and dialog acts (continuation: follow up/maybe follow up/don't follow up; affirmation: yes/no/neither; answerability: answerable/no answer). Validation collected four additional annotations per question (dev/test have five references each).

## 🔬 Methodology

**Methods**:
- Automated metrics (word-level F1)
- Human evaluation (human upper bound, Human Equivalence Score HEQ-Q and HEQ-D)
- Accuracy for dialog act prediction

**Metrics**:
- Word-level F1
- Human Equivalence Score (HEQ-Q, HEQ-D)
- Accuracy (for dialog acts)

**Calculation**: Word-level F1 computed similarly to SQuAD: precision and recall computed from overlapping words between prediction and references after removing stop-words; for no-answer questions, system gets F1=1 if correctly predicts no-answer and 0 otherwise. Maximum F1 among references is used; to make oracle human and system comparable given n references, report average of the maximum F1 computed from each n-1 subset with respect to the held-out reference. HEQ measures percentage of examples (HEQ-Q) or dialogs (HEQ-D) where system F1 meets or exceeds human F1. Dialog act accuracy computed with respect to majority annotation.

**Interpretation**: Higher word-level F1 indicates closer match to reference answers; HEQ-Q and HEQ-D measure whether system output is as good as average human (HEQ-D of 100 means system matches average human quality across entire dialogs). The paper reports a human upper bound of 80.8 F1 and states the best model underperforms humans by ~20 F1, indicating significant room for improvement.

**Baseline Results**: BiDAF++ (w/ 2-ctx) — 60.6 F1 (dev) / 60.1 F1 (test). BiDAF++ (no context) — 51.8 / 50.2 F1. Gold sentence + NA upper bound — 72.4 / 72.7 F1. Human performance — 80.8 / 81.1 F1. (See Table 4 in paper for full baseline comparisons.)

**Validation**: Collected four additional annotations per question for validation; dev and test questions have five reference answers each. Questions with human F1 lower than 40 were excluded from evaluation (removing ~10% of noisy annotations). Validation workers did not maintain dialog context when providing annotations.

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
