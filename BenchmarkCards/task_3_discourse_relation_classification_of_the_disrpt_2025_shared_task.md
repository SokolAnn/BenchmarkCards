# Task 3 (Discourse Relation Classification) of the DISRPT 2025 shared task

## 📊 Benchmark Details

**Name**: Task 3 (Discourse Relation Classification) of the DISRPT 2025 shared task

**Overview**: This work contributes to the shared effort of building a multilingual and cross-framework discourse parser by introducing a unified set of 17 discourse relation labels across 39 corpora in 16 languages and six discourse frameworks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Russian
- Portuguese
- Thai
- Spanish
- German
- Dutch
- Turkish
- Czech
- French
- Persian
- Ewe

**Resources**:
- [GitHub Repository](https://github.com/disrpt/sharedtask2025)
- [Resource](https://huggingface.co)

## 🎯 Purpose and Intended Users

**Goal**: To establish strong baselines for the discourse relation classification task and evaluate how models respond to the newly proposed unified labels.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Discourse Relation Classification

**Limitations**: The class distribution in the dataset is not balanced, with certain labels being overrepresented or underrepresented.

## 💾 Data

**Source**: Datasets provided by the shared task organizers, composed of 39 datasets covering 16 languages and 6 frameworks.

**Size**: 170,000 training instances, 28,000 development instances

**Format**: N/A

**Annotation**: Annotated across multiple discourse relation frameworks for classification.

## 🔬 Methodology

**Methods**:
- Fine-tuning multilingual BERT-based models
- Prompt-based evaluation with large language models
- Hierarchical Dual-Adapter Contrastive learning

**Metrics**:
- Accuracy

**Calculation**: The accuracy is calculated by measuring the correct predictions across the discourse relations in the classification task.

**Interpretation**: Higher accuracy indicates better performance in classifying discourse relations.

**Baseline Results**: HiDAC achieved the highest overall accuracy at 67.5%.

**Validation**: Models were validated using official train/dev/test splits provided for the task.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
