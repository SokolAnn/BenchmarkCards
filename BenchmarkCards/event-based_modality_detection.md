# Event-Based Modality Detection

## 📊 Benchmark Details

**Name**: Event-Based Modality Detection

**Overview**: This paper defines an event-based modality detection task that aims to detect and classify fine-grained modal concepts associated with events in natural language. The task includes modal triggers from any syntactic class and uses a unified taxonomy for modal senses.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/OnlpLab/Modality)
- [GitHub Repository](https://github.com/OnlpLab/Modality-Corpus)

## 🎯 Purpose and Intended Users

**Goal**: To advance the detection and classification of modal expressions in language processing, improving understanding of modality's role in NLP tasks.

**Target Audience**:
- NLP Researchers
- Model Developers

**Tasks**:
- Modal Sense Classification
- Modality Detection and Classification
- Modal-Event Detection

**Limitations**: N/A

## 💾 Data

**Source**: The GME corpus, obtained by expert annotations of the MPQA Opinion Corpus.

**Size**: 11,048 sentences

**Format**: CoNLL

**Annotation**: Expert annotation based on a unified taxonomy for modal senses.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics were calculated using the official CoNLL evaluation script.

**Interpretation**: A higher F1 score indicates better model performance in detecting modal senses.

**Baseline Results**: Baseline model results show high precision for identifying modal triggers with various evaluations across granular levels.

**Validation**: Cross-validation with multiple folds was used for training and testing the models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
