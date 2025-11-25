# MIMIC-Patient

## 📊 Benchmark Details

**Name**: MIMIC-Patient

**Overview**: MIMIC-Patient is a structured dataset built from the MIMIC-III clinical database, designed to support dynamic, patient-level simulations for medical decision-making in a multi-agent framework.

**Data Type**: structured clinical records

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- PubMedQA
- MedMCQA

**Resources**:
- [Resource](https://mimic.mit.edu/docs/iii/tables/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured dataset for simulating interactive and iterative clinical decision-making processes among medical agents.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- AI developers in Medicine

**Tasks**:
- Clinical Decision-Making Simulation

**Limitations**: N/A

## 💾 Data

**Source**: MIMIC-III Clinical database

**Size**: 500 patient records

**Format**: JSON

**Annotation**: Semi-structured extraction using rule-based methods and LLM inference

## 🔬 Methodology

**Methods**:
- Automated metrics
- Multi-Agent Evaluation

**Metrics**:
- Hit@5
- Hit@10
- Recall@5
- Recall@10

**Calculation**: Metrics are calculated based on the ranking of the predicted diagnoses compared to the ground truth ICD-9 codes.

**Interpretation**: Good performance is indicated by higher Hit@K and Recall@K values, reflecting the model's ability to suggest correct diagnoses.

**Baseline Results**: N/A

**Validation**: Extensive experiments were conducted to evaluate the effectiveness of the DynamiCare framework on the MIMIC-Patient dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Data Laws**: Data usage restrictions
- **Privacy**: Data privacy rights alignment, Reidentification
- **Misuse**: Improper usage

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Patient records are de-identified to prevent re-identification.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
