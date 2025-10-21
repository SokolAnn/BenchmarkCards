# WoS Expanded Datasets for Scientific Text Classification

## 📊 Benchmark Details

**Name**: WoS Expanded Datasets for Scientific Text Classification

**Overview**: The paper introduces three new expanded datasets (WoS-53949, WoS-18932, WoS-8716) for scientific text classification, generated through targeted queries on the Web of Science database to enhance model performance through dataset augmentation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/ZhyarUoS/Advancing-Scientific-Text-Classification)

## 🎯 Purpose and Intended Users

**Goal**: To improve the performance of scientific text classification through dataset expansion and fine-tuning of pre-trained language models.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification

**Limitations**: Some domains with sparse data posed challenges in achieving balanced performance.

## 💾 Data

**Source**: Web of Science database.

**Size**: 53,949 documents

**Format**: N/A

**Annotation**: Predicted labels using a hard-voting strategy combined with fine-tuned PLMs.

## 🔬 Methodology

**Methods**:
- Fine-tuning of pre-trained language models
- Hard-voting for label assignment

**Metrics**:
- Micro F1 Score
- Accuracy

**Calculation**: Micro F1 Score computed based on model predictions against true labels.

**Interpretation**: Higher Micro F1 Scores indicate better classification accuracy and model performance.

**Baseline Results**: BERT achieved a Micro F1 Score of 0.8788 on WoS-53949 dataset.

**Validation**: Dynamic learning rate adjustment and early stopping were employed to optimize training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
