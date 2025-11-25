# BoolQ (Boolean Questions)

## 📊 Benchmark Details

**Name**: BoolQ (Boolean Questions)

**Overview**: We build a reading comprehension dataset, BoolQ, of naturally occurring yes/no questions. Each question is paired with a paragraph from Wikipedia that an independent annotator has marked as containing the answer. The task is to take a question and passage as input, and to return “yes” or “no” as output.

**Data Type**: question-passage pairs (text)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- Natural Questions (NQ)
- CoQA
- QuAC
- HotPotQA
- ShARC
- MS Marco
- MultiNLI
- SNLI
- SQuAD 1.1
- SQuAD 2.0
- RACE
- QQP

**Resources**:
- [Resource](https://goo.gl/boolq)
- [Resource](https://arxiv.org/abs/1905.10044)

## 🎯 Purpose and Intended Users

**Goal**: To test models on their ability to answer naturally occurring yes/no questions by providing a reading comprehension dataset of such questions paired with supporting passages.

**Tasks**:
- Question Answering
- Reading Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: Questions gathered from anonymized, aggregated queries to the Google search engine heuristically filtered for yes/no queries; kept when a Wikipedia page was returned among the top five results and paired with a paragraph from that Wikipedia article selected by annotators. Combined with 3k yes/no questions from the Natural Questions training set.

**Size**: 16,000 examples (9,400 train, 3,200 dev, 3,200 test)

**Format**: N/A

**Annotation**: Single annotator labels produced via a three-step process: (1) decide if the question is 'good' (comprehensible, unambiguous, requesting factual information) before seeing the page; (2) for good questions, find a passage within the document that contains enough information to answer the question or mark as 'not answerable'; (3) mark whether the question's answer is 'yes' or 'no'. Authors labeled 110 random examples for quality assessment and reached 90% agreement with the gold-standard labels.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Transfer learning experiments

**Metrics**:
- Accuracy

**Calculation**: Accuracy computed as percentage of examples with correct yes/no prediction. Model results are averaged over five runs for reported experiments.

**Interpretation**: Higher Accuracy indicates better performance on the yes/no QA task. The paper reports a majority-baseline of ~62%, model results (best) of 80.43% accuracy, and human annotator accuracy of 90%, indicating a significant gap between models and humans.

**Baseline Results**: Majority baseline: 62.31% (test). Recurrent model: 67.52% (test). Recurrent + MultiNLI: 74.24% (test). Pre-trained BERT L: 76.70% (test). Pre-trained BERT L + MultiNLI: 80.43% (test). Results averaged over five runs unless otherwise noted.

**Validation**: Dataset split into train (9.4k), dev (3.2k), test (3.2k); questions from Natural Questions kept in train. Annotation quality assessed by three authors labeling 110 random examples achieving 90% agreement with gold-standard; model results averaged over five runs.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Questions are gathered from anonymized, aggregated queries to the Google search engine.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
