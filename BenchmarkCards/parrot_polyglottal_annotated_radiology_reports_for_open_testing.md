# PARROT (Polyglottal Annotated Radiology Reports for Open Testing)

## 📊 Benchmark Details

**Name**: PARROT (Polyglottal Annotated Radiology Reports for Open Testing)

**Overview**: PARROT is a large, multicentric, open-access dataset of fictional radiology reports spanning multiple languages for testing natural-language processing applications in radiology.

**Data Type**: radiology reports

**Domains**:
- Healthcare

**Languages**:
- English
- French
- Italian
- Polish
- German
- Turkish
- Spanish
- Greek
- Afrikaans
- Chinese
- Portuguese
- Romanian
- Russian

**Similar Benchmarks**:
- MIMIC-IV
- MIMIC-CXR

**Resources**:
- [GitHub Repository](https://github.com/PARROT-reports/PARROT_v1.0/)

## 🎯 Purpose and Intended Users

**Goal**: Provide an open-access, multilingual collection of radiology reports to tackle linguistic and accessibility constraints hindering NLP tool development in non-English contexts.

**Target Audience**:
- ML Researchers
- Radiologists
- Healthcare Professionals

**Tasks**:
- Text Classification
- Natural Language Processing

**Limitations**: The dataset is geographically imbalanced, with Europe predominating and only ≈19% of reports originating from the Global South.

## 💾 Data

**Source**: Fictional radiology reports contributed by radiologists, including metadata.

**Size**: 2,658 reports

**Format**: JSONL

**Annotation**: Authors provided ICD-10 codes and reports were generated based on standard reporting practices.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Statistical analysis

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on participants' ability to distinguish human-authored from AI-generated reports.

**Interpretation**: Accuracy above the chance level indicates a potential for identifying differences between human and AI-generated reports.

**Validation**: Reports were subjected to a study where participants assessed if reports were human-authored or AI-generated.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes contributions from 21 countries, allowing for analysis of variations across different regions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All reports are fictional with no patient data, allowing unrestricted sharing under a CC-BY-NC-SA 4.0 license.

**Data Licensing**: CC-BY-NC-SA 4.0

**Consent Procedures**: Contributors attested that all submitted reports were fabricated, no ethical approval required.

**Compliance With Regulations**: Not Applicable
