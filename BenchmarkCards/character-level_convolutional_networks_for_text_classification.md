# Character-level Convolutional Networks for Text Classification

## 📊 Benchmark Details

**Name**: Character-level Convolutional Networks for Text Classification

**Overview**: This article offers an empirical exploration on the use of character-level convolutional networks (ConvNets) for text classification. We constructed several large-scale datasets to show that character-level convolutional networks could achieve state-of-the-art or competitive results.

**Data Type**: text (raw character sequences for classification)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- RCV1

**Resources**:
- [Resource](https://arxiv.org/abs/1509.01626)
- [Resource](http://www.libreoffice.org/)
- [Resource](http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html)

## 🎯 Purpose and Intended Users

**Goal**: Empirical exploration of character-level convolutional networks for text classification and demonstration of their effectiveness using several large-scale datasets.

**Target Audience**:
- Machine Learning Researchers
- Natural Language Processing Researchers

**Tasks**:
- Text Classification
- Sentiment Analysis
- Topic Classification

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from multiple corpora: AG's News corpus (subset of AG corpus of news articles), SogouCA and SogouCS (Sogou News), DBpedia (DBpedia ontology 2014), Yelp Dataset Challenge 2015 (Yelp reviews), Yahoo! Webscope (Yahoo! Answers Comprehensive Questions and Answers v1.0), and Amazon reviews from the Stanford Network Analysis Project (SNAP).

**Size**: AG's News: 120,000 training samples, 7,600 test samples; Sogou News: 450,000 training samples, 60,000 test samples; DBPedia: 560,000 training samples, 70,000 test samples; Yelp Review Polarity: 560,000 training samples, 38,000 test samples; Yelp Review Full: 650,000 training samples, 50,000 test samples; Yahoo! Answers: 1,400,000 training samples, 60,000 test samples; Amazon Review Full: 3,000,000 training samples, 650,000 test samples; Amazon Review Polarity: 3,600,000 training samples, 400,000 test samples.

**Format**: N/A

**Annotation**: Labels derived from original sources or constructed from source metadata: AG's News (selected 4 largest classes from AG corpus), Sogou News (categories labeled by manual classification of domain names/URLs), DBpedia (14 ontology classes selected from DBpedia 2014), Yelp reviews (star ratings used to form full and polarity labels), Yahoo! Answers (10 largest main categories from Yahoo! Webscope), Amazon reviews (review star ratings from SNAP used to form full and polarity labels).

## 🔬 Methodology

**Methods**:
- Automated metrics (test set evaluation)
- Model comparisons (multiple baselines and deep models)

**Metrics**:
- Testing Error (percentage)

**Calculation**: Testing errors are reported as percentage of misclassified examples on the test set. (Table 4: "Numbers are in percentage.")

**Interpretation**: Lower testing error percentage indicates better performance; best and worst results are indicated in Table 4.

**Baseline Results**: Baseline model testing errors are provided in Table 4. Examples (errors in percentage on AG's News): Bag-of-words: 11.19; Bag-of-words TFIDF: 10.36; ngrams TFIDF: 7.64; LSTM: 13.94. (Full table of results across datasets and models reported in Table 4.)

**Validation**: Validation performed on held-out test sets as specified in Table 3. Epoch size (number of minibatches per epoch) is specified per dataset in Table 3; each epoch uses a fixed number of random training samples uniformly sampled across classes.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
