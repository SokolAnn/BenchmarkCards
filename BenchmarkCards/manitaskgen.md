# ManiTaskGen

## 📊 Benchmark Details

**Name**: ManiTaskGen

**Overview**: ManiTaskGen is a universal task generation framework that automatically generates comprehensive mobile manipulation tasks for varying scenes, facilitating both benchmarking and improvement of embodied decision-making agents.

**Data Type**: task instructions

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- ALFRED
- M3Bench
- λ

**Resources**:
- [Resource](https://arxiv.org/abs/2505.20726)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark and improve the capabilities of vision-language models (VLMs) for embodied decision making by generating diverse and comprehensive mobile manipulation tasks for arbitrary scenes.

**Target Audience**:
- ML Researchers
- Robotics Researchers
- AI Practitioners

**Tasks**:
- Mobile Manipulation Task Generation
- Embodied Decision-Making Benchmarking

**Limitations**: N/A

## 💾 Data

**Source**: Generated tasks based on scene information (e.g., object poses, bounding boxes) in diverse environments such as ReplicaCAD, AI2THOR, and SUN-RGBD.

**Size**: 39,871 tasks

**Format**: N/A

**Annotation**: Automatically generated tasks utilizing template-based and VLM voting mechanisms.

## 🔬 Methodology

**Methods**:
- Task Generation
- Automated Benchmark Construction
- Human Evaluation

**Metrics**:
- Validity Rate
- Task Diversity

**Calculation**: Metrics calculated based on the proportion of valid tasks generated and the coverage of diverse objects and locations within the generated tasks.

**Interpretation**: High validity rates indicate effective task generation, while diverse coverage reflects comprehensive task representation across scenes.

**Validation**: Tasks were validated through human evaluation and by utilizing voting mechanisms from multiple VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
