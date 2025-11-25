# DRAMA-X

## 📊 Benchmark Details

**Name**: DRAMA-X

**Overview**: DRAMA-X is a fine-grained benchmark for evaluating multi-class intent prediction and risk reasoning for vulnerable road users in urban driving scenarios. It includes comprehensive annotations for object detection, intent prediction, risk assessment, and action suggestions.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/taco-group/DRAMA-X)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate fine-grained intent prediction and risk reasoning in autonomous driving scenarios involving pedestrians and cyclists.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Object Detection
- Intent Prediction
- Risk Assessment
- Action Suggestion

**Limitations**: The automated annotation pipeline may introduce errors in complex scenes with multiple VRUs.

## 💾 Data

**Source**: Derived from the DRAMA dataset, which contains annotated urban driving scenarios.

**Size**: 5,686 annotated video clips spanning approximately 54,892 frames.

**Format**: JSON

**Annotation**: Automated annotation via a multi-stage pipeline including tracking, motion analysis, and natural language description generation.

## 🔬 Methodology

**Methods**:
- Scene graph generation
- Vision-Language Models for intent prediction
- Risk assessment
- Action suggestion

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on predictions compared to ground-truth annotations for each task.

**Interpretation**: High accuracy and F1 scores are associated with effective intent prediction and risk assessment.

**Baseline Results**: The SGG-Intent framework provides a baseline for evaluating various VLMs across benchmark tasks.

**Validation**: Validation involves testing with state-of-the-art VLMs and evaluating task performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotations derived from visual data with safeguards to prevent privacy violations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
