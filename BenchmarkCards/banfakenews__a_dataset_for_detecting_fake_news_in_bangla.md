# BanFakeNews: A Dataset for Detecting Fake News in Bangla

## 📊 Benchmark Details

**Name**: BanFakeNews: A Dataset for Detecting Fake News in Bangla

**Overview**: An annotated dataset and benchmark for detecting fake news written in Bangla: the paper introduces an annotated dataset of approximately 50,000 Bangla news items for building automated fake news detection systems, provides dataset analysis, and develops benchmark systems using linguistic features and neural models.

**Data Type**: text (news articles: headline and article body, with metadata)

**Domains**:
- Natural Language Processing

**Languages**:
- Bangla

**Similar Benchmarks**:
- LIAR

**Resources**:
- [GitHub Repository](https://github.com/Rowan1697/FakeNews)

## 🎯 Purpose and Intended Users

**Goal**: To create and publicly release an annotated dataset of Bangla news for fake news detection and to develop and evaluate benchmark systems (linguistic-feature based and neural models) for classifying Bangla fake news.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Text Classification
- Fake News Detection

**Limitations**: Imbalanced dataset: authentic news are 37.47 times more numerous than fake news in the dataset. The authors have manually annotated around 8,500 news so far and plan to expand to approximately 50,000.

## 💾 Data

**Source**: Collected authentic news from 22 mainstream trusted Bangladeshi news portals; fake news collected from satirical sites, manual collection of clickbait sites, and fact-checking sites (jaachai.com and bdfactcheck.com). Metadata collected includes domain, publication time, and category; source and headline-article relation were also annotated for a subset.

**Size**: Approximately 50,000 news articles (target/total collected); 8,500 news manually annotated so far

**Format**: N/A

**Annotation**: Manual annotation by an annotator team of undergraduate students. Labels include authentic vs fake, source information, headline-article relation (Related/Unrelated), and categories mapped into 12 generalized categories.

## 🔬 Methodology

**Methods**:
- Automated metrics (Micro-F1, Precision, Recall)
- Human evaluation (human baseline with 5 annotators)

**Metrics**:
- Micro-F1
- Precision
- Recall
- F1 Score

**Calculation**: Micro-F1 computed for overall evaluation; precision, recall and F1 reported for the minority (fake) class. Dataset split 70:30 train:test. For neural models, 10% of test data used as validation. Checkpointing on validation F1 for the fake class. Hyperparameters (e.g., SVM penalty C) tuned on validation.

**Interpretation**: Authors focus on the F1-Score of the fake class as the main evaluation metric due to class imbalance. Linear classifiers with traditional linguistic features achieve the best reported performance and outperform neural network models and the human baseline on the test sets.

**Baseline Results**: Best reported: SVM with all linguistic features — 0.91 F1 (fake class). BERT (fine-tuned multilingual cased) — 0.68 F1 (fake class). CNN — 0.59 F1 (fake class). Human baseline (five annotators) fake-class F1-scores: 58%, 65%, 70%, 68%, 63% (authors report an aggregate human F1 of 64.8% on the human baseline subset).

**Validation**: Train:test split of 70:30. For BiLSTM/CNN/BERT experiments, 10% of the test data used as validation. Models trained up to 50 epochs with checkpoints based on validation F1 of the fake class. SVM penalty parameter tuned based on validation results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Misuse
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Misuse**: Spreading disinformation
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Political manipulation (influence on elections and political opinion)', 'Impact on affected communities (example: 2012 Ramu incident leading to violence against religious sites)', 'Financial impact (damage in finance sector due to fake news)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
