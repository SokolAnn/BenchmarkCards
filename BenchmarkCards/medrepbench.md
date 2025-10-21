# MedRepBench

## 📊 Benchmark Details

**Name**: MedRepBench

**Overview**: MedRepBench is a comprehensive benchmark built from 1,900 de-identified real-world Chinese medical reports to evaluate end-to-end vision-language models (VLMs) for structured medical report understanding. It includes an objective evaluation measuring field-level recall of structured clinical items and an automated subjective evaluation using a large language model to assess factuality, interpretability, and reasoning quality.

**Data Type**: structured clinical data

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate structured interpretation quality in medical reports using vision-language models to assist in healthcare.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners

**Tasks**:
- Information Extraction
- Interpretation

**Limitations**: N/A

## 💾 Data

**Source**: 1,900 de-identified real-world Chinese medical reports collected from diverse departments and acquisition methods.

**Size**: 1,900 reports

**Format**: JSON

**Annotation**: De-identified, annotated by a proprietary OCR system optimized for medical documents.

## 🔬 Methodology

**Methods**:
- Objective evaluation measuring field-level recall
- Automated subjective evaluation using LLM

**Metrics**:
- Recall

**Calculation**: Recall is calculated as the number of correctly extracted fields over the total number of ground-truth fields.

**Interpretation**: Higher recall indicates better extraction performance of the structured clinical content.

**Baseline Results**: N/A

**Validation**: Dataset validation includes filtering, de-identification, and quality checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is de-identified and collected under privacy compliance.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
