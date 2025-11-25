# CLIP (Clinical Action Items from Hospital Discharge Notes)

## 📊 Benchmark Details

**Name**: CLIP (Clinical Action Items from Hospital Discharge Notes)

**Overview**: CLIP is a dataset of clinical action items annotated from hospital discharge notes to assist primary care physicians in identifying actionable information.

**Data Type**: text

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/asappresearch/clip)
- [Resource](https://physionet.org/static/published-projects/mullenbach21/CLIP dataset version 1.0.0)

## 🎯 Purpose and Intended Users

**Goal**: To assist primary care physicians in extracting and identifying action items from clinical discharge notes.

**Target Audience**:
- Healthcare Providers
- Clinical Researchers
- Natural Language Processing Researchers

**Tasks**:
- Information Extraction
- Text Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Annotated clinical notes from the MIMIC-III database.

**Size**: 718 documents, 107,494 sentences

**Format**: N/A

**Annotation**: Annotated by physicians

## 🔬 Methodology

**Methods**:
- Multi-label classification
- Sentence-level classification
- BERT-based models

**Metrics**:
- F1 Score
- AUC

**Calculation**: Metrics are computed using micro and macro averages.

**Interpretation**: Higher F1 and AUC scores indicate better model performance in extracting action items.

**Baseline Results**: Highest binary F1 score from models approaches 0.86, compared to human agreement of 0.93.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset uses de-identified clinical notes from the MIMIC-III database.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Access to dataset requires completion of an ethics course and a Data Use Agreement.
