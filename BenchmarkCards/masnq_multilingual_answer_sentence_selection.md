# mASNQ (Multilingual Answer Sentence Selection)

## 📊 Benchmark Details

**Name**: mASNQ (Multilingual Answer Sentence Selection)

**Overview**: We introduce new high-quality datasets for Answer Sentence Selection (AS2) in five European languages (French, German, Italian, Portuguese, and Spanish), obtained through supervised Automatic Machine Translation (AMT) of existing English AS2 datasets.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- French
- German
- Italian
- Portuguese
- Spanish

**Similar Benchmarks**:
- ASNQ
- WikiQA
- TREC-QA

**Resources**:
- [Resource](https://huggingface.co/datasets/matteogabburo/mASNQ)
- [Resource](https://huggingface.co/datasets/matteogabburo/mWikiQA)
- [Resource](https://huggingface.co/datasets/matteogabburo/mTRECQA)

## 🎯 Purpose and Intended Users

**Goal**: To provide high-quality multilingual AS2 datasets to close the performance gap between English and other languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Answer Sentence Selection

**Limitations**: This paper focuses on five European languages, limiting the applicability of findings to other languages.

## 💾 Data

**Source**: Translated datasets from existing English AS2 datasets (ASNQ, WikiQA, and TREC-QA).

**Size**: 100 million question-answer pairs

**Format**: N/A

**Annotation**: Supervised Automatic Machine Translation

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Average Precision (MAP)
- Precision at 1 (P@1)

**Calculation**: Metrics calculated as per standard information retrieval evaluation practices.

**Interpretation**: Higher MAP and P@1 scores indicate better model performance.

**Validation**: Evaluated performance across multiple multilingual models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
