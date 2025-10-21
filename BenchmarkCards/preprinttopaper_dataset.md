# PreprintToPaper dataset

## 📊 Benchmark Details

**Name**: PreprintToPaper dataset

**Overview**: The PreprintToPaper dataset connects bioRxiv preprints with their corresponding journal publications, enabling large-scale analysis of the preprint-to-publication process, with metadata for 145,517 preprints across two periods.

**Data Type**: metadata records

**Domains**:
- Natural Language Processing
- Bibliometrics

**Languages**:
- English

**Similar Benchmarks**:
- covid19_preprints
- Rxivist

**Resources**:
- [Resource](https://doi.org/10.5281/ZENODO.17185408)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive resource for studying how preprints evolve into published journal articles or remain unpublished.

**Target Audience**:
- ML Researchers
- Policy Makers
- Scholarly Communication Researchers
- Data Scientists

**Tasks**:
- Data Linking
- Text Analysis
- Bibliometric Analysis

**Limitations**: N/A

## 💾 Data

**Source**: bioRxiv and Crossref APIs

**Size**: 145,517 records

**Format**: CSV

**Annotation**: Human-annotated subset for Gray Zone cases

## 🔬 Methodology

**Methods**:
- Automated linking procedures
- Human annotation
- Statistical verification

**Metrics**:
- Accuracy of match scores
- Inter-annotator agreement

**Calculation**: Metrics calculated based on title similarity using SequenceMatcher algorithm.

**Interpretation**: Higher similarity scores indicate a stronger likelihood of a corresponding publication.

**Baseline Results**: High inter-annotator agreement (κ=0.86) for evaluation of Gray Zone matches.

**Validation**: Validated using a human-annotated subset of 299 records.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Data Integrity

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Misclassification of publication status']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
