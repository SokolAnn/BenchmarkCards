# LAiW

## 📊 Benchmark Details

**Name**: LAiW

**Overview**: LAiW is the first Chinese legal LLMs benchmark designed to evaluate legal large language models (LLMs) based on the logic of legal practice. It categorizes legal capabilities into three levels: basic information retrieval, legal foundation inference, and complex legal applications, encompassing 14 tasks to ensure a comprehensive evaluation.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/siat-nlp/LAiW)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of Chinese legal LLMs based on practical legal capabilities and highlight discrepancies between model performance and legal logic requirements.

**Target Audience**:
- Legal Experts
- AI Researchers
- NLP Practitioners

**Tasks**:
- Legal Question Answering
- Named Entity Recognition
- Judicial Summarization
- Case Recognition
- Charge Prediction
- Prison Term Prediction
- Civil Trial Prediction
- Judicial Reasoning Generation
- Legal Consultation

**Limitations**: N/A

## 💾 Data

**Source**: Combines open-source datasets with proprietary legal data.

**Size**: Various datasets spanning multiple legal tasks corresponding to 14 tasks in total.

**Format**: N/A

**Annotation**: Automated evaluation of LLMs and manual evaluations conducted by legal experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- ROUGE-1
- ROUGE-2
- ROUGE-L

**Calculation**: Metrics calculated based on standard evaluation measures for each legal task across automated and manual evaluations.

**Interpretation**: Higher scores indicate better alignment with the expectations of legal reasoning and logic as determined by legal experts.

**Baseline Results**: Various LLMs evaluated against the benchmark, including GPT-4, ChatGPT, and specialized legal LLMs.

**Validation**: Evaluation includes both automated and manual assessments to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sensitive legal data has been anonymized and ethical evaluations have been conducted by legal experts.

**Data Licensing**: All datasets used are publicly available and have corresponding licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
