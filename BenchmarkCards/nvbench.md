# nvBench

## 📊 Benchmark Details

**Name**: nvBench

**Overview**: nvBench is a new dataset created to facilitate the translation of natural languages into data visualization commands and SQL queries. It contains pairs of natural language queries and corresponding data visualization commands in vega zero syntax.

**Data Type**: natural language to visualization command pairs

**Domains**:
- Natural Language Processing
- Data Analysis

**Languages**:
- English

**Similar Benchmarks**:
- SEQ2SQL
- COSQL

**Resources**:
- [GitHub Repository](https://github.com/BerkeleyLounge/nvBench)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the efficiency and productivity of transforming natural language queries into data visualization tasks using the nvBench dataset.

**Target Audience**:
- ML Researchers
- Data Scientists
- Model Developers

**Tasks**:
- Natural Language to Visualization Translation

**Limitations**: N/A

## 💾 Data

**Source**: nvBench dataset containing natural language queries and visualization command pairs.

**Size**: 7,247 visualization queries

**Format**: JSON

**Annotation**: Manually created and curated

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the probability of predicting the next word correctly given part of the label query.

**Interpretation**: Higher accuracy indicates better performance in predicting valid visualization commands from natural language queries.

**Validation**: Models validated through training and testing on the nvBench dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
