# CLIMB

## 📊 Benchmark Details

**Name**: CLIMB

**Overview**: A Benchmark of Clinical Bias in Large Language Models, which evaluates both intrinsic and extrinsic bias in LLMs for clinical decision tasks.

**Data Type**: Clinical diagnoses

**Domains**:
- Healthcare
- Clinical Decision-Making

**Resources**:
- [GitHub Repository](https://github.com/uscnlp-lime/climb)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate clinical bias in large language models (LLMs) used in healthcare settings.

**Target Audience**:
- Researchers
- Healthcare professionals
- AI developers

**Tasks**:
- Evaluate intrinsic and extrinsic biases in LLMs
- Assess diagnostic capabilities of LLMs
- Identify disparities across demographic groups

**Limitations**: None

## 💾 Data

**Source**: MIMIC-IV database

**Size**: 199 instances for counterfactual evaluation

**Format**: ICD-10-CM codes

**Annotation**: Demographic information including sex, ethnicity, and insurance types.

## 🔬 Methodology

**Methods**:
- Intrinsic bias evaluation using AssocMAD metric
- Extrinsic bias evaluation through counterfactual interventions in clinical diagnosis tasks

**Metrics**:
- AssocMAD
- Recall rate in diagnosis prediction

**Calculation**: Mean Absolute Deviation (MAD) is used to measure the disparities in associations across demographic groups.

**Interpretation**: Lower AssocMAD indicates lower bias; performance change indicates extrinsic bias.

**Validation**: Comparison of performance across various LLMs from Mistral and LLaMA families.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias in clinical decision-making
- Inequities in healthcare outcomes
- Unintended reinforcement of stereotypes

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: Analysis based on demographic attributes (sex, ethnicity, insurance type).

**Potential Harm**: Potential harm from biased clinical decisions leading to health disparities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data from de-identified Electronic Health Records (EHRs).

**Data Licensing**: Not specified.

**Consent Procedures**: Not specified.

**Compliance With Regulations**: Adheres to guidelines for the use of clinical data.
