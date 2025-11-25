# A Corpus of English-Hindi Code-Mixed Tweets for Sarcasm Detection

## 📊 Benchmark Details

**Name**: A Corpus of English-Hindi Code-Mixed Tweets for Sarcasm Detection

**Overview**: We present the first English-Hindi code-mixed dataset of tweets marked for presence of sarcasm and irony where each token is also annotated with a language tag. We present a baseline supervised classification system developed using the same dataset which achieves an average F-score of 78.4 after using random forest classifier and performing 10-fold cross validation.

**Data Type**: text (English-Hindi code-mixed tweets with token-level language annotations)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hindi

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Provide a resource of English-Hindi code-mixed tweets containing sarcastic and non-sarcastic tweets with tweet-level sarcasm annotation and token-level language annotation to train, develop and evaluate sarcasm detection and language identification techniques on code-mixed text.

**Target Audience**:
- Researchers developing and evaluating sarcasm detection and language identification systems

**Tasks**:
- Sarcasm Detection
- Language Identification

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Twitter using the Twitter Scraper API by extracting tweets containing hashtags #sarcasm and #irony and keywords such as 'bollywood', 'cricket' and 'politics'; English-Hindi code-mixed tweets were manually selected and annotated.

**Size**: 5,250 tweets (504 sarcastic, 4,746 non-sarcastic)

**Format**: Tweets originally collected in JSON (Twitter Scraper API); released dataset structured into three plain text files: 1) tweet id + tweet text, 2) tweet id + token-level language annotations, 3) tweet id + sarcasm label.

**Annotation**: Tweet-level sarcasm annotation (YES/NO) by annotators fluent in both English and Hindi; token-level language annotation with tags 'en', 'hi' and 'rest' manually verified; inter-annotator agreement Cohen's Kappa = 0.79.

## 🔬 Methodology

**Methods**:
- Supervised classification using Support Vector Machine (RBF kernel)
- Supervised classification using Linear Support Vector Machine
- Supervised classification using Random Forest
- 10-fold cross validation
- Chi-square feature selection (to reduce feature vector size to 500)

**Metrics**:
- F-score
- Precision
- Recall
- Cohen's Kappa (for inter-annotator agreement)

**Calculation**: F-score is defined as the harmonic mean of precision and recall: F-score = 2 * precision * recall / (precision + recall). Precision = tp / (tp + fp). Recall = tp / (tp + fn).

**Interpretation**: F-score is used because the number of sarcastic tweets is less than the number of non-sarcastic tweets and thus accuracy may not be a good metric; higher F-score indicates a better balance of precision and recall.

**Baseline Results**: Best average F-score 78.4 (Random Forest, all features, 10-fold cross validation). Feature-wise F-scores (RBF SVM / Random Forest / Linear SVM): Character n-grams 73.1 / 75.0 / 66.4; Word n-grams 71.4 / 76.7 / 68.0; Sarcasm indicative tokens 66.1 / 72.0 / 70.2; Emoticons 62.8 / 68.5 / 65.7; All features 76.5 / 78.4 / 71.7.

**Validation**: 10-fold cross validation for model evaluation; inter-annotator agreement measured using Cohen's Kappa = 0.79.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
