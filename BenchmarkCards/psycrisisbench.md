# PsyCrisisBench

## 📊 Benchmark Details

**Name**: PsyCrisisBench

**Overview**: PsyCrisisBench is a comprehensive benchmark of 540 annotated transcripts from the Hangzhou Psychological Assistance Hotline, assessing four critical tasks: mood status recognition, suicidal ideation detection, suicide plan identification, and risk assessment.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models in crisis triage, particularly for psychological support hotlines.

**Target Audience**:
- ML Researchers
- Mental Health Professionals

**Tasks**:
- Mood Status Recognition
- Suicidal Ideation Detection
- Suicide Plan Identification
- Risk Assessment

**Limitations**: Mood status recognition remains limited due to contextual and paralinguistic complexity.

## 💾 Data

**Source**: Hangzhou Psychological Assistance Hotline

**Size**: 540 transcripts

**Format**: Text

**Annotation**: Transcripts were manually annotated for mood status, suicidal ideation, suicide plan, and risk level.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Few-shot evaluation
- Fine-tuning

**Metrics**:
- F1 Score

**Calculation**: F1 Score is calculated to balance precision and recall, particularly crucial for sensitive scenarios like crisis assessment.

**Interpretation**: Higher F1 Scores indicate better model performance on the tasks of detecting suicidal ideation and assessing risk.

**Validation**: Evaluation was repeated three times to ensure stability and reliability of results.

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

**Privacy And Anonymity**: Callers are informed that conversations will be recorded and anonymously documented for research purposes.

**Data Licensing**: Not Applicable

**Consent Procedures**: Ethical approval was received, and callers were informed about data usage.

**Compliance With Regulations**: Not Applicable
