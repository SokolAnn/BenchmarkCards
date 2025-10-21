# DailyQA

## 📊 Benchmark Details

**Name**: DailyQA

**Overview**: DailyQA is an automatically updated dynamic dataset that updates questions weekly and contains answers to questions on any given date, designed to evaluate large language models on their ability to handle fast-changing factual data.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TIMEQA
- SITUATEDQA
- FreshLLMs

**Resources**:
- [Resource](https://arxiv.org/abs/2505.17162)

## 🎯 Purpose and Intended Users

**Goal**: To measure LLMs' adaptability and time sensitivity in processing real-world information using dynamically updated queries.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark is intended to evaluate the LLMs’ ability to process Internet information, and does not focus on logical reasoning ability. It contains only one-hop queries.

## 💾 Data

**Source**: Daily updates from Wikipedia revision logs

**Size**: 3,000 queries per week

**Format**: N/A

**Annotation**: Automated query generation and quality checking

## 🔬 Methodology

**Methods**:
- Automated metrics
- Web search augmentation

**Metrics**:
- Subset Match (SM)
- F1 Score
- Rouge-L
- Accuracy

**Calculation**: Metrics are calculated by evaluating model predictions against standard answers.

**Interpretation**: Evaluation reveals the model's capability in matching queries with time-sensitive factual information.

**Baseline Results**: Evaluation on various LLMs demonstrates significant challenges in accuracy, especially for frequently updated queries.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Content derived from Wikipedia, subject to CC BY-SA license terms.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
