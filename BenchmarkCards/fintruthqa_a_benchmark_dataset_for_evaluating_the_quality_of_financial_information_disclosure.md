# FinTruthQA (A Benchmark Dataset for Evaluating the Quality of Financial Information Disclosure)

## 📊 Benchmark Details

**Name**: FinTruthQA (A Benchmark Dataset for Evaluating the Quality of Financial Information Disclosure)

**Overview**: FinTruthQA is a benchmark designed to evaluate advanced natural language processing (NLP) techniques for the automatic quality assessment of information disclosure in financial Q&A data. It comprises 6,000 real-world financial Q&A entries and was manually annotated based on four key evaluation criteria: question identification, question relevance, answer readability, and answer relevance.

**Data Type**: question-answering pairs

**Domains**:
- Finance
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](https://anonymous.4open.science/r/FinTruthQA-218F)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust foundation for the automatic evaluation of financial information disclosure and to foster transparency, fairness, and investor protection.

**Target Audience**:
- Auditors
- Regulators
- Financial Analysts
- Researchers

**Tasks**:
- Question Identification
- Question Relevance
- Answer Readability
- Answer Relevance

**Limitations**: N/A

## 💾 Data

**Source**: Q&A entries collected from the interactive platforms of the Shanghai Stock Exchange (SSE) and Shenzhen Stock Exchange (SZSE).

**Size**: 6,000 examples

**Format**: N/A

**Annotation**: Each Q&A entry was manually annotated based on four evaluation criteria: question identification, question relevance, answer readability, and answer relevance.

## 🔬 Methodology

**Methods**:
- Machine Learning models
- Pre-trained Language models
- Large Language Models

**Metrics**:
- Accuracy
- F1 Score
- Quadratic Weighted Kappa (QWK)

**Calculation**: Evaluation metrics are calculated based on model predictions compared to annotated labels.

**Interpretation**: Higher scores in accuracy, precision, recall, and F1 indicate better performance in identifying and evaluating financial Q&A responses.

**Baseline Results**: FinBERT showed the highest performance metrics across tasks, outperforming all other models.

**Validation**: Models were benchmarked against the annotated dataset, with evaluations performed in a specified training, validation, and testing split.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
