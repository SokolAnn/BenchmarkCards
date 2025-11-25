# Human-related Anomaly Localization

## 📊 Benchmark Details

**Name**: Human-related Anomaly Localization

**Overview**: The Human-related Anomaly Localization benchmark includes 12 types of human-related anomalous behaviors, including fighting, people falling, and robbery, with a total of 1,159 videos and 26.3 hours of footage.

**Data Type**: video with frame-level annotations and text descriptions

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ActivityNet1.3
- THUMOS14

**Resources**:
- [Resource](https://arxiv.org/abs/2504.13460)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for few-shot temporal action localization focused on human-anomalous events.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Temporal Action Localization

**Limitations**: N/A

## 💾 Data

**Source**: Videos manually selected from MSAD, XD-Violence, and CUV A datasets.

**Size**: 1,159 videos totaling 26.3 hours

**Format**: video with annotations

**Annotation**: Frame-level annotations of anomaly intervals, along with corresponding frame captions and logical chain text.

## 🔬 Methodology

**Methods**:
- Feature extraction from videos
- Semantic-aware text-visual alignment
- Chain-of-Thought reasoning method

**Metrics**:
- mean Average Precision (mAP)

**Calculation**: mAP calculated at an IoU threshold of 0.5 for evaluation.

**Interpretation**: Higher mAP indicates better performance in accurately localizing actions within untrimmed videos.

**Baseline Results**: Achieved state-of-the-art performance on public benchmarks with an improvement of 4% on ActivityNet1.3 and 12% on THUMOS14.

**Validation**: The method was validated through extensive experiments on public benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
