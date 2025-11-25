# TEAI (Task Exposure to AI) and TRAI (Task Replacement by AI) Indexes

## 📊 Benchmark Details

**Name**: TEAI (Task Exposure to AI) and TRAI (Task Replacement by AI) Indexes

**Overview**: This paper develops a reproducible framework that assesses job exposure to AI and robotics through the TEAI index, which measures the extent to which AI can perform job-related tasks, and the TRAI index, which measures task substitutability by AI. The framework uses large language models to assess the performance potential of AI across various occupations and tasks.

**Data Type**: task-performance ratings

**Domains**:
- Economics
- Labor Market

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Crisp-Unimib/Terminator-Economy)
- [Resource](https://terminatoreconomy.com/home)

## 🎯 Purpose and Intended Users

**Goal**: To assess the potential exposure of different occupations to artificial intelligence and how AI might complement or substitute human labor.

**Target Audience**:
- Economists
- Labor Market Researchers
- Policy Makers
- AI Researchers

**Tasks**:
- Job Exposure Assessment
- Task Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The data for the TEAI and TRAI indexes is derived from O*NET, which includes descriptions for over 19,000 tasks across 1,000 occupations assessed by large language models (LLMs).

**Size**: 19,281 tasks across 1,016 occupations

**Format**: N/A

**Annotation**: The tasks are evaluated by LLMs based on their ratings of how well AI technologies can perform each task.

## 🔬 Methodology

**Methods**:
- Evaluation by Large Language Models
- Human Evaluation

**Metrics**:
- TEAI Index
- TRAI Index

**Calculation**: TEAI is calculated by aggregating task assessment ratings weighted by task relevance, importance, and frequency from O*NET.

**Interpretation**: Higher TEAI scores indicate higher potential AI capability in job tasks; TRAI measures the extent of task substitution.

**Baseline Results**: Comparison against benchmarks from Frey and Osborne (2017) and others, showing significance in correlation.

**Validation**: Validated through human user evaluation with a sample of evaluators from Prolific.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias, Output bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential job displacement but also productivity improvements.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
