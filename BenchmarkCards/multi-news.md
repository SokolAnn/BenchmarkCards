# MULTI-NEWS+

## 📊 Benchmark Details

**Name**: MULTI-NEWS+

**Overview**: MULTI-NEWS+ is an enhanced version of the Multi-News dataset created to improve dataset quality through LLM-based data cleansing, specifically targeting the identification and removal of noisy and irrelevant documents in multi-document summarization tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Multi-News

**Resources**:
- [GitHub Repository](https://github.com/c-juhwan/multi_news_plus)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for multi-document summarization tasks by cleansing irrelevant and noisy data using LLM-based methods.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multi-document Summarization

**Limitations**: The approach may still misclassify relevant documents, and the majority voting method does not completely eliminate errors associated with LLMs.

## 💾 Data

**Source**: Cleansed from the original Multi-News dataset through LLM-based annotation.

**Size**: 56,216 articles

**Format**: N/A

**Annotation**: LLM-based annotation utilizing chain-of-thought prompting and self-consistency methods to classify document relevance.

## 🔬 Methodology

**Methods**:
- LLM-based annotation
- Human evaluation

**Metrics**:
- ROUGE
- BERTScore
- BARTScore

**Calculation**: Metrics are calculated based on the performance of summarization models trained on MULTI-NEWS+ compared to the original Multi-News dataset.

**Interpretation**: Improvements in metrics indicate better data quality and performance in multi-document summarization tasks.

**Baseline Results**: Models trained on MULTI-NEWS+ outperformed those trained on original Multi-News across multiple metrics.

**Validation**: Human evaluations were conducted to ensure the accuracy of document classifications and the effectiveness of the cleansing method.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential misclassification of relevant documents leading to bias in dataset usage.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
