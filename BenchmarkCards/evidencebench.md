# EvidenceBench

## 📊 Benchmark Details

**Name**: EvidenceBench

**Overview**: EvidenceBench is introduced as a benchmark for extracting relevant evidence from biomedical papers, based on a novel pipeline involving hypothesis generation and sentence-level annotation guided by human expert judgments.

**Data Type**: sentence-level evidence retrieval

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/EvidenceBench/EvidenceBench)

## 🎯 Purpose and Intended Users

**Goal**: To measure model performance on the task of evidence retrieval in biomedical literature.

**Target Audience**:
- ML Researchers
- Biomedical Researchers

**Tasks**:
- Evidence Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: A collection of 107,887 CC-BY open-sourced biomedical research papers and 44,772 review papers from PubMed Central.

**Size**: 107,461 papers

**Format**: JSON

**Annotation**: Manual annotation by experts and automated using Large Language Models (LLMs).

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Aspect Recall

**Calculation**: Aspect Recall measures the fraction of study aspects covered by a retrieved set of sentences.

**Interpretation**: Higher Aspect Recall indicates better model performance in retrieving relevant sentences.

**Baseline Results**: N/A

**Validation**: Performance was validated through a test set of annotated research papers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY license for the dataset.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
