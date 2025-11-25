# FanChuan: A Multilingual and Graph-Structured Benchmark For Parody Detection and Analysis

## 📊 Benchmark Details

**Name**: FanChuan: A Multilingual and Graph-Structured Benchmark For Parody Detection and Analysis

**Overview**: FanChuan is designed to address parody detection in social media by providing diverse datasets enriched with contextual information through user-interaction graphs. It contains a total of 21,210 annotated comments and 14,755 annotated users, facilitating comprehensive experiments in parody detection, comment sentiment analysis, and user sentiment analysis.

**Data Type**: annotated comments and user interactions

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/Lisaaa1017/Fanchuan)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for studying parody detection and analysis in multilingual contexts, leveraging user-interaction data and contextual information.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Parody Detection
- Comment Sentiment Classification
- User Sentiment Classification

**Limitations**: N/A

## 💾 Data

**Source**: Seven datasets collected from various social media platforms in both English and Chinese.

**Size**: 21,210 annotated comments and 14,755 annotated users

**Format**: JSON

**Annotation**: Annotated by native speakers with the help of expert judges and refined using Large Language Models.

## 🔬 Methodology

**Methods**:
- Embedding-based methods
- Inconsistency-based methods
- Outlier detection methods
- Graph-based methods
- Large Language Models

**Metrics**:
- F1 Score
- Macro F1 Score

**Calculation**: F1 scores for evaluating parody detection and sentiment classification tasks.

**Interpretation**: Higher F1 scores indicate better model performance in detecting parody and classifying sentiments.

**Baseline Results**: Traditional methods often outperform advanced LLMs in parody detection.

**Validation**: Models evaluated across multiple datasets with consistent performance metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Misunderstanding cultural contexts in parody texts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User-sensitive content removed; the dataset does not include any personally identifiable information.

**Data Licensing**: CC BY 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
