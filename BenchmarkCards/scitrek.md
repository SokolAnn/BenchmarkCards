# SciTrek

## 📊 Benchmark Details

**Name**: SciTrek

**Overview**: SciTrek is a novel question-answering benchmark designed to evaluate the long-context reasoning capabilities of large language models (LLMs) using scientific articles, addressing previous limitations with complex questions that require information aggregation and synthesis across multiple full-text scientific articles.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NeedleBench
- Ada-LEval
- BABILong
- HELMET
- LongMemEval

**Resources**:
- [GitHub Repository](https://github.com/oaimli/SciTrek)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the long-context reasoning capabilities of large language models using a novel method of constructing question-answering pairs from scientific articles and corresponding SQL queries.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Scientific articles from Semantic Scholar

**Size**: 21,664 question-answer pairs

**Format**: JSON

**Annotation**: Automatically generated via SQL queries against a constructed database.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match
- F1 Score

**Calculation**: Metrics are calculated based on comparing model outputs to ground-truth answers generated from SQL queries.

**Interpretation**: Performance is assessed based on the percentage of correct responses as compared to ground-truth answers.

**Baseline Results**: N/A

**Validation**: Performance and data quality validated through inter-annotator agreement with human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
