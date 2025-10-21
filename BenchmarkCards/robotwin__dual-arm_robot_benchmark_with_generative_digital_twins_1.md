# RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins

## 📊 Benchmark Details

**Name**: RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins

**Overview**: RoboTwin introduces a generative digital twin framework to produce diverse expert datasets and provides a real-world-aligned evaluation platform for dual-arm robotic tasks, enabling standardized evaluation and better alignment between simulated training and real-world performance.

**Data Type**: dual-arm robotic manipulation tasks

**Domains**:
- Robotics

**Languages**:
- N/A

**Similar Benchmarks**:
- MimicGen
- HumanoidBench
- BiGym

**Resources**:
- [Resource](https://robotwin-benchmark.github.io)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of RoboTwin is to assess dual-arm robots' performance using synthetic data generated through a generative digital twin framework.

**Target Audience**:
- ML Researchers
- Robotics Engineers
- Model Developers
- Industry Practitioners

**Tasks**:
- Dual-Arm Manipulation

**Limitations**: N/A

## 💾 Data

**Source**: 300 RoboTwin-generated samples and 20 real-world samples for each task.

**Size**: 100 sets of simulation data and 20 sets of real-world data per task

**Format**: N/A

**Annotation**: Expert demonstrations are generated via a large language model combined with object annotations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Success Rate

**Calculation**: Success rate determined by meeting target pose constraints and ensuring collision-free execution.

**Interpretation**: Higher success rates indicate better performance in task execution.

**Baseline Results**: Policies trained on 300 RoboTwin-generated data improve success rates significantly over those trained solely on real-world data.

**Validation**: Validated using the open-source COBOT Magic Robot platform with simulated task execution.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
