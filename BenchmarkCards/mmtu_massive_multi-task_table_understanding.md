# MMTU (Massive Multi-task Table Understanding)

## 📊 Benchmark Details

**Name**: MMTU (Massive Multi-task Table Understanding)

**Overview**: MMTU is a large-scale benchmark comprising 30,647 questions across 25 real-world table tasks, designed to evaluate models' ability to understand, reason, and manipulate real tables at the expert-level.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/MMTU-Benchmark/MMTU)
- [Resource](https://huggingface.co/datasets/MMTU-benchmark/MMTU)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate models' ability in complex table-related tasks faced by professional users.

**Target Audience**:
- Machine Learning Researchers
- Data Scientists
- Database Administrators

**Tasks**:
- Table Understanding
- Table Question Answering
- SQL Generation
- Data Cleaning
- Schema Matching
- Entity Matching

**Limitations**: A limitation of our benchmark is how our tasks are sampled and selected, which may introduce biases.

## 💾 Data

**Source**: Collected from 52 diverse datasets focusing on real-world challenges in table tasks.

**Size**: 30,647 questions

**Format**: JSON

**Annotation**: Expert-labeled based on decades of computer science research.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on comparisons between model predictions and ground-truth answers.

**Interpretation**: Higher accuracy indicates a better model performance on complex table tasks.

**Validation**: Final evaluation includes manual review and verification by domain experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Robustness**: Data poisoning

**Demographic Analysis**: Analysis of demographic factors related to output performance is not explicitly discussed.

**Potential Harm**: ['Potential inaccuracies in output due to model biases.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data selection and content review processes are implemented to minimize privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
