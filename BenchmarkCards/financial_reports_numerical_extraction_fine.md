# Financial Reports Numerical Extraction (FINE)

## 📊 Benchmark Details

**Name**: Financial Reports Numerical Extraction (FINE)

**Overview**: The dataset aims to address the issue of dataset scarcity in hybrid long documents (HLDs) and supports future work on information extraction from such documents.

**Data Type**: tabular

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for evaluating information extraction from hybrid long documents using large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Information Extraction

**Limitations**: N/A

## 💾 Data

**Source**: SEC’s EDGAR financial reports.

**Size**: 100,000 examples

**Format**: CSV

**Annotation**: Manually annotated financial KPIs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Relative Error Tolerance Accuracy (RETA)
- Accuracy

**Calculation**: RETA measures the correctness of predictions based on relative error thresholds.

**Interpretation**: Higher RETA percentages indicate better performance in extracting information from financial reports.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
