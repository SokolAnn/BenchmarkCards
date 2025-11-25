# Spider-Mismatch

## 📊 Benchmark Details

**Name**: Spider-Mismatch

**Overview**: Spider-Mismatch is a new dataset specifically designed to highlight the mismatch problem in SQL conditional clauses, which aims to bridge the gap between existing benchmarks and real-world scenarios.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Spider
- Spider-SYN
- Spider-DK
- Spider-Realistic

**Resources**:
- [Resource](https://arxiv.org/abs/2408.16991)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the SQL generation capabilities of LLMs in real-world scenarios by addressing common database mismatch problems.

**Target Audience**:
- ML Researchers
- Database Engineers
- Data Scientists

**Tasks**:
- Text-to-SQL

**Limitations**: N/A

## 💾 Data

**Source**: Derived from Spider and its variants by modifying questions and SQL queries.

**Size**: N/A

**Format**: N/A

**Annotation**: Manual modification to introduce conditions that reflect real-world scenarios.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Execution Accuracy
- Exact Match Accuracy

**Calculation**: Metrics are computed based on the comparison of predicted SQL queries with gold queries.

**Interpretation**: Higher accuracy scores indicate better performance in generating correct SQL queries.

**Baseline Results**: Tool-SQL outperformed existing methods by 9.6% on Spider-Mismatch using ChatGPT and 7.1% using GPT-4.

**Validation**: Evaluation conducted against standard Text-to-SQL benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misrepresentations in SQL query generation affecting real-world applications.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
