# FaST (Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data)

## 📊 Benchmark Details

**Name**: FaST (Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data)

**Overview**: This paper introduces two new datasets—DnD and ELIP—for studying the problem of Personalized Preference Alignment with Limited Data (PPALLI) and benchmarks various alignment techniques.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Personalized Soups
- PERSONA
- PRISM
- Perspective
- PersonalLLM

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in personalized preference alignment using limited data.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Personalized Preference Alignment

**Limitations**: N/A

## 💾 Data

**Source**: Two newly created datasets: DnD focusing on character preferences and ELIP focusing on conversational assistant preferences.

**Size**: 1,290 preference tuples for DnD; 800 preference tuples for ELIP

**Format**: N/A

**Annotation**: Responses were annotated by users based on a preference questionnaire.

## 🔬 Methodology

**Methods**:
- Sampling and Tuning
- Supervised Fine-Tuning (SFT)
- Direct Preference Optimization (DPO)

**Metrics**:
- Accuracy
- Personalization Score

**Calculation**: Metrics such as accuracy of preferred response prediction and qualitative evaluation based on LLM-judges.

**Interpretation**: Higher scores denote better alignment with user preferences.

**Validation**: Datasets were validated using multiple random train/validation/test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Privacy**: Data privacy rights alignment
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The datasets and models respect user data by allowing personal preference data to remain on users' devices.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
