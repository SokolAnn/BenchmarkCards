# IDN Tagged Corpus

## 📊 Benchmark Details

**Name**: IDN Tagged Corpus

**Overview**: A publicly released 5-fold dataset split of the IDN Tagged Corpus intended to serve as a standardized benchmark for Indonesian part-of-speech tagging; the authors release their cross-validation splits to provide a common evaluation standard for future work.

**Data Type**: Token sequences with POS tags (text)

**Domains**:
- Natural Language Processing

**Languages**:
- Indonesian

**Similar Benchmarks**:
- PANL10N dataset
- Penn Treebank

**Resources**:
- [Resource](http://www.panl10n.net)
- [GitHub Repository](https://github.com/famrashel/idn-tagged-corpus)
- [GitHub Repository](https://github.com/kmkurn/id-pos-tagging/blob/master/data/dataset.tar.gz)
- [GitHub Repository](https://github.com/andryluthfi/indonesian-postag)
- [GitHub Repository](https://github.com/scrapinghub/python-crfsuite)
- [GitHub Repository](https://github.com/kmkurn/id-pos-tagging)

## 🎯 Purpose and Intended Users

**Goal**: Provide a standardized dataset split of the IDN Tagged Corpus as a common benchmark for Indonesian part-of-speech tagging and to evaluate and compare POS tagging methods (rule-based, CRF, neural).

**Target Audience**:
- Natural Language Processing Researchers
- ML Researchers
- Model Developers

**Tasks**:
- Part-of-Speech Tagging

**Limitations**: Dataset is relatively small (10,000 sentences, 250,000 tokens); contains some annotation inconsistencies (e.g., WH vs SC); multi-word expressions are treated as single tokens in the split.

## 💾 Data

**Source**: IDN Tagged Corpus (manually annotated POS tagging corpus) — original corpus described in Dinakaramani et al. [12]; authors release their 5-fold splits.

**Size**: 10,000 sentences and 250,000 tokens

**Format**: N/A

**Annotation**: Manually annotated POS tags

## 🔬 Methodology

**Methods**:
- Automated metrics (weighted macro-average F1 Score)
- 5-fold cross-validation
- Baseline and model comparisons (rule-based, CRF, neural network architectures)

**Metrics**:
- Weighted macro-average F1 Score
- F1 Score

**Calculation**: Weighted macro-average F1 Score: weighted average of per-tag F1 scores where each weight is the corresponding tag's proportion in the dataset; implemented using scikit-learn.

**Interpretation**: Accuracy and micro-average F1 are inappropriate due to class imbalance (micro-average equals accuracy); weighted macro-average F1 balances per-tag contributions by tag frequency so higher scores indicate better balanced performance across tags.

**Baseline Results**: MAJOR: 9.39 (0.21); MEMO: 90.62 (0.82); Rashel et al. [15]: 85.77 (0.22); CRF: 96.22 (0.22); biLSTM + CRF: 97.47 (0.11) — test F1 scores averaged over 5 folds.

**Validation**: 5-fold cross-validation with scores averaged over folds; development set used for hyperparameter tuning; early stopping and learning rate decay applied during training.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
