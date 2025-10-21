# CODE-ACCORD

## 📊 Benchmark Details

**Name**: CODE-ACCORD

**Overview**: CODE-ACCORD is a dataset of 862 self-contained sentences from the building regulations of England and Finland, annotated to facilitate machine-readable rule generation for Automatic Compliance Checking (ACC).

**Data Type**: text

**Domains**:
- Architecture
- Engineering
- Construction

**Languages**:
- English
- Finnish

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.10210022)
- [GitHub Repository](https://github.com/Accord-Project/CODE-ACCORD/)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate Automatic Compliance Checking (ACC) through machine-readable rule generation from building regulations.

**Target Audience**:
- ML Researchers
- Domain Experts
- Industry Practitioners

**Tasks**:
- Text Classification
- Entity Recognition
- Relation Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Building regulations of England and Finland collected from official government sources.

**Size**: 862 sentences

**Format**: CSV, JSON

**Annotation**: Manual annotation by a team of 12 annotators with expertise in computer science and civil engineering.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Inter-annotator agreement (IAA) was used to measure annotation quality based on matches of annotated entities.

**Interpretation**: High IAA values indicate congruence in entity recognition between annotators.

**Validation**: Annotations were validated through multiple rounds and curated by domain experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
