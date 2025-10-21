# Kitchen-R

## 📊 Benchmark Details

**Name**: Kitchen-R

**Overview**: Kitchen-R is a benchmark that unifies the evaluation of task planning and low-level control within a simulated kitchen environment, featuring more than 500 complex language instructions and enabling holistic benchmarking of language-guided robotic agents.

**Data Type**: text

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- ALFRED
- VirtualHome
- EAI

**Resources**:
- [GitHub Repository](https://github.com/isaac-sim/IsaacSim)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the Kitchen-R benchmark is to provide a unified testbed and baselines for robust agents that can execute complex language commands in realistic environments.

**Target Audience**:
- ML Researchers
- Robotics Practitioners
- Model Developers

**Tasks**:
- Task Planning
- Mobile Manipulation

**Limitations**: N/A

## 💾 Data

**Source**: A digital twin simulated kitchen environment generated using Isaac Sim.

**Size**: 2700 mobile manipulation trajectories, 563 language instructions

**Format**: N/A

**Annotation**: Automatically generated from templates based on kitchen scenes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Exact Match (EM)
- Mean Squared Error (MSE)
- Success Rate (SR)

**Calculation**: EM is calculated as the average of correctly predicted steps of plans, MSE is the average distance between predicted and expert trajectories.

**Interpretation**: A high EM score indicates good performance in planning, while low MSE reflects high accuracy in trajectory prediction.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through data collection and evaluation during the Embodied AI track of the AIJ Contest.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
