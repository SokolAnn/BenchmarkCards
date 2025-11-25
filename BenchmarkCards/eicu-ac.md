# EICU-AC

## 📊 Benchmark Details

**Name**: EICU-AC

**Overview**: EICU-AC is designed to assess the access control for healthcare agents, evaluating whether specific roles have appropriate access to databases related to ICU patient information.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- Mind2Web-SC

**Resources**:
- [Resource](https://guardagent.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the access control mechanisms in healthcare agents against defined safety requests.

**Target Audience**:
- ML Researchers
- Health Informatics Practitioners

**Tasks**:
- Access Control Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: EICU dataset, adapted for access control evaluation.

**Size**: 316 examples

**Format**: CSV

**Annotation**: Manually labeled based on access permission criteria defined by clinicians.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human annotation for validation

**Metrics**:
- Label prediction accuracy
- Explanation accuracy

**Calculation**: Metrics calculated based on predicted labels versus ground truth labels of access permissions.

**Interpretation**: High accuracy indicates effective access control mechanisms.

**Baseline Results**: Over 98% guardrail accuracy reported.

**Validation**: Evaluated against role-specific access permissions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential misuse of sensitive patient information if access is improperly granted.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data contains no personally identifiable information (PII) as access is role-based.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
