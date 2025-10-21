# Doctronic

## 📊 Benchmark Details

**Name**: Doctronic

**Overview**: This paper evaluated a multi-agent LLM-based AI framework as an autonomous AI doctor in a virtual urgent care setting, demonstrating strong concordance with human clinicians across diagnostic and treatment decisions.

**Data Type**: SOAP note pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To assess the effectiveness of the multi-agent AI system Doctronic compared to board-certified clinicians in a real-world clinical setting.

**Target Audience**:
- Healthcare Researchers
- Medical Professionals
- AI Ethics Researchers

**Tasks**:
- Diagnostic Concordance
- Treatment Plan Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: 500 de-identified urgent care telehealth encounters conducted in March 2025.

**Size**: 500 encounters

**Format**: SOAP notes

**Annotation**: Clinical evaluations performed with blinded expert and LLM-based adjudication.

## 🔬 Methodology

**Methods**:
- Blinded expert review
- LLM-based adjudication

**Metrics**:
- Diagnostic Concordance
- Treatment Plan Consistency
- Clinical Similarity Score (CSS)

**Calculation**: Metrics calculated based on matched diagnostic outcomes and treatment plan alignment between AI and clinician notes.

**Interpretation**: Concordance indicates comparable clinical decision-making accuracy between AI and clinicians.

**Baseline Results**: Top diagnosis matched in 81% of cases, treatment plans aligned in 99.2% of cases.

**Validation**: Blinded review by board-certified physicians of discordant encounters.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No patient-identifiable information was used, de-identification ensured confidentiality.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
