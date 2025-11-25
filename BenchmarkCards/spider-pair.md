# Spider-Pair

## 📊 Benchmark Details

**Name**: Spider-Pair

**Overview**: Spider-Pair is a dataset for evaluating the functional correctness of SQL generation, comprising a training set and two testing sets with pairs of SQL queries to simulate diverse evaluation scenarios.

**Data Type**: pairs of SQL queries

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- Spider

**Resources**:
- [GitHub Repository](https://github.com/hggforget/NL2SQL_partial_matching)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the functional correctness of generated SQL queries.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text-to-SQL Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Derived from the Spider dataset, containing natural language and SQL query pairs labeled for functional correctness.

**Size**: 10,181 examples

**Format**: N/A

**Annotation**: Generated SQL pairs using LLMs; manual validation and equivalence rewriting applied.

## 🔬 Methodology

**Methods**:
- Graph Matching Network
- Rule-based Partial Matching

**Metrics**:
- Area Under the Curve (AUC)
- Spearman R
- Kendall-Tau

**Calculation**: Metrics are calculated based on the functional correctness scores of the generated SQL compared to the reference SQL.

**Interpretation**: Higher AUC indicates better functional correctness evaluation performance.

**Baseline Results**: FuncEvalGMN achieves AUCs of 94.32% and 84.80% on test sets.

**Validation**: Results validated against existing SQL evaluation methods and through comparative analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
