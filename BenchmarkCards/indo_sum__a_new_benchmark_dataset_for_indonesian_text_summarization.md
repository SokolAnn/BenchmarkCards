# INDO SUM: A New Benchmark Dataset for Indonesian Text Summarization

## 📊 Benchmark Details

**Name**: INDO SUM: A New Benchmark Dataset for Indonesian Text Summarization

**Overview**: INDO SUM, a new benchmark dataset for Indonesian text summarization, consisting of news articles and manually constructed summaries; the dataset is almost 200x larger than the previous Indonesian summarization dataset of the same domain and is made publicly available to encourage further research and provide baselines.

**Data Type**: article-summary pairs (text)

**Domains**:
- Natural Language Processing

**Languages**:
- Indonesian

**Similar Benchmarks**:
- CNN/DailyMail
- TAC 2011

**Resources**:
- [GitHub Repository](https://github.com/kata-ai/indosum)
- [GitHub Repository](https://github.com/tagucci/pythonrouge)
- [GitHub Repository](https://github.com/cheng6076/NeuralSum)
- [Resource](https://spacy.io)
- [Resource](http://shortir.com)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large publicly available benchmark dataset for Indonesian text summarization and to evaluate and provide baselines for extractive summarization methods.

**Target Audience**:
- Researchers in Natural Language Processing
- Model developers

**Tasks**:
- Text Summarization
- Extractive Summarization
- Abstractive Summarization

**Limitations**: Each article has a single abstractive gold summary (only one reference summary per article), which the authors acknowledge as a limitation.

## 💾 Data

**Source**: Provided by Shortir (an Indonesian news aggregator and summarizer); dataset compiled from online news articles with title, category, source, URL, and an abstractive summary.

**Size**: Approximately 19,000 article-summary pairs (roughly 20K before preprocessing; roughly 19K after cleaning).

**Format**: N/A

**Annotation**: Abstractive gold summaries manually created by a total of 2 native speakers of Indonesian; extractive oracle labels generated using the greedy algorithm from Nallapati et al. to maximize ROUGE against the abstractive gold summary.

## 🔬 Methodology

**Methods**:
- Automated metrics (ROUGE) computed via pythonrouge
- 5-fold cross-validation (dataset split into 5 folds of training, development, and testing)
- Baseline and comparative evaluation of extractive summarization methods (unsupervised, non-neural supervised, neural supervised) including out-of-domain experiments

**Metrics**:
- ROUGE-1 F1 Score
- ROUGE-2 F1 Score
- ROUGE-L F1 Score

**Calculation**: F1 score of ROUGE-1, ROUGE-2, and ROUGE-L computed using pythonrouge. F1 score reported (rather than recall) following prior work; hyperparameters tuned on development set optimizing ROUGE-1.

**Interpretation**: ROUGE-1 and ROUGE-2 measure informativeness and ROUGE-L measures fluency (as noted by the authors); ORACLE acts as the upper bound for extractive summarizers and reported ROUGE scores are compared against this upper bound.

**Baseline Results**: ORACLE: R-1 79.27 (0.25), R-2 72.52 (0.35), R-L 78.82 (0.28). LEAD-3: R-1 62.86 (0.34), R-2 54.50 (0.41), R-L 62.10 (0.37). NEURAL SUM (300 emb. size): R-1 67.96 (0.46), R-2 61.65 (0.48), R-L 67.24 (0.47). (Scores averaged over 5 folds; full table in paper.)

**Validation**: 5-fold cross-validation; hyperparameters tuned on each fold's development set (optimizing ROUGE-1); mean and standard deviation of scores computed over the 5 folds.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Dataset and code are available online under permissive licenses (exact license not specified in the paper).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
