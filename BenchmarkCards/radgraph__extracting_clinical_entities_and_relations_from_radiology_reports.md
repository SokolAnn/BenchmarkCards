# RadGraph: Extracting Clinical Entities and Relations from Radiology Reports

## 📊 Benchmark Details

**Name**: RadGraph: Extracting Clinical Entities and Relations from Radiology Reports

**Overview**: RadGraph is a dataset of clinical entity and relation annotations in full-text chest X-ray radiology reports, designed to facilitate various healthcare applications through a novel information extraction schema.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MIMIC-CXR
- CheXpert

**Resources**:
- [Resource](https://doi.org/10.13026/hm87-5p47)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured dataset of clinical entities and relations from radiology reports to enhance research in medical NLP and multi-modal learning.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Entity Extraction
- Relation Extraction

**Limitations**: N/A

## 💾 Data

**Source**: 500 radiology reports from the MIMIC-CXR dataset and 100 reports from the CheXpert dataset, annotated by board-certified radiologists.

**Size**: 500 reports for development dataset and up to 220,763 reports for inference dataset.

**Format**: N/A

**Annotation**: Annotations were done manually by board-certified radiologists.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Micro F1
- Macro F1

**Calculation**: Metrics are calculated based on the performance of a model compared to independent radiologist annotations for entity and relation extraction.

**Interpretation**: A predicted entity is correct if both the span boundaries and entity types are correct; for relations, both entity pairs and relation types must be accurate.

**Baseline Results**: RadGraph Benchmark achieved a micro F1 of 0.82 on MIMIC-CXR and 0.73 on CheXpert for relation extraction.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Data poisoning

**Demographic Analysis**: The dataset includes demographic statistics related to sex, age, and race, enhancing the assessment of fairness in the context of clinical applications.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Each report is de-identified in compliance with HIPAA regulations.

**Data Licensing**: PhysioNet Credentialed Health Data License 1.5.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: HIPAA compliance for de-identification.
