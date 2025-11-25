# Video-OCR bench

## 📊 Benchmark Details

**Name**: Video-OCR bench

**Overview**: This paper introduces Video-OCR bench, the first comprehensive benchmark to evaluate visual LLMs in various video-OCR tasks. It consists of 1,028 videos and 2,961 question-answer pairs, divided into 6 sub-tasks to evaluate models’ ability on text recognition, semantic understanding, spatial relation, movement detection, text attribute recognition, and temporal localization.

**Data Type**: video-question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/YuHuiGao/FG-Bench.git)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the video OCR performance of multi-modal models in videos and advance research in video LLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Recognition
- Semantic Understanding
- Spatial Relation
- Movement Detection
- Text Attribute Recognition
- Temporal Localization

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using a semi-automated approach that integrates the OCR ability of image LLMs with manual refinement.

**Size**: 1,028 videos, 2,961 question-answer pairs

**Format**: N/A

**Annotation**: Semi-automated with human refinement and manual checks

## 🔬 Methodology

**Methods**:
- Evaluation on multi-modal LLMs
- Using a semi-automated approach to manufacture data

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated by checking whether the model's answer matches the ground truth.

**Interpretation**: High accuracy indicates good performance on OCR tasks.

**Validation**: Human annotators reviewed and refined question-answer pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
