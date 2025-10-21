# Leveraging LLM Embeddings for Cross Dataset Label Alignment and Zero Shot Music Emotion Prediction

## 📊 Benchmark Details

**Name**: Leveraging LLM Embeddings for Cross Dataset Label Alignment and Zero Shot Music Emotion Prediction

**Overview**: This work presents a novel method for music emotion recognition that leverages Large Language Model (LLM) embeddings for label alignment across multiple datasets and zero-shot prediction on novel categories. The method enables robust cross-dataset label alignment and facilitates zero-shot inference on new datasets with previously unseen emotion labels.

**Data Type**: music emotion labels

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/AMAAI-Lab/cross-dataset-emotion-alignment)

## 🎯 Purpose and Intended Users

**Goal**: To develop more comprehensive and robust music emotion recognition models that can generalize to a wider range of emotional experiences beyond the singular datasets used during training.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Zero-Shot Learning
- Music Emotion Recognition

**Limitations**: N/A

## 💾 Data

**Source**: The datasets used include the MTG-Jamendo Dataset, Computer Audition Lab 500 dataset, and the Emotify Dataset.

**Size**: Over 55,000 music recordings, 500 songs, and 400 music excerpts

**Format**: N/A

**Annotation**: Annotations from multiple users, average scores used for determination of true labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro F1 Score

**Calculation**: Calculated based on cosine similarity and average scores across different datasets.

**Interpretation**: Higher F1 scores indicate improved generalization and performance on unseen datasets.

**Baseline Results**: F1 scores include 0.402 for zero-shot on Emotify, 0.248 for MTG-Jamendo, and 0.262 for CAL500.

**Validation**: Validated through extensive experiments and comparison against baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data sourced from openly available datasets under Creative Commons licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
