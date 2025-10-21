# Financial Language Model (FiLM)

## 📊 Benchmark Details

**Name**: Financial Language Model (FiLM)

**Overview**: FiLM is a Financial Language Model trained on a diverse financial corpus, designed to improve the generalization performance of financial PLMs across multiple financial tasks.

**Data Type**: text

**Domains**:
- Finance

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/deep-over/FiLM)
- [Resource](https://huggingface.co/HYdsl/FiLMar)

## 🎯 Purpose and Intended Users

**Goal**: To improve the generalization performance of financial language models by leveraging a diverse corpus of financial data.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Sentiment Classification
- Named Entity Recognition
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: A broad range of financial documents including news articles, SEC filings, earnings call transcripts, research papers, and more.

**Size**: 2.4B tokens

**Format**: Plain text

**Annotation**: Data was processed for cleaning and deduplication, details of specific annotations are not specified.

## 🔬 Methodology

**Methods**:
- Fine-tuning on financial tasks using sequence classification and token classification methods.

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics were calculated based on model evaluations across multiple financial NLP tasks.

**Interpretation**: Performance is interpreted based on F1 scores for classification tasks and accuracy for question answering tasks.

**Baseline Results**: Compared to financial PLMs such as FinBERT and general domain PLMs like BERT and RoBERTa.

**Validation**: Extensive evaluation across six financial NLP tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
