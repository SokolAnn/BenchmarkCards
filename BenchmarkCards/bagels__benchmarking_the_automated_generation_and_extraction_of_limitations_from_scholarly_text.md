# BAGELS: Benchmarking the Automated Generation and Extraction of Limitations from Scholarly Text

## 📊 Benchmark Details

**Name**: BAGELS: Benchmarking the Automated Generation and Extraction of Limitations from Scholarly Text

**Overview**: This paper presents a dataset of research limitations extracted from scientific papers along with methods for generating limitations and a framework for evaluating these limitations.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Machine Learning
- Biomedical Research

**Languages**:
- English

**Similar Benchmarks**:
- LIMITGEN

**Resources**:
- [GitHub Repository](https://github.com/IbrahimAlAzhar/BAGELS_Limitation_Gen)
- [Resource](https://huggingface.co/datasets/IbrahimAlAzhar/limitation-generation-dataset-bagels)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset and framework for studying the extraction and generation of limitations in research articles.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Academic Authors

**Tasks**:
- Limitation Extraction
- Limitation Generation

**Limitations**: The dataset is primarily focused on specific NLP and machine learning conferences which may limit broader applicability.

## 💾 Data

**Source**: Dataset extracted from papers and peer reviews from ACL, NeurIPS, and PeerJ.

**Size**: 6,932 NeurIPS papers, 5,739 ACL papers, and 1,000 PeerJ papers.

**Format**: JSON

**Annotation**: Extracted limitations annotated with LLM assistance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-based evaluation

**Metrics**:
- Precision
- Recall
- F1 Score
- ROUGE-L
- BERTScore

**Calculation**: Metrics are calculated based on comparisons between extracted limitations and ground truth.

**Interpretation**: Higher scores indicate better extraction accuracy for limitations.

**Validation**: Evaluated through human annotation comparing LLM extractions against established limitations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accurate Reporting

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No identifiable information from human annotators was used.

**Data Licensing**: Data sourced from publicly available repositories without filtering based on discriminatory attributes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
