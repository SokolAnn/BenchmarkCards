# SOS-1K: A Fine-grained Suicide Risk Classification Dataset for Chinese Social Media Analysis

## 📊 Benchmark Details

**Name**: SOS-1K: A Fine-grained Suicide Risk Classification Dataset for Chinese Social Media Analysis

**Overview**: This study presents a Chinese social media dataset designed for fine-grained suicide risk classification, focusing on indicators such as expressions of suicide intent and methods of suicide. It contains a total of 1249 entries and provides a foundation for automatic identification of suicidal individuals, facilitating timely psychological intervention.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/HongzhiQ/FineGrainedSuicideDetection)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for fine-grained suicide risk classification in Chinese social media to aid in identifying suicidal tendencies and facilitating interventions.

**Target Audience**:
- ML Researchers
- Mental Health Professionals
- Data Scientists

**Tasks**:
- Fine-grained Classification
- Binary Classification

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from comments on the 'Zoufan' blog on the Weibo social platform, annotated by LLM and reviewed by domain experts.

**Size**: 1,249 entries

**Format**: N/A

**Annotation**: Initial annotation using LLM followed by a secondary review and annotation by domain experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Weighted average precision, recall, and F1-score were used as evaluation metrics for the fine-grained classification task.

**Interpretation**: High F1-scores indicate effective classification of suicide risk.

**Validation**: 5-fold cross-validation was employed to ensure the robustness of the models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was anonymized to remove all information such as user IDs to ensure privacy protection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
