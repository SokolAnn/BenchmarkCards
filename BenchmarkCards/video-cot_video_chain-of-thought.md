# Video-CoT (Video Chain-of-Thought)

## 📊 Benchmark Details

**Name**: Video-CoT (Video Chain-of-Thought)

**Overview**: Video-CoT is a comprehensive dataset designed to enhance spatiotemporal understanding using Chain-of-Thought methodologies, containing 192,000 fine-grained spatiotemporal question-answer pairs and 23,000 high-quality CoT-annotated samples.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://video-cot.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the Video-CoT benchmark is to support research and advancements in understanding complex spatiotemporal relationships in videos using Chain-of-Thought methodologies.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Temporal Video Localization
- Video Captioning
- Spatial Video Grounding
- Spatio-Temporal Video Grounding
- Spatial Relationship Reference
- Temporal Video Reference

**Limitations**: N/A

## 💾 Data

**Source**: The Video-CoT dataset is constructed from publicly available datasets such as VTimeLLM, MSR-VTT, MSVD, and WebVid, with additional annotations from HCSTVG-V1 and VidSTG.

**Size**: 192,000 question-answering pairs

**Format**: N/A

**Annotation**: Annotated using Chain-of-Thought methodologies, ensuring high-quality reasoning chains.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- temporal Intersection over Union (tIoU)
- MENTOR
- Exact Match (EM)
- spatial Intersection over Union (sIoU)

**Calculation**: Metrics are calculated based on the accuracy of localization, relevance of generated captions, and alignment of predicted spatial relationships with ground truth labels.

**Interpretation**: Higher tIoU and sIoU values indicate better temporal and spatial localization performance.

**Baseline Results**: The baseline model tested is Qwen2.5-VL, with improvements shown in both Answer-Supervised Fine-Tuning and Chain-of-Thought-Supervised Fine-Tuning methods compared to the baseline.

**Validation**: The benchmark includes distinct evaluation datasets that ensure unbiased performance assessment across various spatiotemporal reasoning tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
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
