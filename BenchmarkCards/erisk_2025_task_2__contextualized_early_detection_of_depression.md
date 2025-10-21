# eRisk 2025 Task 2: Contextualized Early Detection of Depression

## 📊 Benchmark Details

**Name**: eRisk 2025 Task 2: Contextualized Early Detection of Depression

**Overview**: This benchmark focuses on detecting early signs of depression through full conversational contexts using user-generated text. It requires participants to classify users as showing signs of depression based on their written interactions, leveraging large language models for assessment based on BDI-II criteria.

**Data Type**: text

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- eRisk 2023
- eRisk 2024

**Resources**:
- [GitHub Repository](https://github.com/dsgt-arc/erisk-2025)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and benchmark methodologies for detecting early signs of depression through conversational contexts in user-generated content.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Mental Health Professionals

**Tasks**:
- Binary Classification

**Limitations**: N/A

## 💾 Data

**Source**: User-generated posts from social media platforms (primarily Reddit) within complete conversational contexts.

**Size**: 2,724 users

**Format**: parquet

**Annotation**: Data was presented in JSON format with structured outputs for automated processing.

## 🔬 Methodology

**Methods**:
- Cross-model agreement evaluation
- Internal consistency checks
- Voting classifier
- LightGBM classifier

**Metrics**:
- Depression Category Hit Rate (DCHR)
- Average Difference in Overall Depression Level (ADODL)
- Average Symptom Hit Rate (ASHR)

**Calculation**: Metrics are calculated based on predicted vs. actual BDI-II scores, averaging across multiple runs and models.

**Interpretation**: Good performance is indicated by higher DCHR, ADODL, and ASHR values, with the goal of accurately identifying signs of depression from conversational data.

**Baseline Results**: N/A

**Validation**: Evaluation based on submissions to an official leaderboard.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinterpretation of depressive symptoms', 'Inaccurate assessment leading to mislabeling of users']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data has been anonymized to protect privacy.

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
