# OAKINK2

## 📊 Benchmark Details

**Name**: OAKINK2

**Overview**: OAKINK2 is a dataset of bimanual object manipulation tasks for complex daily activities. It introduces a structured representation for complex tasks, organizing them into three levels of abstraction: Affordance, Primitive Task, and Complex Task. The dataset provides multi-view image streams, 3D-pose annotations for human manipulation processes, and task specifications.

**Data Type**: video with annotations, pose data

**Domains**:
- Robotics

**Languages**:
- N/A

**Similar Benchmarks**:
- OakInk

**Resources**:
- [Resource](https://oakink.net/v2)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for studying bimanual object manipulation in complex task completion using structured task representations and multimodal observation.

**Target Audience**:
- ML Researchers
- Robotics Engineers
- Computer Vision Researchers

**Tasks**:
- Object Manipulation
- Motion Synthesis
- Task Planning

**Limitations**: N/A

## 💾 Data

**Source**: Collected from real-world human interventions in various manipulation scenarios.

**Size**: 4.01M frames across 627 sequences, including 264 complex task sequences.

**Format**: videos and pose data with annotations

**Annotation**: 3D motion, including pose and shape for the human upper-body, hands, and interacting objects.

## 🔬 Methodology

**Methods**:
- Multi-view video capture
- MoCap for 3D pose estimation
- Expert annotation review

**Metrics**:
- Contact Ratio (CR)
- Solid Intersection Volume (SIV)
- Mean Per Joint Position Error (MPJPE)
- Frechet Inception Distance (FID)

**Calculation**: Metrics are computed based on the comparison between predicted and ground truth motions with respect to trajectory accuracy and contact quality.

**Interpretation**: High values of CR and low values of SIV are desirable, indicating effective hand-object interaction without penetration during manipulation.

**Baseline Results**: N/A

**Validation**: Cross-dataset validation with existing hand-object interaction datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Privacy

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured through careful annotation processes and compliance with ethical data collection practices.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
