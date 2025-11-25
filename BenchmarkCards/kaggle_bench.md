# KAGGLE BENCH

## 📊 Benchmark Details

**Name**: KAGGLE BENCH

**Overview**: KAGGLE BENCH is a benchmark of 700 examples spanning 49 domains and 28 task types, capturing the complexity and diversity of real-world data analysis scenarios to evaluate AGENT ADA’s performance.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Finance
- Healthcare
- Legal
- Education
- Robotics
- Computer Vision
- Technology
- Social Networks

**Languages**:
- English

**Similar Benchmarks**:
- Insight-Bench
- DS-1000
- DA-Code

**Resources**:
- [GitHub Repository](https://github.com/ServiceNow/AgentAda)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the analytical capabilities of data analytics agents across a wide range of tasks, skills, and domains.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Data Analysts

**Tasks**:
- Customer Segmentation
- Predictive Maintenance
- Market Analysis
- Association Rule Mining
- Time Series Decomposition
- A/B Testing

**Limitations**: N/A

## 💾 Data

**Source**: High-quality Jupyter notebooks published by data analysts on Kaggle

**Size**: 700 notebooks

**Format**: JSON

**Annotation**: Generated through a two-stage question generation process using GPT-4.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-as-a-judge framework SCORER

**Metrics**:
- Accuracy
- F1 Score
- Depth of Analysis

**Calculation**: Metrics are calculated based on comparison of the generated insights between AGENT ADA and existing analytics tools.

**Interpretation**: Higher scores indicate better performance in generating insightful analytics aligned with user goals.

**Baseline Results**: Comparisons made against other baseline agents including Poirot, Pandas AI, and InfiAgent.

**Validation**: Evaluated on KAGGLE BENCH for robustness and reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misuse of analytics for decision-making without proper evaluation guidelines.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Human evaluators were compensated and provided informed consent.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from all participants before evaluation.

**Compliance With Regulations**: Not Applicable
