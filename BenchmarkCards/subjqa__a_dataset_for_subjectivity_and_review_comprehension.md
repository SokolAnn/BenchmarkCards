# SUBJQA: A Dataset for Subjectivity and Review Comprehension

## 📊 Benchmark Details

**Name**: SUBJQA: A Dataset for Subjectivity and Review Comprehension

**Overview**: We release an English QA dataset (SUBJQA) based on customer reviews, containing subjectivity annotations for questions and answer spans across 6 domains.

**Data Type**: question-answering pairs (text from customer reviews)

**Domains**:
- TripAdvisor
- Restaurants
- Movies
- Books
- Electronics
- Grocery

**Languages**:
- English

**Similar Benchmarks**:
- AmazonQA
- SQuAD
- ReviewQA
- NewsQA
- CoQA
- MLQA

**Resources**:
- [GitHub Repository](https://github.com/megagonlabs/SubjQA)
- [Resource](https://arxiv.org/abs/2004.14283)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the relationship between subjectivity and question answering in customer reviews by providing a QA dataset with subjectivity annotations for questions and answer spans across 6 domains.

**Tasks**:
- Question Answering
- Answer Span Extraction
- Subjectivity Classification

**Limitations**: The dataset generated is not guaranteed to only contain answerable questions; KBs used in dataset construction achieved 35-50% mean precision on various domains; a small fraction of the answer spans are noisy.

## 💾 Data

**Source**: Customer reviews from TripAdvisor (Wang et al., 2010), Yelp dataset (Restaurants), and Amazon product reviews (McAuley and Yang, 2016b); opinion extractions obtained using OpineDB and syntactic extraction patterns.

**Size**: Over 10,000 examples (domain totals provided in paper: TripAdvisor 1,686 examples; Restaurants 1,683 examples; Movies 1,677 examples; Books 1,668 examples; Electronics 1,659 examples; Grocery 1,725 examples).

**Format**: N/A

**Annotation**: Crowdsourced via Appen: annotators write questions from topics/reviews, highlight the shortest answer span in the review or mark the question as unanswerable, and provide subjectivity scores for both the question and the answer span on a 1-5 scale. Quality control included embedded expert-labeled items and a worker accuracy threshold.

## 🔬 Methodology

**Methods**:
- Human crowdsourcing annotation (Appen) for question generation, answer-span highlighting, subjectivity scoring, and answerability labels
- Automated dataset construction using opinion extraction and non-negative matrix factorization (neighborhood model) to pair topics and reviews
- Automated evaluation of QA models (fine-tuning pre-trained models)
- Multi-task learning (subjectivity-aware QA model trained to predict subjectivity label and answer span simultaneously)

**Metrics**:
- F1 Score
- Exact Match
- Accuracy

**Calculation**: N/A

**Interpretation**: Higher F1 Score and Exact Match indicate better QA performance. The paper reports that pre-trained models perform much lower on SUBJQA than on factual datasets; fine-tuning substantially improves F1 on SUBJQA; a subjectivity-aware multi-task model further improves average F1 across domains.

**Baseline Results**: Pre-trained models achieve up to 92.9% F1 on SQuAD. Pre-trained models obtain an average F1 of 30.5% across SUBJQA domains (36.5% F1 at best on any given domain). After fine-tuning on SUBJQA domains the best model achieves an average F1 of 74.1% across domains. The subjectivity-aware multi-task model achieves an average F1 of 76.3% across domains.

**Validation**: Topics partitioned into train/dev/test splits by topic (80%/10%/10%). Crowdsourcing quality control via Appen with embedded expert-labeled items and a worker accuracy requirement (70%). Manual inspection and analysis of sampled items (e.g., manual inspection of 100 randomly chosen questions).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
