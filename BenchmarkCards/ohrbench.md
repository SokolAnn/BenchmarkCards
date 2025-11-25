# OHRBench

## 📊 Benchmark Details

**Name**: OHRBench

**Overview**: OHRBench is a benchmark designed for evaluating the cascading impact of OCR on Retrieval-Augmented Generation (RAG) systems, including various unstructured PDF documents and Q&A pairs derived from multimodal elements in these documents.

**Data Type**: document images and question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/opendatalab/OHR-Bench)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the impact of OCR on RAG systems and assess current OCR solutions' capabilities in constructing knowledge bases for RAG.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- OCR Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Unstructured PDF documents from seven real-world RAG applications: Textbook, Law, Finance, Newspaper, Manual, Academic, and Administration.

**Size**: 8,561 images, 8,498 Q&A pairs

**Format**: PDF, JSON

**Annotation**: Manually annotated and generated Q&A pairs with expert-level review.

## 🔬 Methodology

**Methods**:
- Performance evaluation of OCR solutions

**Metrics**:
- F1 Score
- Edit Distance
- Longest Common Subsequence (LCS)

**Calculation**: Measured the differences between OCR and ground truth data and evaluated retrieval and generation metrics based on the perturbed datasets introduced with OCR noise.

**Interpretation**: Lower values in metrics indicate worse performance in OCR results and their cascading impact on RAG systems.

**Baseline Results**: N/A

**Validation**: Comparative analysis of different OCR solutions using the introduced OHRBench.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Decreased performance in RAG due to OCR errors and noise types.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
