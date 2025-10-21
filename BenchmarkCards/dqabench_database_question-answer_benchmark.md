# DQABench (Database Question-Answer benchmark)

## 📊 Benchmark Details

**Name**: DQABench (Database Question-Answer benchmark)

**Overview**: DQABench is the first comprehensive database QA benchmark for LLMs, featuring an innovative LLM-based method to automate the generation, cleaning, and rewriting of evaluation dataset, resulting in over 200,000 QA pairs in English and Chinese.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Database Management

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate question-answering performance in the database domain and guide future development of LLM-based database applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Database Administrators

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed from a combination of exams, online community questions, and database product manuals.

**Size**: 200,000 QA pairs

**Format**: JSON

**Annotation**: Automated generation, cleaning, and rewriting by large language models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Standardized evaluation process

**Metrics**:
- WinRate
- Multiple Choice Accuracy (MCA)

**Calculation**: Metrics are calculated through a standardized evaluation pipeline that measures the quality of end-to-end answer generation.

**Interpretation**: Higher scores indicate better performance in accurately answering database-related questions.

**Baseline Results**: Compared with performance of seven different LLMs including GPT-4 and GPT-3.5.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
