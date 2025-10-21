# A Benchmark to Understand the Role of Knowledge Graphs on Large Language Model’s Accuracy for Question Answering on Enterprise SQL Databases

## 📊 Benchmark Details

**Name**: A Benchmark to Understand the Role of Knowledge Graphs on Large Language Model’s Accuracy for Question Answering on Enterprise SQL Databases

**Overview**: This study aims to evaluate the accuracy of LLM-powered question answering systems in the context of enterprise questions and SQL databases, while also exploring the role of knowledge graphs in improving accuracy.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- Spider
- WikiSQL
- KaggleDBQA

**Resources**:
- [GitHub Repository](https://github.com/datadotworld/cwd-benchmark-data)
- [Resource](https://www.omg.org/cgi-bin/doc?dtc/13-04-15.ddl)
- [Resource](https://myinsurancecompany.linked.data.world)

## 🎯 Purpose and Intended Users

**Goal**: To understand the accuracy of LLM-powered question answering systems with respect to enterprise questions and the role knowledge graphs play in improving accuracy.

**Target Audience**:
- ML Researchers
- Enterprise Data Analysts
- Business Intelligence Professionals

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark utilizes the OMG Property and Casualty Data Model database schema and includes a set of enterprise natural language questions.

**Size**: 43 questions

**Format**: CSV

**Annotation**: Questions are mapped to expected SQL queries and evaluated based on execution accuracy.

## 🔬 Methodology

**Methods**:
- Zero-shot prompting

**Metrics**:
- Accuracy
- Overall Execution Accuracy (OEA)
- Average Overall Execution Accuracy (AOEA)

**Calculation**: Execution Accuracy is calculated by comparing the output of generated SQL queries against reference SQL queries.

**Interpretation**: A higher OEA signifies a more accurate question answering system capable of matching expected outputs.

**Baseline Results**: GPT-4 achieved an AOEA of 16.7% for SQL and 54.2% for SPARQL over Knowledge Graph.

**Validation**: Results validated by performing numerous executions of queries against sample data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
