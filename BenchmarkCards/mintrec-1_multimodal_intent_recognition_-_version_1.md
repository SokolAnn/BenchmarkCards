# MIntRec-1 (Multimodal Intent Recognition - Version 1)

## 📊 Benchmark Details

**Name**: MIntRec-1 (Multimodal Intent Recognition - Version 1)

**Overview**: The benchmark focuses on multimodal intent detection, analyzing the performance of Large Language Models and their ability to handle modality biases. It introduces a debiasing framework designed to validate and optimize existing datasets for better performance evaluation.

**Data Type**: text, audio, video

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2508.16122)

## 🎯 Purpose and Intended Users

**Goal**: To study modality bias in multimodal intent detection and to propose a framework for debiasing multimodal intent datasets.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multimodal Intent Detection

**Limitations**: N/A

## 💾 Data

**Source**: Two publicly available benchmark multimodal intent detection datasets: MIntRec-1 and MIntRec2.0.

**Size**: 2,224 samples for MIntRec-1

**Format**: N/A

**Annotation**: Manually annotated by domain experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on predictions made by models during the evaluation of intent detection tasks.

**Interpretation**: Higher values in accuracy and F1 score indicate better performance in detecting intents accurately across modalities.

**Baseline Results**: N/A

**Validation**: Cross-validation techniques were employed to ensure reliability of the evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The datasets used do not contain personally sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
