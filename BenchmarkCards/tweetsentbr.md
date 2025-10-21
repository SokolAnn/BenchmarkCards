# TweetSentBR

## 📊 Benchmark Details

**Name**: TweetSentBR

**Overview**: A sentiment corpus for Brazilian Portuguese manually annotated with 15,000 tweets from the TV show domain, labeled in three classes (positive, neutral, negative) by seven annotators; includes baseline polarity classification experiments reported in the paper.

**Data Type**: text (tweets)

**Domains**:
- Natural Language Processing
- Social Media
- Entertainment

**Languages**:
- Brazilian Portuguese

**Similar Benchmarks**:
- ReLi
- Buscape corpus
- Mercado Livre corpus
- Corpus 7x1
- Computer-BR

**Resources**:
- [Resource](http://bitbucket.org/HBrum/tweetsentbr/)
- [GitHub Repository](https://github.com/bear/python-twitter)

## 🎯 Purpose and Intended Users

**Goal**: Provide a manually annotated corpus (TweetSentBR) for polarity (sentiment) classification in Brazilian Portuguese using tweets from TV show-related content.

**Target Audience**:
- Natural Language Processing researchers
- Machine Learning researchers

**Tasks**:
- Sentiment Analysis
- Text Classification

**Limitations**: Due to Twitter Privacy Policy the authors provide only tweet IDs rather than full tweet text; the authors note the corpus could be improved by labeling more data manually or using semi-supervised methods.

## 💾 Data

**Source**: Tweets extracted from Twitter between January and July 2017 using the Python-Twitter wrapper for the Twitter API; focused on nine TV programs from three major Brazilian TV channels; tweets from official accounts and retweets were discarded.

**Size**: 15,000 tweets (17,166 tokens); training set: 12,999 documents; test set: 2,001 documents

**Format**: N/A

**Annotation**: Manual annotation by seven native speakers (from linguistics, journalism and computer science) following a written codebook; annotators could mark a 'doubt' checkbox; majority voting used to determine final label; supervisors annotated a portion to form a revised test set; Krippendorff's Alpha used to measure agreement.

## 🔬 Methodology

**Methods**:
- Naive Bayes
- Support Vector Machine (linear kernel)
- Hybrid classifier (SVM + lexical-based)

**Metrics**:
- F-Measure
- Accuracy

**Calculation**: F-Measure and Accuracy reported for binary (positive/negative) and three-class (positive/neutral/negative) classification; paper does not specify macro vs. micro averaging.

**Interpretation**: The paper reports baseline performance values for the corpus but does not define explicit thresholds for what constitutes good vs. poor performance.

**Baseline Results**: Binary classification (pos/neg): Naive Bayes F-Measure 0.7987, Accuracy 0.8099; SVM F-Measure 0.8099, Accuracy 0.8206; Hybrid Classifier F-Measure 0.7659, Accuracy 0.7684. Three-class classification (pos/neu/neg): Naive Bayes F-Measure 0.5985, Accuracy 0.6462; SVM F-Measure 0.5964, Accuracy 0.6462.

**Validation**: A held-out test set of 2,001 documents was created (partially annotated by supervisors) for evaluation; Krippendorff's Alpha was used during agreement phases; final labels determined by majority voting.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy

**Atlas Risks**:
- **Privacy**: Data privacy rights alignment

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors state that Twitter's Privacy Policy forbids redistribution of full tweet content; therefore only tweet IDs are released and users must have valid Twitter credentials to retrieve the tweets. Retweets and posts from official accounts were discarded.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complies with Twitter Privacy Policy by distributing only tweet IDs rather than full tweet text.
