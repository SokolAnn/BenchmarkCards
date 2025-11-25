# Argument Summarisation and Evaluation (ASE)

## 📊 Benchmark Details

**Name**: Argument Summarisation and Evaluation (ASE)

**Overview**: The ASE dataset captures the end-to-end process of preparing an argumentative essay for a debate, covering tasks of claim and evidence identification, evidence convincingness ranking, argumentative essay summarisation, and quality evaluation based on human feedback.

**Data Type**: argumentative essay examples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- IAM

**Resources**:
- [GitHub Repository](https://github.com/HaoBytes/ArgSum-Datatset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for evaluating end-to-end argument mining and summarisation systems.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Evidence Detection
- Evidence Convincingness Ranking
- Argumentation Summary
- Summary Quality Ranking

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various open-source sources, encompassing 31 debate topics.

**Size**: 14,000 examples

**Format**: N/A

**Annotation**: Annotated by human experts using the Amazon Mechanical Turk platform.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L
- Mean Average Precision (MAP)

**Calculation**: Metrics are calculated using standard evaluation techniques for argument mining tasks.

**Interpretation**: Higher scores indicate better alignment with human preferences and argument quality.

**Validation**: Performance evaluated using human assessments and established automated metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants were informed about the task and could exit at any time.

**Compliance With Regulations**: Not Applicable
