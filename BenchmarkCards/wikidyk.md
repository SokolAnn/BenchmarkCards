# WIKIDYK

## 📊 Benchmark Details

**Name**: WIKIDYK

**Overview**: WIKIDYK is a novel, real-world and large-scale knowledge injection benchmark that evolves continuously over time without requiring human intervention. It leverages facts from Wikipedia’s 'Did You Know...' entries to create diverse question-answer pairs for evaluating knowledge memorization in language models.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- EvolvingQA
- RealtimeQA
- StreamingQA
- TemporalWiki
- CKL

**Resources**:
- [GitHub Repository](https://github.com/zhang-yu-wei/WikiDYK)
- [Resource](https://huggingface.co/datasets/YWZBrandon/wikidyk)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the performance of language models in knowledge injection and memorization capabilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Expert-curated facts from Wikipedia's 'Did You Know...' entries.

**Size**: 12,290 facts and 77,180 questions

**Format**: N/A

**Annotation**: Curated by expert Wikipedia editors based on verifiability and clarity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Match accuracy
- Token-level F1

**Calculation**: Metrics are calculated based on substring matches and token alignment to evaluate answer generation quality.

**Interpretation**: Match accuracy assesses the strict presence of target strings, while Token-level F1 provides a measure of partial lexical overlap.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
