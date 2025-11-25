# USERSUMBENCH

## 📊 Benchmark Details

**Name**: USERSUMBENCH

**Overview**: USERSUMBENCH is a benchmark framework designed to evaluate user summarization approaches through the assessment of user summaries generated from activity timelines, with a focus on aligning future user activity predictions with human preferences.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2408.16966)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for user summarization techniques, facilitating the development of improved LLM-based summarization models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- User Summarization

**Limitations**: N/A

## 💾 Data

**Source**: User activity data from MovieLens, Yelp, and Amazon Review datasets.

**Size**: 6,046 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Quality Metric
- Instruction Following Metric
- Information Density Metric

**Metrics**:
- Quality Metric
- Instruction Following Metric
- Information Density Metric

**Calculation**: Metrics are calculated by assessing the predictive accuracy of generated summaries in forecasting future user activities.

**Interpretation**: Metrics indicate how well summaries capture user information and predict behaviors; higher values correspond to better alignment with human evaluations.

**Baseline Results**: The time-hierarchical and self-critique method serves as a strong baseline for evaluating summarization approaches.

**Validation**: Metrics validated against human ratings across various datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
