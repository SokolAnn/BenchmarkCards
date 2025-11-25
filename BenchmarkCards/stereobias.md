# StereoBias

## 📊 Benchmark Details

**Name**: StereoBias

**Overview**: The StereoBias dataset is labeled for bias and stereotype detection across five categories: religion, gender, socio-economic status, race, profession, and others, enabling a deeper study of their relationship.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- CrowS-Pairs
- ToxicBias

**Resources**:
- [GitHub Repository](https://github.com/aditya20t/StereotypeAsCatalystForBias)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to improve bias detection in AI models by leveraging stereotype detection as a complementary task.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Bias Detection
- Stereotype Detection

**Limitations**: While the study presents promising results, it is limited to models with parameter sizes up to 8B, and the cultural background of annotators may have influenced the annotation process.

## 💾 Data

**Source**: Curated using sentences from StereoSet and CrowS-Pairs datasets.

**Size**: 5,012 sentences

**Format**: N/A

**Annotation**: Annotated by three independent annotators based on detailed guidelines.

## 🔬 Methodology

**Methods**:
- Fine-tuning of pre-trained language models
- Multi-Task Learning (MTL)

**Metrics**:
- Macro-F1

**Calculation**: F1 scores are calculated to evaluate the performance of bias and stereotype classification.

**Interpretation**: Higher Macro-F1 scores indicate better performance in detecting bias and stereotypes.

**Baseline Results**: Encoder-only models achieved competitive scores with RoBERTa-large reaching a maximum of 0.7742 F1 for bias detection.

**Validation**: Validation of results using cross-validation and statistical hypothesis testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes demographic breakdowns across various groups.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets were pre-processed to anonymize and protect personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The study ensures ethical usage of datasets.
