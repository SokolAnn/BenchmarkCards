# CLIBENCH

## 📊 Benchmark Details

**Name**: CLIBENCH

**Overview**: CLIBENCH is a novel benchmark developed from the MIMIC IV dataset, offering a comprehensive and realistic assessment of LLMs’ capabilities in clinical diagnosis. It covers diagnoses from a diverse range of medical cases across various specialties and incorporates clinical tasks like treatment procedure identification, lab test ordering and medication prescriptions.

**Data Type**: multimodal

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MultiMedQA

**Resources**:
- [Resource](https://clibench.github.io)
- [GitHub Repository](https://github.com/clibench/clibench)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the evaluation of LLMs in clinical decision capabilities through a comprehensive benchmark that includes a diverse range of medical cases and clinical tasks.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Diagnosis
- Procedure Identification
- Lab Test Ordering
- Medication Prescription

**Limitations**: N/A

## 💾 Data

**Source**: MIMIC IV dataset

**Size**: 1,000+ examples

**Format**: N/A

**Annotation**: Cross-table data extraction with NLP pipeline and human verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- Micro Precision
- Micro Recall

**Calculation**: Metrics are calculated by comparing predicted decisions with factual decisions across different levels of granularity.

**Interpretation**: Scores are interpreted at various levels from chapter-level to specific code matching, reflecting the model's decision-making complexity.

**Baseline Results**: Preliminary results highlight strengths and weaknesses of leading LLMs in clinical decision-making.

**Validation**: Evaluation set is sampled to cover a diverse and broad range of output space.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
