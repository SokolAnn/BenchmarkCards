# TWEET QA: A Social Media Focused Question Answering Dataset

## 📊 Benchmark Details

**Name**: TWEET QA: A Social Media Focused Question Answering Dataset

**Overview**: We present the first large-scale dataset for QA over social media data. To ensure that the tweets we collected are useful, we only gather tweets used by journalists to write news articles. We then ask human annotators to write questions and answers upon these tweets. Unlike other QA datasets like SQuAD in which the answers are extractive, we allow the answers to be abstractive.

**Data Type**: question-answering pairs (tweets as context)

**Domains**:
- Natural Language Processing
- Social Media

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- CNN/Daily Mail
- NewsQA
- WIKIMOVIES
- MS MARCO
- SWAG

**Resources**:
- [Resource](https://tweetqa.github.io/)
- [Resource](https://arxiv.org/abs/1907.06292)
- [GitHub Repository](https://github.com/huggingface/pytorch-pretrained-BERT)
- [Resource](https://archive.org/)

## 🎯 Purpose and Intended Users

**Goal**: Create the first large-scale question answering dataset that focuses on social media (Twitter) to enable development and evaluation of QA systems for informal social media text and real-time event understanding.

**Target Audience**:
- Researchers in Natural Language Processing
- Machine Learning researchers
- Model developers

**Tasks**:
- Question Answering

**Limitations**: N/A

**Out of Scope Uses**:
- Videos, images or inserted links should not be considered.
- No background knowledge should be required to answer the question.
- No Yes-no questions should be asked.

## 💾 Data

**Source**: Tweets embedded in news articles crawled from archived snapshots of two major news websites (CNN and NBC); tweets were extracted from tweet blocks embedded in these news articles.

**Size**: 13,757 question-answer pairs; 17,794 tweets; 10,898 articles. Split: 10,692 training triples, 1,086 development triples, 1,979 test triples.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk (workers located in major English-speaking countries with acceptance rate >95%); post-filtering of QA pairs; separate validation HITs for test and development sets; 492 workers wrote QA pairs; 59 workers participated in validation.

## 🔬 Methodology

**Methods**:
- Automated metrics (BLEU-1, METEOR, ROUGE-L)
- Human performance evaluation (validation HITs)
- Model-based evaluation (baselines: Query-Matching, Generative RNN-based model, BiDAF, fine-tuned BERT)

**Metrics**:
- BLEU-1
- METEOR
- ROUGE-L

**Calculation**: Scores computed using both the original answer and the validation answer as references. For human performance, validation answers are treated as generated outputs and original answers as references.

**Interpretation**: Higher metric scores indicate better performance. Human performance provides a reference point (e.g., HUMAN BLEU-1 ~76.4 (dev) / 78.2 (test)); baseline model scores substantially lower (e.g., BERT BLEU-1 67.3 (dev) / 69.6 (test)), indicating room for improvement.

**Baseline Results**: HUMAN: BLEU-1 76.4 (dev) / 78.2 (test); METEOR 63.7 / 66.7; ROUGE-L 70.9 / 73.5. EXTRACT-UB (extractive upper bound): BLEU-1 79.5 / 80.3; METEOR 68.8 / 69.8; ROUGE-L 74.3 / 75.6. Query-Matching: BLEU-1 30.3 / 29.4; METEOR 12.0 / 12.1; ROUGE-L 17.0 / 17.4. BiDAF: BLEU-1 48.3 / 48.7; METEOR 31.6 / 31.4; ROUGE-L 38.9 / 38.6. Generative: BLEU-1 53.4 / 53.7; METEOR 32.1 / 31.8; ROUGE-L 39.5 / 39.0. BERT (fine-tuned): BLEU-1 67.3 / 69.6; METEOR 56.9 / 58.6; ROUGE-L 62.6 / 64.1.

**Validation**: Validation HITs: workers answered questions in test/dev and could label questions as 'NA' if unanswerable (3.1% labeled unanswerable). Manual agreement check on 200 random development samples: 90% semantically equivalent, 2% partially equivalent, 8% totally inconsistent. 59 workers participated in validation.

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
