# MSRS (Multi-Source Retrieval-Augmented Generation)

## 📊 Benchmark Details

**Name**: MSRS (Multi-Source Retrieval-Augmented Generation)

**Overview**: MSRS introduces two new benchmarks, MSRS-S TORY for narrative synthesis and MSRS-M EET for summarization tasks, designed to evaluate retrieval-augmented generation systems by necessitating the integration of information from multiple sources.

**Data Type**: query-summary pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuALITY
- QMSum

**Resources**:
- [GitHub Repository](https://github.com/yale-nlp/MSRS)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate retrieval-augmented generation systems by requiring the synthesis of information from multiple complementary documents.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-Document Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from existing long-context, query-focused summarization datasets including SQuALITY and QMSum.

**Size**: 1,071 examples for MSRS-S TORY and 436 examples for MSRS-M EET

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE
- BERTScore
- G-E VAL

**Calculation**: Metrics are computed based on the generated summaries compared to ground truth summaries.

**Interpretation**: Higher scores indicate better retrieval and generation quality.

**Baseline Results**: MSRS-S TORY shows significant improvements with dense retrieval models over sparse models like BM25.

**Validation**: Human evaluations found high quality and utility across the datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
