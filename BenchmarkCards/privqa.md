# PRIVQA

## 📊 Benchmark Details

**Name**: PRIVQA

**Overview**: PRIVQA is a multimodal benchmark to assess the privacy/utility trade-off when a model is instructed to protect specific categories of personal information in a simulated scenario.

**Data Type**: text and image question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://llm-access-control.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To test the ability of language models and vision-language models to follow instructions to protect personal information.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: A curated collection of existing QA datasets such as TriviaQA and visual QA datasets like KVQA.

**Size**: 4,678 textual examples and 2,000 visual examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Red teaming

**Metrics**:
- Response F1
- Protection Score

**Calculation**: Response F1 is calculated using the standard token-level QA evaluation metric; Protection Score is calculated based on sensitivity and specificity.

**Interpretation**: High Response F1 indicates good accuracy, while a high Protection Score reflects effective privacy protection.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis found significant bias based on popularity and race.

**Potential Harm**: The benchmark aims to detect or prevent privacy leaks of personal information.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
