# RescueADI

## 📊 Benchmark Details

**Name**: RescueADI

**Overview**: RescueADI is a novel dataset for Adaptive Disaster Interpretation (ADI), containing high-resolution remote sensing images with annotations for planning, perception, and recognition tasks to facilitate comprehensive analysis of disaster scenes.

**Data Type**: remote sensing images

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for disaster interpretation tasks using autonomous agents to enhance decision-making in disaster scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Planning
- Perception
- Recognition

**Limitations**: N/A

## 💾 Data

**Source**: High-resolution remote sensing images primarily sourced from the RescueNet dataset.

**Size**: 4,044 remote sensing images, 16,949 semantic masks, 14,483 object bounding boxes, 13,424 interpretation requests

**Format**: N/A

**Annotation**: Annotated for planning, perception, and recognition tasks, providing a tuple of required sub-tasks for each interpretation request.

## 🔬 Methodology

**Methods**:
- Agent-based planning
- Object detection
- Semantic segmentation

**Metrics**:
- Accuracy
- Mean Intersection over Union (mIoU)
- Mean Average Precision (mAP)

**Calculation**: Metrics calculated based on the performance of the planning, perception, and recognition outputs.

**Interpretation**: Good performance is indicated by high planning accuracy, high mIoU for segmentation, and high mAP for object detection.

**Baseline Results**: 9% higher accuracy in comparison to existing VQA methods.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
