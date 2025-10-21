# The NarrativeQA Reading Comprehension Challenge

## 📊 Benchmark Details

**Name**: The NarrativeQA Reading Comprehension Challenge

**Overview**: A new dataset and set of tasks in which readers must answer questions about stories (books and movie scripts). Tasks are designed so that answering requires understanding the underlying narrative across full documents rather than relying on shallow pattern matching or local context similarity.

**Data Type**: text (question-answering pairs; full-length books and movie scripts and plot summaries)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MCTest
- CNN/Daily Mail
- Children’s Book Test (CBT)
- BookTest
- SQuAD
- NewsQA
- MS MARCO
- SearchQA
- MovieQA

**Resources**:
- [Resource](https://arxiv.org/abs/1712.07040)
- [Resource](http://www.gutenberg.org/)
- [Resource](http://www.imsdb.com/)
- [Resource](http://www.dailyscript.com/)
- [Resource](http://www.awesomefilm.com/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reading comprehension dataset and tasks that require narrative-level understanding of long documents (books and movie scripts), encouraging development of models that integrate information across full stories rather than rely on superficial cues.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Machine Reading / Natural Language Processing Community

**Tasks**:
- Reading Comprehension
- Question Answering
- Answer Generation
- Answer Selection (Ranking)

**Limitations**: Dataset size limited by availability of corresponding summaries; the full-story reading task is currently intractable for existing neural models without retrieval or other scalable approaches.

## 💾 Data

**Source**: Stories (books from Project Gutenberg and movie scripts scraped from the web) matched to plot summaries from Wikipedia; question–answer pairs collected from Amazon Mechanical Turk based solely on summaries. Stories and summaries were matched and verified by human annotators.

**Size**: 1,567 stories; 46,765 question–answer pairs. Train: 1,102 documents (32,747 QAs); Validation: 115 documents (3,461 QAs); Test: 355 documents (10,557 QAs). Avg. #tokens in stories: ~57,780–62,743; Avg. #tokens in summaries: ~638–659.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk: annotators wrote questions and answers based solely on summaries (instructions and JavaScript constraints prevented copying). Multiple annotators produced approximately 30 Q-A pairs per summary and a second reference answer was collected for each question (annotators also judged answerability).

## 🔬 Methodology

**Methods**:
- Automated metrics for generated text
- Ranking evaluation (answer selection)
- Information retrieval baselines
- Neural model baselines (Seq2Seq, Attention Sum Reader, span-prediction models)
- Human baseline

**Metrics**:
- BLEU-1
- BLEU-4
- Meteor
- ROUGE-L
- Mean Reciprocal Rank (MRR)

**Calculation**: Generated-answer metrics computed using two reference answers per question (except human baseline which uses one reference vs the other). Candidates and references lowercased, end-of-sentence marker and final full stop removed. MRR computed by ranking answers associated with the same summary/story and taking mean reciprocal rank.

**Interpretation**: Higher scores are better for all metrics. Human performance is reported by scoring the second reference against the first. Models are compared to oracle IR models and human baselines to quantify gap.

**Validation**: Dataset partitioned into non-overlapping training, validation, and test sets by stories/summaries. Models tuned on the validation set; model selection reported using either ROUGE-L or MRR as selection criteria. Human baseline obtained by comparing reference answers.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Named entities in narratives are replaced with generic entity markers (e.g., @entity42) which are permuted during training and testing; entities are replaced according to a heuristic based on capitalization and lowercase occurrence.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
