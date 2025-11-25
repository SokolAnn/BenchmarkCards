# QFMTS (Query-Focused Multi-Table Summarization)

## 📊 Benchmark Details

**Name**: QFMTS (Query-Focused Multi-Table Summarization)

**Overview**: This paper introduces the QFMTS dataset, which consists of 4,909 query-summary pairs associated with multiple tables to facilitate research in query-focused multi-table summarization.

**Data Type**: query-summary pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- QTSumm

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset specifically tailored for the query-focused multi-table summarization task.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Query-Focused Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from the Spider dataset with additional multi-table examples.

**Size**: 4,909 examples

**Format**: N/A

**Annotation**: Manual and LLM-assisted annotation for generating summaries.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE-L
- BERTScore

**Calculation**: Metrics are calculated using baseline comparisons and human evaluations.

**Interpretation**: Higher ROUGE-L and BERTScore indicate better summary quality.

**Baseline Results**: N/A

**Validation**: Includes automated evaluation followed by human assessment for faithfulness and fluency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
