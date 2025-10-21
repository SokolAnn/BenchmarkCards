# PEOPLE JOIN

## 📊 Benchmark Details

**Name**: PEOPLE JOIN

**Overview**: PEOPLE JOIN is a benchmark for evaluating LM-mediated collaborative problem solving. It comprises two evaluation domains: PEOPLE JOIN-QA, which focuses on questions about tabular data, and PEOPLE JOIN-DOCCREATION, which addresses document creation tasks.

**Data Type**: question-answering pairs, document creation tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SPIDER
- MULTI NEWS

**Resources**:
- [GitHub Repository](https://github.com/microsoft/peoplejoin)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of PEOPLE JOIN is to evaluate the effectiveness of LLM-powered agents in facilitating collaborative information gathering tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Document Creation

**Limitations**: N/A

## 💾 Data

**Source**: The PEOPLE JOIN benchmark consists of synthetic organizations with users, where each user has distinct access to documents crucial for solving collaborative tasks.

**Size**: 500 test tasks for PEOPLE JOIN-QA, 200 test instances for PEOPLE JOIN-DOCCREATION

**Format**: JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- ROUGE-L
- G-Eval

**Calculation**: Metrics are computed based on the comparison of agent responses to ground-truth answers and reference summaries.

**Interpretation**: Metrics indicate the effectiveness of agents in coordinating information gathering and producing accurate responses.

**Baseline Results**: The max accuracy score achievable is 54.8 in PEOPLE JOIN-QA with gpt-4-turbo.

**Validation**: Evaluations are conducted using LM agent implementations and include metrics for both correctness and efficiency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy
- Robustness

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy risks emerge when agents access personal documents.

**Data Licensing**: SPIDER dataset is available under CC BY-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
