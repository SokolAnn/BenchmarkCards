# Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation

## 📊 Benchmark Details

**Name**: Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation

**Overview**: The paper presents a systematic benchmark for LLM-based Text-to-SQL, addressing the absence of a systematic evaluation framework. It proposes a new integrated solution, DAIL-SQL, which achieves a performance of 86.6% execution accuracy on the Spider leaderboard, surpassing previous methodologies.

**Data Type**: question-SQL pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Spider

**Resources**:
- [GitHub Repository](https://github.com/taoyds/test-suite-sql-eval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive, systematic, and fair benchmark for LLM-based Text-to-SQL, facilitating better understanding and further research in this domain.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text-to-SQL

**Limitations**: N/A

## 💾 Data

**Source**: Spider dataset

**Size**: 8659 training samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Execution Accuracy

**Calculation**: Metrics are calculated based on the output correctness of SQL queries compared to ground truth queries.

**Interpretation**: Higher execution accuracy indicates better performance in translating natural language questions to SQL queries.

**Baseline Results**: Previous state-of-the-art methods include DIN-SQL with 85.3% execution accuracy.

**Validation**: Empirical evaluation against existing state benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
