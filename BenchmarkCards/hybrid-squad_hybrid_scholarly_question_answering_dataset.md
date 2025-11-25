# Hybrid-SQuAD (Hybrid Scholarly Question Answering Dataset)

## 📊 Benchmark Details

**Name**: Hybrid-SQuAD (Hybrid Scholarly Question Answering Dataset)

**Overview**: Hybrid-SQuAD is a novel large-scale QA dataset designed to facilitate answering questions incorporating both text and KG facts. It consists of 10.5K question-answer pairs generated from DBLP and SemOpenAlex alongside corresponding text from Wikipedia.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DBLP-QuAD
- SciQA
- QASA

**Resources**:
- [GitHub Repository](https://github.com/semantic-systems/hybrid-squad)

## 🎯 Purpose and Intended Users

**Goal**: To fill the gap in existing Scholarly Question Answering datasets by fostering the development of hybrid QA systems that integrate information from multiple heterogeneous sources.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Hybrid-SQuAD was created using question-answer pairs generated via a large language model and incorporates data from DBLP and SemOpenAlex as well as Wikipedia text.

**Size**: 10,500 question-answer pairs

**Format**: JSON

**Annotation**: Automatically generated using a large language model

## 🔬 Methodology

**Methods**:
- Automated question-answer generation

**Metrics**:
- Exact Match (EM)
- F-Score

**Calculation**: Metrics are calculated based on the proportion of predictions that match the gold answers in the dataset.

**Interpretation**: An exact match score reflects the model's ability to produce precise outputs, with higher scores indicating better performance.

**Baseline Results**: RAG-based (ChatGPT-3.5) achieved an EM score of 69.65 and F-Score of 74.91 on Hybrid-SQuAD.

**Validation**: The dataset was evaluated using baseline models compared to existing scholarly QA models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
