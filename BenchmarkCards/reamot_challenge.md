# ReaMOT Challenge

## 📊 Benchmark Details

**Name**: ReaMOT Challenge

**Overview**: The ReaMOT Challenge is designed to advance the research on Reasoning-based Multi-Object Tracking (ReaMOT) and evaluate the models’ reasoning capabilities. It includes 1,156 language instructions with reasoning characteristics, 423,359 image-language pairs, and 869 diverse scenes, categorized into three levels of reasoning difficulty: Easy, Medium, and Hard.

**Data Type**: image-language pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/chen-si-jia/ReaMOT)

## 🎯 Purpose and Intended Users

**Goal**: To advance research in reasoning-based multi-object tracking and evaluate models' reasoning capabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multi-Object Tracking

**Limitations**: The analysis of the ReaMOT Challenge dataset is not sufficiently comprehensive.

## 💾 Data

**Source**: Constructed from 12 datasets including Argoverse-HD, DanceTrack, GMOT-40, KITTI, MOT17, MOT20, MPHOI, PathTrack, PoseTrack, SportsMOT, UA-DETRAC, and UAVDT.

**Size**: 423,359 image-language pairs, 1,156 language instructions, 869 scenes.

**Format**: video

**Annotation**: Manual annotation combined with GPT-assisted annotation.

## 🔬 Methodology

**Methods**:
- Evaluation using new tailored metrics for the ReaMOT task.

**Metrics**:
- RIDF1
- RMOTA
- RRcll
- RPrcn

**Calculation**: Metrics are calculated using a combination of language instructions' reasoning scores.

**Interpretation**: Higher scores indicate better performance in reasoning-based multi-object tracking.

**Baseline Results**: ReaTrack achieves state-of-the-art performance on the ReaMOT Challenge benchmark.

**Validation**: Extensive experiments demonstrate the effectiveness of the ReaTrack framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
