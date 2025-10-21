# Lat-KID (Latvian Question-Answer Dataset) and Lit-KID (Lithuanian Question-Answer Dataset)

## 📊 Benchmark Details

**Name**: Lat-KID (Latvian Question-Answer Dataset) and Lit-KID (Lithuanian Question-Answer Dataset)

**Overview**: The study introduces the Lat-KID and Lit-KID datasets, comprising 502 Latvian and 690 Lithuanian question-answer pairs designed to evaluate large language models' abilities in short answer matching. The datasets include matched and non-matched answers generated via specific alteration rules.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Latvian
- Lithuanian

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models on the short answer matching task for Latvian and Lithuanian languages.

**Target Audience**:
- ML Researchers
- Model Developers
- Education Practitioners

**Tasks**:
- Short Answer Matching

**Limitations**: N/A

## 💾 Data

**Source**: Generated from Wikipedia articles.

**Size**: 502 unique questions for Latvian and 690 unique questions for Lithuanian.

**Format**: JSON

**Annotation**: Partially manually verified for quality and accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy and F1 scores calculated based on models' predictions of matched/non-matched answers.

**Interpretation**: Models are expected to output 'True' for matched answers and 'False' for non-matched answers.

**Validation**: Manual evaluation by native speakers of Latvian and Lithuanian.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
