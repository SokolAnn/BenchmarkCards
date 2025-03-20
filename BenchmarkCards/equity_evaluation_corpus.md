# Equity Evaluation Corpus

## 📊 Benchmark Details

**Name**: Equity Evaluation Corpus

**Overview**: The Equity Evaluation Corpus (EEC) consists of 8,640 English sentences specifically designed to examine biases towards certain races and genders across various sentiment analysis systems.

**Data Type**: Text

**Domains**:
- Natural Language Processing
- Sentiment Analysis

**Languages**:
- English

**Resources**:
- [Resource](http://saifmohammad.com/WebPages/Biases-SA.html)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset to analyze gender and race biases in sentiment analysis systems.

**Target Audience**:
- Researchers
- Developers
- Data Scientists

**Tasks**:
- Evaluate sentiment intensity predictions regarding race and gender bias.

**Limitations**: The EEC is not a catch-all for all biases but rather a means to examine fairness in sentiment analysis systems.

## 💾 Data

**Source**: Equity Evaluation Corpus compiled from various templates.

**Size**: 8,640 sentences

**Format**: Text

**Annotation**: Sentences chosen to reveal bias towards gender and race.

## 🔬 Methodology

**Methods**:
- Statistical tests to compare predicted scores

**Metrics**:
- Intensity scores
- Statistical significance (t-tests)

**Calculation**: Mean difference of predicted scores between sentences differing only in gender or race.

**Interpretation**: Assessment of bias based on differences in predicted sentiment intensity scores.

**Baseline Results**: Baseline SVM system showed small biases with 0.03 maximum score difference across gender pairs.

**Validation**: Statistical significance established using paired two-sample t-tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias in Sentiment Analysis
- Discrimination in NLP Systems

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Biases were statistically analyzed across gender and race.

**Potential Harm**: Potential perpetuation of human biases in machine learning systems could lead to negative experiences for affected groups.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
