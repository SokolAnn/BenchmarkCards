# ParlaSent Multilingual Training Dataset for Sentiment Identification in Parliamentary Proceedings

## 📊 Benchmark Details

**Name**: ParlaSent Multilingual Training Dataset for Sentiment Identification in Parliamentary Proceedings

**Overview**: The paper presents a new training dataset of sentences in 7 languages, manually annotated for sentiment, which are used in a series of experiments focused on training a robust sentiment identifier for parliamentary proceedings.

**Data Type**: sentence-level sentiment data

**Domains**:
- Natural Language Processing
- Political Science

**Languages**:
- Bosnian
- Croatian
- Czech
- English
- Serbian
- Slovak
- Slovenian

**Resources**:
- [Resource](http://hdl.handle.net/11356/1585)
- [Resource](https://huggingface.co/classla/xlm-r-parlasent)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the process of collecting, cleaning, and processing textual data for political science research and to develop sentiment analysis tools for parliamentary discourse.

**Target Audience**:
- Social Scientists
- Political Analysts
- Machine Learning Researchers

**Tasks**:
- Sentiment Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Sentences sampled from parliamentary proceedings of seven European countries.

**Size**: 2,600 sentences per language group

**Format**: JSONL

**Annotation**: Manually annotated by native speakers using a six-item scale for sentiment polarity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- R2 Score
- Mean Average Error (MAE)

**Calculation**: Metrics are calculated based on the predictions made by models on annotated data.

**Interpretation**: Higher R2 values signify better performance in predicting sentiment, while MAE indicates average error per instance.

**Baseline Results**: Dummy model and comparisons to XLM-R base and large models for reference.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-SA 4.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
