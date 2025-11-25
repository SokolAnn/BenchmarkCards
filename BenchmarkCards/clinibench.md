# CliniBench

## 📊 Benchmark Details

**Name**: CliniBench

**Overview**: CliniBench is the first benchmark that enables comparability of well-studied encoder-based classifiers and generative LLMs for discharge diagnosis prediction from admission notes in the MIMIC-IV dataset.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate and compare generative LLMs and encoder-based classifiers for diagnosis prediction.

**Target Audience**:
- ML Researchers
- Medical Practitioners
- Model Developers

**Tasks**:
- Diagnosis Prediction

**Limitations**: N/A

## 💾 Data

**Source**: MIMIC-IV dataset, specifically focused on admission notes and discharge codes.

**Size**: 87,687 notes

**Format**: JSON

**Annotation**: Annotated by clinical experts within the healthcare domain.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Mean Average Precision (MAP)
- Recall
- Precision

**Calculation**: Metrics calculated based on the model predictions compared to the ground truth codes in the dataset.

**Interpretation**: Higher scores indicate better performance in predicting accurate discharge diagnoses.

**Baseline Results**: Encoder-based classifiers outperformed generative LLMs in diagnosis prediction tasks.

**Validation**: Validated through extensive comparison experiments across various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential patient care risks from inaccurate predictions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data used is de-identified from the MIMIC-IV dataset to protect patient privacy.

**Data Licensing**: Subject to PhysioNet license restrictions; clinical notes are not shared to comply with data protection laws.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Conforms to HIPAA regulations.
