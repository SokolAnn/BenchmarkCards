# NTX (Numerical and Temporal eXpressions)

## 📊 Benchmark Details

**Name**: NTX (Numerical and Temporal eXpressions)

**Overview**: A multi-lingual evaluation dataset - NTX - covering diverse temporal and numerical expressions across 14 languages and covering extraction, normalization, and resolution.

**Data Type**: text (sentences with temporal and numerical entity annotations, normalization, and resolution)

**Domains**:
- Natural Language Processing
- Information Retrieval

**Languages**:
- English
- Chinese
- Dutch
- French
- German
- Italian
- Japanese
- Korean
- Portuguese
- Spanish
- Swedish
- Turkish
- Hindi
- Arabic

**Similar Benchmarks**:
- TempEval
- TimeBank
- OntoNotes 5.0
- Wikiwars
- TIDES TIMEX2
- TimeML TIMEX3
- TempEval-3

**Resources**:
- [Resource](https://aka.ms/NTX)
- [GitHub Repository](https://github.com/microsoft/Recognizers-Text)

## 🎯 Purpose and Intended Users

**Goal**: To provide a multi-lingual benchmark dataset that covers numerical and temporal entities and expressions at the extraction, normalization, and resolution levels, with fine-grained sub-types and representations designed for downstream usability.

**Target Audience**:
- Model Developers
- ML Researchers
- Industry Practitioners

**Tasks**:
- Entity Extraction
- Entity Normalization
- Temporal and Numerical Resolution

**Limitations**: Ambiguities in type were resolved by consensus of expert annotators; future versions plan to include alternative type interpretations. The baseline rule-based system has known limitations including handling of false positives and certain languages/features are not supported by the baseline (temporal expressions in Swedish, Korean, and Arabic; numerical expressions with units in Arabic). The current dataset schema may be somewhat unintuitive to manual inspection.

## 💾 Data

**Source**: Manually created and annotated sentences: initially generated and annotated in English and Chinese by hired specialist vendors with linguistic expertise, validated by two expert annotators; language expansion via native-speaker translations and additional examples collected from long-term commercial usage and Recognizers-Text failure feedback.

**Size**: Over 26,000 sentences across 14 languages

**Format**: JSON files

**Annotation**: Manual annotation by hired specialist vendors (level 1) with validation by two expert annotators (level 2); translations performed by native-speaker vendors; annotations reviewed and corrected informed by baseline system failures; metadata marks cases unsupported by the baseline.

## 🔬 Methodology

**Methods**:
- Baseline rule-based system evaluation (Recognizers-Text)
- Automated metrics (Precision/Recall/F1) via provided evaluation scripts

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Precision/Recall/F1 are calculated using the provided evaluation scripts included with the open-sourced code.

**Interpretation**: N/A

**Validation**: Annotations validated by two expert annotators; the baseline rule-based system was run in parallel to surface failure cases which led to annotation corrections or extensions to the system; disputed/unsupported cases were documented in metadata.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
