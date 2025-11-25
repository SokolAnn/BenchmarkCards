# IntentGrasp

## 📊 Benchmark Details

**Name**: IntentGrasp

**Overview**: IntentGrasp is a benchmark supporting multi-target grasping under flexible instructions, allowing for the assessment of robotic systems in understanding indirect verbal commands and grasping multiple objects in a 3D environment.

**Data Type**: 3D point clouds with object annotations and grasp poses

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- Grasp-Anything-6D

**Resources**:
- [GitHub Repository](https://github.com/cxmomo/GraspCoT)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate robotic grasping capabilities under flexible instructions and enrich the existing benchmarks for multi-object grasp detection.

**Target Audience**:
- Robotics Researchers
- ML Researchers
- Robotics Developers

**Tasks**:
- Grasp Detection
- Language Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Adapted from the Grasp-Anything-6D dataset with structured prompt templates for flexible instruction generation.

**Size**: 1 million scenes with approximately 3 million objects

**Format**: N/A

**Annotation**: Automatically generated using a large language model for contextual instructions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Joint training with visual and textual modalities

**Metrics**:
- Coverage Rate (CR)
- Earth Mover's Distance (EMD)
- Collision-Free Rate (CFR)

**Calculation**: Metrics are calculated based on the alignment of predicted grasp poses with ground-truth annotations.

**Interpretation**: Higher coverage rates indicate better performance in accurately grasping objects as per flexible instructions.

**Baseline Results**: GraspCoT outperformed baseline models like 3DAPNet and LGrasp6D in all metrics on the IntentGrasp benchmark.

**Validation**: Extensive experiments were conducted in both simulated and real-world settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential safety hazards due to failure in grasp detection leading to drops or collisions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
