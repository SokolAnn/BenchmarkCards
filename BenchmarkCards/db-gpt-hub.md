# DB-GPT-Hub

## 📊 Benchmark Details

**Name**: DB-GPT-Hub

**Overview**: DB-GPT-Hub is an open benchmark suite for LLM-empowered text-to-SQL, focusing on tuning LLMs at large scales and providing a standardized evaluation of text-to-SQL tasks.

**Data Type**: question-SQL pairs

**Domains**:
- Natural Language Processing
- Database

**Languages**:
- English

**Similar Benchmarks**:
- Spider
- BIRD
- WikiSQL
- CoSQL

**Resources**:
- [GitHub Repository](https://github.com/eosphoros-ai/DB-GPT-Hub)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive open benchmark framework for the evaluation of text-to-SQL models utilizing large language models.

**Target Audience**:
- ML Researchers
- Database Practitioners
- Model Developers

**Tasks**:
- Text-to-SQL

**Limitations**: N/A

## 💾 Data

**Source**: Spider and BIRD datasets, among other publicly available datasets.

**Size**: 10,181 examples (Spider), 12,751 examples (BIRD)

**Format**: JSON

**Annotation**: The datasets contain question-SQL pairs, manually annotated.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Execution Accuracy (EX)
- Exact-set match accuracy (EM)

**Calculation**: Metrics are calculated by comparing predicted SQL queries with ground truth SQL queries.

**Interpretation**: Higher EX and EM values indicate better performance, with EX providing a precise estimate of model performance through execution outputs.

**Validation**: The benchmark was validated using standardized protocols and extensive testing across different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache License 2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
