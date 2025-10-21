# Spider 2.0

## 📊 Benchmark Details

**Name**: Spider 2.0

**Overview**: Spider 2.0 is an evaluation framework comprising 632 real-world text-to-SQL workflow problems derived from enterprise-level database use cases, addressing complex SQL environments and multiple SQL dialects.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Spider 1.0
- BIRD

**Resources**:
- [GitHub Repository](https://github.com/sparrell/spider2-sql)
- [Resource](https://spider2-sql.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark that reflects real-world data workflows for evaluating text-to-SQL models in enterprise applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text-to-SQL

**Limitations**: N/A

## 💾 Data

**Source**: Derived from enterprise-level database use cases including Google Analytics and Salesforce, incorporating complex data transformations and SQL workflows.

**Size**: 632 problems

**Format**: JSON

**Annotation**: Tasks are annotated by experts proficient in SQL, with a focus on ensuring complex SQL queries are executed correctly.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Execution Accuracy (EX)
- Success Rate (SR)

**Calculation**: Metrics calculated through evaluation scripts determining the success of SQL queries based on execution results.

**Interpretation**: Higher metrics indicate better model performance; EX measures correctness of SQL query execution, while SR measures the overall task success rate.

**Baseline Results**: The best performance on Spider 2.0 by existing LLMs achieves only 21.3% success rate.

**Validation**: Evaluation procedures ensure rigorous testing through human validation and automated checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Increased model complexity may lead to reduced performance in certain demographics or SQL dialects.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
