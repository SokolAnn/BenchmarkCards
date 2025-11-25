# MEDEC (Medical Error Detection and Correction in Clinical Notes)

## 📊 Benchmark Details

**Name**: MEDEC (Medical Error Detection and Correction in Clinical Notes)

**Overview**: MEDEC is the first publicly available benchmark for medical error detection and correction in clinical notes, covering five types of errors. It consists of 3,848 clinical texts to assess the ability of language models to validate existing or generated medical text for correctness and consistency.

**Data Type**: clinical texts

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/abachaa/MEDEC)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for assessing automated medical error detection and correction in clinical notes.

**Target Audience**:
- ML Researchers
- Model Developers
- Healthcare Professionals

**Tasks**:
- Error Detection
- Error Correction

**Limitations**: The dataset is limited in terms of size and types of medical errors.

## 💾 Data

**Source**: 3,848 clinical texts from three US hospital systems, with errors introduced by medical annotators.

**Size**: 3,848 clinical texts

**Format**: N/A

**Annotation**: Annotated by eight medical annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Recall
- ROUGE-1
- BERTScore
- BLEURT

**Calculation**: Metrics describe error detection and correction performance, comparing models with human annotations.

**Interpretation**: Higher scores indicate better performance in error detection and correction tasks.

**Validation**: Tested on clinical texts, comparing LLM performance with medical doctors' assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Clinical notes were de-identified.

**Data Licensing**: The UW subset requires signing a data usage agreement (DUA).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
