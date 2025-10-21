# Leader360V (A Large-scale, Real-world 360 Video Dataset for Multi-task Learning in Diverse Environments)

## 📊 Benchmark Details

**Name**: Leader360V (A Large-scale, Real-world 360 Video Dataset for Multi-task Learning in Diverse Environments)

**Overview**: Leader360V is the first large-scale (10K+), labeled real-world 360 video dataset specifically designed for instance segmentation and tracking in diverse environments. It integrates existing public datasets with self-collected 360 videos to facilitate automated annotation through A3360V, a three-phase pipeline, thereby enhancing model performance in 360 video understanding.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- 360VOS
- PanoVOS
- 360VOT

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and scalable dataset for multi-task learning in 360 video understanding, focusing on instance segmentation and tracking.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Instance Segmentation
- Object Tracking

**Limitations**: Our current Leader360V dataset does not yet cover all object classes commonly encountered in daily life, nor does it include annotations for the motion states of moving objects.

## 💾 Data

**Source**: Integral combination of existing public datasets and self-collected 360 videos in diverse environments.

**Size**: 10,000+ videos

**Format**: 360 Video

**Annotation**: Automated through the A3360V pipeline, involving LLMs for semantic labeling and human oversight for final revisions.

## 🔬 Methodology

**Methods**:
- Automated Annotation Pipelines
- User Studies for Validation

**Metrics**:
- J&F Score
- Region Accuracy
- Boundary Accuracy

**Calculation**: Metrics are calculated based on frame-level annotations against ground truth for segmentation and tracking tasks.

**Interpretation**: Higher J&F scores indicate better performance in object segmentation and tracking accuracy.

**Baseline Results**: Performance evaluations against existing benchmarks like YouTube-VOS to demonstrate improvement in segmentation and tracking.

**Validation**: Extensive user studies and evaluations confirm the effectiveness of annotation and usage processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential data bias due to uneven representation of indoor vs outdoor scenes.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Videos include face anonymization to protect privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
