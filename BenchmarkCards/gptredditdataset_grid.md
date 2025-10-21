# GPTRedditDataset (GRiD)

## 📊 Benchmark Details

**Name**: GPTRedditDataset (GRiD)

**Overview**: GPTRedditDataset (GRiD) is a novel GPT-generated text detection dataset designed to assess the performance of detection models in identifying generated responses from ChatGPT. The dataset consists of a diverse collection of context-prompt pairs based on Reddit, with human-generated and ChatGPT-generated responses.

**Data Type**: context-prompt pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/madlab-ucr/GriD)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and advance detection techniques for distinguishing between human and GPT-generated text.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Reddit and the OpenAI API

**Size**: 6,513 samples

**Format**: CSV

**Annotation**: Labeled as GPT-generated or human-generated

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- ROC-AUC

**Calculation**: Metrics are calculated using 10-fold cross-validation.

**Interpretation**: Higher F1 Score and ROC-AUC values indicate better performance in distinguishing between human and GPT-generated text.

**Baseline Results**: BERT: F1 0.934, AUC 0.984; SVM: F1 0.813, AUC 0.845; Random Forest: F1 0.787, AUC 0.825; GpTen (proposed): F1 0.667, AUC 0.708.

**Validation**: Employs 10-fold cross-validation for evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
