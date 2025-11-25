# StagePro-V1

## 📊 Benchmark Details

**Name**: StagePro-V1

**Overview**: StagePro-V1 is a comprehensive dataset for evaluating stage generation tasks, featuring annotated stage images, scripts, and 3D scene layouts.

**Data Type**: image and script pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://deadsmither5.github.io/2025/01/03/StageDesigner/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundational resource for AI-driven stage scenography research.

**Target Audience**:
- ML Researchers
- Stage Designers
- Theater Artists

**Tasks**:
- Stage Generation
- Scene Layout Generation

**Limitations**: N/A

## 💾 Data

**Source**: Created in collaboration with professional stage designers, capturing various historical stage productions.

**Size**: 276 unique stage scenes

**Format**: images and scripts in various formats

**Annotation**: Annotations include thematic and spatial cues extracted from theater scripts.

## 🔬 Methodology

**Methods**:
- User Studies
- Qualitative Analysis
- Quantitative Analysis

**Metrics**:
- Overlap-inter-Stage (OIS)
- CLIP Similarity
- Out-of-Bound (OOB)
- Intersection-with-Ground truth (IWG)
- Class Diversity

**Calculation**: Metrics calculated based on the spatial coherence and thematic accuracy of the generated stages.

**Interpretation**: Higher scores in metrics indicate better alignment with the narrative and spatial requirements of stage designs.

**Baseline Results**: Baseline comparison made with LayoutGPT for measuring stage generation quality.

**Validation**: User studies with general users and professionals to validate effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
