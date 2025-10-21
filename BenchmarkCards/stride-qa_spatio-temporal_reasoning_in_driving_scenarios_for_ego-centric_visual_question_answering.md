# STRIDE-QA (Spatio-Temporal Reasoning In Driving Scenarios for Ego-centric Visual Question Answering)

## 📊 Benchmark Details

**Name**: STRIDE-QA (Spatio-Temporal Reasoning In Driving Scenarios for Ego-centric Visual Question Answering)

**Overview**: STRIDE-QA is a large-scale visual question answering (VQA) dataset designed for spatiotemporal reasoning in urban driving, consisting of 285 K frames and 16 million QA pairs.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- nuScenes-QA
- ToD3Cap
- Refer-KITTI

**Resources**:
- [Resource](https://arxiv.org/abs/2508.10427)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of STRIDE-QA is to enable fine-grained spatial reasoning and temporal prediction in visual question answering for autonomous driving.

**Target Audience**:
- ML Researchers
- Autonomous Driving Practitioners

**Tasks**:
- Object-centric Spatial QA
- Ego-centric Spatial QA
- Ego-centric Spatiotemporal QA

**Limitations**: N/A

## 💾 Data

**Source**: Self-collected multi-sensor driving data from urban areas in Tokyo.

**Size**: 100 hours of driving data, 285 K frames, 16 million QA pairs

**Format**: N/A

**Annotation**: Automatically generated through a modular pipeline combining LiDAR and multi-camera data.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Localization Success Rate (LSR)
- Mean Localization Success Rate (MLSR)
- Temporal Localization Consistency (TLC)

**Calculation**: Metrics are calculated based on spatial and temporal predictions compared to ground truth.

**Interpretation**: Higher LSR, MLSR, and TLC scores indicate better spatiotemporal reasoning capabilities.

**Baseline Results**: Baseline models included GPT-4o and InternVL2.5-8B, showing significantly lower performance compared to STRIDE-QA fine-tuned models.

**Validation**: Validation procedures were carried out using manually verified annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset includes automatic blurring of identifiable faces and license plates.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
