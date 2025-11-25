# Zero-Shot Relation Extraction via Reading Comprehension

## 📊 Benchmark Details

**Name**: Zero-Shot Relation Extraction via Reading Comprehension

**Overview**: The paper reduces relation extraction to answering reading-comprehension questions by associating one or more natural-language questions with each relation slot, enabling (1) training relation-extraction models using neural reading-comprehension techniques, (2) building very large training sets by combining relation-specific crowd-sourced questions with distant supervision, and (3) zero-shot learning by extracting new relation types specified at test-time for which no labeled training examples exist.

**Data Type**: text (question-answering pairs)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- WikiReading
- SQuAD
- Simple QA
- InfoboxQA
- QA-SRL

**Resources**:
- [Resource](https://nlp.cs.washington.edu/zeroshot)
- [Resource](https://arxiv.org/abs/1706.04115)

## 🎯 Purpose and Intended Users

**Goal**: Enable relation extraction via reading comprehension questions, including zero-shot extraction of relation types defined at test-time, by creating a large question-sentence-answer dataset and adapting reading-comprehension models to decide answerability.

**Target Audience**:
- Machine Learning Researchers
- Information Extraction Researchers
- Machine Reading Researchers
- Application Developers

**Tasks**:
- Relation Extraction
- Question Answering
- Reading Comprehension
- Slot Filling

**Limitations**: Zero-shot generalization to unseen relation types is possible but at lower accuracy levels; dataset contains annotation errors (e.g., missing entries in Wikidata) and noisy distant supervision; some model errors arise from inaccurate span selection.

## 💾 Data

**Source**: Slot-filling examples derived from the WikiReading dataset, which aligns Wikidata relations with corresponding Wikipedia articles; question templates collected via crowdsourcing (Mechanical Turk) and instantiated over WikiReading examples.

**Size**: Over 30,000,000 question-sentence-answer examples in total; 1,192 validated question templates spanning 120 relations; over 2,000,000 generated negative examples.

**Format**: N/A

**Annotation**: Schema-level crowdsourced annotation via Amazon Mechanical Turk (collection and verification phases) combined with distant supervision from WikiReading to select sentences; verification required majority-correct answers (6/10) and token-overlap F1 filter.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation (Precision/Recall/F1)
- Model-based evaluation (reading-comprehension models adapted from BiDAF)
- Comparison to baseline systems (Random NE, RNN Labeler, Miwa & Bansal variants)
- Cross-partition experiments (unseen entities, unseen question templates, unseen relations)

**Metrics**:
- Precision
- Recall
- F1
- Token-overlap F1

**Calculation**: Each instance is evaluated by comparing the tokens in the labeled answer set with those of the predicted span. Precision = true positives / number of times the system returned a non-null answer. Recall = true positives / number of instances that have an answer. Token-overlap F1 used as a secondary filter in template verification.

**Interpretation**: Higher Precision/Recall and F1 indicate better extraction performance. The approach generalizes to new question paraphrases with minor F1 loss; zero-shot extraction of unseen relations yields substantially lower F1 (paper reports up to 41% F1 in zero-shot cases), setting a baseline for future work.

**Baseline Results**: Unseen entities (Table 1): KB Relation F1 90.29%, NL Relation F1 89.60%, Multiple Templates F1 89.44%, Question Ensemble F1 89.80%; RNN Labeler F1 62.40%, Miwa & Bansal F1 72.87%. Seen vs Unseen questions (Table 2): Seen F1 86.63%, Unseen F1 83.10%. Unseen relations zero-shot (Table 3): Multiple Templates F1 39.61%, Question Ensemble F1 41.11%, Single Template F1 33.90%, NL Relation F1 33.40%, KB Relation F1 4.32%, Miwa & Bansal F1 0.00%.

**Validation**: Question templates verified by sampling sentences and requiring majority-correct answers (6/10) and token-overlap F1 >= 0.75 as a secondary filter; experiments use train/dev/test partitions (including 10-fold splits for unseen-questions and unseen-relations experiments) and stratified sampling along entities or relations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
