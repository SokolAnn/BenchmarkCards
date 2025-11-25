# PEM-Rel-8K

## 📊 Benchmark Details

**Name**: PEM-Rel-8K

**Overview**: PEM-Rel-8K is a multi-disciplinary benchmark including over 8,000 relationships drawn from three widely used ontologies: IEEE, PhySH, and MeSH, evaluated for identifying semantic relationships among research topics.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Engineering
- Physics
- Biomedicine

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ImTanay/LLM-Multi-Domain-Ontology)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate model performance in identifying semantic relations between research topics across multiple academic domains.

**Target Audience**:
- ML Researchers
- Ontology Developers
- Academic Researchers

**Tasks**:
- Semantic Relationship Identification

**Limitations**: N/A

## 💾 Data

**Source**: PEM-Rel-8K dataset constructed from IEEE, PhySH, and MeSH taxonomies.

**Size**: 8,075 relationships

**Format**: CSV

**Annotation**: Manually annotated by domain experts.

## 🔬 Methodology

**Methods**:
- Zero-Shot Learning
- Fine-Tuning

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the model's classification performance on test datasets.

**Interpretation**: High F1 scores indicate effective identification of semantic relationships, while lower scores suggest misclassifications.

**Validation**: Models were validated across training and test sets, examining performance consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
