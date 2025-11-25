# ROBOSPATIAL

## 📊 Benchmark Details

**Name**: ROBOSPATIAL

**Overview**: ROBOSPATIAL is a large-scale dataset for spatial understanding in robotics, consisting of real indoor and tabletop scenes, captured as 3D scans and egocentric images, annotated with rich spatial information relevant to robotics.

**Data Type**: 2D images and 3D scans with spatial relationship annotations

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- BLINK-Spatial
- SpatialBot
- SpatialRGPT-Bench
- EmbSpatial-Bench

**Resources**:
- [Resource](https://chanh.ee/RoboSpatial/)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate spatial understanding in vision-language models (VLMs) for robotics applications.

**Target Audience**:
- ML Researchers
- Robotics Practitioners
- Model Developers

**Tasks**:
- Spatial Reasoning
- Object Manipulation
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Annotated indoor scene and tabletop RGBD datasets.

**Size**: 1M images, 5k 3D scans, 3M annotated spatial relationships

**Format**: N/A

**Annotation**: Automatically generated from 3D geometry and 2D image annotations using a customizable data generation pipeline.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on model predictions compared to ground truth spatial relationships.

**Interpretation**: Higher accuracy indicates better spatial reasoning capabilities.

**Baseline Results**: Models trained on ROBOSPATIAL consistently outperform baseline methods on evaluation benchmarks.

**Validation**: Validated through comprehensive experimentation on held-out and out-of-domain benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
