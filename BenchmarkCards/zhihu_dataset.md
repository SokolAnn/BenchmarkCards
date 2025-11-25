# Zhihu dataset

## 📊 Benchmark Details

**Name**: Zhihu dataset

**Overview**: Constructed because the KanShan-Cup dataset did not provide original texts; the authors crawled questions from Zhihu for the top 1,999 frequent topics to provide a dataset with original texts and topic labels for multi-label topic tagging research.

**Data Type**: text (question-topic pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- KanShan-Cup dataset
- Amazon Review Polarity
- Amazon Review Full
- AG's News
- Yahoo! Answers
- DBPedia

**Resources**:
- [Resource](https://biendata.com/competition/zhihu/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a dataset with original Zhihu question texts and topic labels to enable analyses (e.g., visualization and case study) that were inconvenient with KanShan-Cup due to privacy-motivated text removal.

**Target Audience**:
- Researchers

**Tasks**:
- Text Classification
- Multi-Label Classification

**Limitations**: N/A

## 💾 Data

**Source**: Crawled questions from Zhihu for the top 1,999 frequent topics (authors constructed the dataset).

**Size**: 3,300,000 questions (3,000,000 train, 30,000 validation, 300,000 test)

**Format**: N/A

**Annotation**: Topic labels (multi-label, up to 5 topics per question)

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation
- Baseline comparison

**Metrics**:
- Precision (weighted)
- Recall@5
- F1

**Calculation**: Precision: weighted Precision = sum_{pos in {1..5}} Precision@pos / log(pos + 1) (as Eqn. 11). F1: harmonic average computed as F1 = 2 * Precision * Recall@5 / (Precision + Recall@5) (as Eqn. 12).

**Interpretation**: N/A

**Baseline Results**: On Zhihu dataset (Table 4): EXAM (Ours) — Precision 1.267, Recall@5 0.578, F1 0.397. Baselines (selected): FastText — Precision 1.235, Recall@5 0.564, F1 0.387; TextCNN — Precision 1.241, Recall@5 0.566, F1 0.389; Word-TextRNN — Precision 1.240, Recall@5 0.566, F1 0.389.

**Validation**: 30,000-sample validation set used for early stopping; test set contains 300,000 samples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy

**Atlas Risks**:
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper explicitly mentions user privacy and data security as reasons KanShan-Cup did not provide original texts. The Zhihu dataset was constructed by crawling Zhihu, and the paper does not describe anonymization procedures.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
