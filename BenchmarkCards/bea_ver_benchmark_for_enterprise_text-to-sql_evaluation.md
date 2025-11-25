# BEA VER (Benchmark for Enterprise Text-to-SQL Evaluation)

## 📊 Benchmark Details

**Name**: BEA VER (Benchmark for Enterprise Text-to-SQL Evaluation)

**Overview**: BEA VER is the first enterprise text-to-SQL benchmark sourced from real private enterprise data warehouses, providing natural language queries and their corresponding SQL statements collected from actual query logs.

**Data Type**: question-SQL pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Spider
- KaggleDBQA
- Bird

**Resources**:
- [Resource](https://peterbaile.github.io/beaver/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating text-to-SQL systems under enterprise settings and identify challenges in using LLMs for real-world enterprise queries.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text-to-SQL
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Two real-world enterprise data warehouses containing a variety of information related to physical administration of plants and enterprise networking.

**Size**: 203 queries

**Format**: N/A

**Annotation**: Annotated by graduate students and database administrators based on real user query logs and reports.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Execution accuracy
- F1 Score
- Exact score

**Calculation**: Execution accuracy is calculated by comparing the execution outputs of predicted SQL statements with gold SQL statements.

**Interpretation**: Higher execution accuracy indicates better performance of SQL generation in responding to user queries.

**Baseline Results**: Off-the-shelf models demonstrated close to 0 end-to-end execution accuracy on BEA VER.

**Validation**: Evaluated against existing public text-to-SQL datasets for comparison.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All database contents and questions will be anonymized according to rules set by the private organizations before releasing them to the public.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
