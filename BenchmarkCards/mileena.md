# Mileena

## 📊 Benchmark Details

**Name**: Mileena

**Overview**: Mileena is a fast, private, and high-quality task-based dataset search platform built on pre-computed semi-ring sketches for efficient ML training and evaluation. It utilizes a novel Factorized Privacy Mechanism for differential privacy while maintaining performance.

**Data Type**: dataset search results

**Domains**:
- Natural Language Processing
- Data Science

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2308.05637)

## 🎯 Purpose and Intended Users

**Goal**: To develop a platform that identifies complementary datasets to improve machine learning model performance while addressing latency, privacy, and data quality issues.

**Target Audience**:
- Data Scientists
- Machine Learning Researchers
- Industry Practitioners

**Tasks**:
- Dataset Augmentation

**Limitations**: N/A

## 💾 Data

**Source**: Various dataset repositories and providers.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Semi-ring sketches for data discovery and augmentation
- Differentially private algorithms for query execution

**Metrics**:
- Task utility (R2 Score)
- Response latency

**Calculation**: Metrics calculated via ML model evaluations after dataset augmentation using semi-ring operations.

**Interpretation**: Higher R2 scores indicate better model performance and utility from the augmentations.

**Baseline Results**: Compared against existing dataset search platforms such as ARDA and AutoML services.

**Validation**: Ongoing experiments and evaluations to assess the accuracy of the datasets and models used.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Data Quality
- Latency

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Utilizes differential privacy mechanisms to ensure user data confidentiality.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Adheres to differential privacy standards to comply with data protection regulations.
