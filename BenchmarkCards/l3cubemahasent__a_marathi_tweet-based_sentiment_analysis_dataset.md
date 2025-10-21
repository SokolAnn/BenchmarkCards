# L3CubeMahaSent: A Marathi Tweet-based Sentiment Analysis Dataset

## 📊 Benchmark Details

**Name**: L3CubeMahaSent: A Marathi Tweet-based Sentiment Analysis Dataset

**Overview**: L3CubeMahaSent is the first major publicly available Marathi Sentiment Analysis dataset, curated using tweets from various Maharashtrian personalities. It consists of 16,000 distinct tweets classified into three broad classes: positive, negative, and neutral.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Marathi

**Resources**:
- [GitHub Repository](https://github.com/l3cube-pune/MarathiNLPar)

## 🎯 Purpose and Intended Users

**Goal**: To advance NLP research for the Marathi language through a publicly available sentiment analysis dataset.

**Target Audience**:
- ML Researchers
- Data Scientists
- NLP Practitioners

**Tasks**:
- Sentiment Analysis
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Tweets extracted from various Maharashtrian personalities' Twitter accounts.

**Size**: 16,000 tweets

**Format**: CSV

**Annotation**: Manually annotated into three classes: positive, negative, and neutral.

## 🔬 Methodology

**Methods**:
- Deep Learning models including CNN, BiLSTM, ULMFiT, mBERT, and IndicBERT

**Metrics**:
- Accuracy

**Calculation**: Accuracy was calculated on the classification results using the various architectures implemented.

**Interpretation**: Higher accuracy indicates better classification performance on the sentiment analysis task.

**Baseline Results**: CNN with Indic fastText embeddings achieved the highest accuracy in 2-class classification at 93.13%.

**Validation**: The dataset was split into training, validation, and testing sets, ensuring class balance in the training and validation datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All tweets kept original hashtags, mentions, and special symbols in the publicly available version.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
