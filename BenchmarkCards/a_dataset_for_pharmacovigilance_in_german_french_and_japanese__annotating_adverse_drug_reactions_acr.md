# A Dataset for Pharmacovigilance in German, French, and Japanese: Annotating Adverse Drug Reactions across Languages

## 📊 Benchmark Details

**Name**: A Dataset for Pharmacovigilance in German, French, and Japanese: Annotating Adverse Drug Reactions across Languages

**Overview**: This paper presents a multilingual corpus of texts concerning Adverse Drug Reactions (ADRs) in German, French, and Japanese. The corpus includes annotations covering 12 entity types, four attribute types, and 13 relation types to aid in the extraction and analysis of ADRs from user-generated content.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- German
- French
- Japanese

**Resources**:
- [GitHub Repository](https://github.com/Dotkat-dotcome/KEEPHA-ADR)
- [GitHub Repository](https://github.com/DFKI-NLP/keepha_annotation_guidelines/blob/main/KEEPHA_annotation_guidelines.pdf)

## 🎯 Purpose and Intended Users

**Goal**: To support pharmacovigilance across languages by extracting information on ADRs from user-generated content.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Named Entity Recognition
- Attribute Classification
- Relation Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Multilingual corpus collected from social media, patient forums, and clinical reports.

**Size**: 837 documents

**Format**: N/A

**Annotation**: Annotated by native speakers with expertise in healthcare.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Evaluated using brat format for span boundaries and converted evaluations to appropriate formats.

**Interpretation**: Micro and macro average F1 scores are reported for task evaluations.

**Baseline Results**: Micro F1 scores for Named Entity Recognition range from 48.8% to 82.5% across different language models.

**Validation**: Initial annotations were done in English and guided by established annotation standards.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is de-identified, but potential identification risks remain due to the public nature of social media.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data collected from publicly accessible forums.

**Compliance With Regulations**: Not Applicable
