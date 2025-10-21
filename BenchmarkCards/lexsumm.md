# LexSumm

## 📊 Benchmark Details

**Name**: LexSumm

**Overview**: LexSumm is a benchmark designed for evaluating legal summarization tasks in English. It comprises eight English legal summarization datasets from diverse jurisdictions, such as the US, UK, EU, and India.

**Data Type**: document-summary pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LexGLUE
- LegalBench
- LawBench

**Resources**:
- [GitHub Repository](https://github.com/TUMLegalTech/LexSumm-LexT5)

## 🎯 Purpose and Intended Users

**Goal**: To serve as an evaluation platform to foster development of approaches dealing with long legal text using efficient transformer architectures.

**Target Audience**:
- Legal Researchers
- NLP Researchers
- Model Developers

**Tasks**:
- Text Summarization

**Limitations**: An important limitation of our benchmark is its reliance on English-only evaluation, which limits the generalizability of our findings to legal systems operating in languages other than English.

## 💾 Data

**Source**: A collection of eight legal NLG datasets in English language from diverse jurisdictions.

**Size**: 22,218 document-summary pairs from various datasets

**Format**: CSV

**Annotation**: Sourced from governmental and legal institutions, with some datasets containing expert-written summaries.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BERTScore

**Calculation**: Metrics are calculated based on the lexical and semantic overlap between the model-generated output and the reference summary.

**Interpretation**: Higher scores indicate better performance in generating summaries that accurately reflect the content of the legal documents.

**Validation**: Evaluation against existing benchmarks and human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential bias in model generated outputs affecting legal decisions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets are publicly available data, obtained in accordance with data protection laws.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
