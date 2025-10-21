# HUMOTO (Human Motions with Objects)

## 📊 Benchmark Details

**Name**: HUMOTO (Human Motions with Objects)

**Overview**: HUMOTO is a high-fidelity dataset of human-object interactions for motion generation, computer vision, and robotics applications, featuring 736 sequences (7,875 seconds at 30 fps) capturing interactions with 63 modeled objects and various activities.

**Data Type**: video

**Domains**:
- Computer Vision
- Robotics

**Languages**:
- N/A

**Similar Benchmarks**:
- BEHA VE
- OMOMO
- IMHD
- ParaHome
- GRAB

**Resources**:
- [Resource](https://jiaxin-lu.github.io/humoto/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of HUMOTO is to provide a comprehensive dataset for advancing realistic human-object interaction modeling across various research domains.

**Target Audience**:
- ML Researchers
- Robotics Researchers
- Animators

**Tasks**:
- Human-Object Interaction
- Motion Generation

**Limitations**: Due to motion capture suit size constraints, the dataset includes only a single performer, which may introduce bias.

## 💾 Data

**Source**: Captured from a custom motion capture setup utilizing dual-Kinect cameras and a motion capture suit.

**Size**: 736 sequences, totaling 7,875 seconds of motion

**Format**: N/A

**Annotation**: Textual annotations provided at multiple levels, including concise titles and detailed scripts for each sequence.

## 🔬 Methodology

**Methods**:
- Multi-sensor capture
- Scene-driven LLM scripting

**Metrics**:
- Foot Sliding
- Jerk
- Motion Signal-to-Noise Ratio (MSNR)
- Contact Quality
- State Consistency

**Calculation**: Metrics calculated as per defined formulas in the methodology, providing insights into motion quality and interaction realism.

**Interpretation**: Lower foot sliding and jerk values indicate more natural motion, while MSNR values are used to compare motion quality against other datasets.

**Baseline Results**: Compared against other datasets like Mixamo, HUMOTO shows lower foot sliding and jerk, indicating high motion fidelity.

**Validation**: Licensed industry professionals verified the motion and annotations for quality assurance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Limited to single performer, which could introduce demographic bias.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
