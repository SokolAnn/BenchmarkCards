# NewsEdits

## 📊 Benchmark Details

**Name**: NewsEdits

**Overview**: The first publicly available dataset of news revision histories, NewsEdits, a large-scale multilingual corpus containing 1.2 million articles with 4.6 million versions from over 22 English- and French-language newspaper sources (2006-2021); defines article-level edit actions (Addition, Deletion, Edit, Refactor) and introduces three prediction tasks to assess whether and how articles update.

**Data Type**: Document-level news article text (sentence-level edit pairs)

**Domains**:
- Natural Language Processing
- Computational Journalism

**Languages**:
- English
- French

**Similar Benchmarks**:
- WiKed Error Corpus
- WikiAtomicEdits
- WiCoPaCo
- WikiHow-ToImprove
- WikiNews

**Resources**:
- [GitHub Repository](https://github.com/isi-nlp/NewsEdits.git)
- [Resource](https://arxiv.org/abs/2206.07106)
- [Resource](https://www.newssniffer.co.uk/)
- [GitHub Repository](https://github.com/DocNow/diffengine)
- [Resource](https://opensource.org/licenses/AGPL-3.0)
- [Resource](https://creativecommons.org/licenses/by-nd/4.0)
- [Resource](https://huggingface.co/roberta-base)

## 🎯 Purpose and Intended Users

**Goal**: Facilitate analysis of narrative and factual evolution in news articles by providing a large-scale dataset of news revision histories, extracted edit-actions, and predictive tasks to assess whether and how articles change.

**Target Audience**:
- Natural Language Processing Researchers
- Computational Journalism Researchers
- Journalists
- Model Developers

**Tasks**:
- Document Classification (Will the document be updated?)
- Document-level Multi-class Classification (Predict binned counts of Additions, Deletions, Edits, Refactors)
- Sentence-level Classification (Edit Action Prediction: Addition, Deletion, Edit, Refactor; Refactor direction; Addition above/below)

**Limitations**: The dataset does not include a robust non-Western language source; the only two languages are English and French.

## 💾 Data

**Source**: Collected from two online trackers of news article updates: NewsSniffer and DiffEngine, covering article versions from 22 media outlets (including The New York Times, Washington Post, Associated Press, BBC, Guardian, Reuters) across 2006-2021.

**Size**: 1.2 million articles; 4.6 million versions. Paper reports summary statistics including ≈36.1 million changed sentences, 21.7 million added sentences, 14.2 million removed sentences, and the paper also states 'We count over 40 million Edits, Additions, Deletions or Refactors' in NewsEdits.

**Format**: SQLite (5 tables: articles, sentence_diffs, word_diffs, plus two summary-statistic tables)

**Annotation**: Automatic extraction of sentence-level edit-actions using an asymmetrical sentence-matching algorithm (embedding- and BLEU-based variants) applied to the full corpus; manual annotation by expert annotators (two expert annotators for 280 documents for sentence matching to set hyperparameters and evaluate matching; five professional journalists for human evaluation tasks and task annotations).

## 🔬 Methodology

**Methods**:
- Automated metrics (F1 Score, Macro F1, Micro F1)
- Human evaluation (expert journalists)
- Baseline modeling using RoBERTa-based architectures

**Metrics**:
- F1 Score
- Macro F1
- Micro F1

**Calculation**: Counts for Task 2 are binned ([0,1), [1,3), [3,∞)) and predictions evaluated as multiclass classification; Macro and Micro F1 are reported across bins. Reported scores are the median of 1,000 bootstrap resamples of the evaluation dataset.

**Interpretation**: Higher F1 indicates better prediction. The paper shows current large language model-based predictors provide a baseline above random guessing in most tasks, though expert human journalists perform significantly better.

**Baseline Results**: Task 1 (next-version prediction): Baseline RoBERTa = 60.8 F1 (median), Random = 50.6, Most Popular = 56.6, Human = 80.1. Task 2 (binned counts): Example Num. Additions baseline (n=150,000) Macro F1 = 29.7, Micro F1 = 36.3; Human Num. Additions Macro F1 = 66.4, Micro F1 = 69.3. Task 3 (sentence-level): Sentence Operations baseline Macro F1 = 36.5, Micro F1 = 61.9; Human Sentence Operations Macro F1 = 63.8, Micro F1 = 63.5. (All scores are reported in paper tables as medians over 1,000 bootstrap resamples.)

**Validation**: Human-annotated sentence matches (n=280) were split 50% for hyperparameter tuning and 50% for evaluation of matching algorithms. Evaluation sets for tasks were sampled balanced by class labels (4k documents per evaluation set where noted). Reported task scores are medians over 1,000 bootstrap resamples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Laws
- Intellectual Property
- Legal Compliance
- Misuse
- Governance

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Intellectual Property**: Data usage rights restrictions
- **Legal Compliance**: Legal accountability
- **Misuse**: Improper usage
- **Governance**: Lack of testing diversity

**Demographic Analysis**: Annotators: five professional journalists; four identify as white and one as Latinx; four identify as male and one as female. Dataset language coverage: English and French; sources primarily from US, UK, and Canada.

**Potential Harm**: ['Misuse to disparage or denigrate media outlets (explicitly discussed as a possible misuse)', 'Potential inclusion of libelous or slanderous content in earlier article versions (paper notes some earlier versions may have been updated or removed for that reason)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors state: 'We believe that there are no adverse privacy implications in this dataset.' The dataset comprises news articles already published in the public domain.

**Data Licensing**: NewsSniffer is released under AGPL-3.0; DiffEngine is released under an Attribution-NoDerivatives 4.0 International license. The authors state they received permission from the original owners and used the data within the bounds of intended use.

**Consent Procedures**: Annotators consented to participate, were paid $1 per task (above highest U.S. minimum wage), and the data collection was covered under a university IRB.

**Compliance With Regulations**: Not Applicable
