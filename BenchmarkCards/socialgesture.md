# SocialGesture

## 📊 Benchmark Details

**Name**: SocialGesture

**Overview**: SocialGesture is the first large-scale dataset specifically designed for multi-person gesture analysis, featuring a diverse range of natural scenarios and supporting multiple gesture analysis tasks, including video-based recognition and temporal localization.

**Data Type**: video clips

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- HaGRID
- LD-ConGR
- EgoGesture

**Resources**:
- [Resource](https://huggingface.co/datasets/IrohXu/SocialGesture)

## 🎯 Purpose and Intended Users

**Goal**: To advance the study of gesture during complex social interactions through the introduction of a comprehensive multi-person gesture dataset.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Gesture Recognition
- Temporal Action Localization
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: YouTube and Ego4D

**Size**: 9,889 video clips

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- mAP (mean Average Precision)

**Calculation**: Metrics are calculated based on gesture localization and recognition performance.

**Interpretation**: Accuracy and mAP indicate the performance of models in recognizing and localizing gestures in videos.

**Baseline Results**: Various models were benchmarked with state-of-the-art accuracy results ranging up to 84.43%.

**Validation**: Experiments conducted using a split of raw videos into training and test sets, ensuring a range of scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Exposing personal information

**Demographic Analysis**: Demographic factors were considered for annotators, with a diverse representation used in the dataset.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collections and annotations were approved by the Institutional Review Board (IRB).

**Data Licensing**: Creative Commons Attribution Non Commercial 3.0 (cc-by-nc-3.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
