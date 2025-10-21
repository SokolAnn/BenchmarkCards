# A Benchmark Study of Machine Learning Models for Online Fake News Detection

## 📊 Benchmark Details

**Name**: A Benchmark Study of Machine Learning Models for Online Fake News Detection

**Overview**: In this research, we conducted a benchmark study to assess the performance of different applicable machine learning approaches on three different datasets where we accumulated the largest and most diversified one.

**Data Type**: text (news articles)

**Domains**:
- Natural Language Processing
- Journalism

**Languages**:
- N/A

**Similar Benchmarks**:
- LIAR
- Fake or Real News

**Resources**:
- [GitHub Repository](https://github.com/JunaedYounusKhan51/FakeNewsDetection)
- [Resource](https://www.kaggle.com/mrisdal/fake-news)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate a wide range of machine learning approaches (traditional, deep learning, and advanced pre-trained language models) for fake news detection across three datasets, and to provide a large, diverse combined dataset for comparative benchmarking.

**Target Audience**:
- research community
- news sites/blogs
- online news portals and social media

**Tasks**:
- Text Classification
- Binary Classification (Fake News Detection)

**Limitations**: N/A

## 💾 Data

**Source**: Three datasets: LIAR (12.8K human-labeled short statements from POLITIFACT.COM), Fake or Real News (dataset by George McIntire: fake portion from Kaggle fake news dataset; real portion collected from New York Times, WSJ, Bloomberg, NPR, the Guardian), Combined Corpus (built by the authors containing news collected from multiple sources; fake news sources include The Onion, Borowitz Report, Clickhole, American News, DC Gazette, Natural News, Activist Report; real news sources include New York Times, Breitbart, CNN, Business Insider, the Atlantic, Fox News, Talking Points Memo, Buzzfeed News, National Review, New York Post, the Guardian, NPR, Gigaword News, Reuters, Vox, the Washington Post).

**Size**: LIAR: 12,791 examples; Fake or Real News: 6,335 examples; Combined Corpus: 79,548 examples

**Format**: N/A

**Annotation**: LIAR: 12.8K human-labeled truthfulness ratings converted to binary labels by the authors (pants-fire/false/barely-true -> fake; half-true/mostly-true/true -> true). Fake or Real News: labels provided in the repository (balanced fake and real). Combined Corpus: labeled based on source (news collected from known fake news sites labelled fake and trusted news sources labelled real).

## 🔬 Methodology

**Methods**:
- Model-based evaluation (comparison of 19 models: traditional, deep learning, and pre-trained language models)
- Train/test split (80:20)

**Metrics**:
- Accuracy
- Precision (macro-average)
- Recall (macro-average)
- F1 Score (macro-average)

**Calculation**: Accuracy = (TP + TN) / (TP + FN + TN + FP). Precision and Recall computed per class (real and fake) and then macro-averaged. F1 is the harmonic mean of precision and recall.

**Interpretation**: Higher Accuracy/Precision/Recall/F1 indicates better model performance. The paper reports that pre-trained language models (BERT, RoBERTa, DistilBERT, ELECTRA) outperform traditional and deep learning models; deep learning models outperform traditional models on larger datasets but are prone to overfitting on small datasets; Naive Bayes with n-gram can achieve competitive performance on sufficiently large datasets.

**Baseline Results**: Key reported results: Naive Bayes (bigram TF-IDF) achieves 93% accuracy on Combined Corpus. Bi-LSTM and C-LSTM achieve 95% accuracy on Combined Corpus. RoBERTa achieves 96% accuracy on Combined Corpus and 98% accuracy on Fake or Real News. BERT achieves 95% on Combined Corpus. DistilBERT 93% on Combined Corpus. ELECTRA 95% on Combined Corpus. ELMo 91% on Combined Corpus. On LIAR, best pre-trained models achieve ~62% accuracy.

**Validation**: 80:20 train-test split used for each dataset. For LIAR and Fake or Real News the split was random. For Combined Corpus, 80% (train) and 20% (test) were taken from each topic to maintain balanced distribution. Early stopping was applied using validation loss (delta set to zero).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Governance
- Misuse
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Governance**: Unrepresentative risk testing, Lack of testing diversity
- **Misuse**: Spreading disinformation
- **Societal Impact**: Impact on affected communities

**Potential Harm**: ['Fake news can create devastating impacts and affect people physically and mentally (example: health-related misinformation and COVID-19 related fake news causing public safety issues)', 'Propagation of disinformation (infodemic) impacting public safety']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
