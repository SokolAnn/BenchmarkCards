# Spider Benchmark Extended for Heterogeneous Data Sources

## 📊 Benchmark Details

**Name**: Spider Benchmark Extended for Heterogeneous Data Sources

**Overview**: This paper introduces a benchmark that assesses the ability of tools to handle a mixture of database accesses and API calls to answer natural language questions, modifying the existing Spider benchmark to include API integrations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Spider

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating the performance of question-answering systems in heterogeneous data environments.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: The execution accuracy of the final results is the only metric considered; performance metrics like efficiency are suggested for future work.

## 💾 Data

**Source**: Extended Spider benchmark dataset modified to include API calls along with traditional database tables.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Execution Accuracy

**Calculation**: Execution accuracy is measured by comparing system-generated SQL statements against the gold standard SQL queries from the original Spider benchmark.

**Interpretation**: Higher execution accuracy indicates better performance in translating natural language questions into appropriate database and API queries.

**Baseline Results**: The performance of siwarex is benchmarked against a baseline using Gorilla and SQLDatabaseToolkit.

**Validation**: Performance is validated through experimental evaluation against the modified Spider benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
