# Stanford Question Answering Dataset v1.0 (SQuAD)

## 📊 Benchmark Details

**Name**: Stanford Question Answering Dataset v1.0 (SQuAD)

**Overview**: A new reading comprehension dataset consisting of 100,000+ questions posed by crowdworkers on a set of Wikipedia articles, where the answer to each question is a segment of text (span) from the corresponding reading passage.

**Data Type**: question-answering pairs (span-based answers from Wikipedia passages)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MCTest
- CNN/Daily Mail
- CBT
- WikiQA
- TREC-QA
- BAbI
- Algebra
- Science

**Resources**:
- [Resource](https://stanford-qa.com)
- [Resource](https://worksheets.codalab.org/worksheets/0xd53d03a48ef64b329c16b9baf0f99b0c/)
- [Resource](https://arxiv.org/abs/1606.05250)

## 🎯 Purpose and Intended Users

**Goal**: Introduce a large, high-quality reading comprehension dataset on Wikipedia articles with crowdsourced question-answer pairs to drive progress in machine reading comprehension.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Question Answering
- Reading Comprehension
- Span-based Answer Extraction

**Limitations**: SQuAD contains only span-based answers extracted from the passage, which is more constrained than interpretative questions in advanced standardized tests; 77.3% of correct answers in the development set are constituents (placing an effective ceiling when considering only constituent candidate spans); over the development and test sets, 2.6% of questions were marked unanswerable by at least one additional crowdworker.

## 💾 Data

**Source**: Crowdsourced question-answer pairs created by crowdworkers (via the Daemo platform with Amazon Mechanical Turk as backend) on paragraphs extracted from 536 English Wikipedia articles sampled uniformly from the top 10,000 English Wikipedia articles by PageRank.

**Size**: 107,785 question-answer pairs on 536 articles; 23,215 paragraphs

**Format**: N/A

**Annotation**: Primary annotation: crowdworkers asked and answered up to 5 questions per paragraph by highlighting the answer span in the paragraph. Additional answers: at least two additional answers collected for each question in the development and test sets via crowdworkers selecting the shortest span that answers the question.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation
- Human evaluation (inter-annotator agreement used to measure human performance)
- Baseline model evaluation (sliding window baselines, logistic regression model)

**Metrics**:
- Exact Match
- Macro-averaged F1 score

**Calculation**: Exact Match: percentage of predictions that match any one of the ground truth answers exactly (ignoring punctuation and articles). Macro-averaged F1: treat prediction and ground truth as bags of tokens, compute F1; take the maximum F1 over all ground truth answers for a question, then average over all questions (ignoring punctuation and articles).

**Interpretation**: Higher Exact Match and F1 indicate better performance. Human performance (measured via inter-annotator agreement) provides an upper reference (test set human F1 = 86.8%); model performance substantially below human indicates remaining challenge.

**Baseline Results**: Random Guess: Exact Match Dev 1.1%, Test 1.3%; F1 Dev 4.1%, Test 4.3%. Sliding Window: Exact Match Dev 13.2%, Test 12.5%; F1 Dev 20.2%, Test 19.7%. Sliding Window + Distance: F1 Dev 20.2%, Test 20.0%. Logistic Regression: Exact Match Dev 40.0%, Test 40.4%; F1 Dev 51.0%, Test 51.0%. Human: Exact Match Dev 80.3%, Test 77.0%; F1 Dev 90.5%, Test 86.8%.

**Validation**: Articles partitioned randomly into training (80%), development (10%), and test (10%). Collected at least two additional answers for each question in the development and test sets; human performance computed via inter-annotator agreement by treating a second answer as the human prediction.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Crowdworkers were required to be located in the United States or Canada; no other demographic breakdowns are provided.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
