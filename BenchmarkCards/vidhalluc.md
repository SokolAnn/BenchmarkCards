# VIDHALLUC

## 📊 Benchmark Details

**Name**: VIDHALLUC

**Overview**: VIDHALLUC is the largest benchmark designed to examine hallucinations in Multimodal Large Language Models (MLLMs) for video understanding, assessing hallucinations across three dimensions: action, temporal sequence, and scene transition using 5,002 videos and 9,295 QA pairs.

**Data Type**: video-question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- HallusionBench
- VideoHallucer
- Vript-HAL

**Resources**:
- [Resource](https://people-robots.github.io/vidhalluc)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate hallucinations in Multimodal Large Language Models during video understanding tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Action Recognition
- Temporal Reasoning
- Scene Transition Detection

**Limitations**: N/A

## 💾 Data

**Source**: Automated data collection pipeline utilizing existing video description datasets, including ActivityNet, YouCook2, and VALOR32K.

**Size**: 5,002 videos and 9,295 QA pairs

**Format**: N/A

**Annotation**: Automatically generated questions verified by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Matthews correlation coefficient (MCC)

**Calculation**: Accuracy is calculated as the number of correctly answered questions divided by the total number of questions.

**Interpretation**: Higher accuracy indicates better performance in identifying actions, sequences, and scene transitions.

**Baseline Results**: N/A

**Validation**: Extensive testing shows that most MLLMs are vulnerable to hallucinations across key dimensions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
