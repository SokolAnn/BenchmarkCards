# BaitBuster -Bangla: A Comprehensive Dataset for Clickbait Detection in Bangla with Multi -Feature and Multi -Modal Analysis

## 📊 Benchmark Details

**Name**: BaitBuster -Bangla: A Comprehensive Dataset for Clickbait Detection in Bangla with Multi -Feature and Multi -Modal Analysis

**Overview**: This study presents a large multi-modal Bangla YouTube clickbait dataset consisting of 253,070 data points collected through an automated process using the YouTube API and Python web automation frameworks. The dataset contains 18 diverse features categorized into metadata, primary content, engagement statistics, and labels for individual videos from 58 Bangla YouTube channels.

**Data Type**: text, table

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Resources**:
- [Resource](https://data.mendeley.com/datasets/3c6ztw5nft/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for clickbait detection in Bangla, aiding research in low-resource languages and enabling multi-modal analyses of clickbait.

**Target Audience**:
- Researchers
- Data Scientists

**Tasks**:
- Clickbait Detection
- Classification

**Limitations**: N/A

## 💾 Data

**Source**: YouTube API

**Size**: 253,070 records

**Format**: CSV, Parquet, XLSX

**Annotation**: Initial labels were assigned based on predefined channel classifications, followed by manual annotation of a stratified sample of 10,000 data points.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Macro
- F1 Micro
- Kappa

**Calculation**: Metrics were calculated based on the model performances on validation and test datasets.

**Interpretation**: High accuracy and F1 scores indicate effective detection of clickbait.

**Validation**: The dataset was validated through rigorous preprocessing, denoising, deduplication, and debiasing, alongside evaluations of model performances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data has been de-identified and anonymized to protect the privacy of users.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was not required as the data collected is publicly available on YouTube.

**Compliance With Regulations**: The data collection process complied with the terms of service of the YouTube platform.
