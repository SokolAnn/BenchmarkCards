# Generalized Cross-domain Few-shot (GCFS) Task

## 📊 Benchmark Details

**Name**: Generalized Cross-domain Few-shot (GCFS) Task

**Overview**: The GCFS task focuses on adapting a source-pretrained model for high performance on both common and novel classes in a target domain with few-shot samples, addressing challenges related to data scarcity and domain adaptation.

**Data Type**: 3D object detection

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- NuScenes
- Waymo
- KITTI
- A2D2

**Resources**:
- [GitHub Repository](https://github.com/open-mmlab/OpenPCDet)

## 🎯 Purpose and Intended Users

**Goal**: To provide a framework for rapid deployment of 3D object detection models in diverse environments with few-shot learning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- 3D Object Detection

**Limitations**: N/A

## 💾 Data

**Source**: NuScenes, Waymo, KITTI, A2D2 datasets.

**Size**: ∼28K samples from NuScenes, ∼24K from Waymo, ∼7K from KITTI, ∼12K from A2D2

**Format**: Point cloud

**Annotation**: Annotated by respective datasets

## 🔬 Methodology

**Methods**:
- Multi-modal fusion
- Contrastive-enhanced prototype learning

**Metrics**:
- Mean Average Precision (mAP)

**Calculation**: Based on Average Precision (AP) at 40 recall positions for each class.

**Interpretation**: High mAP indicates strong performance in detecting both common and novel objects.

**Baseline Results**: Compared against VoxelRCNN and other SOTA methods.

**Validation**: Conducted through comprehensive experiments across different K-shot settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
