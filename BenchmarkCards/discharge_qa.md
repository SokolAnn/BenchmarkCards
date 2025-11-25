# DISCHARGE QA

## 📊 Benchmark Details

**Name**: DISCHARGE QA

**Overview**: DISCHARGE QA is a clinical question-answering dataset designed for evaluating the ability of large language models (LLMs) to simulate clinical decision-making processes during patient discharge, including diagnosis inference, medication inference, and discharge instructions.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jou2024/EXPRAG)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of retrieval-augmented generation (RAG) systems in answering discharge-related clinical questions.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: MIMIC-IV Electronic Health Record (EHR) database

**Size**: 1,280 QA pairs

**Format**: JSON

**Annotation**: Generated using historical EHR data to ensure clinical relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy is calculated as the percentage of correctly answered questions; F1 Score is used for multi-select problems.

**Interpretation**: A higher accuracy and F1 Score indicate better performance in correctly identifying discharge diagnoses and instructions.

**Baseline Results**: N/A

**Validation**: To ensure realistic scenarios, questions are generated based on a filtering process of EHR records.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Inaccurate medical diagnoses due to potential biases in the dataset.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
