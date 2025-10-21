# NaijaSenti: A Nigerian Twitter Sentiment Corpus for Multilingual Sentiment Analysis

## 📊 Benchmark Details

**Name**: NaijaSenti: A Nigerian Twitter Sentiment Corpus for Multilingual Sentiment Analysis

**Overview**: NaijaSenti is the first large-scale human-annotated Twitter sentiment dataset for the four most widely spoken languages in Nigeria—Hausa, Igbo, Nigerian-Pidgin, and Yorùbá—consisting of around 30,000 annotated tweets per language, including a significant fraction of code-mixed tweets.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Hausa
- Igbo
- Nigerian-Pidgin
- Yorùbá

**Resources**:
- [GitHub Repository](https://github.com/hausanlp/NaijaSenti)

## 🎯 Purpose and Intended Users

**Goal**: To foster research on sentiment analysis in under-represented languages and provide a benchmark dataset for multilingual sentiment analysis.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Sentiment Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Tweets collected using the Twitter Academic API and annotated by native speakers

**Size**: 120,000 tweets (approximately 30,000 tweets per language)

**Format**: N/A

**Annotation**: Manually annotated by native speakers with a training and quality control process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Micro F1
- Weighted F1

**Calculation**: F1 scores calculated based on classification tasks for sentiment analysis.

**Interpretation**: Higher F1 scores indicate better model performance in classifying sentiment.

**Baseline Results**: AfriBERTa achieves the best performance across all languages.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
