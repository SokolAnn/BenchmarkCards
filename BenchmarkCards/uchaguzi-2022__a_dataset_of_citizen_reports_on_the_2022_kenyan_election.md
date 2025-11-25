# Uchaguzi-2022: A Dataset of Citizen Reports on the 2022 Kenyan Election

## 📊 Benchmark Details

**Name**: Uchaguzi-2022: A Dataset of Citizen Reports on the 2022 Kenyan Election

**Overview**: Uchaguzi-2022 is a dataset of 14,169 categorized and geotagged citizen reports related to the 2022 Kenyan General Election, focusing on election-related issues such as misconduct and violence.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Social Media Analysis

**Languages**:
- English
- Swahili

**Resources**:
- [Resource](https://github.ushahidi.org/uchaguzi-ai/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for modeling and understanding citizen reports on election issues to support AI for Social Good.

**Target Audience**:
- ML Researchers
- Political Analysts
- AI Practitioners

**Tasks**:
- Text Classification
- Geotagging

**Limitations**: The topic labels are not specific to the context of Kenyan elections, which may limit their applicability in other regions.

## 💾 Data

**Source**: Citizen reports collected via the Uchaguzi platform during the 2022 Kenyan General Election.

**Size**: 14,169 examples

**Format**: JSON

**Annotation**: Manual annotation by Ushahidi volunteers

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Micro F1
- Macro F1

**Calculation**: Performance metrics are calculated based on predictions compared to volunteer and expert annotations.

**Interpretation**: Higher F1 scores indicate better model performance in categorization and geotagging tasks.

**Baseline Results**: Human annotation (baseline) achieved 50.4% Micro F1.

**Validation**: Performance is benchmarked against volunteer and expert annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset contains only publicly available data and does not include personally identifiable information.

**Data Licensing**: Data is available for research purposes only upon agreement not to use it for malicious purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The data collection process follows the terms of service of the Uchaguzi platform.
