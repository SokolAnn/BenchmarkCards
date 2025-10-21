# MULTI CONIR

## 📊 Benchmark Details

**Name**: MULTI CONIR

**Overview**: MULTI CONIR is a benchmark specifically designed to evaluate retrieval and reranking models under nuanced multi-condition query scenarios across five diverse domains.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare
- Legal
- Entertainment
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/EIT-NLP/MultiConIR)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate information retrieval models in realistic multi-condition scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Information Retrieval

**Limitations**: The dataset relies on automated query generation, which may introduce biases in condition representation.

## 💾 Data

**Source**: Constructed from publicly available sources across five domains.

**Size**: Approximately 2,500 multi-condition queries with corresponding documents.

**Format**: N/A

**Annotation**: Queries and hard negatives were created using structured prompts with LLM-assisted modifications.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Win Rate
- Precision@1
- NDCG@k

**Calculation**: Win Rate is calculated as the proportion of pairwise comparisons where a candidate that fulfills more conditions ranks above one that fulfills fewer.

**Interpretation**: Higher Win Rate indicates better performance in distinguishing documents based on the number of satisfied conditions.

**Validation**: Models were evaluated against both LLM-generated and human-annotated queries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential biases in automated query generation affecting retrieval effectiveness.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not contain sensitive or personally identifiable information.

**Data Licensing**: Publicly available datasets, no specific restrictions stated.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
