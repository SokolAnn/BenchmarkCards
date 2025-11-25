# Building for Tomorrow: Assessing the Temporal Persistence of Text Classifiers

## 📊 Benchmark Details

**Name**: Building for Tomorrow: Assessing the Temporal Persistence of Text Classifiers

**Overview**: This paper establishes an evaluation setup for assessing the temporal persistence of text classification models, performs longitudinal classification experiments on three datasets spanning between 6 and 19 years, and proposes methods to predict how model performance decays over time based on model behaviour in restricted timeframes and dataset linguistic characteristics.

**Data Type**: text (longitudinal labeled text for classification: tweets and book reviews)

**Domains**:
- Natural Language Processing
- Social Media
- E-commerce

**Languages**:
- English

**Similar Benchmarks**:
- ACM-DL
- MedLine
- NYTimes
- RCV1
- ARR
- Haspeede
- TWITA
- MultiFC
- Reddit Time Corpus (RTC)
- WMT
- ARXIV
- CUSTOMNEWS

**Resources**:
- [Resource](http://jmcauley.ucsd.edu/data/amazon/)
- [Resource](https://huggingface.co/bert-base-uncased)
- [Resource](https://huggingface.co/roberta-base)
- [Resource](https://huggingface.co/gpt2)
- [Resource](https://nlp.stanford.edu/projects/glove/)
- [Resource](https://fasttext.cc/docs/en/pretrained-vectors.html)
- [Resource](https://code.google.com/archive/p/word2vec)
- [Resource](https://aclanthology.org/D19-1018)
- [Resource](http://www.zubiaga.org/)

## 🎯 Purpose and Intended Users

**Goal**: Assessing how different factors (representation models, classification algorithms, dataset characteristics) affect text classification performance over time, and determining whether temporal performance can be predicted when annotated data covers only a small timeframe.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Stance Detection
- Sentiment Analysis
- Review Rating Prediction

**Limitations**: The study focuses on binary classification setups, does not perform extensive hyperparameter tuning, and aggregated results for larger temporal gaps can be less stable due to fewer experiments for large gaps.

## 💾 Data

**Source**: Three longitudinal datasets: Gender Equality Stance Detection (GESD) — tweets retrieved via Twitter API using hashtags; Temporal Multilingual Sentiment Analysis (TESA) — tweets labeled via emojis/emoticons; Amazon Books Rating Reviews (ABRR) — Amazon book reviews (Ni et al., 2019).

**Size**: GESD total 288,000 (48,000 per year, time range 2014-2019); TESA total 798,400 (99,800 per year, time range 2013-2020); ABRR total 497,800 (26,200 per year, time range 2000-2018).

**Format**: N/A

**Annotation**: GESD: Aggregated hashtags (distant supervision) indicating stance (support/oppose); TESA: Aggregated emojis/emoticons (distant supervision) indicating sentiment (positive/negative); ABRR: User-provided review ratings (originally 1-5; sampled to binary 1 or 5 for this study).

## 🔬 Methodology

**Methods**:
- Longitudinal temporal-split evaluation across yearly slices
- Temporal Gap aggregation (grouping train-test year pairs by year difference)
- Use of multiple pretrained language representations (static and contextual) and a range of classification algorithms (traditional and deep learning)
- Lexical analyses (familiarity score, Jaccard index, TF-IDF similarity, information rate)
- Temporal contextual analysis via time-specific masked language model fine-tuning and cosine similarity of aspect embeddings

**Metrics**:
- Macro-averaged F1-score (F-macro)
- Performance Change Metric P(G) (average F-macro over all train-test pairs with temporal gap G)
- Pearson correlation coefficient (used to correlate lexical measures with model performance)

**Calculation**: Model Evaluation Metric: For each training year i and test year j, compute macro-averaged F1-score (F-macro). Performance Change Metric P(G) is computed as the average of F-macro over all pairs (i,j) such that j - i = G.

**Interpretation**: Higher F-macro indicates better model performance on a given train-test pair. Smaller decreases in P(G) as |G| increases indicate better temporal persistence. In TP/FP analysis, optimal results minimize false positive rates and maximize true positive rates (points in top-left of the plotted grids are ideal). Familiarity score and other lexical measures positively correlate with preserved performance over time.

**Baseline Results**: The best-performing combination reported is contextual word representations with a Hierarchical Attention Network (CWRs-HAN). Example explicit result: BERT representation drops by more than 15% for GESD when testing on data 5 years in the past and by more than 10% for data 5 years in the future. (Results aggregated and averaged across runs; reported experiment averages are over three runs.)

**Validation**: Early stopping using a held-out development set from the same training year; stratified per-year splits (75% train, 10% dev, 15% test); reported results are averages of three runs. Temporal validation is performed by aggregating performance across all train-test year pairs grouped by temporal gap.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
