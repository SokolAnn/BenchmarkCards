# BIDWESH (Bangla Dialectal Hate Speech Detection Dataset)

## 📊 Benchmark Details

**Name**: BIDWESH (Bangla Dialectal Hate Speech Detection Dataset)

**Overview**: BIDWESH is the first multi-dialectal Bangla hate speech dataset, constructed by translating and annotating 9,183 instances from the BD-SHS corpus into three major regional dialects. Each entry was manually verified and labeled for hate presence, type, and target group, providing a linguistically rich and inclusive resource for advancing hate speech detection in Bangla.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Similar Benchmarks**:
- BD-SHS

**Resources**:
- [Resource](https://doi.org/10.17632/6y3s457g84.1)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to advance hate speech detection in Bangla by providing a dataset that captures the diversity of regional dialects.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Hate Speech Detection

**Limitations**: N/A

## 💾 Data

**Source**: BD-SHS corpus

**Size**: 9,183 instances

**Format**: CSV

**Annotation**: Manual annotation by linguistic experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics were calculated based on the proportion of correctly identified hate and non-hate instances compared to the total instances.

**Interpretation**: High accuracy and F1 scores indicate effective hate speech detection capabilities across dialects.

**Baseline Results**: N/A

**Validation**: A comprehensive five-stage validation process was implemented, including re-evaluation and final checks for semantic consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: The dataset aims to prevent harmful speech and reduce bias in detection capabilities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
