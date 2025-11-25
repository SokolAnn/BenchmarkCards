# NewsQA

## 📊 Benchmark Details

**Name**: NewsQA

**Overview**: We present NewsQA, a challenging machine comprehension dataset of over 100,000 human-generated question-answer pairs. Crowdworkers supply questions and answers based on a set of over 10,000 news articles from CNN, with answers consisting of spans of text from the corresponding articles. The dataset is designed to solicit exploratory questions that require reasoning and to provide a large-scale, challenging benchmark for machine comprehension.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- CNN/Daily Mail
- MCTest
- Children's Book Test (CBT)
- BookTest

**Resources**:
- [Resource](https://datasets.maluuba.com/NewsQA)
- [Resource](https://datasets.maluuba.com/NewsQA/stats)
- [Resource](https://arxiv.org/abs/1611.09830)
- [GitHub Repository](https://github.com/tylin/coco-caption)

## 🎯 Purpose and Intended Users

**Goal**: To construct a large-scale corpus of naturally posed questions that necessitate reasoning-like behaviors (e.g., synthesis across sentences) and to provide a challenging dataset for advancing machine comprehension research.

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Question Answering
- Reading Comprehension

**Limitations**: The paper leaves the challenge of identifying unanswerable questions for future work; the corpus is constructed from CNN news articles only.

## 💾 Data

**Source**: CNN news articles retrieved using the script from Hermann et al. (2015); questions and answers collected from crowdworkers via a four-stage process (article curation, question sourcing, answer sourcing, validation); answers are spans highlighted in articles by crowdworkers.

**Size**: 119,633 question-answer pairs; 12,744 articles. Dataset splits: training 90%, development 5%, test 5%. Subset with answer agreements used in experiments: 92,549 training samples, 5,166 validation samples, 5,126 test samples.

**Format**: N/A

**Annotation**: Answers are annotated as text spans by Answerers (average 2.73 answerers per question). A separate validation stage (average 2.48 validators) selects best answers or rejects all. After validation, 86.0% of questions have answers agreed upon by at least two crowdworkers. Multi-span answers merged if spans are less than 3 words apart.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation (neural baselines: match-LSTM and BARB)

**Metrics**:
- F1
- Exact Match (EM)
- BLEU
- CIDEr

**Calculation**: F1 and Exact Match calculated using the official SQuAD evaluation script. BLEU and CIDEr calculated using the coco-caption implementation (https://github.com/tylin/coco-caption).

**Interpretation**: Higher F1/EM/BLEU/CIDEr indicate better performance. Human performance is treated as an upper reference; the reported gap between human and machine (0.198 F1 on NewsQA) indicates the dataset's challenge and room for improvement.

**Baseline Results**: Human (NewsQA, 1,000-sample evaluation): Exact Match 0.465, F1 0.694, BLEU 0.560, CIDEr 3.596. mLSTM (NewsQA): Dev EM 0.344, Test EM 0.349, Dev F1 0.496, Test F1 0.500. BARB (NewsQA): Dev EM 0.361, Test EM 0.341, Dev F1 0.496, Test F1 0.482.

**Validation**: Validation stage: a third set of crowdworkers sees the full article, question, and candidate answers and selects the best answer or rejects all. Validation applied to questions without answer agreement (43.2% of questions). Each article-question pair in validation averaged 2.48 validators.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
