# A ground-truth dataset of real security patches

## 📊 Benchmark Details

**Name**: A ground-truth dataset of real security patches

**Overview**: The dataset provides a ground-truth dataset of natural language artifacts, meta-data, and code changes, integrating a total of 8057 security-relevant commits—the equivalent to 5942 security patches from 1339 different projects spanning 146 types of vulnerabilities and 20 languages.

**Data Type**: CSV files containing code changes, commit messages, and meta-data

**Domains**:
- Computer Security

**Languages**:
- English

**Similar Benchmarks**:
- Secbench
- Big-Vul
- Pontas et al.

**Resources**:
- [GitHub Repository](https://github.com/TQRG/security-patches-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a larger dataset of vulnerabilities validated by experts to support research using natural language, code changes, and codebases.

**Target Audience**:
- ML Researchers
- Software Engineers
- Security Researchers

**Tasks**:
- Vulnerability Detection
- Patch Analysis
- Security Program Analysis

**Limitations**: The dataset integrates security patches without a CVE assigned, leading to missing descriptive data in about 10% of rows.

## 💾 Data

**Source**: Publicly scraped data from the CVE Details database and merged with other datasets.

**Size**: 8057 security-relevant commits, 110,161 non-security-related commits

**Format**: CSV

**Annotation**: Data cleaned and processed to create a comprehensive dataset with natural language artifacts, commit comments, and metadata.

## 🔬 Methodology

**Methods**:
- Data Scraping
- Data Cleaning
- Dataset Merging

**Metrics**:
- Commit Count
- Patch Count

**Calculation**: The number of commits and patches were calculated based on the data collected from the merged datasets.

**Interpretation**: Higher numbers of commits and patches indicate a larger dataset available for analysis.

**Baseline Results**: N/A

**Validation**: Data was validated through expert validation of identified security patches.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Risk of misclassification due to unbalanced dataset']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
