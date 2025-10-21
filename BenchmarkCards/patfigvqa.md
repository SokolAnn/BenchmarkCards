# PatFigVQA

## 📊 Benchmark Details

**Name**: PatFigVQA

**Overview**: We introduce a novel visual question answering (VQA) dataset called PatFigVQA suitable to fine-tune and evaluate LVLMs in a few-shot learning scenario to close the domain gap of pre-trained LVLMs for patents.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/TIBHannover/patent-figure-classification)

## 🎯 Purpose and Intended Users

**Goal**: To study patent figure VQA and classification using LVLM in zero-shot and few-shot settings.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Visual Question Answering
- Patent Figure Classification

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from Extended CLEF-IP 2011 and DeepPatent2 datasets.

**Size**: 35,926 figures for PatFigVQA; Exact sizes for PatFigCLS not specified

**Format**: N/A

**Annotation**: Manual question formulation for the dataset.

## 🔬 Methodology

**Methods**:
- Fine-tuning of LVLMs
- Tournament-style classification approach
- Multiple-choice questions based classification

**Metrics**:
- Top-1 accuracy
- SemEq

**Calculation**: Calculated based on top classification performance and semantic equivalency with ground truth.

**Interpretation**: Higher accuracy indicates better performance in classifying patent figures.

**Validation**: Validation performed using specific splits on dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
