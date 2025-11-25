# LLM4AD (Large Language Models for Autonomous Driving)

## 📊 Benchmark Details

**Name**: LLM4AD (Large Language Models for Autonomous Driving)

**Overview**: The paper proposes a comprehensive benchmark for evaluating the instruction-following abilities of LLM4AD in simulation, introduced along with the LaMPilot-Bench dataset.

**Data Type**: traffic scene datasets

**Domains**:
- Transportation
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- CARLA Leaderboard 1.0 Benchmark
- LaMPilot-Bench

**Resources**:
- [GitHub Repository](https://github.com/Farama-Foundation/HighwayEnv)
- [Resource](https://leaderboard.carla.org/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the instruction-following capabilities and performance of LLM-based agents in autonomous driving tasks.

**Target Audience**:
- Research Organizations
- Automotive Industry
- Machine Learning Practitioners

**Tasks**:
- Autonomous Driving
- Simulation Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: LaMPilot-Bench dataset consisting of 4.9K semi-human-annotated traffic scenes, with a subset of 500 samples for testing.

**Size**: 4,900 examples

**Format**: N/A

**Annotation**: Semi-human annotation

## 🔬 Methodology

**Methods**:
- Automated metrics
- Simulation evaluation

**Metrics**:
- Time-to-Collision (TTC)
- Driving Score
- Route Completion (RC)
- Infraction Penalty (IP)

**Calculation**: Metrics calculated based on predefined scenarios and their respective outcomes.

**Interpretation**: Higher scores indicate better performance in safe driving and task completion.

**Baseline Results**: Human driver performance established for comparative analysis.

**Validation**: Internal testing through real-world vehicle experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Value Alignment

**Atlas Risks**:
- **Societal Impact**: Impact on Jobs
- **Privacy**: Data privacy rights alignment
- **Value Alignment**: Harmful output

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
