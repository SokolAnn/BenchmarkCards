# SearchQA

## 📊 Benchmark Details

**Name**: SearchQA

**Overview**: SearchQA is a large-scale dataset for machine comprehension / question-answering constructed by crawling question-answer pairs from J! Archive (Jeopardy!) and augmenting each pair with multiple text snippets retrieved from the Google search engine, with the goal of reflecting a full end-to-end question-answering pipeline (information retrieval + answer synthesis) and serving as a benchmark for question-answering research.

**Data Type**: question-answer pairs with text snippets (text)

**Domains**:
- Natural Language Processing
- Information Retrieval

**Similar Benchmarks**:
- DeepMind CNN/DailyMail
- SQuAD
- MS MARCO
- NEWSQA
- SimpleQA

**Resources**:
- [GitHub Repository](https://github.com/nyu-dl/SearchQA)
- [Resource](http://j-archive.com)
- [Resource](http://pytorch.org/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale dataset (SearchQA) that more closely reflects a realistic, noisy information retrieval context by augmenting Jeopardy! question-answer pairs with Google search snippets, to serve as a benchmark for advancing question-answering / machine comprehension research.

**Target Audience**:
- Machine comprehension researchers
- Natural Language Processing researchers
- Model developers

**Tasks**:
- Question Answering
- Machine Comprehension

**Limitations**: Only includes question-answer-context tuples whose retrieved snippets contain the answer; answers are limited to three or fewer words; snippets are noisy excerpts (often not full sentences); human evaluation results may be affected by participant exhaustion.

## 💾 Data

**Source**: Question-answer pairs crawled from J! Archive (Jeopardy!) augmented with text snippets retrieved by the Google search engine. Additional metadata from Jeopardy! (category, dollar value, show number, air date) and from Google (URL, title, related links) are included in the public release.

**Size**: 140,461 question-answer pairs; 6.9 million snippets in total; 1,257,327 unique tokens; average 49.6 snippets per question-answer pair; average snippet length 37.3 tokens; average answer length 1.47 tokens.

**Format**: JSON (.json)

**Annotation**: Automatically constructed from Jeopardy! question-answer pairs and Google-retrieved snippets with dataset cleaning; no additional manual annotation process described besides manual checking/removal of some URLs during cleaning.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation (baselines: TF-IDF Max, Attention Sum Reader)

**Metrics**:
- Accuracy
- Top-5 Accuracy
- F1 Score

**Calculation**: For unigram answers: report top-1 and top-5 accuracies. For n-gram (multi-word) answers: report F1 score. Human evaluation reports per-question and per-user accuracy statistics and standard deviations.

**Interpretation**: Higher Accuracy / Top-5 Accuracy / F1 Score indicates better performance. Human performance is provided as a guideline but is not necessarily an upper bound due to dataset noise and human factors; a meaningful gap between human and machine performance indicates remaining challenge.

**Baseline Results**: Human volunteers (unigram per-question average accuracy 66.97%, n-gram per-question average accuracy 42.86%; per-user average unigram 64.85% (std 8.16%), per-user average n-gram 43.85% (std 10.43%); F1 score for n-gram 57.62%). TF-IDF Max: Validation Acc 13.0, Acc@5 49.3; Test Acc 12.7, Acc@5 49.0. Attention Sum Reader (ASR): Validation Acc 43.9, Acc@5 67.3, F1 24.2; Test Acc 41.3, Acc@5 65.1, F1 22.8.

**Validation**: A predefined train/validation/test split is provided with non-overlapping years: training (99,820 examples), validation (13,393 examples), test (27,248 examples). Validation and test sets contain question-answer pairs from years later than the training set to assess generalization to future questions.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
