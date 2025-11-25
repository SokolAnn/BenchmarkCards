# Reasoning Grasping Benchmark

## 📊 Benchmark Details

**Name**: Reasoning Grasping Benchmark

**Overview**: The Reasoning Grasping Benchmark measures robot performance in generating grasp poses based on implicit instructions from human users. It includes various object and part grasping scenarios derived from the GraspNet-1 billion dataset, enhanced with reasoning instructions.

**Data Type**: grasping poses

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- GraspNet

**Resources**:
- [Resource](https://reasoning-grasping.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To advance robotic systems' ability to interpret implicit human commands and generate appropriate grasping actions.

**Target Audience**:
- Robotics Researchers
- Industry Practitioners

**Tasks**:
- Grasping

**Limitations**: The model struggles with novel objects not seen during training.

## 💾 Data

**Source**: Extended GraspNet-1 billion dataset with reasoning instructions.

**Size**: 1,730 reasoning instructions, 64 objects, 109 parts, approximately 100 million grasping poses

**Format**: N/A

**Annotation**: Manual segmentation of parts and automated generation of reasoning instructions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Grasp prediction accuracy
- Success rate in lifting objects

**Calculation**: Metrics are calculated based on the intersection over union (IoU) score and the angular deviation of predicted grasp poses compared to ground truth.

**Interpretation**: Higher precision in grasping indicates better model performance in understanding implicit instructions.

**Baseline Results**: The model outperformed baseline methods including CLIP and LLaV A models in grasping prediction tasks.

**Validation**: The benchmark was validated through extensive real-world experiments with human instructions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
