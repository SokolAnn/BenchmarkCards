# Dynamic Adversarial Question Generation Dataset

## 📊 Benchmark Details

**Name**: Dynamic Adversarial Question Generation Dataset

**Overview**: The paper introduces a new dataset of adversarially authored questions aimed at improving the performance of question answering models by utilizing dynamic adversarial question generation techniques.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2401.11185)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset that facilitates the generation of challenging questions for question answering models, leveraging dynamic adversarial techniques.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Adversarially authored questions created using an interactive interface with guidance from LLMs and retrieval models.

**Size**: 399 adversarial questions collected

**Format**: N/A

**Annotation**: Manual annotation by authors to improve question quality and adversarial nature.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation via competition

**Metrics**:
- Discriminability
- Difficulty margin

**Calculation**: Metrics based on Item Response Theory (IRT) used to derive parameters that assess question quality.

**Interpretation**: Questions with higher discriminability and suitable difficulty levels are considered better adversarial examples.

**Validation**: Validation through competitions between human authors and AI models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The study was pre-monitored by an official IRB review board to protect the participants’ privacy rights.

**Data Licensing**: Not Applicable

**Consent Procedures**: Consent forms displayed before task completion to ensure participants agree to data usage for academic purposes.

**Compliance With Regulations**: Not Applicable
