# A Dataset for Automated Model Card Generation

## 📊 Benchmark Details

**Name**: A Dataset for Automated Model Card Generation

**Overview**: This paper introduces a dataset of 500 question-answer pairs for 25 machine learning models, designed to automate the generation of model cards that document details about machine learning models such as training configurations, datasets, biases, architecture details, and training resources.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://osf.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured dataset of question-answer pairs that can be used to train models for generating model cards automatically.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Model Card Generation

**Limitations**: N/A

## 💾 Data

**Source**: Peer-reviewed research papers documenting the 25 machine learning models.

**Size**: 500 question-answer pairs

**Format**: N/A

**Annotation**: Answers were extracted from original research papers by annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Expert annotation

**Metrics**:
- BLEU
- ROUGE-L
- BERT-Score

**Calculation**: Metrics are calculated based on the generated answers from LLMs against the ground truth.

**Interpretation**: Higher scores in BLEU and ROUGE-L indicate better performance in generating accurate model card information.

**Baseline Results**: ChatGPT-3.5 performs the best in generating answers compared to LLaMa and Galactica models.

**Validation**: The dataset was validated through a two-stage annotation process involving preliminary and expert reviews.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
