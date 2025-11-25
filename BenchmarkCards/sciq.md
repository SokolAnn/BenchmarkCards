# SciQ

## 📊 Benchmark Details

**Name**: SciQ

**Overview**: A dataset of 13,679 multiple choice science exam questions (SciQ) created via a two-step crowdsourcing method that leverages a corpus of science study textbooks and model-suggested document selection and answer-distractor choices to aid crowd workers in producing high-quality, domain-targeted multiple choice science questions.

**Data Type**: multiple choice question-answer pairs (text)

**Domains**:
- Natural Language Processing
- Education
- Science Education

**Similar Benchmarks**:
- SQuAD
- MS MARCO
- Wikireading
- WikiQA

**Resources**:
- [Resource](http://allenai.org/data.html)
- [Resource](https://arxiv.org/abs/1707.06209)

## 🎯 Purpose and Intended Users

**Goal**: Provide a method for crowdsourcing high-quality, domain-targeted multiple-choice science questions and release SciQ, a dataset of 13,679 such questions for research.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Education Researchers

**Tasks**:
- Question Answering
- Reading Comprehension
- Multiple Choice Question Answering

**Limitations**: A small percentage of passages were unreleasable, making the direct-answer version smaller (10,481 train, 887 dev, 884 test).

## 💾 Data

**Source**: Crowdsourced multiple-choice science exam questions created from passages drawn from a base corpus of 28 science study textbooks (including OpenStax and CK-12) using Amazon Mechanical Turk. The crowdsourcing process was aided by a distractor-ranking model trained on existing science exam questions.

**Size**: 13,679 multiple choice questions (direct-answer version: 10,481 train, 887 dev, 884 test)

**Format**: N/A

**Annotation**: Annotated via crowdsourcing on Amazon Mechanical Turk in a two-stage process: (1) workers select a passage and formulate a question and correct answer; (2) separate workers validate the question and produce/validate distractors, aided by model-suggested distractors.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (state-of-the-art QA and reading comprehension models)
- Human evaluation

**Metrics**:
- Accuracy
- Exact Match
- F1 Score
- Validation Accuracy

**Calculation**: Accuracy computed as percentage of correctly answered multiple-choice questions. Exact Match and F1 computed for the direct-answer setting as in SQuAD. Validation accuracy reported for the distractor-ranking model on an 80/20 split of training questions.

**Interpretation**: Higher Accuracy indicates better multiple-choice selection performance. Improvements in Accuracy when augmenting training data with SciQ indicate that SciQ provides useful in-domain training data for answering real science exam questions.

**Baseline Results**: Multiple-choice test set accuracies: Lucene (80.0), Aristo (77.4), AS Reader (74.1), GA Reader (73.8), TableILP (31.8), Humans 87.8 ± 0.045. Direct-answer (BiDAF) on SciQ: Exact Match 66.7%, F1 Score 75.7%. Adding SciQ to 4th-grade training improved AS Reader from 40.7% to 45.0% and GA Reader from 37.6% to 45.4%; adding SciQ to 8th-grade training improved AS Reader from 41.2% to 43.0% and GA Reader from 41.0% to 44.3%.

**Validation**: Dataset split: 1,000 questions for validation and 1,000 for test, remainder for training. Distractor model trained on 3,705 science exam questions with an 80%/20% train/validation split. Qualitative human evaluation: 100 original vs 100 crowdsourced question pairs judged by humans. Early stopping used for model training based on validation performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Laws

**Atlas Risks**:
- **Data Laws**: Data usage restrictions

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Source study books include OpenStax and CK-12 under Creative Commons licenses (CK-12: Creative Commons Attribution-Non-Commercial 3.0 Unported). Some source passages were unreleasable, reducing the size of the direct-answer release.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
