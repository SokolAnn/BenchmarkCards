# TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension

## 📊 Benchmark Details

**Name**: TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension

**Overview**: We present TriviaQA, a challenging reading comprehension dataset containing over 650K question-answer-evidence triples. TriviaQA includes 95K question-answer pairs authored by trivia enthusiasts and independently gathered evidence documents (on average six per question) collected from Wikipedia and Web search results, designed to test complex compositional questions, substantial syntactic and lexical variability, and multi-sentence reasoning.

**Data Type**: question-answer-evidence triples (text)

**Domains**:
- Natural Language Processing
- Information Retrieval
- Open-domain Question Answering

**Similar Benchmarks**:
- SQuAD
- MS Marco
- NewsQA
- WikiQA
- TREC
- MCTest
- SearchQA

**Resources**:
- [Resource](http://nlp.cs.washington.edu/triviaqa/)
- [Resource](https://arxiv.org/abs/1705.03551)

## 🎯 Purpose and Intended Users

**Goal**: To introduce TriviaQA, a new reading comprehension dataset designed to simultaneously test complex compositional questions, syntactic and lexical variability between questions and evidence, and multi-sentence reasoning, and to provide resources for training and evaluating reading-comprehension models.

**Target Audience**:
- Model Developers
- Machine Learning Researchers

**Tasks**:
- Reading Comprehension
- Question Answering

**Limitations**: Evidence documents are automatically gathered and are not guaranteed to contain all facts needed to answer questions (distant supervision); the distant supervision assumption holds approximately 75% of the time according to the paper. The web-domain data is noisy and redundant; training and evaluation required truncating long documents (e.g., to the first 800 words for BiDAF training). A clean human-annotated subset of 1,975 question-document-answer triples is provided for verified evaluation.

## 💾 Data

**Source**: Question-answer pairs collected from 14 trivia and quiz-league websites. Evidence documents collected from two sources: (1) Web search results via Bing (top 50 results; crawled top 10 pages after filtering) and (2) Wikipedia pages identified via TAGME entity linking applied to questions. Additionally a human-annotated verified subset was created.

**Size**: Over 650,000 question-answer-evidence triples; 95,956 question-answer pairs; 662,659 evidence documents. Full unfiltered dataset: 110,495 QA pairs and 740,000 evidence documents. Clean human-annotated subset: 1,975 question-document-answer triples.

**Format**: N/A

**Annotation**: Evidence documents automatically gathered (distant supervision). A clean, human-annotated subset of 1,975 question-document-answer triples whose documents are certified to contain all facts required to answer the questions.

## 🔬 Methodology

**Methods**:
- Automated metrics (exact match and F1)
- Human evaluation (verification/annotation of dev and test subsets)

**Metrics**:
- Exact Match (EM)
- F1 Score (word-level F1 over answers)

**Calculation**: Exact Match and F1 are computed over words in the answer(s) following SQuAD conventions. For Numerical and FreeForm answers a single given answer is used as ground truth. For Wikipedia-entity answers, Wikipedia aliases are accepted as valid answers. Evaluation is performed at the question-level for the Wikipedia domain and at the document-level for the Web domain.

**Interpretation**: Higher Exact Match and F1 indicate better performance. The paper reports a large gap between model performance and human performance (human verified accuracy: 79.7% on Wikipedia, 75.4% on Web), indicating the dataset's difficulty.

**Baseline Results**: Baseline results (distant supervision, development set): BiDAF (Wikipedia dev) EM 40.26%, F1 45.74%; Entity classiﬁer (Wikipedia dev) EM 23.42%, F1 27.68%; Random baseline (Wikipedia dev) EM 12.72%, F1 22.91%. Human verified performance reported as 79.7% (Wikipedia) and 75.4% (Web).

**Validation**: Random 80/10/10 train/dev/test split of QA pairs. A human annotator verified subsets of dev and test (verified dev/test) used for clean evaluation. Verified sets used to evaluate whether documents contain the minimal facts required to answer questions; verified accuracy reported for Wikipedia and Web domains.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
