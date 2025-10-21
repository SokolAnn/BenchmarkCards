# X-Topic

## 📊 Benchmark Details

**Name**: X-Topic

**Overview**: X-Topic is a multilingual dataset featuring content in four distinct languages (English, Spanish, Japanese, and Greek), crafted for the purpose of tweet topic classification. It addresses the lack of labelled multilingual social media data and encourages the development of new methods for multilingual topic classification.

**Data Type**: tweet topic classification data

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Japanese
- Greek

**Similar Benchmarks**:
- TweetTopic

**Resources**:
- [Resource](https://huggingface.co/datasets/cardiffnlp/tweet_topic_multilingual)
- [Resource](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-topic-multilingual)
- [Resource](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-large-topic-multilingual)

## 🎯 Purpose and Intended Users

**Goal**: To expand the resources available for the task of tweet classification, particularly in a multi-label setting and across multiple languages.

**Target Audience**:
- Researchers
- Industry Practitioners
- Data Scientists

**Tasks**:
- Topic Classification

**Limitations**: While our paper provides a comprehensive analysis, the number of languages included in X-Topic selected is relatively small given budget constraints.

## 💾 Data

**Source**: Data collected using Twitter API from social media platform X (Twitter).

**Size**: Approximately 220,000 tweets for each of the four languages, totaling around 880,000 tweets.

**Format**: N/A

**Annotation**: Annotated by five coders, where each coder selects one or more labels from a selection of 19 topics, using an agreement of at least two annotators for topic assignment.

## 🔬 Methodology

**Methods**:
- Machine Learning
- Zero-shot Evaluation
- Few-shot Evaluation
- Monolingual Evaluation
- Cross-lingual Evaluation
- Multilingual Evaluation

**Metrics**:
- Macro-F1 Score
- Micro-F1 Score

**Calculation**: Scores computed based on precision and recall across multiple language settings and models.

**Interpretation**: Macro-F1 measures are used for assessing overall performance, with higher scores indicating better classification quality.

**Validation**: Evaluated through 5-fold cross-validation across various settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset includes diverse linguistic representation but does not specifically analyze demographic factors beyond language.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User mentions are masked to ensure privacy, and guidelines were followed to protect privacy during data collection.

**Data Licensing**: X-Topic will be shared under the CC BY-NC 4.0 Deed (Attribution-NonCommercial 4.0 International).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
