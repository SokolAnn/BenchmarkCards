# FakeSum (Misinformation Detection Dataset)

## 📊 Benchmark Details

**Name**: FakeSum (Misinformation Detection Dataset)

**Overview**: We propose an approach for generating a dataset using adversarial prompting to create a robust fake news dataset that helps in understanding the anatomy of LLM-generated misinformation. This dataset captures various misinformation patterns and exhibits how LLMs can be leveraged for generating misinformation, which lays the groundwork for effectively fighting against it.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the dataset is to assist in the training of models for misinformation detection by providing a controlled generation of factually incorrect summaries.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Misinformation Detection
- Fact Verification

**Limitations**: N/A

## 💾 Data

**Source**: 5000 news articles collected from CNN-News185

**Size**: 5000 correct and about 1000 incorrect summaries

**Format**: N/A

**Annotation**: Generated using GPT-3.5 and GPT-4 models

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Macro F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the classification tasks performed on the dataset.

**Interpretation**: A model that achieves higher F1 scores is deemed to perform better in distinguishing between correct summaries and those with misinformation.

**Baseline Results**: The dataset has been evaluated using SVC, BiLSTM, BERT, and RoBERTa models with varying F1 scores across settings.

**Validation**: Split into training, validation, and test sets with a ratio of 70:10:20.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: The dataset aims to address misinformation, which can have harmful societal impacts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
