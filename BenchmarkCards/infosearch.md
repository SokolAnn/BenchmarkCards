# InfoSearch

## 📊 Benchmark Details

**Name**: InfoSearch

**Overview**: InfoSearch is a novel retrieval evaluation benchmark spanning six document-level attributes: Audience, Keyword, Format, Language, Length, and Source. It introduces novel metrics – Strict Instruction Compliance Ratio (SICR) and Weighted Instruction Sensitivity Evaluation (WISE) – to accurately assess the models’ responsiveness to instructions.

**Data Type**: query-document pairs

**Domains**:
- Information Retrieval

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/EIT-NLP/InfoSearcharXiv:2410.23841v2)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the instruction-following capabilities of various retrieval models beyond content relevance.

**Target Audience**:
- ML Researchers
- Information Retrieval Practitioners

**Tasks**:
- Information Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Query-document pairs constructed via web-retrieved content and existing datasets.

**Size**: 6,392 documents

**Format**: N/A

**Annotation**: Manual validation of instructions.

## 🔬 Methodology

**Methods**:
- Evaluation on various retrieval models using instructed, reverse-instructed, and original modes.

**Metrics**:
- Strict Instruction Compliance Ratio (SICR)
- Weighted Instruction Sensitivity Evaluation (WISE)

**Calculation**: Metrics are calculated based on the model's responsiveness to both positive and negative instructions as detailed in the methodology section.

**Interpretation**: Higher SICR and WISE scores indicate better adherence to instructions; a comprehensive evaluation of instruction-following capabilities.

**Validation**: Models were evaluated across multiple dimensions and modes to capture their instruction-following capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
