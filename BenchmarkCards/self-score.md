# Self-Score

## 📊 Benchmark Details

**Name**: Self-Score

**Overview**: SelfScore is a novel benchmark designed to assess the performance of automated Large Language Model (LLM) agents on help desk and professional consultation tasks. It enables the comparison of automated agents and human workers by evaluating agents on problem complexity and response helpfulness.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2410.16285)

## 🎯 Purpose and Intended Users

**Goal**: To quantitatively compare the performance of automated LLM agents to human agents in help desk and consultation tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Customer Support
- Help Desk Assistance

**Limitations**: N/A

## 💾 Data

**Source**: Stack Exchange forum posts

**Size**: 2,360 entries

**Format**: JSON

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Helpfulness
- Complexity

**Calculation**: Scores are derived from a 10-point scale based on user and agent helpfulness assessments.

**Interpretation**: Higher scores indicate better performance in responding to customer inquiries, and reflect the quality of both the agent's responses and the user's input.

**Baseline Results**: Human control group had a final score of 23.12.

**Validation**: The benchmark was validated by comparing automated LLM agent performances against human interactions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
