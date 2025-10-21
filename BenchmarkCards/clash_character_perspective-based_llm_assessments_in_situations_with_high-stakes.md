# CLASH (Character perspective-based LLM Assessments in Situations with High-stakes)

## 📊 Benchmark Details

**Name**: CLASH (Character perspective-based LLM Assessments in Situations with High-stakes)

**Overview**: CLASH is a meticulously curated dataset consisting of 345 high-impact dilemmas along with 3,795 individual perspectives of diverse values, aiming to study value-based decision-making processes and LLMs' capabilities in navigating high-stakes dilemmas.

**Data Type**: dilemma-perspective pairs

**Domains**:
- Natural Language Processing
- Healthcare
- Finance
- Legal
- Education

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/launch/CLASH)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs on their ability to make value-sensitive decisions in high-stakes dilemmas.

**Target Audience**:
- ML Researchers
- Ethicists
- Model Developers

**Tasks**:
- Value Reasoning Evaluation
- Moral Judgment

**Limitations**: N/A

## 💾 Data

**Source**: Human-written long-form dilemmas curated from public web sources

**Size**: 345 dilemmas, 3,795 perspectives

**Format**: JSON

**Annotation**: Manually inspected and validated by expert annotators

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on model predictions against ground-truth responses for each dilemma.

**Interpretation**: Higher accuracy indicates better alignment with human values and decision-making.

**Validation**: Inter-annotator agreement was measured with an average Cohen’s Kappa score of 0.985.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: Improper value judgment leading to real-world ethical challenges.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
