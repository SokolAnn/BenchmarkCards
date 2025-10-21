# RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

## 📊 Benchmark Details

**Name**: RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation

**Overview**: RoboTwin 2.0 is a scalable simulation-based data generation framework designed to produce high-quality, diverse, realistic, and interaction-rich datasets for bimanual manipulation, integrating an expert data generation pipeline with a comprehensive benchmark for evaluating policy generalization to cluttered environments and open-ended language goals.

**Data Type**: multi-embodiment trajectory data

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- RoboTwin 1.0
- ManiSkill2
- Meta-World

**Resources**:
- [Resource](https://robotwin-platform.github.io)
- [Resource](https://huggingface.co/datasets/TianxingChen/RoboTwin2.0/tree/main/dataset)

## 🎯 Purpose and Intended Users

**Goal**: To support scalable research in robust bimanual manipulation by providing a diverse and realistic dataset along with standardized evaluation protocols.

**Target Audience**:
- Robotics Researchers
- ML Researchers
- Industry Practitioners

**Tasks**:
- Bimanual Manipulation

**Limitations**: N/A

## 💾 Data

**Source**: RoboTwin-OD, a large-scale object library and automated data generation pipeline.

**Size**: 100,000+ trajectories

**Format**: Raw trajectory data

**Annotation**: Annotated with semantic and manipulation-relevant labels.

## 🔬 Methodology

**Methods**:
- Automated data generation
- Expert code generation via MLLMs
- Domain randomization

**Metrics**:
- Average Success Rate (ASR)
- Top-5 ASR
- Refinement Iterations
- Token Count

**Calculation**: Metrics are calculated based on the success rate of generated programs and efficiency of the data generation pipeline.

**Interpretation**: Higher ASR indicates better performance of the generated policies, with lower Token Count reflecting higher efficiency.

**Baseline Results**: Baseline results from RoboTwin 1.0 indicate significant improvements in ASR and efficiency.

**Validation**: Through controlled experiments evaluating performance on benchmark tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
