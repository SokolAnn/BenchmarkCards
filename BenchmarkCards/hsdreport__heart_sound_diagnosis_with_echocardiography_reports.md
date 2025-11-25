# HSDreport: Heart Sound Diagnosis with Echocardiography Reports

## 📊 Benchmark Details

**Name**: HSDreport: Heart Sound Diagnosis with Echocardiography Reports

**Overview**: HSDreport is a new benchmark for heart sound diagnosis (HSD) that mandates the direct utilization of heart sounds obtained from auscultation to predict echocardiography reports. It aims to merge the convenience of auscultation with the comprehensive nature of echocardiography reports.

**Data Type**: heart sound samples and echocardiography reports

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2408.08669)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark that utilizes both heart sounds and echocardiography for more accurate diagnosis of congenital heart diseases.

**Target Audience**:
- Medical Researchers
- Healthcare Practitioners

**Tasks**:
- Multi-label Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected from 2,275 participants who underwent echocardiography, comprising audio recordings of heart sounds and their corresponding echocardiography reports.

**Size**: 2,275 heart sound samples

**Format**: N/A

**Annotation**: Manually annotated with corresponding echocardiography reports.

## 🔬 Methodology

**Methods**:
- Knowledge-aware query-based transformer

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the performance comparison with state-of-the-art models.

**Interpretation**: Higher scores indicate better performance in diagnosing congenital heart diseases.

**Baseline Results**: Compared against traditional heart sound diagnosis models (STFT-HSC, DS-CNN, CTENN) with significant improvements in F1 scores.

**Validation**: The benchmark was validated through comparative analysis with existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Focuses on pediatric subjects, potentially not representative of the broader population.

**Potential Harm**: ['Potential misdiagnosis due to the variability of heart sound interpretation.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Informed consent was obtained from all participants and personal identifiers were removed from datasets.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from all participants or their legal guardians.

**Compliance With Regulations**: The study adhered to national regulations and was approved by an independent ethics committee.
