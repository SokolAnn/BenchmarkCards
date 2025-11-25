# Software Heritage License Dataset (2022 Edition)

## 📊 Benchmark Details

**Name**: Software Heritage License Dataset (2022 Edition)

**Overview**: The dataset consists of a collection of 6.9 million unique license documents obtained from public code repositories, aiming to characterize software licenses and facilitate further research and analysis related to license terms.

**Data Type**: text

**Domains**:
- Software Engineering
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SPDX
- ScanCode LicenseDB

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.8200352)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to produce a comprehensive dataset that aids in understanding software licenses used in publicly available source code and to assist in the development of tools and methods for license detection and analysis.

**Target Audience**:
- Researchers
- Industry Practitioners
- Legal Analysts

**Tasks**:
- License Detection
- NLP Analysis of Legal Texts
- Automated License Classifier Training

**Limitations**: N/A

## 💾 Data

**Source**: Software Heritage archive

**Size**: 6.9 million documents

**Format**: CSV, JSON, TAR

**Annotation**: Manual annotation combined with automated ScanCode analysis.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual annotation

**Metrics**:
- Document Count
- License Presence Rate

**Calculation**: Metrics are calculated through a combination of automated analysis using ScanCode and manual review of a random sample of the dataset.

**Interpretation**: Results are used to evaluate the completeness and usefulness of the dataset for licensing information analysis.

**Baseline Results**: Accuracy of ScanCode was high, with 70% of licenses detected scoring 100 on the confidence scale.

**Validation**: Sample validated through manual annotations and comparisons with existing license databases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open data

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
