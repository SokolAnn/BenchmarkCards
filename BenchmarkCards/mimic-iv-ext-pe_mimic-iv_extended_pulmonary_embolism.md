# MIMIC-IV-Ext-PE (MIMIC-IV Extended Pulmonary Embolism)

## 📊 Benchmark Details

**Name**: MIMIC-IV-Ext-PE (MIMIC-IV Extended Pulmonary Embolism)

**Overview**: This benchmark adds nearly 20,000 labeled CTPA radiology reports from the MIMIC-IV dataset, which can be utilized for better identification and research of pulmonary embolism (PE).

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/username/repo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a publicly available dataset of labeled CTPA reports to improve PE detection and enhance research in the field of hemostasis and thrombosis.

**Target Audience**:
- ML Researchers
- Healthcare Researchers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: MIMIC-IV database

**Size**: 19,942 examples

**Format**: N/A

**Annotation**: Manually labeled by two physicians and verified using a transformer language model

## 🔬 Methodology

**Methods**:
- Manual annotation
- Automated metrics

**Metrics**:
- Sensitivity
- Positive Predictive Value (PPV)

**Calculation**: Sensitivity calculated by the ratio of true positive cases to the total actual positives.

**Interpretation**: Higher sensitivity indicates better performance in identifying true PE cases.

**Validation**: The performance was validated against manual adjudication by physicians.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data in MIMIC-IV has been de-identified.

**Data Licensing**: Not Applicable

**Consent Procedures**: Approved by institutional review boards.

**Compliance With Regulations**: Complies with applicable ethical guidelines.
