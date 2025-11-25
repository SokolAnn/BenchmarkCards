# EHRCon

## 📊 Benchmark Details

**Name**: EHRCon

**Overview**: EHRCon is a new dataset and task designed to ensure data consistency between structured tables and unstructured notes in Electronic Health Records, featuring manual annotations of 4,101 entities across 105 clinical notes.

**Data Type**: entities with labels

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TabFact
- INFOTABS

**Resources**:
- [GitHub Repository](https://github.com/dustn1259/EHRCon)
- [Resource](https://physionet.org/content/mimiciii/1.4/)

## 🎯 Purpose and Intended Users

**Goal**: To improve the accuracy and reliability of Electronic Health Records by verifying the consistency between clinical notes and structured databases.

**Target Audience**:
- Healthcare Professionals
- Medical Researchers
- AI Researchers

**Tasks**:
- Data Consistency Checking
- Named Entity Recognition
- Fact Verification

**Limitations**: The inconsistencies identified may not be present in real hospital data due to preprocessing.

## 💾 Data

**Source**: MIMIC-III EHR dataset

**Size**: 4,101 entities from 105 clinical notes

**Format**: JSON

**Annotation**: Manual annotation by trained healthcare professionals

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall
- Precision
- Intersection

**Calculation**: Metrics are calculated based on the comparison between predicted and gold-standard entity annotations.

**Interpretation**: High recall indicates successful identification of actually consistent/inconsistent entities, while precision indicates the correctness of the identified entities.

**Baseline Results**: Recall performance achieved was 61.06% in few-shot scenarios with the framework CheckEHR.

**Validation**: Validation was performed collaboratively with practitioners to define labeling instructions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets are de-identified to protect patient privacy.

**Data Licensing**: Released under MIT License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
