# ArabJobs: A Multinational Corpus of Arabic Job Ads

## 📊 Benchmark Details

**Name**: ArabJobs: A Multinational Corpus of Arabic Job Ads

**Overview**: ArabJobs is a publicly available corpus of Arabic job advertisements collected from Egypt, Jordan, Saudi Arabia, and the United Arab Emirates. The dataset captures linguistic, regional, and socio-economic variation in the Arab labour market, aiming to support analyses of gender representation and occupational structure.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Labour Market Analysis
- Sociolinguistics

**Languages**:
- Arabic

**Similar Benchmarks**:
- MADAR
- NADI
- ALDi

**Resources**:
- [GitHub Repository](https://github.com/drelhaj/ArabJobs)

## 🎯 Purpose and Intended Users

**Goal**: To provide a diverse dataset of Arabic job advertisements for NLP and socio-economic research, supporting tasks like gender bias detection and profession classification.

**Target Audience**:
- ML Researchers
- Data Scientists
- Sociolinguists
- NLP Practitioners

**Tasks**:
- Gender Bias Detection
- Profession Classification
- Salary Estimation
- Dialect Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Collected from seven publicly accessible recruitment platforms across Egypt, Jordan, Saudi Arabia, and the UAE.

**Size**: 8,546 advertisements

**Format**: JSON

**Annotation**: Data processed using large language models for salary estimation and classification tasks, with human verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE)
- Accuracy in gender bias detection

**Calculation**: MAE and RMSE were calculated based on salary estimations against known values.

**Interpretation**: Lower MAE and RMSE indicate better accuracy in salary predictions.

**Baseline Results**: Model performances with MAE of 11.83 and RMSE of 14.84.

**Validation**: Validated through human evaluations and comparisons to known salary data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset includes gender representation across job ads, analyzing disparities in job roles and salaries.

**Potential Harm**: Subtle reinforcement of gender biases in job advertisements.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Personally identifiable information was removed during processing.

**Data Licensing**: The corpus is distributed under a research-only license for non-commercial academic use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data collected in compliance with robots.txt directives of the source sites.
