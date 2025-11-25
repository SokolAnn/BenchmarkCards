# OffMix-3L

## 📊 Benchmark Details

**Name**: OffMix-3L

**Overview**: OffMix-3L is a novel three-language code-mixed test dataset in Bangla-Hindi-English for offensive language identification. It contains 1,001 instances annotated by speakers of the three languages and serves as a benchmark for evaluating offensive language identification models in a code-mixed context.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bangla
- Hindi
- English

**Resources**:
- [GitHub Repository](https://github.com/LanguageTechnologyLab/OffMix-3L)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset for the evaluation of offensive language identification models using mixed code from Bangla, Hindi, and English.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Model Developers

**Tasks**:
- Offensive Language Identification

**Limitations**: The dataset is comparatively smaller in size, since it is costly to generate data by a specific set of people who are fluent in all 3 target languages.

## 💾 Data

**Source**: Manually collected and annotated from three undergraduate students fluent in Bangla, Hindi, and English.

**Size**: 1,001 instances

**Format**: N/A

**Annotation**: Annotated by students and NLP researchers fluent in the three languages.

## 🔬 Methodology

**Methods**:
- Model Evaluation
- Human Annotation

**Metrics**:
- F1 Score

**Calculation**: F1 scores are calculated based on model predictions against the annotated labels in the dataset.

**Interpretation**: Higher F1 scores indicate better performance of the models in identifying offensive language.

**Baseline Results**: BanglishBERT achieved the highest F1 score of 0.68.

**Validation**: Validated through multiple rounds of annotation and consensus.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not contain personally identifiable information as it was developed using volunteer contributions.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The dataset adheres to ethical standards in research.
