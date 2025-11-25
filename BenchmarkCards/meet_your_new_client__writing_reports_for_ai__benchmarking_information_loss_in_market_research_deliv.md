# Meet Your New Client: Writing Reports for AI – Benchmarking Information Loss in Market Research Deliverables

## 📊 Benchmark Details

**Name**: Meet Your New Client: Writing Reports for AI – Benchmarking Information Loss in Market Research Deliverables

**Overview**: This study quantifies the information loss that occurs when documents are converted to Markdown for retrieval-augmented generation (RAG). It compares how well documents in PDF and PPTX formats can be used by large language models to answer factual questions, introducing an end-to-end benchmark and a corpus of 41 PPTX documents.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Market Research

**Languages**:
- English

**Similar Benchmarks**:
- DocLayNet
- FinanceBench

**Resources**:
- [GitHub Repository](https://github.com/psimm/meet-your-new-client)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate information loss during document ingestion into retrieval-augmented generation systems and provide guidance for delivering AI-ready reports.

**Target Audience**:
- Market Researchers
- AI Practitioners
- Consultancies

**Tasks**:
- Question Answering

**Limitations**: Information loss may occur in the conversion process, particularly from complex layout elements.

## 💾 Data

**Source**: 41 PPTX documents sourced from GitHub repositories and Q Agentur für Forschung.

**Size**: 41 documents

**Format**: Markdown

**Annotation**: Manual annotation of questions and verifying ground truth answers.

## 🔬 Methodology

**Methods**:
- Document conversion comparison
- Question answering evaluations

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the sum of correct answers divided by the total number of questions.

**Interpretation**: Higher accuracy indicates better performance of the document conversion and questioning process.

**Baseline Results**: Best configuration achieves accuracy of 79% as reported in FinanceBench.

**Validation**: Results validated through comparison with human-annotated ground truth.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**
- **Fairness**

**Demographic Analysis**: Reports cover a range of topics from different market fields, ensuring diverse content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
