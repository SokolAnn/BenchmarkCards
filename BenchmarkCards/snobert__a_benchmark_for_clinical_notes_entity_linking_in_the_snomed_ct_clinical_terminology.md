# SNOBERT: A Benchmark for Clinical Notes Entity Linking in the SNOMED CT Clinical Terminology

## 📊 Benchmark Details

**Name**: SNOBERT: A Benchmark for Clinical Notes Entity Linking in the SNOMED CT Clinical Terminology

**Overview**: This work presents a 'SNOBERT' method for linking text spans in clinical notes with specific topics in the SNOMED CT clinical terminology using a two-stage approach. The method was applied to the 'SNOMED CT Entity Linking Challenge'.

**Data Type**: annotated clinical notes

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/MikhailKulyabin/SNOBERT)

## 🎯 Purpose and Intended Users

**Goal**: To automate the process of linking clinical notes to specific concepts in SNOMED CT terminology.

**Target Audience**:
- Healthcare Researchers
- NLP Practitioners

**Tasks**:
- Entity Linking
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: MIMIC-IV-Note dataset containing hospital discharge summaries.

**Size**: 331,794 de-identified notes

**Format**: N/A

**Annotation**: Annotated data comprising up to 300 annotated discharge summaries.

## 🔬 Methodology

**Methods**:
- Candidate Selection
- Candidate Matching
- NER classification

**Metrics**:
- Macro-F1 score
- mIoU (mean Intersection over Union)
- cosine similarity

**Calculation**: Metrics are calculated as follows: Macro-F1 is computed across all labels; mIoU measures the overlap between predicted and ground truth spans.

**Interpretation**: Higher scores indicate better performance in linking clinical notes to SNOMED CT concepts.

**Validation**: 4-Fold Cross-Validation was used for model training and evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
