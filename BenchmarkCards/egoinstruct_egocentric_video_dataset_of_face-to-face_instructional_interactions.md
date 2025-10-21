# EgoInstruct (Egocentric Video Dataset of Face-to-face Instructional Interactions)

## 📊 Benchmark Details

**Name**: EgoInstruct (Egocentric Video Dataset of Face-to-face Instructional Interactions)

**Overview**: A new egocentric video dataset of face-to-face instruction that provides ground-truth annotations for procedural step segmentation and conversation-state classification.

**Data Type**: video

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Japanese

**Similar Benchmarks**:
- Ego4D
- HoloAssist
- EPIC-KITCHENS

**Resources**:
- [Resource](https://arxiv.org/abs/2509.22019)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundation for the analysis of face-to-face instructional interactions through a new dataset and benchmark models for understanding instructional effectiveness.

**Target Audience**:
- ML Researchers
- Educational Technologists
- Computer Vision Researchers

**Tasks**:
- Procedural Step Segmentation
- Conversation-State Classification

**Limitations**: N/A

## 💾 Data

**Source**: Recorded video sessions of face-to-face instructional interactions using Aria Glasses and GoPro cameras.

**Size**: 8 hours of video across 38 sessions

**Format**: Video

**Annotation**: Annotations for procedural step segmentation and conversation-state classification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on segmentation precision and classifications of conversation states.

**Interpretation**: High scores indicate good performance on recognizing procedural steps and accurate detection of conversation states.

**Baseline Results**: ASFormer and conventional task-specific models were used for comparison.

**Validation**: Five-fold cross-validation was conducted for model evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants' consent obtained; identity anonymized in annotations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Explicit consent was taken from all participants involved in the video recordings.

**Compliance With Regulations**: Not Applicable
