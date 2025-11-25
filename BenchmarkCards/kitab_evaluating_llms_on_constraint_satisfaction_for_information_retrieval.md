# KITAB (Evaluating LLMs on Constraint Satisfaction for Information Retrieval)

## 📊 Benchmark Details

**Name**: KITAB (Evaluating LLMs on Constraint Satisfaction for Information Retrieval)

**Overview**: KITAB is a dataset for measuring constraint satisfaction abilities of language models, consisting of book-related data across more than 600 authors and 13,000 queries.

**Data Type**: queries with constraints

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/microsoft/kitab)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the constraint satisfaction capabilities of large language models in the context of information retrieval.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Constraint Satisfaction

**Limitations**: N/A

## 💾 Data

**Source**: Dynamic data collection from WikiData and Open Library based on constraints from author information and book parameters.

**Size**: 13,000 queries

**Format**: CSV

**Annotation**: Data cleaning involves manual verification and checks for consistency and correctness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Irrelevant information
- Satisfaction
- Completeness
- All Correctness

**Calculation**: Metrics are based on the fraction of model outputs that satisfy various constraints defined in the KITAB dataset.

**Interpretation**: Model performance is categorized based on the relevance and correctness of responses to constraint-based queries.

**Validation**: What constitutes good vs. poor performance is determined through comprehensive statistical analysis on the provided queries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
