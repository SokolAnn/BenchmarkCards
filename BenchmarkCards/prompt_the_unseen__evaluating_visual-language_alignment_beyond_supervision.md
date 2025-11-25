# Prompt the Unseen: Evaluating Visual-Language Alignment Beyond Supervision

## 📊 Benchmark Details

**Name**: Prompt the Unseen: Evaluating Visual-Language Alignment Beyond Supervision

**Overview**: This study introduces a new evaluation framework for assessing the generalization ability of projection layers in Vision-Language Models (VLMs) to unseen labels, leveraging object detection datasets to provide controlled, prompt-based evaluations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/raemoi93/PromptTheUnseen)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the generalization capability of projection layers in Vision-Language Models to unseen labels.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Visual Genome (Krishna et al. 2017)

**Size**: 108,249 images

**Format**: N/A

**Annotation**: Bounding box annotations converted into prompt-style training samples.

## 🔬 Methodology

**Methods**:
- Multiple-choice QA evaluation

**Metrics**:
- Accuracy

**Calculation**: Macro-averaged accuracy calculated by averaging accuracy per class and then taking the mean across all classes.

**Interpretation**: The performance drop in unseen categories indicates the model's ability to generalize beyond the training labels.

**Validation**: Using separate splits for seen and unseen labels in evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
