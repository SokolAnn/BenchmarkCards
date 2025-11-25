# GameTileNet

## 📊 Benchmark Details

**Name**: GameTileNet

**Overview**: GameTileNet is a dataset designed to provide semantic labels for low-resolution digital game art, advancing procedural content generation and related AI research as a vision-language alignment task.

**Data Type**: game tiles with semantic annotations

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/RimiChen/2024-GameTileNet)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate narrative-driven procedural content generation through visual-language alignment.

**Target Audience**:
- ML Researchers
- Game Developers

**Tasks**:
- Object Detection
- Semantic Labeling

**Limitations**: Some tiles blur lines between categories and inconsistent naming introduces noise.

## 💾 Data

**Source**: Collected from OpenGameArt.org under Creative Commons licenses.

**Size**: 2,142 labeled game objects

**Format**: N/A

**Annotation**: Annotated by both human annotators and original asset authors.

## 🔬 Methodology

**Methods**:
- Object Detection
- Semantic Labeling

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics were calculated based on ground truth labels compared against predicted labels.

**Interpretation**: A higher score indicates better performance in distinguishing game tile objects.

**Baseline Results**: Best model achieved 92.2% test accuracy.

**Validation**: Validation procedures include consistency assessment through relabeling experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All images included in GameTileNet are used under one of three Creative Commons licenses: CC0, CC-BY (3.0 or 4.0), or CC-BY-SA (3.0 or 4.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
