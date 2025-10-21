# Named Entity Swapping for Metadata Anonymization

## 📊 Benchmark Details

**Name**: Named Entity Swapping for Metadata Anonymization

**Overview**: This work introduces an anonymization scheme for a corpus of texts to safeguard metadata from disclosure, specifically preventing large language models from identifying metadata associated with texts by using named entity swapping.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/lsablica/spheroids)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to provide an effective anonymization technique that can prevent metadata disclosure from correlated documents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Data Privacy Professionals

**Tasks**:
- Text Anonymization

**Limitations**: The method can only be applied to a fraction of text chunks in the corpus.

## 💾 Data

**Source**: Earnings call transcripts from various companies.

**Size**: 1,819 chunks

**Format**: Plain text

**Annotation**: Automated identification of named entities using spaCy.

## 🔬 Methodology

**Methods**:
- Named Entity Swapping
- Clustering-based weighting scheme
- Decision-theoretic framework

**Metrics**:
- Data utility
- Disclosure risk

**Calculation**: Metrics calculated by evaluating swaps against pre-swap contingency tables.

**Interpretation**: The balancing act between maintaining data utility and minimizing disclosure risk.

**Validation**: Empirical analysis through predictive checks using state-of-the-art LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Reduction in metadata discovery rate by LLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The method aims to anonymize data by preventing identification of named entities related to metadata.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
