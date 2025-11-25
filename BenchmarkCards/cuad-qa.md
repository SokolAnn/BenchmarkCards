# CUAD-QA

## 📊 Benchmark Details

**Name**: CUAD-QA

**Overview**: CUAD-QA is a corpus of 85k question-answer pairs generated over 510 real-world CUAD contract documents, encompassing simple, complex, and summarization-style queries, designed to evaluate the efficacy of the CON-QA framework in securely answering queries while preserving privacy.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/IOTPL-research/con_QA/tree/main/result/nlp_domain_participant_rating)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CUAD-QA is to evaluate privacy-preserving mechanisms in enterprise legal settings and to explore the privacy-utility trade-offs in cloud-based contract question answering.

**Target Audience**:
- ML Researchers
- Legal Experts
- Data Scientists

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: CUAD (Contract Understanding Atticus Dataset) corpus

**Size**: 85,000 question-answer pairs

**Format**: N/A

**Annotation**: The questions were generated using ChatGPT-4o-mini prompted with individual pages from contract documents.

## 🔬 Methodology

**Methods**:
- Empirical evaluations
- Human assessments

**Metrics**:
- Private Entity Restoration Accuracy
- Response Relevancy
- Answer Correctness
- Faithfulness

**Calculation**: Metrics are calculated based on the comparisons with ground-truth answers and through expert evaluations.

**Interpretation**: Higher scores indicate better privacy preservation without a significant decrease in answer quality and context richness.

**Validation**: Evaluated through experimental assessments and expert human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The framework ensures strong protection of sensitive contractual entities through structured anonymization and session-consistent deanonymization.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
