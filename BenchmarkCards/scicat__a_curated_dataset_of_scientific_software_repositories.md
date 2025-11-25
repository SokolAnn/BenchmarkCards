# SciCat: A Curated Dataset of Scientific Software Repositories

## 📊 Benchmark Details

**Name**: SciCat: A Curated Dataset of Scientific Software Repositories

**Overview**: The SciCat dataset is a comprehensive collection of Free-Libre Open Source Software (FLOSS) projects, designed to address the need for a curated repository of scientific and research software.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- English

**Resources**:
- [Resource](https://worldofcode.org/)

## 🎯 Purpose and Intended Users

**Goal**: To enable studies that focus on trends, common practices, challenges, and evolution in scientific software development.

**Target Audience**:
- ML Researchers
- Software Engineers
- Data Scientists

**Tasks**:
- Software Classification
- Software Trends Analysis

**Limitations**: The accuracy and completeness of the dataset depend on the information extracted from README.md files.

## 💾 Data

**Source**: World of Code dataset, consisting of FLOSS repositories.

**Size**: 350,308 README.md files

**Format**: Pickle file in a tar.gz archive

**Annotation**: Classified by OpenAI’s language models based on README.md files.

## 🔬 Methodology

**Methods**:
- Automated classification using OpenAI's language models
- Manual validation of selected projects

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics were calculated based on Cohen’s Kappa and F1 score metrics from evaluations.

**Interpretation**: Higher F1 scores indicate better identification of scientific application software.

**Validation**: Validation conducted using human raters and comparison with existing datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Analysis of the gender distribution of project authors included.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
