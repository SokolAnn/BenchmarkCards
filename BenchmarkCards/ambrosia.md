# Ambrosia

## 📊 Benchmark Details

**Name**: Ambrosia

**Overview**: Ambrosia is a novel benchmark designed to study ambiguity in semantic parsing, specifically for text-to-SQL tasks. The dataset includes ambiguous questions, their interpretations, and complex SQL queries, generated from multi-table databases in various domains.

**Data Type**: question-answering pairs

**Domains**:
- Education
- Banking
- Entertainment
- Hospitality
- Filmmaking
- Agriculture

**Languages**:
- English

**Similar Benchmarks**:
- Spider
- WikiSQL
- NoisySP

**Resources**:
- [GitHub Repository](https://github.com/saparina/ambrosia)
- [Resource](https://ambrosia-benchmark.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To develop text-to-SQL parsers capable of interpreting ambiguous user requests.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Semantic Parsing
- Text-to-SQL Generation

**Limitations**: N/A

**Out of Scope Uses**:
- N/A

## 💾 Data

**Source**: Generated from multi-table databases supporting various types of ambiguity.

**Size**: 846 databases, 1,277 ambiguous questions, 2,965 SQL queries

**Format**: N/A

**Annotation**: Questions and interpretations were written by human annotators; SQL queries were generated automatically and validated.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Recall
- Precision
- AllFound

**Calculation**: Recall is calculated based on the number of correct SQL queries predicted from the total interpretations.

**Interpretation**: High recall indicates better performance in predicting multiple interpretations for ambiguous questions.

**Baseline Results**: N/A

**Validation**: Model performance was validated through execution of SQL queries against the generated databases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal identifiable information is included in the dataset.

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Participants were informed via Prolific and provided consent.

**Compliance With Regulations**: Not Applicable
