# PeerQA

## 📊 Benchmark Details

**Name**: PeerQA

**Overview**: PeerQA is a document-level Question Answering dataset that source questions from peer reviews of scientific articles. The dataset contains 579 QA pairs from 208 academic papers, focusing on evidence retrieval, unanswerable question classification, and answer generation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science
- Geoscience
- Public Health

**Languages**:
- English

**Similar Benchmarks**:
- BioASQ
- QASPER
- QASA

**Resources**:
- [GitHub Repository](https://github.com/UKPLab/peerqa)

## 🎯 Purpose and Intended Users

**Goal**: To advance and study question answering on scientific documents using peer review sourced questions.

**Target Audience**:
- ML Researchers
- AI Practitioners
- NLP Experts

**Tasks**:
- Evidence Retrieval
- Question Answering
- Answer Generation

**Limitations**: The dataset is limited in size compared to general domain QA datasets, and it primarily focuses on scientific articles written in English.

## 💾 Data

**Source**: Collected from peer reviews of scientific articles and annotated by the original authors.

**Size**: 579 QA pairs from 208 articles

**Format**: JSON

**Annotation**: Expert annotations by the authors of the respective papers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Recall

**Calculation**: Metrics are calculated based on retrieved evidence and generated answers.

**Interpretation**: The evaluation determines how accurately and effectively the QA system answers questions based on the retrieved evidence.

**Baseline Results**: Baseline results are established for all three tasks in PeerQA, detailing model performances.

**Validation**: Validated through expert annotations and comparison with previously established benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis includes examination across different scientific domains but is limited by the predominance of ML and NLP.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authors participated voluntarily, and no personal information was collected beyond their public email addresses.

**Data Licensing**: PeerQA's questions and answers are published under CC-BY-NC-SA 4.0 licenses.

**Consent Procedures**: Authors were contacted via email to participate in the dataset creation.

**Compliance With Regulations**: Not Applicable
