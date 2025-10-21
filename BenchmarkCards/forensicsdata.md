# ForensicsData

## 📊 Benchmark Details

**Name**: ForensicsData

**Overview**: ForensicsData is an extensive Question-Context-Answer (Q-C-A) dataset sourced from actual malware analysis reports, consisting of more than 5,000 Q-C-A triplets aimed at advancing digital forensics by enabling reproducible experiments and fostering collaboration.

**Data Type**: question-context-answer pairs

**Domains**:
- Natural Language Processing
- Cybersecurity
- Digital Forensics

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://arxiv.org/abs/2509.05331)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured and comprehensive Q-C-A dataset for the digital forensics community to support research and tool development.

**Target Audience**:
- Digital Forensics Researchers
- Cybersecurity Professionals

**Tasks**:
- Question Answering
- Data Annotation

**Limitations**: N/A

## 💾 Data

**Source**: 1,500 execution reports sourced from the ANY.RUN malware analysis platform, which provides detailed logs of process execution, file system activity, and behavioral indicators.

**Size**: 5,000 Q-C-A triplets

**Format**: JSON

**Annotation**: Automatically generated via a multi-layered LLM annotation pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Logical Validity
- Relevance
- Completeness

**Calculation**: Metrics assessed through a structured evaluation that measures the logical soundness, relevance to questions, and completeness of answers.

**Interpretation**: Results are interpreted based on logical correctness, relevance of answers to their questions, and the completeness of the information provided.

**Baseline Results**: N/A

**Validation**: Multi-layered validation involving format validation, deduplication, similarity filtering, and LLM-as-Judge review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was generated synthetically to avoid issues related to the privacy of actual data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The dataset generation complies with privacy regulations by not using real sensitive data.
