# FactEHR

## 📊 Benchmark Details

**Name**: FactEHR

**Overview**: FactEHR is a dataset for fact decomposition and textual entailment created from 2,168 clinical notes across four document types from three hospital systems, aimed at evaluating the factuality in clinical notes using large language models.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedNLI
- MultiNLI
- SciTail
- SNLI

**Resources**:
- [GitHub Repository](https://github.com/som-shahlab/factehr)
- [Resource](https://som-shahlab.github.io/factehr-website/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the performance of large language models in fact decomposition and entailment tasks on clinical note data.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Clinical Researchers

**Tasks**:
- Fact Decomposition
- Textual Entailment

**Limitations**: N/A

## 💾 Data

**Source**: 2,168 clinical notes from various datasets including MIMIC, CORAL, and MedAlign, processed to create fact decompositions.

**Size**: 987,266 entailment pairs

**Format**: N/A

**Annotation**: Fact decompositions were generated using large language models, and a subset was reviewed by medical experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Fact Precision
- Fact Recall
- F1 Score

**Calculation**: Fact Precision measures the proportion of facts in a decomposition that are entailed by the clinical note; Fact Recall measures how well the decomposed facts capture the sentences in the clinical note.

**Interpretation**: Higher Fact Precision indicates more accurate decompositions, while higher Fact Recall shows completeness regarding the cover of the original notes.

**Baseline Results**: N/A

**Validation**: Evaluated using manual annotations from clinical experts for entailment with a total of 1,036 human-annotated pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset used de-identified clinical notes to ensure patient privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
