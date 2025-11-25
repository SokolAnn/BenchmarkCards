# MKP-QA

## 📊 Benchmark Details

**Name**: MKP-QA

**Overview**: MKP-QA is a novel multi-product knowledge-augmented QA framework that introduces new benchmark datasets focused on three Adobe products: Adobe Experience Platform, Target, and Customer Journey Analytics, aimed at enhancing multi-domain question answering.

**Data Type**: query-document pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust framework for multi-product question answering in enterprise software ecosystems and to evaluate domain-specific and cross-domain RAG-QA systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available Adobe Experience League documentation focusing on Adobe Experience Platform, Target, and Customer Journey Analytics.

**Size**: 31,000 query-document pairs for uni-domain datasets and 2,730 query-document pairs for cross-domain datasets.

**Format**: N/A

**Annotation**: Query-document pairs are created by subject matter experts and annotated using both manual and LLM-assisted methods.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Relevancy
- Faithfulness

**Calculation**: Metrics are calculated based on the relevance of retrieved documents and the quality of generated responses against ground truth documentation.

**Interpretation**: Good performance is indicated by high retrieval accuracy and relevancy or faithfulness scores.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
