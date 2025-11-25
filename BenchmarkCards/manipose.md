# ManiPose

## 📊 Benchmark Details

**Name**: ManiPose

**Overview**: ManiPose is a pioneering benchmark designed to advance the study of pose-varying manipulation tasks, encompassing simulation environments for POM, a comprehensive dataset with geometrically consistent 6D pose labels, and a baseline method leveraging LLM capabilities for enhanced manipulation.

**Data Type**: 6D pose labels

**Domains**:
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](https://sites.google.com/view/manipose)

## 🎯 Purpose and Intended Users

**Goal**: To catalyze the development of learning algorithms for pose-aware object manipulation (POM).

**Target Audience**:
- Robotics Researchers
- ML Researchers

**Tasks**:
- Pose Estimation
- Object Manipulation

**Limitations**: N/A

## 💾 Data

**Source**: Real-world scanned rigid objects from YCB, OmniObject3D, PACE, and articulated objects from PartNet Mobility.

**Size**: 3,036 objects across 59 categories

**Format**: 3D meshes

**Annotation**: Geometrically consistent and manipulation-oriented 6D pose labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- 6D pose estimation accuracy

**Calculation**: Accuracy measured through origin error and orientation error comparisons against ground truth.

**Interpretation**: Lower origin and orientation errors indicate better pose estimation and manipulation effectiveness.

**Baseline Results**: Results demonstrate notable improvements in pose estimation and manipulation success rates.

**Validation**: Validation occurs through experiments in simulated environments and real-robot implementations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
