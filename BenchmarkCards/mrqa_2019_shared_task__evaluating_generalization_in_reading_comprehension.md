# MRQA 2019 Shared Task: Evaluating Generalization in Reading Comprehension

## 📊 Benchmark Details

**Name**: MRQA 2019 Shared Task: Evaluating Generalization in Reading Comprehension

**Overview**: The MRQA 2019 Shared Task evaluates the generalization capabilities of reading comprehension systems by adapting and unifying 18 distinct question answering datasets into a single, unified extractive QA format and testing systems on held-out out-of-domain datasets.

**Data Type**: text (extractive question-answering pairs: question, context passage, answer span)

**Domains**:
- Natural Language Processing
- Healthcare
- Education

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- NewsQA
- TriviaQA
- SearchQA
- HotpotQA
- Natural Questions
- BioASQ
- DROP
- DuoRC
- RACE
- RelationExtraction
- TextbookQA
- BioProcess
- ComplexWebQuestions
- MCTest
- QAMR
- QAST
- TREC

**Resources**:
- [GitHub Repository](https://github.com/mrqa/MRQA-Shared-Task-2019)
- [Resource](https://worksheets.codalab.org)
- [Resource](http://catalog.elra.info)
- [Resource](https://arxiv.org/abs/1910.09753)

## 🎯 Purpose and Intended Users

**Goal**: Test extractive question answering models on their ability to generalize to data distributions different from the distribution on which they were trained (evaluate out-of-domain generalization).

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Question Answering
- Reading Comprehension
- Extractive Question Answering

**Limitations**: The shared task is restricted to English-language extractive question answering; passages are concatenated and truncated to the first 800 tokens; the task does not test unanswerable, multi-turn, or open-domain question types.

**Out of Scope Uses**:
- Unanswerable question evaluation
- Multi-turn question answering
- Open-domain question answering

## 💾 Data

**Source**: Adapted and unified 18 sub-domain QA datasets (see Table 1): SQuAD, NewsQA, TriviaQA, SearchQA, HotpotQA, Natural Questions, BioASQ, DROP, DuoRC, RACE, RelationExtraction, TextbookQA, BioProcess, ComplexWebQuestions, MCTest, QAMR, QAST, TREC.

**Size**: Varies by sub-domain (per Table 1). Examples: SQuAD: 86,588 train / 10,507 dev; NewsQA: 74,160 train / 4,212 dev; TriviaQA: 61,688 train / 7,785 dev; SearchQA: 117,384 train / 16,980 dev; HotpotQA: 72,928 train / 5,904 dev; Natural Questions: 104,071 train / 12,836 dev. Testing portions of Splits II and III were balanced to 1,500 examples per sub-domain.

**Format**: Unified extractive QA format (question, context, answer string/span). Contexts concatenated and truncated to first 800 tokens; documents separated with [DOC], titles with [TLE], paragraphs with [PAR].

**Annotation**: Uses original dataset annotations where available. For datasets without labeled answer spans, all occurrences of the answer string in the context are provided. Multiple-choice datasets: keep correct answer if contained in context and discard other options; random examples manually verified for quality.

## 🔬 Methodology

**Methods**:
- Automated evaluation metrics (Exact Match, word-level F1 Score)
- Macro-averaged test F1 ranking across 12 held-out test datasets
- Baseline multi-task BERT-based model evaluation
- Meta-analysis of submitted systems (techniques included data sampling, multi-task learning, adversarial training, ensembling)

**Metrics**:
- Exact Match (EM)
- Word-level F1 Score (F1)
- Macro-averaged F1 across the 12 hidden test datasets (used for final ranking)

**Calculation**: Follow SQuAD evaluation normalization rules (ignore articles and punctuation). EM requires exact answer string match; F1 measures token-level overlap with gold answer(s). Scores are macro-averaged across the 12 test datasets for final ranking. Scoring is based on answer string match rather than token index match in the context.

**Interpretation**: Higher EM and F1 indicate better extractive QA performance. Systems are ranked by macro-averaged F1 across the 12 held-out test datasets to measure out-of-domain generalization. The paper reports absolute improvements over the provided BERT baselines (e.g., best system improved by 10.7 F1 over baseline).

**Baseline Results**: Ours: BERT-Large baseline achieved 61.8 macro-averaged F1 on the combined Split II + III test (12 datasets). Ours: BERT-Base baseline achieved 58.5 macro-averaged F1 on Split II + III. The top submitted system (D-Net) achieved 72.5 macro-averaged F1 on Split II + III.

**Validation**: Participants trained on a fixed training split of six datasets and were evaluated on 12 held-out datasets (six with dev data, six fully hidden). Test splits for Splits II and III were balanced to 1,500 examples per sub-domain; partitioning was done by context so no context is shared across development and testing portions to avoid leakage.

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
