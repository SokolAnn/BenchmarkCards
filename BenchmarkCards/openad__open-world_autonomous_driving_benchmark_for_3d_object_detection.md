# OpenAD: Open-World Autonomous Driving Benchmark for 3D Object Detection

## 📊 Benchmark Details

**Name**: OpenAD: Open-World Autonomous Driving Benchmark for 3D Object Detection

**Overview**: OpenAD is the first real open-world autonomous driving benchmark for 3D object detection, built upon a corner case discovery and annotation pipeline that integrates with a multimodal large language model (MLLM).

**Data Type**: bounding box annotations (2D and 3D)

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- nuScenes
- KITTI
- Waymo

**Resources**:
- [GitHub Repository](https://github.com/VDIGPKU/OpenAD)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate models' abilities in open-world scenarios for 3D object detection in autonomous driving.

**Target Audience**:
- ML Researchers
- Autonomous Driving Developers
- Computer Vision Practitioners

**Tasks**:
- 3D Object Detection

**Limitations**: OpenAD exclusively supports 2D and 3D object detection tasks, and all re-annotated data is allocated for benchmarking purposes.

## 💾 Data

**Source**: Five autonomous driving perception datasets: Argoverse 2, KITTI, nuScenes, ONCE, and Waymo.

**Size**: 2,000 scenes, 19,761 annotated objects

**Format**: Unified format for 2D and 3D bounding boxes

**Annotation**: Manual annotation of corner cases and existing objects combined with automatic annotations from MLLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Average Precision (AP)
- Average Recall (AR)
- Average Translation Error (ATE)
- Average Scale Error (ASE)

**Calculation**: AP and AR depend on True Positive (TP) metrics, utilizing IoU for positional scores and cosine similarity for semantic scores.

**Interpretation**: A model's performance is determined through calculated metrics reflecting its detection abilities in both seen and unseen categories.

**Validation**: Evaluated on specialized and open-world models through various designed methodologies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: The benchmark addresses varying object types across multiple vehicles and environments.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data utilized in OpenAD are sourced from published datasets. No personal data is present.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The study does not foresee potential privacy-related issues.
