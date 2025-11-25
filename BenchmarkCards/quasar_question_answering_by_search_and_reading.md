# QUASAR (QUestion Answering by Search And Reading)

## 📊 Benchmark Details

**Name**: QUASAR (QUestion Answering by Search And Reading)

**Overview**: We present two new large-scale datasets aimed at evaluating systems designed to comprehend a natural language query and extract its answer from a large corpus of text. The QUASAR-S dataset consists of 37,362 cloze-style queries constructed from definitions of software entity tags on StackOverflow with the StackOverflow posts/comments as the background corpus. The QUASAR-T dataset consists of 43,012 trivia questions and their answers obtained from various internet sources with ClueWeb09 as the background corpus. The datasets are posed as a challenge for two related subtasks: (1) searching for relevant pieces of text that include the correct answer to a query, and (2) reading the retrieved text to answer the query.

**Data Type**: question-answering pairs (with background corpora of web/forum documents as context)

**Domains**:
- Natural Language Processing
- Information Retrieval
- Computer Programming

**Languages**:
- English

**Similar Benchmarks**:
- CNN / DailyMail
- SQuAD
- MS MARCO
- TriviaQA
- SearchQA
- WikiQA
- MOVIES QA
- Who-Did-What
- NewsQA
- Children's Book Test (CBT)

**Resources**:
- [GitHub Repository](https://github.com/bdhingra/quasar)
- [Resource](https://arxiv.org/abs/1707.03904)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research into two related subtasks for factoid question answering from large corpora: (1) searching a large corpus of text for relevant passages that may contain candidate answers, and (2) reading the retrieved passages to extract answers. To enable study of whether joint training/integration of search and reading components improves end-task performance.

**Target Audience**:
- Researchers

**Tasks**:
- Information Retrieval
- Reading Comprehension
- Question Answering

**Limitations**: QUASAR-S: Cloze generation heuristic is noisy and clozes for terms common in English were discarded (dataset omits clozes for many common English terms). QUASAR-T: raw trivia collection was noisy and was filtered to remove unparseable entries and multiple-choice/True-False questions. Evaluation for QUASAR-T is imperfect (preprocessing can penalize equivalent but differently-formatted answers, e.g. '0' vs 'zero'). Some questions were discarded if retrieval produced zero results. Human evaluation is limited by experts' knowledge and by the usefulness of the provided search over short pseudo-documents.

## 💾 Data

**Source**: QUASAR-S: Cloze questions constructed from StackOverflow tag 'excerpt' entries; background corpus built from top 50 StackOverflow threads per entity (questions, answers, comments). QUASAR-T: Trivia questions sourced from a Reddit user collection (007craft) and other internet sources; background corpus is ClueWeb09 (about 1 billion web pages). Retrieved documents (short and long pseudodocuments) for each question are provided.

**Size**: QUASAR-S: 37,362 questions (31,049 train / 3,174 validation / 3,139 test). QUASAR-T: 43,012 questions (37,012 train / 3,000 validation / 3,000 test). Background corpus: ClueWeb09 (~1 billion web pages) used for QUASAR-T; QUASAR-S background: top 50 threads per tag from StackOverflow.

**Format**: N/A

**Annotation**: Human annotations collected on subsets of the development sets: QUASAR-S: 226 relation annotations for 136 questions (27 discarded due to ties, 109 annotated questions remaining). QUASAR-T: 144 annotated questions (12 marked ambiguous, 132 non-ambiguous remaining) with 214 genre annotations and 122 entity-type annotations after discards. Retrieved documents and the authors' retrieved documents per question are included in the release.

## 🔬 Methodology

**Methods**:
- Automated metrics (exact match, F1, accuracy)
- Human evaluation (closed-book experts and open-book non-experts)
- Baseline system evaluation (heuristic baselines, n-gram and RNN language models, neural reading comprehension models such as GA Reader and BiDAF)

**Metrics**:
- Accuracy
- Exact Match
- F1 Score

**Calculation**: QUASAR-S: report average Accuracy of predictions since answers come from a fixed output vocabulary. QUASAR-T: preprocessing removes punctuation, whitespace and definite/indefinite articles from answer strings; Exact Match measures equality of preprocessed strings; F1 Score is computed by constructing a bag of tokens for each preprocessed string and measuring token overlap F1 between predicted and gold answer.

**Interpretation**: Overall performance is the product of Search Accuracy (fraction of instances where the correct answer is present in the retrieved context) and Reading Accuracy (accuracy of extracting the answer given it is present). Retrieving more documents increases Search Accuracy but tends to decrease Reading Accuracy; thus good overall performance requires balancing retrieval and reading. Human performance is reported for closed-book experts and open-book non-experts for comparison.

**Baseline Results**: Best automatic baselines achieve 33.6% Accuracy on QUASAR-S and 28.5% F1 on QUASAR-T (BiRNN for QUASAR-S at 33.6% overall; BiDAF achieves 28.5% F1 on QUASAR-T). Neural readers achieve higher Reading Accuracy when the answer is in context (e.g., GA Reader reading accuracy ~48.3% on QUASAR-S instances with answer-in-context), but Search Accuracy limits overall results. Human performance reported: QUASAR-S ~50% (non-expert open-book 50.0% / expert closed-book 46.8% reported in paper) and QUASAR-T ~60.4% (expert closed-book 60.4% / non-expert open-book 60.6% reported in paper). Baseline gaps: baselines lag human performance by 16.4% (QUASAR-S) and 32.1% (QUASAR-T).

**Validation**: Datasets split into training, validation and test sets (QUASAR-S and QUASAR-T splits provided). The number of retrieved context documents (short/long pseudodocuments) was tuned on the validation set to maximize overall accuracy. Questions with zero retrieval results for the indexing/query procedure were discarded during construction. Human evaluation and annotations were collected on development subsets.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
