# FinEval (Financial Domain Knowledge Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: FinEval (Financial Domain Knowledge Evaluation Benchmark)

**Overview**: FinEval is designed to evaluate the financial domain knowledge and practical abilities of large language models (LLMs) with a focus on various aspects of finance including academic knowledge, industry knowledge, security knowledge, and agent capabilities.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- BIG-bench
- FinQA (Financial Question Answering)
- CFLUE (Chinese Financial Language Understanding Evaluation)

**Resources**:
- [GitHub Repository](https://github.com/SUFE-AIFLM-Lab/FinEval)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of FinEval is to provide a comprehensive benchmark for evaluating the capabilities of large language models in the Chinese financial domain, particularly focusing on financial security and agent tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Financial Experts

**Tasks**:
- Financial Academic Knowledge Evaluation
- Financial Industry Knowledge Evaluation
- Financial Security Knowledge Evaluation
- Financial Agent Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Publicly accessible mock exams and adaptations from various financial websites, created and reviewed by financial experts.

**Size**: 8,351 questions

**Format**: N/A

**Annotation**: Questions were adapted from existing exams and manually reviewed by financial professionals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics such as Accuracy are calculated based on the proportion of correct answers out of the total questions in each task category.

**Interpretation**: A higher score indicates better performance in evaluating financial knowledge and abilities of the models being tested.

**Baseline Results**: Claude 3.5-Sonnet achieved the highest weighted average score of 72.9 under zero-shot settings.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: Analysis of performance across different demographic groups in financial knowledge.

**Potential Harm**: ['Inaccurate financial advice leading to poor investment decisions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
