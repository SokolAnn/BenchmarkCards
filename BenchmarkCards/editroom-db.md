# EditRoom-DB

## 📊 Benchmark Details

**Name**: EditRoom-DB

**Overview**: EditRoom-DB is a large-scale dataset for language-guided 3D scene layout editing that includes 83k editing pairs generated through an automatic data augmentation pipeline, facilitating comprehensive training and evaluation of methods for natural language command-based scene manipulation.

**Data Type**: editing pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- 3D-FRONT

**Resources**:
- [Resource](https://eric-ai-lab.github.io/edit-room.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust dataset for evaluating and training models in the field of language-guided 3D scene editing.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Single Operation Editing
- Multi-Operation Editing

**Limitations**: N/A

## 💾 Data

**Source**: Generated through an automatic data augmentation pipeline based on the existing 3D scene synthesis datasets.

**Size**: 83,000 examples

**Format**: N/A

**Annotation**: Automatically paired editing operations with natural language descriptions.

## 🔬 Methodology

**Methods**:
- Benchmark Evaluation
- Statistical Analysis

**Metrics**:
- Accuracy
- Semantic Intersection Over Union (S-IOU)
- LPIPS
- CLIP

**Calculation**: Metrics calculated based on comparisons between generated scenes and target scenes.

**Interpretation**: Higher scores indicate better alignment and accuracy in scene editing.

**Baseline Results**: EditRoom outperformed baselines across all metrics.

**Validation**: Validated through comparisons against existing state-of-the-art models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
