# WIKITABLE QUESTIONS

## 📊 Benchmark Details

**Name**: WIKITABLE QUESTIONS

**Overview**: A new task and dataset: answering complex questions on semi-structured HTML tables using question-answer pairs as supervision.

**Data Type**: question-answering pairs (text) on semi-structured HTML tables

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- WEBQUESTIONS
- FREE917
- Geoquery
- Freebase

**Resources**:
- [Resource](http://nlp.stanford.edu/software/sempre/wikitable/)
- [Resource](https://www.codalab.org/worksheets/0xf26cd79d4d734287868923ad1067cf4c/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and train semantic parsers that answer complex, compositional questions using semi-structured HTML tables as the knowledge source, learned from question-table-answer triples.

**Tasks**:
- Question Answering
- Semantic Parsing

**Limitations**: Authors state that 21% of examples cannot be answered using any logical form generated from the current deduction rules. Annotation artifacts and unhandled question types (e.g., yes-no questions, phrases like "same" or "consecutive"), complex cell formats, and incorrect annotations are noted in Section 7.4. Approximately 69% of the questions remain after answer-agreement filtering.

## 💾 Data

**Source**: Randomly selected HTML tables from Wikipedia (tables with at least 8 rows and 5 columns); question-answer pairs authored and validated via Amazon Mechanical Turk.

**Size**: 22,033 question-answer pairs on 2,108 HTML tables (20% of tables held out as test set)

**Format**: HTML tables (preprocessed: non-textual contents omitted; merged cells unmerged and duplicated into unmerged cells)

**Annotation**: Two-stage Amazon Mechanical Turk: (1) workers wrote trivia questions about each table using one of 36 generic prompts; (2) separate workers answered each question based on the table. Answers were kept only if agreed upon by at least two workers; approximately 69% of questions remain after this filtering.

## 🔬 Methodology

**Methods**:
- Automated evaluation (Accuracy, Oracle score)
- Comparison to baselines (IR baseline, WQ baseline)
- Development using three random 80:20 splits of the training data; held-out test tables (20% of tables)

**Metrics**:
- Accuracy
- Oracle score

**Calculation**: Accuracy: number of examples (x,t,y) on which the system outputs the correct answer y. Oracle score: number of examples where at least one generated candidate logical form z in Z_x executes to y.

**Interpretation**: Accuracy measures final output correctness; oracle score measures whether a correct logical form was generated among candidates (an upper bound on generation coverage).

**Baseline Results**: On test data: IR baseline accuracy 12.7% (oracle 70.6%), WQ baseline accuracy 24.3% (oracle 35.6%), Our system accuracy 37.1% (oracle 76.6%).

**Validation**: 20% of tables and their questions set aside as test set. Development used three random 80:20 splits of the remaining training data. Evaluation ensures tables in test do not appear during training.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
