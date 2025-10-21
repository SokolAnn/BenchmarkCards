# RealDex

## 📊 Benchmark Details

**Name**: RealDex

**Overview**: RealDex is a pioneering dataset capturing authentic dexterous hand grasping motions infused with human behavioral patterns, enriched by multi-view and multimodal visual data. It is crucial for training dexterous hands to mimic human movements more naturally and precisely.

**Data Type**: grasping motion sequences with visual data

**Domains**:
- Robotics

**Languages**:
- N/A

**Similar Benchmarks**:
- DVGG
- DexGraspNet
- MultiDex

**Resources**:
- [Resource](https://4dvlab.github.io/RealDex)

## 🎯 Purpose and Intended Users

**Goal**: Advance research and practical applications of human-like robotic dexterous grasping in real-world environments.

**Target Audience**:
- Robotics Researchers
- Robotic Engineers
- ML Practitioners

**Tasks**:
- Dexterous Grasping
- Human-Robot Interaction

**Limitations**: N/A

## 💾 Data

**Source**: Collected using a teleoperation system with a Shadow Hand robot and multiple RGB-D cameras.

**Size**: 2.6k sequences of grasping motions, 955k frames of visual data

**Format**: Point cloud, RGB images

**Annotation**: Manually adjusted annotations for hand-object interactions and grasp poses.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automatic pose generation
- Motion synthesis

**Metrics**:
- User scores for human-likeness
- Stability measures
- Mean Per-Joint Positional Error (MPJPE)
- Average Variance Error (A VE)

**Calculation**: Comparisons made against pre-defined ground truth data for motion sequences and grasping poses.

**Interpretation**: Higher scores indicate better performance in generating human-like grasping motions.

**Baseline Results**: Compared against methods like SAGA and GOAL.

**Validation**: Extensive experiments and real robot testing demonstrate the performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
